from protorpc import remote
from protorpc import messages

from momentum.fatcatmap.api import MomentumAPIService


class ChartsAPIService(MomentumAPIService):

	#@remote.method()
	def generate(self, request):
		pass
		
	#@remote.method()
	def generateFromSeries(self, request):
		pass