from momentum.fatcatmap.handlers import WebHandler


class BrowseLanding(WebHandler):

	def get(self):

		"""Simply returns a Response object with an enigmatic salutation."""

		return self.render('content/browse/landing.html')