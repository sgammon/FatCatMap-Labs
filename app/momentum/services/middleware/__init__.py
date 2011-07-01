

class ServiceGatewayMiddleware(object):

	debug = False
	config = {}

	def __init__(self, debug=False, config={}):
		self.debug = debug
		self.config = config
		
	def __call__(self, request, reponse):
		raise NotImplemented