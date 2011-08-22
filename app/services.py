import os
import sys

import bootstrap
bootstrap.MomentumBootstrapper.prepareImports()

import ndb
import config
import logging

## App Engine Imports
import webapp2 as webapp
from protorpc import registry
from webapp2_extras import protorpc

from google.appengine.ext.webapp import util
from google.appengine.dist import use_library

from momentum.services import MomentumServiceHandlerFactory

## Get services configuration
services_config = config.config.get('momentum.fatcatmap.services')

def enable_appstats(app):
	
	""" Utility function that enables appstats middleware."""
	
	from google.appengine.ext.appstats import recording
	app = recording.appstats_wsgi_middleware(app)
	return app


def generateServiceMappings(svc_cfg):
	
	#('/'.join(svc_cfg['config']['url_prefix'].split('/')+svc_cfg['config']['registry']['endpoint']), registry.RegistryService)
	service_mappings = []
	
	## Generate service mappings in tuple(<invocation_url>, <classpath>) format
	for service, cfg in svc_cfg['services'].items():
		if cfg['enabled'] == True:
			service_mappings.append(('/'.join(svc_cfg['config']['url_prefix'].split('/')+[service]), cfg['service']))
			
	if len(service_mappings) > 0:
		return service_mappings
	else:
		return None
		  

def main():
	
	global services_config
		
	ndb.debug = config.debug
	
	if services_config['enabled'] == True:
		service_mappings = generateServiceMappings(services_config)
		if service_mappings is not None:
			
			## Map URL's to services
			protorpc.ServiceHandlerFactory = MomentumServiceHandlerFactory
			service_mappings = protorpc.service_mapping(service_mappings, '/_registry')

			## Build application
			application = webapp.WSGIApplication(service_mappings)
	
			## Consider services config
			services_cfg = config.config.get('momentum.services')
			if services_cfg['hooks']['appstats']['enabled'] == True:
				application = enable_appstats(application)
	
			util.run_wsgi_app(application)


if __name__ == '__main__':
	main()