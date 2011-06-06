from ndb import key as k

from momentum.fatcatmap.handlers import WebHandler

from momentum.fatcatmap.models.core.object import Node
from momentum.fatcatmap.models.core.object import Object


class MapLanding(WebHandler):

	def get(self):

		""" Renders a graph, given a starting node. """

		rpc = {}
		node = None
		elements = {}
		if 'n' in self.request.args: ## Pull direct node request
			node_key = k.Key(urlsafe=self.request.args.get('n'))
			node = node_key.get()
			if node is not None:
				rpc['origin'] = self.request.args.get('n')
			else:
				elements['errorNotice'] = "The specified node key could not be found. :("
				
		if 'o' in self.request.args:
			object_key = k.Key(urlsafe=self.request.args.get('o'))
			object_m = object_key.get()
			if object_m is not None:
				rpc['object'] = self.request.args.get('o')
			else:
				elements['errorNotice'] = "The specified object key could not be found. :("

		return self.render('content/map/landing.html', elements=elements, rpc_params=rpc, origin=node)