from momentum.services.middleware import ServiceGatewayMiddleware


class MonitoringMiddleware(ServiceGatewayMiddleware):

	def before_request(self, service, request, response):
		return (service, request, response)