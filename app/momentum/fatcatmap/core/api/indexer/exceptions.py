from momentum.fatcatmap.core.api import exceptions


class IndexerAPIException(exceptions.FCMCoreAPIException):
	pass
	
	
class IndexingAdapterExtension(exceptions.FCMCoreAPIException):
	pass
	
class EmptyInput(IndexingAdapterExtension): pass