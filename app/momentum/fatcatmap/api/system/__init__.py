import logging
from momentum.services import remote

from momentum.fatcatmap.api import FatCatMapAPIService
from momentum.fatcatmap.messages import system as messages


class SystemAPIService(FatCatMapAPIService):
	
	@remote.method(messages.EchoRequest, messages.EchoResponse)
	def echo(self, request):
		
		if request.message is not None:
			return messages.EchoResponse(message=request.message)
		else:
			raise remote.ApplicationError('Must include a message in ECHO.')
			
	@remote.method(messages.HelloRequest, messages.EchoResponse)
	def hello(self, request):
		
		if request.name is not None:
			return messages.EchoResponse(message="Hello, "+str(request.name)+"!")
		else:
			return messages.EchoResponse(message="Hello, stranger!")