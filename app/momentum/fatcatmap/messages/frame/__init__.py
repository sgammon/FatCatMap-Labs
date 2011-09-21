from protorpc import messages
from momentum.fatcatmap.messages.util import DatastoreKey


# ==== Frame API-related messages ==== #
class FrameContextArtifact(messages.Message):
	
	class ArtifactReferenceType(messages.Enum):
		
		SYS = 1
		ENVIRON = 2
		USER = 3
		SESSION = 4
		DATASTUB_VAR = 5
		DATASTUB_CONTENT = 6
	
	name = messages.StringField(1, required=True)
	ref = messages.BooleanField(2, default=False)
	value = messages.StringField(3)
	ref_type = messages.EnumField(ArtifactReferenceType, 4)
	default = messages.StringField(5)
	

class FrameRequest(messages.Message):

	path = messages.StringField(1)
	raw = messages.BooleanField(2)	
	minify = messages.BooleanField(3)
	context = messages.MessageField(FrameContextArtifact, 4, repeated=True)
	
	
class RawFrameResponse(messages.Message):
	
	path = messages.StringField(1)
	raw = messages.StringField(2)
	
	
class RenderedFrameResponse(messages.Message):
	
	path = messages.StringField(1)
	src = messages.StringField(2)