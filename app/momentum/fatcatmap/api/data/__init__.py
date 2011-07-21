from protorpc import remote
from protorpc import messages

from momentum.fatcatmap.api import FatCatMapAPIService


class TestDataRequest(messages.Message):
	
	key = messages.StringField(1)


class TestDataResponse(messages.Message):
	
	response = messages.StringField(2)


class DataAPIService(FatCatMapAPIService):

	config_path = 'services.data.config'

	@remote.method(TestDataRequest, TestDataResponse)
	def get(self, request):
		return TestDataResponse(response='Hello, JavaScript!')
		
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