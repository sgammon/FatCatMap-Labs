from momentum.fatcatmap.handlers import WebHandler


class MapLanding(WebHandler):

	def get(self):

		"""Simply returns a Response object with an enigmatic salutation."""

		rpc = {}
		if 'n' in self.request.args: ## Pull direct node request
			rpc['origin'] = self.request.args.get('n')

		return self.render('content/map/landing.html', rpc_params=rpc)