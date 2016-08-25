from protorpc import remote
from protorpc import messages

from google.appengine.api import channel

from momentum.fatcatmap.api import FatCatMapAPIService
from momentum.fatcatmap.messages import session as messages


class SessionAPIService(FatCatMapAPIService):
	
	config_path = 'services.session.config'

	#@remote.method()
	def authenticate(self, request):
		pass
		
	@remote.method(messages.SessionInitRequest, messages.SessionInitResponse)
	def init(self, request):
		pass
		
		
	@remote.method(messages.SessionCheckinRequest, messages.SessionCheckinResponse)
	def checkin(self, request):
		pass