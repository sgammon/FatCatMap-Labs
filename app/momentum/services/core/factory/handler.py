import config
import logging
import protorpc
import webapp2

from momentum.services.core import handler
from momentum.services.core import dialects
from momentum.services.core.dialects import *

from webapp2_extras import protorpc as proto
from protorpc.webapp import service_handlers

from momentum.services.core.factory.service import MomentumServiceFactory

## Service layer middleware cache
_middleware_cache = {}


class MomentumServiceHandlerFactory(proto.ServiceHandlerFactory):
	
	@webapp2.cached_property
	def servicesConfig(self):
		return config.config.get('momentum.services')
	
	def log(self, message):
		if self.servicesConfig['logging'] is True:
			if config.debug:
				message_handler = logging.info
			else:
				message_handler = logging.debug
			message_handler('ServiceHandlerFactory: '+str(message))
			
	def error(self, message):
		logging.error('ServiceHandlerFactory ERROR: '+str(message))
		
	@classmethod	
	def default(cls, service_factory, parameter_prefix=''):
		
		factory = cls(service_factory)
		
		factory.add_request_mapper(service_handlers.ProtobufRPCMapper())
		factory.add_request_mapper(service_handlers.URLEncodedRPCMapper())
		factory.add_request_mapper(dialects.jsonrpc.FCM_JSONRPC_Mapper())
		
		return factory
		
	
	def __call__(self, request, remote_path, remote_method):
		
		global _middleware_cache
		global_debug = config.debug
		
		## Extract response
		response = request.response

		## Manufacture service + handler
		service = self.service_factory()
		service._initializeMomentumService()

		## Consider service middleware
		middleware = self.servicesConfig.get('middleware', False)
		if middleware is not False and len(middleware) > 0:
			
			for name, cfg in middleware:
				self.log('Considering '+str(name)+' middleware...')
				if cfg['enabled'] is True:
					try:
						if name not in _middleware_cache or config.debug:
							middleware_class = webapp2.import_string(cfg['path'])
						else:
							middleware_class = _middleware_cache[name]
							
						middleware_object = middleware_class(debug=cfg['debug'], config=self.servicesConfig, opts=cfg.get('args', {}))
						service.middleware[name] = middleware_object
						
						if hasattr(middleware_object, 'before_request'):
							service, request, response = middleware_object.before_request(service, request, response)
							continue
						else:
							self.log('Middleware '+str(name)+' does not have pre_request method. Continuing.')
							continue
						
					except Exception, e:
						self.error('Middleware "'+str(name)+'" raise an unhandled exception of type "'+str(e)+'".')
						if config.debug:
							raise
						else:
							continue
						
				else:
					self.log('Middleware '+str(name)+' is disabled.')
					continue
		else:
			self.log('Middleware was none or 0.')
			
		service_handler = MomentumServiceFactory.new(handler.MomentumServiceHandler(self, service))
		service_handler.request = request
		service_handler.response = response
		
		self.log('Handler prepared. Dispatching...')
		
		service_handler.dispatch(self, service)