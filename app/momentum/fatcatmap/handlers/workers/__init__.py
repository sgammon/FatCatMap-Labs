from momentum.fatcatmap.handlers import WebHandler


class Worker(WebHandler):

	args = []
	kwargs = {}
	
	def get(self, *args, **kwargs):
		self.args = args
		self.kwargs = kwargs
		return self.run()

	def post(self, *args, **kwargs):
		self.args = args
		self.kwargs = kwrags
		return self.run()		
	
	
class Main(Worker):
	
	def run(self, *args):
		self.response.write('<b>Main</b>')