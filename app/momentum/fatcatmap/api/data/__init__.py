import logging

import ndb
import base64
from ndb import key
from ndb import model

from protorpc import remote
from protorpc import messages

from google.appengine.ext import db
from google.appengine.api import datastore
from google.appengine.api import datastore_types
from google.appengine.api import datastore_errors

from momentum.fatcatmap.messages.data import *
from momentum.fatcatmap.api.data import exceptions

from momentum.fatcatmap.messages import util as Util
from momentum.fatcatmap.messages import data as Data

from momentum.fatcatmap.api import FatCatMapAPIService


class DataAPIService(FatCatMapAPIService):

	config_path = 'services.data.config'

	@remote.method(Data.ObjectRequest, Data.ObjectResponse)
	def get(self, request):
		
		if request.key is not None:
			
			try:
				try:
					r_key = key.Key(urlsafe=request.key)
					r_entity = datastore.Get(r_key.urlsafe())

					if r_key is not None and r_entity is not None:

						if r_key.parent() is None:
							parent = None
						else:
							parent = str(r_key.parent())

						dk = Util.DatastoreKey(encoded=r_key.urlsafe(), parent=parent, kind=r_key.kind())
						object_r = Data.DatastoreObject(key=dk)
						response = Data.ObjectResponse(objects=[object_r], count=1)
						
				except datastore_errors.BadKeyError, e:
					try:
						r_key = db.Key(request.key)
						r_entity = datastore.Get(str(r_key))
						
						if r_key.parent() is None:
							parent = None
						else:
							parent = str(r_key.parent())

						dk = Util.DatastoreKey(encoded=str(r_key), parent=parent, kind=r_key.kind())
						object_r = Data.DatastoreObject(key=dk)

					except datastore_errors.BadKeyError, e:
						raise exceptions.InvalidKey("Could not determine proper key origin library.")

			except exceptions.InvalidKey, e:
				raise
				
			except exceptions.KeyNotFound, e:
				raise
				
			else:
				
				self.setflag('freshness', 'FRESH')
				return Data.ObjectResponse(objects=[self.convert_entity_to_message(r_entity, object_r)], count=1)
				
		elif request.keys is not None and len(request.keys) > 0:
			
			try:
				samplekey = request.keys[0]
				try:
					r_sample_key = model.Key(urlsafe=samplekey)
				except datastore_errors.BadKeyError, e:
					
					try:
						r_sample_key = db.Key(samplekey)
					except datastore_errors.BadKeyError, e:
						raise exceptions.InvalidKey("Could not determine proper key origin library. Invalid key: '"+str(samplekey)+"', at position 0.")
					else:
						resolved_keys = [db.Key(k) for k in request.keys]
						resolved_entities = datastore.Get([str(_key) for _key in resolved_keys])
				else:
					resolved_keys = [model.Key(urlsafe=k) for k in request.keys]
					resolved_entities = datastore.Get([_key.urlsafe() for _key in resolved_keys])
					
					ds_objects = []
					for rs_key, rs_entity in zip(resolved_keys, resolved_entities):
						
						rs_parent = rs_key.parent()
						if rs_parent is not None:
							rs_parent = rs_parent.urlsafe()
						else:
							rs_parent = None
						
						m_dk = Util.DatastoreKey(encoded=rs_key.urlsafe(), parent=rs_parent, kind=rs_key.kind())
						m_object_r = Data.DatastoreObject(key=m_dk)
						ds_objects.append(m_object_r)
					
					resolved_datastore_objects = []
					for rs_key_c, rs_entity_c, rs_object_c in zip(resolved_keys, resolved_entities, ds_objects):
						resolved_datastore_objects.append(self.convert_entity_to_message(rs_entity_c, rs_object_c))
					
			except exceptions.InvalidKey, e:
				raise
				
			else:
				self.setflag('freshness', 'FRESH')				
				return Data.ObjectResponse(objects=resolved_datastore_objects, count=len(resolved_datastore_objects))			
		else:
			raise exceptions.InvalidKey("Must provide a key or list of keys to retrieve.")
	
	@classmethod
	def serialize_property(cls, value, _type=None):
		
		logging.info('Serializing value of type '+str(type(value)))

		if isinstance(value, datastore_types.Blob):
			try: ## check and see if it could be a LocalStructuredProperty...
				pb = datastore.entity_pb.EntityProto()
				pb.MergePartialFromString(value)
				properties_list = pb.property_list()+pb.raw_property_list()
				pb_properties = cls.serialize_properties(zip([i.name() for i in properties_list], [cls.resolve_pb_property_value(p) for p in properties_list]))
				serialized_value = Data.DatastoreObject(key=Util.DatastoreKey(encoded=None, parent=None), properties=pb_properties)
			except:
				serialized_value = base64.b64encode(value)

		elif isinstance(value, (basestring, str, unicode)):
			serialized_value = value
			
		elif isinstance(value, (long, int, bool)):
			serialized_value = value
		
		elif isinstance(value, (key.Key, db.Key)):
			if isinstance(value, key.Key):
				parent_key = value.parent()
				if parent_key is not None:
					parent_key = parent_key.urlsafe()
				serialized_value = Util.DatastoreKey(encoded=value.urlsafe(), parent=parent_key)
			else:
				parent_key = value.parent()
				if parent_key is not None:
					parent_key = str(parent_key)
				serialized_value = Util.DatastoreKey(encoded=str(value), parent=str(parent_key))
		
		elif isinstance(value, (model.Model, db.Model)):
			if isinstance(value, model.Model):
				entity_key = value.key
				if entity_key is not None:
					parent_key = entity_key.parent()
					if parent_key is not None:
						parent_key = parent_key.urlsafe()
					entity = entity_key.get()
				else:
					entity = value
				entity_properties = cls.serialize_properties(zip(entity._properties, [getattr(entity, k) for k in entity._properties]))
				serialized_value = Data.DatastoreObject(properties=entity_properties)
				if entity_key is not None:
					serialized_value.key = Util.DatastoreKey(encoded=entity_key.urlsafe(), parent=parent_key)
				else:
					serialized_value.key = Util.DatastoreKey(encoded=None, parent=None)
			else:
				entity_key = value.key()
				parent_key = entity_key.parent()
				if parent_key is not None:
					parent_key = str(parent_key)
				entity = db.get(entity_key)
				entity_properties = cls.serialize_properties(zip([k for k, v in entity.properties()], [getattr(entity, k) for k, v in entity.properties()]))
				serialized_value = Data.DatastoreObject(key=Util.DatastoreKey(encoded=str(entity_key), parent=parent_key), properties=entity_properties)				
		
		return serialized_value
	

	@classmethod
	def serialize_properties(cls, items):

		properties = {}
		for prop, value in items:

			if value is None: ## empty values
				properties[prop] = None

			elif isinstance(value, list): ## list values

				if len(value) > 0:
					p_values = []
					for v in value:
						value = cls.serialize_property(v, type(v))
						p_values.append(value)
					properties[prop] = p_values
					
				else:
					properties[prop] = None
			else:
				properties[prop] = cls.serialize_property(value)
		
		return properties
	
	@classmethod
	def resolve_pb_property_value(cls, pb_property):

		types = {
		
			'has_booleanvalue': 'booleanvalue',
			'has_doublevalue': 'doublevalue',
			'has_int64value': 'int64value',
			'has_pointvalue': 'pointvalue',
			'has_referencevalue': 'referencevalue',
			'has_stringvalue': 'stringvalue',
		
		}
		
		value = pb_property.value()
		for k in types.keys():
			if getattr(value, k)():
				return getattr(value, types[k])()

	@classmethod
	def convert_entity_to_message(cls, entity, r_object):
		
		
		if 'createdAt' in entity:
			r_object.created = entity['createdAt']
		
		if 'modifiedAt' in entity:
			r_object.modified = entity['modifiedAt']
	
		## Serialize properties
		r_object.properties = cls.serialize_properties(entity.items())
		
		return r_object