from momentum.fatcatmap.handlers import WebHandler


class VisualizeLanding(WebHandler):
	
	def get(self):
		return self.render('content/visualize/news.html')