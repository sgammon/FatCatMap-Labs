from google.appengine.api import users
from momentum.fatcatmap.handlers import WebHandler


class Landing(WebHandler):

	def get(self):

		"""Simply returns a Response object with an enigmatic salutation."""

		if users.get_current_user() is None:
			username = 'stranger'
			
		else:
			username = users.get_current_user().nickname()

		return self.render('main/landing.html', name=username)
		
		
class Offline(WebHandler):
	
	def get(self):
		return self.render('main/offline.html')