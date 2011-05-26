from momentum.platform.handlers.core import CoreHandler


class StartHook(CoreHandler):

	def get(self):
		
		return self.response('SUCCESS')