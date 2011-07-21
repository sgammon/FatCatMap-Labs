from google.appengine.api import channel
from momentum.fatcatmap.core.api import MomentumCoreAPI
from momentum.fatcatmap.core.api.cache import CoreCacheAPI


class CoreLiveAPI(MomentumCoreAPI):


	def retrieveOrMakeChannelToken(self, seed):
		pass