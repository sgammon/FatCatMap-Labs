import config
import logging
import protorpc

import webapp2

from protorpc import remote
from protorpc import webapp
from protorpc.webapp import service_handlers

from werkzeug import import_string
from werkzeug import cached_property

from webapp2_extras import protorpc as proto

global_debug = config.debug
_middleware_cache = {}



## Expose service flags (middleware decorators)
flags = DictProxy({

	'audit': DictProxy({
		'monitor': audit.Monitor,
		'debug': audit.Debug,
		'loglevel': audit.LogLevel,
	}),
	
	'caching': DictProxy({
		'local': caching.LocalCacheable,
		'memcache': caching.MemCacheable,
		'cacheable': caching.Cacheable,
	}),
	
	'security': DictProxy({
		'authorize': security.Authorize,
		'authenticate': security.Authenticate,
		'admin': security.AdminOnly
	})

})


## Top-Level Service Class
class MomentumService(remote.Service):
	
	''' Top-level parent class for ProtoRPC-based API services. '''
	
	middleware = {}
	state = {'request': {}, 'opts': {}, 'service': {}}
	config = {'global': {}, 'module': {}, 'service': {}}

	@cached_property
	def globalConfig(self):
		return config.config.get('momentum.services')
		
	def __init__(self, *args, **kwargs):
		super(MomentumService, self).__init__(*args, **kwargs)
		
	def initiate_request_state(self, state):
		super(MomentumService, self).initiate_request_state(state)

	def _initializeMomentumService(self):

		##### ==== Step 1: Copy over global, module, and service configuration ==== ####
		
		## Copy global config
		self.config['global'] = self.globalConfig
		
		## Module configuration
		if hasattr(self, 'moduleConfigPath'):
			self.config['module'] = config.config.get(getattr(self, 'moduleConfigPath', '__null__'), {})

			## If we have a module + service config path, pull it from the module's branch
			if hasattr(self, 'configPath'):
				path = getattr(self, 'configPath').split('.')
				if len(path) > 0:
					fragment = self.config['module']
					for i in xrange(0, len(path)-1):
						if path[i] in fragment:
							fragment = fragment[path[i]]
					if isinstance(fragment, dict):
						self.config['service'] = fragment

		## No module configuration
		else:
			## Copy over default module config
			self.config['module'] = self.config['global']['defaults']['module']
			
			## If we have a service config path but no module config path...
			if hasattr(self, 'configPath'):
				## Try importing it as a top-level namespace
				toplevel = config.config.get(self.configPath, None)
				if toplevel is None:
					## If that doesn't work, copy it over from defaults...
					self.config['service'] = self.config['global']['defaults']['service']
				else:
					self.config['service'] = toplevel
					
			else:
				## If we have nothing, copy over defaults...
				self.config['service'] = self.config['global']['defaults']['service']
				

		##### ==== Step 2: Check for an initialize hook ==== ####
		if hasattr(self, 'initialize'):
			self.initialize()
		
	def _setstate(self, key, value):
		self.state['service'][key] = value
		
	def _getstate(self, key, default):
		if key in self.state['service']:
			return self.state['service'][key]
		else: return default
		
	def _delstate(self, key):
		if key in self.state['service']:
			del self.state['service'][key]
		
	def __setitem__(self, key, value):
		self._setstate(key, value)
		
	def __getitem__(self, key):
		return self._getstate(key, None)
		
	def __delitem__(self, key):
		self._delstate(key)

	def __repr__(self):
		return '<MomentumService::'+'.'.join(self.__module__.split('.')+[self.__class__.__name__])+'>'
		

class MomentumServiceHandler(webapp2.RequestHandler, service_handlers.ServiceHandler):

	@cached_property
	def servicesConfig(self):
		return config.config.get('momentum.services')
		
	def log(self, message):
		if self.servicesConfig['logging'] is True:
			if config.debug:
				handler = logging.info
			else:
				handler = logging.debug
			handler('ServiceHandler: '+str(message))

	def error(self, message):
		logging.error('ServiceHandler ERROR: '+str(message))
				
	def run_post_action_middleware(self, service):
		
		global global_debug
		global _middleware_cache
		
		middleware = self.servicesConfig.get('middleware', False)
		if middleware is not False and len(middleware) > 0:
			
			for name, middleware_object in service.middleware.items():
				self.log('Considering '+str(name)+' middleware...')
				try:
						
					if hasattr(middleware_object, 'after_request'):
						middleware_object.after_request(self.service, self.request, self.response)
						continue
					else:
						self.log('Middleware '+str(name)+' does not have after_request method. Continuing.')
						continue
						
				except Exception, e:
					self.error('Middleware "'+str(name)+'" raised an unhandled exception of type "'+str(e)+'".')
					if config.debug:
						raise
					continue

		else:
			self.log('Middleware is none or 0.')
			

	def dispatch(self, factory, service):
		# Unfortunately we need to access the protected attributes.
		self._ServiceHandler__factory = factory
		self._ServiceHandler__service = service

		request = self.request
		request_method = request.method
		method = getattr(self, request_method.lower(), None)
		service_path, remote_method = request.route_args
		if method:
			self.handle(request_method, service_path, remote_method)
			self.run_post_action_middleware(service)
		else:
			message = 'Unsupported HTTP method: %s' % request_method
			logging.error(message)
			self.response.status = '405 %s' % message

		if request_method == 'GET':
			status = self.response.status_int
			if status in (405, 415) or not request.content_type:
				# Again, now a protected method.
				self._ServiceHandler__show_info(service_path, remote_method)


class MomentumServiceHandlerFactory(proto.ServiceHandlerFactory):
	
	@cached_property
	def servicesConfig(self):
		return config.config.get('momentum.services')
	
	def log(self, message):
		if self.servicesConfig['logging'] is True:
			if config.debug:
				handler = logging.info
			else:
				handler = logging.debug
			handler('ServiceHandlerFactory: '+str(message))
			
	def error(self, message):
		logging.error('ServiceHandlerFactory ERROR: '+str(message))
	
	def __call__(self, request, remote_path, remote_method):
		
		global global_debug
		global _middleware_cache
		
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
							middleware_class = import_string(cfg['path'])
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
			
		handler = MomentumServiceHandler(request, response)
		handler.dispatch(self, service)