import logging
import ndb as n
import simplejson as json

from google.appengine.ext import db

from ProvidenceClarity.struct.util import ConfigurableStruct
from ProvidenceClarity.struct.util import SerializableStruct

from momentum.fatcatmap import models as m
from momentum.fatcatmap.core.adapters.format import FormatAdapter


###### ========== Key/Model Encoders ========== ######
def encodeKey(key):

	if isinstance(key, n.key.Key):
		return {'type': ('NDB', 'KEY'), 'value': key.urlsafe(), 'pairs':key.pairs(), 'kind':key.kind(), 'namespace':key.namespace(), 'parent': key.parent(), 'id':key.pairs()[-1][-1]}
			
	elif isinstance(key, db.Key):
		return {'type': ('LDB', 'KEY'), 'value': str(key), 'kind':key.kind(), 'namespace':key.namespace(), 'parent':key.parent(), 'id':key.id_or_name()}

	
def encodeModel(model):

	struct = {'key':None, 'properties':{}}
	struct['key'] = encodeKey(model.key)
	if isinstance(model, n.model.Model):
		## Calculate model properties and schema
		struct['type'] = ('NDB', 'MODEL')
						
		struct['properties'] = {}
		for k, v in model._properties.items():
			struct['properties'][k] = getattr(model, k)
		
	elif isinstance(model, db.Model):
		struct['type'] = ('LDB', 'MODEL')
		
		p = model.properties()
		for k, v in p.items():
			struct['schema'].append({'name':k, 'type': str(v.__class__.__name__)})
		
		struct['schema'] = [(k, str(v)) for k, v in model.properties().items()]
		struct['properties'] = {}
		for k, v in model.properties().items():
			struct['properties'][k] = getattr(model, k)
	
	return struct


###### ========== Encoder Middleware ========== ######
_encoder = None
class FCMJSONEncoderMiddleware(json.JSONEncoder, ConfigurableStruct):

	def default(self, o):
		if isinstance(o, (n.model.Model, db.Model)):
			return encodeModel(o)
		elif isinstance(o, (n.key.Key, db.Key)):
			return encodeKey(o)
		elif isinstance(o, SerializableStruct):
			return o.normalize()
		else:
			return o
			
	
	@classmethod
	def _loadEncoder(cls):
		global _encoder
		if _encoder is not None:
			return _encoder
		else:
			_encoder = cls(ensure_ascii=False)
		return _encoder
	
	@classmethod
	def _encodeToJSON(cls, input_s, **kwargs):
		return cls._loadEncoder().encode(input_s, **kwargs)


###### ========== Decoder Middleware ========== ######
_decoder = None
class FCMJSONDecoderMiddleware(json.JSONDecoder, ConfigurableStruct):

	@classmethod
	def decode_object(cls, o):
		logging.info('DEFAULT CALLED WITH OBJECT: '+str(o))
		return o
		
	@classmethod
	def _loadDecoder(cls):
		global _decoder
		if _decoder is not None:
			return _decoder
		else:
			_decoder = FCMJSONDecoderMiddleware()
		return _decoder
	
	@classmethod
	def _decodeFromJSON(cls, input_s, **kwargs):
		return cls()._loadDecoder().decode(input_s, **kwargs)
		

###### ======== JSON Adapter Interface ======== ######
class FCMJSONAdapter(FormatAdapter):

	encoder = FCMJSONEncoderMiddleware
	decoder = FCMJSONDecoderMiddleware
	
	
	def encode(self, s_input=None, **kwargs):
		if s_input is not None:
			self.set_input(s_input)
		self.set_output(self.encoder._encodeToJSON(self.get_input(), **kwargs))
		return self
	
	def decode(self, s_input=None, **kwargs):
		if s_input is not None:
			self.set_input(s_input)
		self.set_output(self.decoder._decodeFromJSON(self.get_input(), **kwargs))
		return self
	
	@classmethod
	def loads(cls, s_input, **kwargs):
		return cls.decode_and_adapt(s_input, **kwargs)
	
	@classmethod
	def dumps(cls, s_input, **kwargs):
		return cls.adapt_and_encode(s_input, **kwargs)