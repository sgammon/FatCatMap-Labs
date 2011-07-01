import hashlib
import logging

from tipfy import Response

from google.appengine.api import users

from momentum.fatcatmap.handlers import WebHandler
from momentum.fatcatmap.core.adapters.format.json import FCMJSONAdapter

_api_services = {}


class FatcatmapAPIDispatcher(WebHandler):
	pass
	
class JavascriptAPIDispatcher(WebHandler):
	
	def get(self):
		
		
		## Generate list of services to expose to user
		svcs = []
		services_cfg = self.config.get('momentum.fatcatmap.services')

		for name, config in services_cfg['services'].items():
			if config['enabled'] is True:

				security_profile = services_cfg['config']['security']['profiles'][config['config']['security']]

				service_action = services_cfg['config']['url_prefix'].split('/')
				service_action.append(name)
				service_action_url = '/'.join(service_action)

				if security_profile['expose'] == 'all':
					svcs.append((name, service_action_url, config))

				elif security_profile['expose'] == 'admin':
					if users.is_current_user_admin():
						svcs.append((name, service_action_url, config))
						
				elif security_profile['expose'] == 'none':
					continue
		
		return self.render('snippets/page_object.js', services=svcs, content_type='text/javascript', script_tag=False)