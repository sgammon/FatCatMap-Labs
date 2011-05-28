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
		seen_types = []
		graph_schema = {'node_types': {}, 'edge_types': {}}
		for node in graph.nodes():
			
			k = DatastoreKey(encoded=node['key'].urlsafe(), kind=node['key'].kind())
			if node['key'].parent() is not None:
				k.parent = node['key'].parent().urlsafe()

			g = GraphNode(key=k, label=node['label'], kind=node['type'].id(), scope=node['scope'])
			
			## Add node type if we don't already have it...
			if node['type'].id() not in seen_types:
				seen_types.append(node['type'].id())
				graph_schema['node_types'][node['type'].id()] = {'type': node['type'].kind(), 'path': node['type'].id(), 'key': node['type'].urlsafe()}
			
			graph_nodes.append(g)
			node_index[node['key'].urlsafe()] = graph_nodes.index(g)
			
		
		## Create Edges & Hints
		graph_edges, graph_hints = [], []
		edges, hints = graph.edges()
		for edge in edges:
			e = GraphEdge(source=node_index[edge['source']['key'].urlsafe()], target=node_index[edge['target']['key'].urlsafe()])
			
			## Add node type if we don't already have it...
			if 'type' in edge:
				if edge['type'].id() not in seen_types:
					seen_types.append(edge['type'].id())
					graph_schema['edge_types'][edge['type'].id()] = {'type': edge['type'].kind(), 'path': edge['type'].id(), 'key': edge['type'].urlsafe()}
			
			graph_edges.append(e)


		for hint in hints:
			k = DatastoreKey(encoded=hint['hint'].urlsafe(), kind=hint['hint'].kind())
			hint_nodes = []
			for node in hint['nodes']:
				hint_nodes.append(GraphNodeStub(key=node['key'].urlsafe(), index=node_index[node['key'].urlsafe()]))

			h = GraphHint(key=k, nodes=hint_nodes)
			graph_hints.append(h)
			
			origin = GraphNodeStub(key=graph.origin().urlsafe(), index=node_index[graph.origin().urlsafe()])
			_graph = Graph(origin=origin, nodes=graph_nodes, edges=graph_edges, hints=graph_hints)
			
		return GraphResponse(graph=_graph)
		
	#@remote.method()
	def constructFromNode(self, request):
		pass
		
	#@remote.method()
	def constructFromObject(self, request):
		pass