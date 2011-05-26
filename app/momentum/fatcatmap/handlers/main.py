from momentum.fatcatmap.handlers import WebHandler


class Landing(WebHandler):

	def get(self):

		"""Simply returns a Response object with an enigmatic salutation."""

		return self.render('main/landing.html')


class Map(WebHandler):

	def get(self):

		"""Simply returns a Response object with an enigmatic salutation."""

		rpc = {}
		if 'n' in self.request.args: ## Pull direct node request
			rpc['origin'] = self.request.args.get('n')

		return self.render('main/map.html', rpc_params=rpc)