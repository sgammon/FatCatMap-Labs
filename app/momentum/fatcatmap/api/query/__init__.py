from protorpc import remote
from protorpc import messages

from momentum.fatcatmap.api import MomentumAPIService


class QueryAPIService(MomentumAPIService):

	#@remote.method()
	def search(self, request):
		pass
		
	#@remote.method()
	def gql(self, request):
		pass