import logging
from momentum.services.middleware import ServiceGatewayMiddleware


class AuthenticationMiddleware(ServiceGatewayMiddleware):

	def before_request(self, service, request, response):
		
		logging.info('SERVICE: '+str(service))
		logging.info('REQUEST_TOKEN: '+str(request.GET.get('token', '_NOTOKEN_')))
				
		return (service, request, response)
	
	
class AuthorizationMiddleware(ServiceGatewayMiddleware):

	def before_request(self, service, request, response):
		return (service, request, response)