from momentum.fatcatmap.core.api.live import CoreLiveAPI
from momentum.fatcatmap.core.api.output import HandlerMixin


class LiveServicesMixin(HandlerMixin):

	__live_api = CoreLiveAPI()
		
		
	def getChannelLib(self):
		return '<script type="text/javascript" src="/_ah/channel/jsapi"></script>'
		
	def getLiveChannel(self, client):
		return self.__live_api.retrieveOrMakeChannelToken(client)