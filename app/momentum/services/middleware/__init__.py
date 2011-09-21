

class ServiceGatewayMiddleware(object):

	debug = False
	opts = {}
	config = {}

	def __init__(self, debug=False, config={}, opts={}):
		self.debug = debug
		self.config = config
		self.opts = opts
		
	def __call__(self, request, reponse):
		raise NotImplemented