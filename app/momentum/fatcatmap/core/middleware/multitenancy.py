import os
from google.appengine.api import namespace_manager


class AppVersionNamespacingMiddleware(object):
	
	''' Sets the app's namespace to the current major version. '''
	
	def post_make_app(self, app):
		version = os.environ.get('CURRENT_VERSION_ID').split('.')
		if isinstance(version, list) and len(version) > 1:
			version = version[0]
		
		try:
			namespace_manager.validate_namespace(version)
			namespace_manager.set_namespace(version)
		except:
			logging.critical('Error encountered validating or setting namespace to: '+str(version)+'.')
			
		app.namespace = version
		return app
		
		
class GoogleAppsNamespacingMiddleware(object):
	
	''' Sets the app's namespace to the attached Google Apps domain. '''
	
	def post_make_app(self, app):
		try:
			namespace_manager.validate_namespace(namespace_manager.google_apps_namespace())
			namespace_manager.set(namespace_manager.google_apps_namespace())
		except:
			logging.critical('Error encountered validating or setting namespace to: '+str(namespace_manager.google_apps_namespace()))
			
		app.namespace = namespace_manager.google_apps_namespace()
		return app
		
		
class SubdomainNamespacingMiddleware(object):
	
	''' Sets the app's namespace to the current subdomain. '''
	
	def post_make_app(self, app):
		hostname = os.environ.get('HTTP_HOST').split('.')
		try:
			namespace_manager.validate_namespace(hostname[0])
			namspace_manager.set(hostname[0])
		except:
			logging.critical('Error encountered validating or setting namespace to: "'+str(hostname[0])+'" of hostname "'+str(hostname)+'".')