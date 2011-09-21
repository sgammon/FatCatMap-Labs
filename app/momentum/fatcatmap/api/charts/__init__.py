from protorpc import remote
from protorpc import messages

from momentum.fatcatmap.api import FatCatMapAPIService


class ChartsAPIService(FatCatMapAPIService):
	
	config_path = 'services.charts.config'

	#@remote.method()
	def generate(self, request):
		pass
		
	#@remote.method()
	def generateFromSeries(self, request):
		pass