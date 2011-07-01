from momentum.services.middleware import ServiceGatewayMiddleware


class MonitoringMiddleware(ServiceGatewayMiddleware):

	def __call__(self, request, response):
		return (request, response)