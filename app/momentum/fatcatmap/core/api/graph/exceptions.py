from momentum.fatcatmap.core.api import exceptions


class GraphAPIException(exceptions.FCMCoreAPIException):
	pass
	
	
class GraphFactoryException(GraphAPIException): pass
class InvalidNode(GraphFactoryException): pass
class InvalidEdge(GraphFactoryException): pass