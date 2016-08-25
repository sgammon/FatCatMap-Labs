from momentum.fatcatmap.handlers import WebHandler


class SearchLanding(WebHandler):

	def get(self):

		"""Simply returns a Response object with an enigmatic salutation."""

		return self.render('content/search/landing.html')