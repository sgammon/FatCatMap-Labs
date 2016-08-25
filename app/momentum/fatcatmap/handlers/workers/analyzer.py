from momentum.fatcatmap.handlers.workers import Worker


class Main(Worker):
	
	def run(self):
		self.response.write('<b>Analyzer.Main</b>')