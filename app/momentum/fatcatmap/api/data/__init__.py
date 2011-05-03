from protorpc import remote
from protorpc import messages

from momentum.fatcatmap.api import MomentumAPIService


class DataAPIService(remote.Service):

	#@remote.method()
	def get(self, request):
		pass
		
	#@remote.method()
	def retrieveGraphObject(self, request):
		pass
		
	#@remote.method()
	def retrieveNative(self, request):
		pass
		
	#@remote.method()
	def retrieveAsset(self, request):
		pass
		
	#@remote.method()
	def uploadAsset(self, request):
		pass