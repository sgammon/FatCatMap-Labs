from protorpc import messages


# ==== Frame API-related messages ==== #
class EchoRequest(messages.Message):

	message = messages.StringField(1, required=True)
	
	
class HelloRequest(messages.Message):
	
	name = messages.StringField(1)
	
	
class EchoResponse(messages.Message):
	
	message = messages.StringField(1)