from momentum.fatcatmap.handlers import WebHandler


class Index(WebHandler):
	
	def get(self):
		return self.render('admin/index.html')