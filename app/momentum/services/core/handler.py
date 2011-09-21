import config
import logging
import werkzeug

from protorpc.webapp import service_handlers


class MomentumServiceHandler(service_handlers.ServiceHandler):

	## == Request/Response Containers == ##
	_response_envelope = {
	
		'id': None,
		'flags': {},
		'status': 'fail'
	
	}


	## == Config == ##
	@werkzeug.cached_property
	def servicesConfig(self):
		return config.config.get('momentum.services')


	## == Log Management == #
	def log(self, message):
		if self.servicesConfig['logging'] is True:
			if config.debug:
				handler = logging.info
			else:
				handler = logging.debug
			handler('ServiceHandler: '+str(message))

	def error(self, message):
		logging.error('ServiceHandler ERROR: '+str(message))
	

	## == Response Flags == ##
	def setflag(self, name, value):
		self._response_envelope['flags'][name] = value
		return
		
	def getflag(self, name):
		if name in self._response_envelope['flags']:
			return self._response_envelope['flags'][name]
		else:
			return None
		
	def getflags(self):
		return self._response_envelope['flags']


	## == Envelope Access == ##
	def setstatus(self, status):
		self._response_envelope['status'] = status
		return
		
	def getstatus(self):
		return self._response_envelope['status']
		
	def setid(self, id):
		self._response_envelope['id'] = id
		return
		
	def getid(self):
		return self._response_envelope['id']

	
	## == Middleware == ##
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
			

	## == Remote method execution == ##
	def dispatch(self, factory, service):
		# Unfortunately we need to access the protected attributes.
		self._ServiceHandler__factory = factory
		self._ServiceHandler__service = service

		## Link the service and handler both ways so we can pass stuff back and forth
		service.handler = self

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