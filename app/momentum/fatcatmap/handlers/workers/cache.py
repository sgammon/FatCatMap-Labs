from momentum.fatcatmap.handlers.workers import Worker


class Warmup(Worker):
	
	def run(self):	
		self.response.write('<b>Warmup <pre>Routine:'+str(self.kwargs.get('routine', 'None'))+'</pre></b>')