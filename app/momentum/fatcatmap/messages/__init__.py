from protorpc import messages as m


class APIMessage(m.Message):
	pass


class FCMClientStanza(APIMessage):
	pass
	

class FCMPlatformStanza(APIMessage):
	

class FCMRequestParam(APIMessage):

	name = m.StringField(0)
	value = m.StringField(0)


class FCMRequestEnvelope(APIMessage):

	id = m.StringField(0)
	jsonrpc = m.FloatField(1)
	version = m.FloatField(2)
	client = m.MessageField(3, FCMClientStanza)
	method = m.StringField(4)
	params = m.MessageField(5, FCMRequestParam, repeated=True)
	
	
class FCMResponse(APIMessage):
	pass
	
	
class FCMResponseEnvelope(APIMessage):

	id = m.StringField(0)
	jsonrpc = m.FloatField(1)
	version = m.FloatField(2)
	platform = m.MessageField(3, FCMPlatformStanza)
	response = m.MessageField(4, FCMResponse)