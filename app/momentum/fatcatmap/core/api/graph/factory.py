import config
import logging

from ndb import query as q
from ndb import model as n
from ndb import context as c
from ndb import tasklets as t

from werkzeug import cached_property

from momentum.fatcatmap import models as m
from momentum.fatcatmap.core.api import MomentumCoreAPI

from momentum.fatcatmap.models.core import native as e
from momentum.fatcatmap.models.core import object as o
from momentum.fatcatmap.models.core import relation as r

from ProvidenceClarity.struct.util import ConfigurableStruct

from momentum.fatcatmap.core.api.graph import GraphAPI

from momentum.fatcatmap.core.api.graph.struct import Node as FCMNode
from momentum.fatcatmap.core.api.graph.struct import Edge as FCMEdge
from momentum.fatcatmap.core.api.graph.struct import Graph as FCMGraph


_graph_cache = None

class GraphFactory(GraphAPI, ConfigurableStruct):
	
	"""		
			=====================================================
			------------ FatCatMap Recursive Grapher ------------
			-----------------------------------------------------
			| Information:										|
			-----------------------------------------------------
			| 	Version: 2.3									|
			| 	Author: Sam Gammon <sam@momentum.io>  			|
			| 	Description: This library recursively builds an	|
			| 		efficient in-memory graph data structure	|
			|		suitable for serialization and storage.		|
			-----------------------------------------------------
			| Change Log:										|
			-----------------------------------------------------
			|   -Version 2.3 // 8-28-2011 // sam:				|
			|		Fixed and improved debug tools, filled in	|
			|		methods for thread-local caching, filled	|
			|		out methods for constructing different		|
			|		graphs and structures via Objects.
			|	-Version 2.2 // 5-23-2011 // sam:				|
			|		Adding compatibility with ProtoRPC, adding	|
			|		ability to pull Objects and Natives.		|
			|	-Version 2.1 // 3-19-2011 // sam:				|
			|		First port from early prototypes of FCM,	|
			|		converted algorithm to work with NDB		|
			-----------------------------------------------------
			-----------------------------------------------------			
			=====================================================
	"""

	_query = {}
	_cache = {}
	_graph = None
	_schema = {}
	_artifacts = {}
	_current_depth = 0


	######## ======== Util Methods ======== ########
	def __init__(self, **kwargs):
		
		''' Init - copies grapher cache to internal graph structure (if one exists in thread memory) and binds config from kwargs. '''

		if len(kwargs) > 0:
			for c_key, c_value in kwargs.items():
				self.config[c_key] = c_value

		self.load_cache()
		if len(kwargs) > 0:
			self.bind_config(kwargs)


	@cached_property
	def FactoryConfig(self):
		return config.config.get('momentum.fatcatmap.core.graph.factory')
			

	def load_cache(self):

		''' Load cached Graph items. '''
		
		return None
		
		
	def send_to_cache(self):
		
		''' Save Graph items on the current object to the local instance cache. '''
		
		return None
			

	@t.tasklet
	def fill_artifacts(self):
		
		''' Converts keys in the _artifacts property to full models. '''
		
		if self.FactoryConfig.get('debug', False):		
			logging.info('======Filling artifacts.')
		
		for key, value in self._artifacts.items():
			
			if self.FactoryConfig.get('debug', False):
				logging.info('=========Examining artifact \''+str(key)+'\'...')
			
			if key not in self._cache:
				
				## If the artifact is a Node (only one key)...
				if isinstance(value, n.Key):
					self._cache[key] = value.get_async()
					
				## If the artifact is an Edge (tuple of two keys)...
				elif isinstance(value, tuple):
					source, target = self._artifacts[key]
					self._cache[key] = source.get_async(), target.get_async()
			
		for key, value in self._artifacts.items():
			if isinstance(value, n.Model):
				continue
				
			elif isinstance(value, n.Key):
				if key in self._cache:
					self._artifacts[key] = self._cache[key].get_result()  
				
			elif isinstance(value, tuple):
				self._artifacts[key] = self._cache[key][0].get_result(), self._cache[key][1].get_result()
				
		for key, value in self._artifacts.items():
			if isinstance(value, m.NDBModel):
				if isinstance(value, o.Node):
					self._graph.set_node_data(value.key, type=value.type, label=value.label, scope=value.scope, native=False)
				
		raise t.Return(self)


	def flush_graph(self):
		
		''' Prepares the factory to create a new graph object. '''
		
		self._graph = FCMGraph()
		return self._graph
		

	def export_graph(self):
		
		''' Returns a NetworkX graph object representing the Graph, and a dict of database records represented in the Graph.  '''
		
		return (self._graph, self._artifacts)
	

	def EdgeHintQuery(self, node_key, n_limit):

		''' Tasklet that generates a Query object to pull edge hints for a node. '''
		
		if isinstance(node_key, m.NDBModel):
			node_key = node_key.key
		hint_query = r.EdgeHint.query(ancestor=node_key)
		hint_opts = q.QueryOptions(limit=n_limit, keys_only=True, deadline=3)
		return hint_opts, hint_query		
	

	#### ==== Mid-Level Methods ==== ####
	def encounterNode(self, node, **kwargs):
		
		''' Add/update a node in the '_graph' and '_artifacts'. '''
		
		## Add to artifacts, graph object on first encounter
		if isinstance(node, m.NDBModel):
			node_key = node.key
		else:
			node_key = node
				
		if node_key not in self._artifacts:
			
			if self.FactoryConfig.get('debug', False):			
				logging.info('=========Adding node to artifacts...')
			
			self._artifacts[node_key] = node
			if self._graph is None:
				self.flush_graph()
			
			if self.FactoryConfig.get('debug', False):			
				logging.info('=========Adding node to graph object...')
				
			self._graph.add_node(node_key, native=None, type=None, label=None, scope=None)		
	

	def encounterHint(self, hint, **kwargs):
		
		''' Add/update an edge in the '_graph' and '_artifacts', based on an EdgeHint record. '''
		
		## Add to artifacts, graph object on first encounter
		if isinstance(hint, m.NDBModel):
			hint_key = hint.key
		else:
			hint_key = hint
			
		if hint_key not in self._artifacts:

			if self.FactoryConfig.get('debug', False):
				logging.info('=========Adding hint to artifacts...')

			## Retrieve edge parent for source, key name for target
			source = hint.parent()
			target = n.Key(urlsafe=hint.pairs()[-1][1])

			if self.FactoryConfig.get('debug', False):
				logging.info('=========Source: '+str(source))
				logging.info('=========Target: '+str(target))

			self._artifacts[hint_key] = (source, target)
			if self._graph is None:
				self.flush_graph()
			
			if self.FactoryConfig.get('debug', False):			
				logging.info('=========Adding hint to graph object...')
							
			## Add to graph
			self._graph.add_edge(hint_key, [source.urlsafe(), target.urlsafe()], native=None, type=None)
			
			return source, target
			
		else:
			return self._artifacts[hint_key]	
	

	@t.tasklet
	def traverseNode(self, node_key, depth=0, **kwargs):
		
		''' Encounter and traverse through a node, possibly with a recursive call for that node's edge-connected nodes. '''
		
		if self.FactoryConfig.get('debug', False):
			logging.info('======Traversing node '+str(node_key)+'...')
			logging.info('======Depth: '+str(depth))

		# Graph depth must be more than 0, if it is not unset
		if self.config['depth'] is not None and self.config['depth'] < 1:
			raise ValueError, "Graph depth must be greater than 0."
			
		self.encounterNode(node_key, **kwargs)
		q_options, query = self.EdgeHintQuery(node_key, self.config['limit'])

		for hint in query.iter(options=q_options):
			source, target = self.encounterHint(hint)
			if depth is None or self.config['depth'] > depth: ## Recurse
			
				if self.FactoryConfig.get('debug', False):
					logging.info('======Depth is greater than depth. Recursing.')
			
				yield self.traverseNode(target, depth+1)
			else:

				if self.FactoryConfig.get('debug', False):				
					logging.info('======Depth is not greater than depth. Returning.')
				
				raise t.Return(self)



	#### ==== High Level Methods ==== ####
	@c.toplevel
	def buildFromNode(self, node_key, **kwargs):
		
		''' Build a graph from an origin node key. '''
		
		if self.FactoryConfig.get('debug', False):
			logging.info('===================== Build from Node =====================')
			logging.info('NodeKey: '+str(node_key))
			logging.info('Limit: '+str(self.config['limit']))
			logging.info('Depth: '+str(self.config['depth']))
			logging.info('Kwargs: '+str(kwargs))
			logging.info('Graph: '+str(self._graph))
		
			logging.info('===Flushing graph...')
		
		self.flush_graph()
		self._graph.set_origin(node_key)
		
		if self.FactoryConfig.get('debug', False):
			logging.info('Graph: '+str(self._graph))
		
		if isinstance(node_key, str):
			node_key = n.Key(urlsafe=node_key)
			
		yield self.traverseNode(node_key)
		yield self.fill_artifacts()
		
		raise t.Return(self)


	@c.toplevel
	def buildFromObject(self, object_key, limit, depth, **kwargs):
		
		''' Build a graph from an origin object key. '''		
		pass