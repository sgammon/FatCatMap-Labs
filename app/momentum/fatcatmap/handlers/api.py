import hashlib
import logging

from tipfy import Response
from werkzeug import cached_property

from google.appengine.api import users
from google.appengine.api import memcache

from momentum.fatcatmap.handlers import WebHandler
from momentum.fatcatmap.core.adapters.format.json import FCMJSONAdapter

_api_services = {}
jsapi_cache = None


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
		
		global jsapi_cache
				
		## Generate list of services to expose to user
		svcs = []
		opts = {}

		if jsapi_cache is not None:
			return jsapi_cache
		else:
			jsapi = memcache.get('jsapi-main')
			if jsapi is not None:
				return jsapi
			else:
				for name, config in self.fcmServicesConfig['services'].items():
					if config['enabled'] is True:

						security_profile = self.globalServicesConfig['middleware_config']['security']['profiles'].get(config['config']['security'], None)
				
						caching_profile = self.globalServicesConfig['middleware_config']['caching']['profiles'].get(config['config']['caching'], None)

						if security_profile is None:

							## Pull default profile if none is specified
							security_profile = self.globalServicesConfig['middleware_config']['security']['profiles'][self.globalServicesConfig['defaults']['service']['config']['security']]

						if caching_profile is None:
							caching_profile = self.globalServicesConfig['middleware_config']['caching']['profiles'][self.globalServicesConfig['defaults']['service']['config']['caching']]

						## Add caching to local opts
						opts['caching'] = caching_profile['activate'].get('local', False)

						## Grab prefix
						service_action = self.fcmServicesConfig['config']['url_prefix'].split('/')

						## Add service name
						service_action.append(name)
				
						## Join into endpoint URL
						service_action_url = '/'.join(service_action)

						## Expose depending on security profile
						if security_profile['expose'] == 'all':
							svcs.append((name, service_action_url, config, opts))

						elif security_profile['expose'] == 'admin':
							if users.is_current_user_admin():
								svcs.append((name, service_action_url, config, opts))
						
						elif security_profile['expose'] == 'none':
							continue
		
				jsapi = self.render('snippets/page_object.js', services=svcs, content_type='text/javascript', script_tag=False)
				memcache.set('jsapi-main', jsapi)
				jsapi_cache = jsapi
				return jsapi