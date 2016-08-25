from momentum.fatcatmap.handlers.workers import Worker


class Main(Worker):
	
	def run(self):	
		self.response.write('<b>Crawler.Main</b>')