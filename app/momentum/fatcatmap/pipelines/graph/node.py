from momentum.fatcatmap.pipelines.graph import FCMGraphPipeline

from momentum.fatcatmap.models.core.object import Node
from momentum.fatcatmap.models.core.object import Object
from momentum.fatcatmap.models.core.object import NodeType


###### ====== Graph Node (Low Level) Pipelines ====== ######
class GraphNode(FCMGraphPipeline):

	def run(self, object_k, node_type, label, scope=None):
		nt = self.ndb.model.Key('NodeType', node_type)
		o = self.ndb.model.Key(urlsafe=object_k)
		n = Node(key=self.ndb.model.Key(pairs=o.pairs() + [(Node._get_kind(), 1)]), type=nt, label=label).put()
		
		self.log.info('===== NODE KEY: '+str(o.urlsafe())+' =====')
		
		return str(n.urlsafe())
	

class UpdateGraphNode(FCMGraphPipeline):

	def run(self):
		pass
	
	
class DeleteGraphNode(FCMGraphPipeline):

	def run(self):
		pass