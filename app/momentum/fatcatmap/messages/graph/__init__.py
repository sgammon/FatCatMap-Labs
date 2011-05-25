from protorpc import messages
from momentum.fatcatmap.messages.util import DatastoreKey


# ==== Graph Message Structures ==== #
class GraphSchemaItem(messages.Message):

	key = messages.MessageField(DatastoreKey, 1)
	kind = messages.StringField(2)
	scope = messages.StringField(3)
	

class GraphNode(messages.Message):

	key = messages.MessageField(DatastoreKey, 1)
	label = messages.StringField(2)
	kind = messages.StringField(3)
	scope = messages.StringField(4, repeated=True)
	
	
class GraphNodeStub(messages.Message):
	
	key = messages.StringField(1)
	index = messages.IntegerField(2)


class GraphEdge(messages.Message):

	source = messages.IntegerField(2)
	target = messages.IntegerField(3)
	

class GraphHint(messages.Message):
	
	key = messages.MessageField(DatastoreKey, 1)
	nodes = messages.MessageField(GraphNodeStub, 2, repeated=True)
	
	
class Graph(messages.Message):

	nodes = messages.MessageField(GraphNode, 1, repeated=True)
	edges = messages.MessageField(GraphEdge, 2, repeated=True)
	hints = messages.MessageField(GraphHint, 3, repeated=True)


# ==== Graph RPC Message Structures ==== #
class GraphRequest(messages.Message):
	
	origin = messages.StringField(1)
	degree = messages.IntegerField(2, default=1)
	limit = messages.IntegerField(3, default=5)

	
class GraphResponse(messages.Message):

	graph = messages.MessageField(Graph, 1)
	limit = messages.IntegerField(2, default=5)
	degree = messages.IntegerField(3, default=1)
	origin = messages.MessageField(GraphNode, 4)
	schema = messages.MessageField(GraphSchemaItem, 5, repeated=True)	