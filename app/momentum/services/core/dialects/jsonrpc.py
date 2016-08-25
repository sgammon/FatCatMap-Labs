import base64
import config
import logging
import datetime

try:
	import json2 as json
except:
	try:
		from django.utils import json
	except:
		import simplejson as json

import protorpc

from protorpc import messages
from protorpc import protojson

from google.appengine.api import users

from protorpc.webapp import service_handlers


class _FCMMessageJSONEncoder(protojson._MessageJSONEncoder):
	
	indent = None
	encoding = 'utf-8'
	sort_keys = True
	allow_nan = True
	ensure_ascii = True
	check_circular = True
	skipkeys = True
	use_decimal = False
	
	current_indent_level = 0
	
	def __init__(self, *args, **kwargs):
		for k, v in kwargs.items():
			setattr(self, k, v)
			
	def default(self, value):
		
		if isinstance(value, messages.Enum):
			return str(value)

		if isinstance(value, messages.Message):
			result = {}
			for field in value.all_fields():
				item = value.get_assigned_value(field.name)
				if item not in (None, [], ()):
					result[field.name] = self.jsonForValue(item)
					if isinstance(item, list): ## for repeated values...
						result[field.name] = [self.jsonForValue(x) for x in item]
					
			else:
				return super(_FCMMessageJSONEncoder, self).default(value)
		else:
			return super(_FCMMessageJSONEncoder, self).default(value)
			
		return result
		
	def jsonForValue(self, value):
		
		if isinstance(value, (basestring, int, float, bool)):
			return value
			
		elif isinstance(value, (datetime.datetime, datetime.date, datetime.time)):
			return str(value)
			
		elif isinstance(value, messages.Message):
			for item in value.all_fields():
				self.jsonForValue(item)
				
		else:
			return str(value)



class FCM_JSONRPC_Mapper(service_handlers.JSONRPCMapper):

	_request = {
	
		'id': None,
		'opts': {},
		'agent': {}
	
	}

	def __init__(self):
		super(FCM_JSONRPC_Mapper, self).__init__()
		
	def encode_request(self, struct):
		encoded = _FCMMessageJSONEncoder().encode(struct)
		return encoded
		
	def build_response(self, handler, response):
		
		try:
			response.check_initialized()
			envelope = self.encode_request(self.envelope(handler._response_envelope, response))

		except messages.ValidationError, err:
			raise ResponseError('Unable to encode message: %s' % err)
		else:
			handler.response.headers['Content-Type'] = "application/json"
			handler.response.out.write(envelope)
			return envelope

		
	def envelope(self, wrap, response):

		sysconfig = config.config.get('momentum.fatcatmap')
		if config.debug:
			debugflag = True
			
		return {

			'id': wrap['id'],
			'status': 'ok',
			
			'response': {
				'content': response,
				'type': str(response.__class__.__name__)
			},
			
			'flags': wrap['flags'],
			'platform': {
				'name': 'FatCatMap',
				'version': '.'.join(map(lambda x: str(x), [sysconfig['version']['major'], sysconfig['version']['minor'], sysconfig['version']['micro']])),
				'build': sysconfig['version']['build'],
				'release': sysconfig['version']['release'],
				'engine': 'Providence/Clarity::v1.1 Embedded'
			}
			
		}


	def decode_request(self, message_type, dictionary):
		
		def decode_dictionary(message_type, dictionary):
			
			message = message_type()
			if isinstance(dictionary, dict):
				for key, value in dictionary.iteritems():
					if value is None:
						message.reset(key)
					continue

					try:
						field = message.field_by_name(key)
					except KeyError:
						# TODO(rafek): Support saving unknown values.
						continue

					# Normalize values in to a list.
					if isinstance(value, list):
						if not value:
							continue
						else:
							value = [value]

						valid_value = []
						for item in value:
							if isinstance(field, messages.EnumField):
								item = field.type(item)
							elif isinstance(field, messages.BytesField):
								item = base64.b64decode(item)
							elif isinstance(field, messages.MessageField):
								item = decode_dictionary(field.type, item)
							elif (isinstance(field, messages.FloatField) and
									isinstance(item, (int, long))):
								item = float(item)
							valid_value.append(item)

					if field.repeated:
						existing_value = getattr(message, field.name)
						setattr(message, field.name, valid_value)
					else:
						setattr(message, field.name, valid_value[-1])
			return message
		
		message = message_type()
		if isinstance(dictionary, list):
			return message
		elif isinstance(dictionary, dict):
			for key, value in dictionary.iteritems():
				if value is None:
					message.reset(key)
					continue

				try:
					field = message.field_by_name(key)
				except KeyError:
					# TODO(rafek): Support saving unknown values.
					continue

				# Normalize values in to a list.
				if isinstance(value, list):
					if not value:
						continue
				else:
					value = [value]

				valid_value = []
				for item in value:
					if isinstance(field, messages.EnumField):
						item = field.type(item)
					elif isinstance(field, messages.BytesField):
						item = base64.b64decode(item)
					elif isinstance(field, messages.MessageField):
						item = decode_dictionary(field.type, item)
					elif (isinstance(field, messages.FloatField) and
							isinstance(item, (int, long))):
						item = float(item)
					valid_value.append(item)

				if field.repeated:
					existing_value = getattr(message, field.name)
					setattr(message, field.name, valid_value)
				else:
					setattr(message, field.name, valid_value[-1])

		return message


	def build_request(self, handler, request_type):

		try:
			request_object = protojson._load_json_module().loads(handler.request.body)
			
			try:
				request_id = request_object['id']
				request_agent = request_object['agent']
				request_body = request_object['request']
				request_opts = request_object['opts']
			except AttributeError, e:
				raise service_handlers.RequestError('Request is missing a valid ID, agent, request opts or request body.')

			self._request['id'] = request_id
			self._request['agent'] = request_agent
			self._request['opts'] = request_opts
			
			handler._response_envelope['id'] = self._request['id']
			
			return self.decode_request(request_type, request_body['params'])

		except (messages.ValidationError, messages.DecodeError), err:
			raise service_handlers.RequestError('Unable to parse request content: %s' % err)