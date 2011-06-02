import hashlib
import logging

from tipfy import Response

from momentum.fatcatmap.handlers import WebHandler
from momentum.fatcatmap.core.adapters.format.json import FCMJSONAdapter

_api_services = {}


class FatcatmapAPIDispatcher(WebHandler):
	pass
	
class JavascriptAPIDispatcher(WebHandler):
	
	def get(self):
		return self.render('snippets/page_object.js', content_type='text/javascript', script_tag=False)