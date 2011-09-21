from momentum.fatcatmap.handlers.workers import Worker


class FetchExternal(Worker):
	
	def run(self):	
		self.response.write('<b>Fetch <Routine:'+str(self.kwargs.get('routine', 'None'))+'></b>')