from protorpc import remote
from protorpc import messages

from momentum.fatcatmap.api import MomentumAPIService


class SessionAPIService(MomentumAPIService):

	#@remote.method()
	def authenticate(self, request):
		pass
		
	#@remote.method()
	def init(self, request):
		pass
		
	#@remote.method()
	def checkin(self, request):
		pass