from momentum.fatcatmap.pipelines.graph import FCMGraphPipeline

from momentum.fatcatmap.pipelines.graph.edge import GraphEdge
from momentum.fatcatmap.pipelines.graph.edge import GraphEdgeHint
from momentum.fatcatmap.pipelines.graph.vector import GraphVector


###### ====== Graph Relation (High Level) Pipelines ====== ######
class NewObjectRelation(FCMGraphPipeline):
	
	output_names = ['edges','hints']

	def run(self, edge_type, nodes, f_struct=None, **kwargs):
		
		if f_struct is not None:
			self.fill(self.outputs.edges, str(f_struct['edges']))
			self.fill(self.outputs.hints, str(f_struct['hints']))
			yield self.common.Return(f_struct)
		
		else:
			## Create and yield Object
			e = yield GraphEdge(edge_type, nodes[0], nodes[1])
			h = yield GraphEdgeHint(nodes[0], nodes[1])
			
			f_struct = yield self.common.Dict(edges=e, hints=h)
			yield NewObjectRelation(None, None, f_struct)
	
	
class UpdateObjectRelation(FCMGraphPipeline):
	pass
	
	
class DeleteObjectRelation(FCMGraphPipeline):
	pass