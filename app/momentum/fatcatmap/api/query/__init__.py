from protorpc import remote
from protorpc import messages

from momentum.fatcatmap.api import FatCatMapAPIService


class QueryAPIService(FatCatMapAPIService):

	config_path = 'services.query.config'

	#@remote.method()
	def search(self, request):
		pass
		
	#@remote.method()
	def gql(self, request):
		pass