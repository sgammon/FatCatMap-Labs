from momentum.fatcatmap.pipelines.graph import FCMGraphPipeline

from momentum.fatcatmap.pipelines.graph.node import GraphNode
from momentum.fatcatmap.pipelines.graph.object import GraphObject
from momentum.fatcatmap.pipelines.graph.native import GraphNative


###### ====== Graph Collection (High Level) Pipelines ====== ######
class NewObjectCollection(FCMGraphPipeline):

	output_names = ['object', 'node', 'native']

	def run(self, object_type, node_type, label, scope=None, f_struct=None, **kwargs):
		
		if f_struct is not None:
			self.fill(self.outputs.object, str(f_struct['object']))
			self.fill(self.outputs.node, str(f_struct['node']))
			self.fill(self.outputs.native, str(f_struct['native']))
			yield self.common.Return(f_struct)
		
		else:
			## Create and yield Object
			o = yield GraphObject(object_type)
			n = yield GraphNode(o, node_type, label, scope)
			a = yield GraphNative(n, properties=kwargs)
		
			f_struct = yield self.common.Dict(object=o, node=n, native=a)
			yield NewObjectCollection(None, None, None, None, f_struct)
	

class UpdateObjectCollection(FCMGraphPipeline):
	pass
	
	
class DeleteObjectCollection(FCMGraphPipeline):
	pass