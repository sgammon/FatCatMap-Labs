from protorpc import remote
from protorpc import messages

from momentum.fatcatmap.api import FatCatMapAPIService


class FrameAPIService(FatCatMapAPIService):

	#@remote.method()
	def render(self, request):
		pass