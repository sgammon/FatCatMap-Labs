from protorpc import messages
from momentum.fatcatmap.messages.util import DatastoreKey


# ==== Frame API-related messages ==== #
class FrameRequest(messages.Message):

	path = messages.StringField(1)
	raw = messages.BooleanField(2)	
	minify = messages.BooleanField(3)
	
	
class FrameResponse(messages.Message):
	
	key = messages.StringField(1)
	tpl = messages.StringField(2)