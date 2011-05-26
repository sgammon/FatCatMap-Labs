import logging
import ndb as n
from protorpc import remote

from momentum.fatcatmap import models as m

from momentum.fatcatmap.models.core.object import Node

from momentum.fatcatmap.messages.util import DatastoreKey

from momentum.fatcatmap.messages.graph import Graph
from momentum.fatcatmap.messages.graph import GraphNode
from momentum.fatcatmap.messages.graph import GraphEdge
from momentum.fatcatmap.messages.graph import GraphHint
from momentum.fatcatmap.messages.graph import GraphRequest
from momentum.fatcatmap.messages.graph import GraphResponse
from momentum.fatcatmap.messages.graph import GraphNodeStub
from momentum.fatcatmap.messages.graph import GraphSchemaItem

from momentum.fatcatmap.core.api.graph.factory import GraphFactory


class GraphAPIService(remote.Service):

	@remote.method(GraphRequest, GraphResponse)
	def construct(self, request):
		
		logging.info('====== GRAPH API SERVICE =====')
		logging.info('Request origin: '+str(request.origin))
		logging.info('Request degree: '+str(request.degree))
		logging.info('Request limit: '+str(request.limit))
		
		if request.origin is not None:
			origin_key = n.key.Key(urlsafe=request.origin)
		else:
			node = Node.query().get()
			origin_key = node.key

		graph, artifacts = GraphFactory(request.degree, request.limit).buildFromNode(origin_key).export_graph()
		
		## Create nodes
		graph_nodes = []
		node_index = {}
		for node in graph.nodes():
			
			k = DatastoreKey(encoded=node['key'].urlsafe(), kind=node['key'].kind())
			if node['key'].parent() is not None:
				k.parent = node['key'].parent().urlsafe()

			g = GraphNode(key=k, label=node['label'], kind=node['type'].id(), scope=node['scope'])
			graph_nodes.append(g)
			node_index[node['key'].urlsafe()] = graph_nodes.index(g)
			
		
		## Create Edges & Hints
		graph_edges, graph_hints = [], []
		edges, hints = graph.edges()
		for edge in edges:
			e = GraphEdge(source=node_index[edge['source']['key'].urlsafe()], target=node_index[edge['target']['key'].urlsafe()])
			graph_edges.append(e)

		for hint in hints:
			k = DatastoreKey(encoded=hint['hint'].urlsafe(), kind=hint['hint'].kind())
			hint_nodes = []
			for node in hint['nodes']:
				hint_nodes.append(GraphNodeStub(key=node['key'].urlsafe(), index=node_index[node['key'].urlsafe()]))

			h = GraphHint(key=k, nodes=hint_nodes)
			graph_hints.append(h)
			
		return GraphResponse(graph=Graph(nodes=graph_nodes, edges=graph_edges, hints=graph_hints))
		
	#@remote.method()
	def constructFromNode(self, request):
		pass
		
	#@remote.method()
	def constructFromObject(self, request):
		pass