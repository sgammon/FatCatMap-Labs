import logging
from momentum.services.middleware import ServiceGatewayMiddleware


class CachingMiddleware(ServiceGatewayMiddleware):
	
	def before_request(self, service, request, response):
		return (service, request, response)


	def after_request(self, service, request, response):
		pass