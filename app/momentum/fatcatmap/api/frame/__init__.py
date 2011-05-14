from protorpc import remote
from protorpc import messages

from momentum.fatcatmap.api import MomentumAPIService


class FrameAPIService(MomentumAPIService):

	#@remote.method()
	def generateDetailView(self, request):
		pass
		
	#@remote.method()
	def generateSummaryView(self, request):
		pass