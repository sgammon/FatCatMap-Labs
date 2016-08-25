from protorpc import messages
from momentum.fatcatmap.messages.util import DatastoreKey

# ==== Type Message Structures ==== #
class GraphVertexType(messages.Message):
	
	key = messages.MessageField(DatastoreKey, 1)


class GraphVectorType(messages.Message):
	
	key = messages.MessageField(DatastoreKey, 1)
	

class GraphArtifactTypeStub(messages.Message):
	
	key = messages.StringField(1)
	path = messages.StringField(2)


# ==== Graph Message Structures ==== #
class MediaStub(messages.Message):
	
	key = messages.MessageField(DatastoreKey, 1)
	name = messages.StringField(2)
	href = messages.StringField(3)
	

class GraphSchemaItem(messages.Message):

	key = messages.MessageField(DatastoreKey, 1)
	kind = messages.StringField(2)
	scope = messages.StringField(3)


class GraphVertex(messages.Message):
	
	key = messages.MessageField(DatastoreKey, 1)
	label = messages.StringField(2)


class GraphNode(messages.Message):

	key = messages.MessageField(DatastoreKey, 1)
	label = messages.StringField(2)
	kind = messages.StringField(3)
	scope = messages.StringField(4, repeated=True)
	media = messages.MessageField(MediaStub, 5, repeated=True)
	type = messages.MessageField(GraphArtifactTypeStub, 6)
	
	
class GraphNodeStub(messages.Message):
	
	key = messages.StringField(1)
	index = messages.IntegerField(2)
	

class GraphEdge(messages.Message):

	source = messages.IntegerField(1)
	target = messages.IntegerField(2)
	kind = messages.MessageField(GraphArtifactTypeStub, 3)	
	

class GraphHint(messages.Message):
	
	key = messages.MessageField(DatastoreKey, 1)
	nodes = messages.MessageField(GraphNodeStub, 2, repeated=True)
	

class GraphArtifactTypeSpec(messages.Message):
	
	vertex_types = messages.MessageField(GraphVertexType, 1, repeated=True)
	vector_types = messages.MessageField(GraphVectorType, 2, repeated=True)
	
	
class Graph(messages.Message):

	vertices = messages.MessageField(GraphNode, 1, repeated=True)
	vectors = messages.MessageField(GraphEdge, 2, repeated=True)
	hints = messages.MessageField(GraphHint, 3, repeated=True)
	origin = messages.MessageField(GraphNodeStub, 4)


# ==== Graph RPC Message Structures ==== #
class VertexFilter(messages.Message):
	pass
	
	
class VectorFilter(messages.Message):
	pass
	

class GraphRequest(messages.Message):
	
	origin = messages.StringField(1)
	depth = messages.IntegerField(2, default=1)
	limit = messages.IntegerField(3, default=4)
	scope = messages.StringField(4, default='global')
	context = messages.StringField(5)
	vertexFilters = messages.MessageField(VertexFilter, 6, repeated=True)
	vectorFilters = messages.MessageField(VectorFilter, 7, repeated=True)

	
class GraphResponse(messages.Message):

	graph = messages.MessageField(Graph, 1)
	limit = messages.IntegerField(2, default=10)
	degree = messages.IntegerField(3, default=3)
	origin = messages.MessageField(GraphNodeStub, 4)
	schema = messages.MessageField(GraphSchemaItem, 5, repeated=True)	