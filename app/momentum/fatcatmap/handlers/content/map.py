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
		args = self.request.arguments()
		if 'n' in args: ## Pull direct node request
			node_key = k.Key(urlsafe=self.request.get('n'))
			node = node_key.get()
			if node is not None:
				rpc['origin'] = self.request.get('n')
			else:
				elements['errorNotice'] = "The specified node key could not be found. :("
				
		if 'o' in args:
			object_key = k.Key(urlsafe=self.request.get('o'))
			object_m = object_key.get()
			if object_m is not None:
				rpc['object'] = self.request.get('o')
			else:
				elements['errorNotice'] = "The specified object key could not be found. :("
				
		if '_nd' in args:
			rpc['depth'] = int(self.request.get('_nd'))
			
		if '_cl' in args:
			rpc['limit'] = int(self.request.get('_cl'))
			
		if '_gs' in args:
			rpc['scope'] = self.request.get('_gs')
			
		if '_vcontext' in args:
			rpc['context'] = self.request.get('_vcontext')

		return self.render('content/map/landing.html', elements=elements, rpc_params=rpc, origin=node)