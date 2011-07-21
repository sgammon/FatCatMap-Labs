from protorpc import remote
from protorpc import messages

from momentum.fatcatmap.api import FatCatMapAPIService


class SessionAPIService(FatCatMapAPIService):
	
	config_path = 'services.session.config'

	#@remote.method()
	def authenticate(self, request):
		pass
		
	#@remote.method()
	def init(self, request):
		pass
		
	#@remote.method()
	def checkin(self, request):
		pass