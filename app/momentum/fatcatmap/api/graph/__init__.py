from protorpc import remote
from protorpc import messages

from momentum.fatcatmap.api import MomentumAPIService


class GraphAPIService(MomentumAPIService):

	#@remote.method()
	def construct(self, request):
		pass
		
	#@remote.method()
	#def constructFromNode(self, request):
		pass
		
	#@remote.method()
	def constructFromObject(self, request):
		pass