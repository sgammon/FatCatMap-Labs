import logging
from momentum.services.middleware import ServiceGatewayMiddleware


class AuthenticationMiddleware(ServiceGatewayMiddleware):

	def __call__(self, request, response):
		
		logging.info('REQUEST_HEADERS: '+str(request.headers))
		logging.info('REQUEST_GETVARS: '+str(request.str_queryvars))
				
		return (request, response)
	
	
class AuthorizationMiddleware(ServiceGatewayMiddleware):

	def __call__(self, request, response):
		return (request, response)