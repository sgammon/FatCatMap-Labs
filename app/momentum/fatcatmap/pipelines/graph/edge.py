from momentum.fatcatmap.pipelines.graph import FCMGraphPipeline

from momentum.fatcatmap.models.core.object import Node
from momentum.fatcatmap.models.core.relation import Edge
from momentum.fatcatmap.models.core.relation import EdgeType
from momentum.fatcatmap.models.core.relation import EdgeHint


###### ====== Graph Edge (Low Level) Pipelines ====== ######
class GraphEdge(FCMGraphPipeline):
	
	def run(self, edge_type, node_source, node_target):
		
		## Pull edge type
		nt = self.ndb.model.Key('EdgeType', edge_type)
		
		## Pull source + target nodes
		source = self.ndb.model.Key(urlsafe=node_source)
		target = self.ndb.model.Key(urlsafe=node_target)
		
		## Create source + target edges
		source_edge = Edge(key=self.ndb.model.Key(pairs=source.pairs() + [(Edge._get_kind(), 1)]), source=source, target=target, type=nt).put()
		target_edge = Edge(key=self.ndb.model.Key(pairs=target.pairs() + [(Edge._get_kind(), 1)]), source=target, target=source, type=nt).put()
		
		self.log.info('===== SOURCE EDGE KEY: '+str(source_edge.urlsafe())+' =====')
		self.log.info('===== TARGET EDGE KEY: '+str(target_edge.urlsafe())+' =====')
		
		return [source_edge.urlsafe(), target_edge.urlsafe()]
		
		
class GraphEdgeHint(FCMGraphPipeline):

	def run(self, node_source, node_target):

		## Pull source + target nodes
		source = self.ndb.model.Key(urlsafe=node_source)
		target = self.ndb.model.Key(urlsafe=node_target)
		
		source_hint_key = self.ndb.model.Key(pairs=source.pairs() + [(EdgeHint._get_kind(), target.urlsafe())])
		target_hint_key = self.ndb.model.Key(pairs=target.pairs() + [(EdgeHint._get_kind(), source.urlsafe())])
		
		## Check existence
		source_hint = source_hint_key.get_async().get_result()
		target_hint = target_hint_key.get_async().get_result()
		
		if source_hint is None and target_hint is None:
			## Create source + target edges
			source_hint = EdgeHint(key=source_hint_key).put()
			target_hint = EdgeHint(key=target_hint_key).put()
		
		self.log.info('===== SOURCE HINT KEY: '+str(source_hint.urlsafe())+' =====')
		self.log.info('===== TARGET HINT KEY: '+str(target_hint.urlsafe())+' =====')
	
		return [source_hint.urlsafe(), target_hint.urlsafe()]
	
	
class UpdateGraphEdge(FCMGraphPipeline):
	pass
	
	
class DeleteGraphEdge(FCMGraphPipeline):
	pass