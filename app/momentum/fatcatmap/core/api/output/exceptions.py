from momentum.fatcatmap.core.api.exceptions import FCMCoreAPIException


class CoreOutputAPIException(FCMCoreAPIException):
	pass
	
## == Assets Module Exceptions == ##
class AssetException(CoreOutputAPIException): pass
class InvalidAssetType(AssetException): pass
class InvalidAssetEntry(AssetException): pass