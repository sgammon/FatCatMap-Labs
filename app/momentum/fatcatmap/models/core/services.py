from momentum.fatcatmap import models as m


#### ==== Service Models ==== ####
class ExtService(m.FCMModel):
	name = m.db.StringProperty()
	description = m.db.TextProperty()
	homepage = m.db.LinkProperty()

class ExtServiceKey(m.FCMModel):
	name = m.db.StringProperty()
	value = m.db.StringProperty()
	service = m.db.ReferenceProperty(ExtService, collection_name='keys')
	last_used = m.db.DateTimeProperty()
	global_uses = m.db.IntegerProperty()
	enforce_limits = m.db.BooleanProperty()
	global_usage_limit = m.db.IntegerProperty()
	daily_usage_limit = m.db.IntegerProperty()

class ExtInteraction(m.FCMPolyModel):
	method = m.db.StringProperty()
	result = m.db.StringProperty(choices=['success','failure'])
	request = m.db.BlobProperty()
	response = m.db.BlobProperty()
	service = m.db.ReferenceProperty(ExtService, collection_name='interactions')
	timestamp = m.db.DateTimeProperty(auto_now_add=True)
	enable_caching = m.db.BooleanProperty()


#### ==== External ID Models ==== ####
class ExtID(m.NDBModel):
	name = m.ndb.StringProperty(default=None)
	value = m.ndb.StringProperty()
	link = m.ndb.LinkProperty()
	service = m.ndb.KeyProperty()
	
	
#### ==== Data Engine Models ==== ####
class DataEngine(m.FCMPolyModel):
	enabled = m.db.BooleanProperty()

class Mapper(DataEngine):
	name = m.db.StringProperty()
	input_reader = m.db.StringProperty(choices=['datastore','datastore_key','blobstore_line','blobstore_zip'])
	handler = m.db.StringListProperty(indexed=False)
	params = m.db.StringListProperty(indexed=False)
	param_defaults = m.db.StringListProperty(indexed=False)

class ServiceMapper(Mapper):
	service = m.db.ReferenceProperty(ExtService, collection_name='mappers')

class Pipeline(DataEngine):
	name = m.db.StringProperty()
	path = m.db.StringListProperty(indexed=False)
	async = m.db.BooleanProperty(default=False)

class ServicePipeline(Pipeline):
	service = m.db.ReferenceProperty(ExtService, collection_name='pipelines')

class Worker(DataEngine):
	name = m.db.StringProperty()
	worker_endpoint = m.db.StringProperty()

class ServiceWorker(Worker):
	service = m.db.ReferenceProperty(ExtService, collection_name='workers')

class WorkerMethod(m.FCMPolyModel):
	name = m.db.StringProperty()