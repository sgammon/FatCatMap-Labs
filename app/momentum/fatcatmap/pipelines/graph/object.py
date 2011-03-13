from momentum.fatcatmap.pipelines.graph import FCMGraphPipeline

from momentum.fatcatmap.models.core.object import Object
from momentum.fatcatmap.models.core.object import ObjectType


###### ====== Graph Object (Low Level) Pipelines ====== ######
class GraphObject(FCMGraphPipeline):

	def run(self, o_type):
		ot = self.ndb.model.Key('ObjectType', o_type)
		o = Object(type=ot).put()
		
		self.log.info('===== OBJECT KEY: '+str(o.urlsafe())+' =====')
		
		return str(o.urlsafe())
	

class UpdateGraphObject(FCMGraphPipeline):

	def run(self):
		pass
	
	
class DeleteGraphObject(FCMGraphPipeline):

	def run(self):
		pass
