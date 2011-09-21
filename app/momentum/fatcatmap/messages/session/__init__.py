from protorpc import messages


class SessionInitRequest(messages.Message):

	client_id = messages.StringField(1)
	enable_live = messages.BooleanField(2, default=False)
	
	
class SessionInitResponse(messages.Message):

	session_id = messages.StringField(1)
	channel_id = messages.StringField(2)
	
	
class SessionCheckinRequest(messages.Message):
	pass
	
	
class SessionCheckinResponse(messages.Message):
	pass