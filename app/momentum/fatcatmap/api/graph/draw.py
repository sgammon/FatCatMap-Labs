import ndb as n
from momentum.fatcatmap import api
from momentum.fatcatmap import models as m
from momentum.fatcatmap.api.graph import GraphAPIService

from momentum.fatcatmap.core.api.graph import GraphFactory


class GraphDrawService(GraphAPIService):


	def drawFromNode(self, node, limit=5, degree=3):
		graph, artifacts = GraphFactory(degree, limit).buildFromNode(n.key.Key(urlsafe=node))
		return {'data': artifacts, 'graph': graph}