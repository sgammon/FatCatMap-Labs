from protorpc import remote
from protorpc import messages

from momentum.fatcatmap.api import MomentumAPIService


class EchoRequest(messages.Message):
	
	name = messages.StringField(1)
	
	
class EchoResponse(messages.Message):
	
	result = messages.StringField(1)


class DataAPIService(remote.Service):

	@remote.method(EchoRequest, EchoResponse)
	def echo(self, request):
		if request.name:
			return EchoResponse(result='Hello, '+str(request.name)+'! Welcome to the Momentum API!')
		else:
			return EchoResponse(result='Hello, stranger! Welcome to the Momentum API!')