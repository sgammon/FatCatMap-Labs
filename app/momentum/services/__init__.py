import config
import logging

from werkzeug import import_string
from webapp2_extras import protorpc


_services_cfg = config.config.get('momentum.services')


class MomentumServiceHandler(protorpc.ServiceHandler):
	pass


class MomentumServiceHandlerFactory(protorpc.ServiceHandlerFactory):
	
	def log(self, message):
		if _services_cfg['logging'] is True:
			logging.debug('ServiceHandlerFactory: '+str(message))
			
	def error(self, message):
		logging.error('ServiceHandlerFactory ERROR: '+str(message))
	
	def __call__(self, request, response):

		## Consider service middleware
		middleware = _services_cfg.get('middleware', False)
		if middleware is not False and len(middleware) > 0:
			
			for name, config in middleware:
				self.log('Considering '+str(name)+' middleware...')
				if config['enabled'] is True:
					try:
						middleware_class = import_string(config['path'])
						middleware_object = middleware_class(debug=config['debug'], config=config.get('args', {})) 
						request, response = middleware_object(request, response)
					except Exception, e:
						self.error('Middleware "'+str(name)+'" raise an unhandled exception of type "'+str(Exception)+'".')
						continue
			
		handler = MomentumServiceHandler(request, response)
		handler.dispatch(self, self.service_factory())