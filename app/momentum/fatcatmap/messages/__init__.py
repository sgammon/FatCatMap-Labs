from protorpc import messages as m


class FCMClientStanza(m.Message):
	pass
	

class FCMRequestParam(m.Message):

	name = m.StringField(0)
	value = m.StringField(0)


class FCMRequest(m.Message):

	id = m.StringField(0)
	jsonrpc = m.IntegerField(1)
	version = m.IntegerField(2)
	client = m.MessageField(3, FCMClientStanza)
	method = m.StringField(4)
	params = m.MessageField(5, FCMRequestParam, repeated=True)
	
	
class FCMResponse(m.Message):
	pass