import hashlib
import logging

from tipfy import Response

from tipfy.ext.jsonrpc import JSONRPCMixin
from lovely.jsonrpc.dispatcher import JSONRPCDispatcher

from momentum.fatcatmap.handlers import WebHandler
from momentum.fatcatmap.core.adapters.format.json import FCMJSONAdapter

_api_services = {}


class FatcatmapAPIDispatcher(WebHandler, JSONRPCMixin):
	
	
	def dispatchAPICall(self, module, service, method, format, http_method):
		
		global _api_services
		service_path = '.'.join(['momentum','fatcatmap','api', module, service, str(module).capitalize()+str(service).capitalize()+'Service'])
		if service_path in _api_services:
			api_module = _api_services[api_module]
		else:
			api_module = __import__('.'.join(service_path.split('.')[0:-1]), globals(), locals(), [service_path.split('.')[-1]])
			api_module = getattr(api_module, service_path.split('.')[-1])()


		logging.info('=============== API DISPATCHER ===============')
		logging.info('--Module: '+str(module))
		logging.info('--Service: '+str(service))
		logging.info('--Method: '+str(method))
		logging.info('--Format: '+str(format))
		logging.info('--HTTP Method: '+str(http_method))
		logging.info('--Request Data: '+str(self.request.data))
			
		## Set JSONRPC params
		self.jsonrpc_service = api_module
	
		logging.info('--Service: '+str(self.jsonrpc_service))
		logging.info('--Name: '+str(self.jsonrpc_name))
		logging.info('--Summary: '+str(self.jsonrpc_summary))
		logging.info('=== RUNNING DISPATCHER ===')
	
		res = self.json_rpc_dispatcher().dispatch(self.request.data)
	
		logging.info('--Result: '+str(res))
		logging.info('Finished request. Responding.')
		response = FCMJSONAdapter().dumps(res)
		
		return Response(str(response), mimetype='application/json')
				
	def json_rpc_dispatcher(self):
		return JSONRPCDispatcher(instance=self.jsonrpc_service,
								 name=self.jsonrpc_name,
								 summary=self.jsonrpc_summary,
								 help=self.jsonrpc_help,
								 address=self.jsonrpc_address,
								 json_impl=FCMJSONAdapter)

		
	# =============== MAP HTTP METHODS TO DISPATCHER =============== #
	def get(self, module, service=None, method=None, format='json'):
		return self.dispatchAPICall(module, service, method, format, 'GET')
		
	def post(self, module, service=None, method=None, format='json'):
		return self.dispatchAPICall(module, service, method, format, 'POST')
		
	def put(self, module, service=None, method=None, format='json'):
		return self.dispatchAPICall(module, service, method, format, 'PUT')
		
	def delete(self, module, service=None, method=None, format='json'):
		return self.dispatchAPICall(module, service, method, format, 'DELETE')
		
	def options(self, module, service=None, method=None, format='json'):
		return self.dispatchAPICall(module, service, method, format, 'OPTIONS')
		
	def head(self, module, service=None, method=None, format='json'):
		return self.dispatchAPICall(module, service, method, format, 'HEAD')
		
	def trace(self, module, service, method=None, format='json'):
		return self.dispatchAPICall(module, service, method, format, 'TRACE')