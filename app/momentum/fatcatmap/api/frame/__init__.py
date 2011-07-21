from momentum.services import remote

from momentum.fatcatmap.api import FatCatMapAPIService
from momentum.fatcatmap.messages import frame as messages


class FrameAPIService(FatCatMapAPIService):

	config_path = 'services.frame.config'

	@remote.method(messages.FrameRequest, messages.FrameResponse)
	def raw(self, request):
		pass

	@remote.method(messages.FrameRequest, messages.FrameResponse)
	def render(self, request):
		pass