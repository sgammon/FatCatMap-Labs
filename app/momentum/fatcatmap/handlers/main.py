from momentum.fatcatmap.handlers import WebHandler


class Landing(WebHandler):

	def get(self):

		"""Simply returns a Response object with an enigmatic salutation."""

		return self.render('main/landing.html')
		
		
class Offline(WebHandler):
	
	def get(self):
		return self.render('main/offline.html')