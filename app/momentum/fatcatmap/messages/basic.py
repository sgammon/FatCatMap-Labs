from momentum.fatcatmap import messages as m


class EchoRequest(m.FCMMessage):
	
	say = m.StringField(1)
	
	
class EchoResponse(m.FCMMessage):

	result = m.StringField(1)