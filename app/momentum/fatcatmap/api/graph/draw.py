import ndb as n
from momentum.fatcatmap import api
from momentum.fatcatmap import models as m
from momentum.fatcatmap.api.graph import GraphAPIService

from momentum.fatcatmap.core.api.graph import GraphFactory

from momentum.fatcatmap.models.core.object import Node


class GraphDrawService(GraphAPIService):


	def drawFromNode(self, node=None, limit=5, degree=3):
		if node is not None:
			graph, artifacts = GraphFactory(degree, limit).buildFromNode(n.key.Key(urlsafe=node))
		else:
			n = Node.query().fetch(1)
			graph, artifacts = GraphFactory(degree, limit).buildFromNode(n[0].key)
		return {'data': artifacts, 'graph': graph}