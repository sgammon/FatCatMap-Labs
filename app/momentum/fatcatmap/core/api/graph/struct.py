from ProvidenceClarity.struct.util import SerializableStruct
from ProvidenceClarity.struct.util import ConfigurableStruct

from momentum.fatcatmap.core.api.graph import exceptions
from momentum.fatcatmap.core.struct.rpc import FCM_RPCResponseStructure
		
	
#### ==== API Structures ===== ####
class FCMGraph(SerializableStruct):
	
	''' An efficient in-memory representation of a graph, made up of vertexes (nodes) and vectors (edges). '''
	
	_nodes = []
	_edges = []
	_objects = {}
	
	def add_node(self, key, **kwargs):
		if key not in self._objects:
			self._nodes.append(key)
			self._objects[key] = {'index':self._nodes.index(key)}
		if len(kwargs) > 0:
			for k, v in kwargs.items():
				self._objects[key][k] = v
				
	def set_node_data(self, node, **kwargs):
		if node not in self._objects:
			raise exceptions.InvalidNode, "Cannot set Node data for invalid node %s." % str(node)
		else:
			for k, v in kwargs.items():
				self._objects[node][k] = v
		
	def add_edge(self, hint, nodes, **kwargs):
		if hint not in self._objects:
			self._edges.append(hint)
			self._objects[hint] = {'nodes':nodes, 'index':self._edges.index(hint)}
		if len(kwargs) > 0:
			for k, v in kwargs.items():
				self._objects[hint][k] = v
				
	def set_edge_data(self, edge, **kwargs):
		if edge not in self._objects:
			raise exceptions.InvalidEdge, "Cannot set Edge data for invalid edge %s." % str(node)
		else:
			for k, v in kwargs.items():
				self._objects[edge][k] = v
				
	def nodes(self):
		nodes = []
		for _node in self._nodes:
			node = {'key':_node}
			for k, v in self._objects[_node].items():
				node[k] = v
			nodes.append(node)
		return nodes
		
	def edges(self):
		edges = []
		hints = []
		seen_edges = []
		for hint in self._edges:
			node_0_key = self._objects[hint]['nodes'][0]
			node_1_key = self._objects[hint]['nodes'][1]
			if (self._objects[node_0_key]['index'], self._objects[node_1_key]['index']) in seen_edges:
				continue
			elif (self._objects[node_1_key]['index'], self._objects[node_0_key]['index']) in seen_edges:
				continue
			else:
				edges.append({'source':self._objects[node_0_key]['index'], 'target':self._objects[node_1_key]['index'], 'value':1})
				hints.append({'hint':hint, 'nodes':[{'key':node_0_key, 'index':self._objects[node_0_key]['index']}, {'key':node_1_key, 'index':self._objects[node_1_key]['index']}]})
				seen_edges.append((self._objects[node_0_key]['index'], self._objects[node_1_key]['index']))
				seen_edges.append((self._objects[node_1_key]['index'], self._objects[node_0_key]['index']))
		return edges, hints
		
	def normalize(self):
		graph = {}
		graph['nodes'] = self.nodes()
		graph['edges'], graph['hints'] = self.edges()
		return graph
	

class FCMGraphAPIResponse(FCM_RPCResponseStructure):

	data = None
	graph = {}