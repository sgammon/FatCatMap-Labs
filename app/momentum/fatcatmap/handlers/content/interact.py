from momentum.fatcatmap.handlers import WebHandler


class InteractLanding(WebHandler):

	def get(self):

		"""Simply returns a Response object with an enigmatic salutation."""

		return self.render('content/interact/landing.html')