from protorpc import messages
from momentum.fatcatmap.messages.util import DatastoreKey

from momentum.services.core.fields.variant import VariantField


class AssetRequest(messages.Message):

	key = messages.MessageField(DatastoreKey, 1)
	cached = messages.BooleanField(2)
	version = messages.FloatField(3)
	optimize = messages.BooleanField(4)
	reference = messages.BooleanField(5)
	
	
class AssetResponse(messages.Message):

	key = messages.MessageField(DatastoreKey, 1)

	class AssetFreshness(messages.Enum):
		
		FRESH = 1
		CACHED = 2
		
	freshness = messages.EnumField(AssetFreshness, 2)
	reference = messages.StringField(3)
	content = messages.StringField(4)
	mimetype = messages.StringField(5)


class ObjectKeyValue(messages.Message):

	name = messages.StringField(1)
	value = VariantField(2)
	empty = messages.BooleanField(3)
	

class ObjectRepeatedKeyValue(messages.Message):
	
	name = messages.StringField(1)
	value = VariantField(2, repeated=True)
	empty = messages.BooleanField(3)

	
class ObjectRequest(messages.Message):

	key = messages.StringField(1)
	keys = messages.StringField(2, repeated=True)
	cached = messages.BooleanField(3)


class DatastoreObject(messages.Message):

	key = messages.MessageField(DatastoreKey, 1)
	updated = messages.StringField(2)
	created = messages.StringField(3)
	properties = VariantField(4)
	
	
class ObjectResponse(messages.Message):
	
	count = messages.IntegerField(1)
	objects = messages.MessageField(DatastoreObject, 2, repeated=True)