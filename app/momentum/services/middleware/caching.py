import os
import logging
import hashlib

from momentum.fatcatmap.core.api.cache import CoreCacheAPI
from momentum.services.middleware import ServiceGatewayMiddleware


class CachingMiddleware(ServiceGatewayMiddleware):
	
	key = None	
	ttl = None
	profile = None
	
	def generateKey(self, service, request, localize=False):

		## Add service class, request URI, method and body
		request_descriptor = [service.__repr__(), request.uri, request.method, request.body]
		
		## Add GET and POST vars if they exist
		if len(request.GET) > 0: request_descriptor.append(str(request.GET)) ## Add getvars
		if len(request.POST) > 0: request_descriptor.append(str(request.POST)) ## Add postvars
		
		return hashlib.sha256(reduce(lambda x, y: x+':::'+y, request_descriptor)).hexdigest()
	
	def before_request(self, service, request, response):
		
		if 'caching' in service.config.get('service')['config']:
			self.profile = self.config['middleware_config']['caching']['profiles'][service.config['service']['config']['caching']]
			
			logging.info('CACHING PROFILE: '+str(self.profile))
			
			if self.profile['activate']['internal'] is True or self.profile['activate']['response'] is True:
				self.key = self.generateKey(service, request, self.profile.get('localize', False))
				service._setstate('cache_key', self.key)
			else:
				logging.info('CACHING NOT ACTIVATED')
				
		else:
			logging.info('NO CACHING IN '+str(service.config.get('service')))
		
		return (service, request, response)


	def after_request(self, service, request, response):
		pass
