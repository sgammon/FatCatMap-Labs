from momentum.fatcatmap.pipelines.graph import FCMGraphPipeline
from momentum.fatcatmap.models.core.native import Native


###### ====== Graph Native (Low Level) Pipelines ====== ######
class GraphNative(FCMGraphPipeline):

	def run(self,  parent, properties={}, version=None, **kwargs):
		self.log.info('======== GRAPH NATIVE ========')
		return '//GraphNative//'
		

class UpdateNative(FCMGraphPipeline):

	def run(self, node, properties={}, version=None, **kwargs):
		pass
	

class DeleteNative(FCMGraphPipeline):

	def run(self, node, version=None):
		pass