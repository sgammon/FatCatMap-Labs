import hashlib
import logging

from tipfy import Response
from werkzeug import cached_property

from google.appengine.api import users

from momentum.fatcatmap.handlers import WebHandler
from momentum.fatcatmap.core.adapters.format.json import FCMJSONAdapter

_api_services = {}


class FatcatmapAPIDispatcher(WebHandler):
	pass
	
class JavascriptAPIDispatcher(WebHandler):
	
	''' Returns a rendered JavaScript template to initialize the the JSAPI environment with server-side values. '''
	
	@cached_property
	def fcmServicesConfig(self):
		return self.config.get('momentum.fatcatmap.services')
	
	@cached_property
	def globalServicesConfig(self):
		return self.config.get('momentum.services')
	
	def get(self):
		
		## Generate list of services to expose to user
		svcs = []

		for name, config in self.fcmServicesConfig['services'].items():
			if config['enabled'] is True:

				security_profile = self.globalServicesConfig['middleware_config']['security']['profiles'].get(config['config']['security'], None)

				if security_profile is None:

					## Pull default profile if none is specified
					security_profile = self.globalServicesConfig['middleware_config']['security']['profiles'][self.globalServicesConfig['defaults']['service']['config']['security']]

				## Grab prefix
				service_action = self.fcmServicesConfig['config']['url_prefix'].split('/')

				## Add service name
				service_action.append(name)
				
				## Join into endpoint URL
				service_action_url = '/'.join(service_action)

				## Expose depending on security profile
				if security_profile['expose'] == 'all':
					svcs.append((name, service_action_url, config))

				elif security_profile['expose'] == 'admin':
					if users.is_current_user_admin():
						svcs.append((name, service_action_url, config))
						
				elif security_profile['expose'] == 'none':
					continue
		
		## Render!
		return self.render('snippets/page_object.js', services=svcs, content_type='text/javascript', script_tag=False)