# -*- coding: utf-8 -*-
"""WSGI app setup."""
import os
import sys
import config
import logging
import bootstrap

bootstrap.MomentumBootstrapper.prepareImports()

from tipfy import Tipfy
from urls import get_rules

rules = get_rules()
	

def enable_appstats(app):
	
	""" Utility function that enables appstats middleware."""
	
	from google.appengine.ext.appstats.recording import appstats_wsgi_middleware
	app.wsgi_app = appstats_wsgi_middleware(app.wsgi_app)
	return app
	
	
def enable_apptrace(app):
	
	""" Utility function that enables apptrace middleware. """
	
	from apptrace import middleware
	middleware.Config.URL_PATTERNS = ['^/$']
	app.wsgi_app = middleware.apptrace_middleware(app.wsgi_app)
	return app
	

def enable_jinja2_debugging():

	""" Enables blacklisted modules that help Jinja2 debugging. """

	# Enables better debugging info for errors in Jinja2 templates.
	from google.appengine.tools.dev_appserver import HardenedModulesHook
	HardenedModulesHook._WHITE_LIST_C_MODULES += ['_ctypes', 'gestalt']
	
	
def run(app):

	""" Default run case - no profiler. """
	
	app.run()


def main():

	""" INCEPTION! :) """

	global run
	global rules
	
	if config.debug:
		rules = get_rules()
	
	## Grab debug and system config
	debug = config.debug
	sys_config = config.config.get('momentum.system')
	
	## Create the app, get it ready for middleware
	app = Tipfy(rules=rules, config=config.config, debug=debug)

	## By default, just run the app
	action = run

	try:
		## If we're in debug mode, automatically activate some stuff
		if debug:
			logging.info('CORE: Jinja2 debugging enabled.')
			enable_jinja2_debugging()

		## Consider system hooks
		if sys_config.get('hooks', False) != False:
		
			## First up - appstats (RPC tracking)
			if sys_config['hooks'].get('appstats', False) != False:
				if sys_config['hooks']['appstats']['enabled'] == True:
					logging.info('CORE: AppStats enabled.')		
					app = enable_appstats(app)
				
			## Next up - apptrace (Memory footprint tracking)
			if sys_config['hooks'].get('apptrace', False) != False:
				if sys_config['hooks']['apptrace']['enabled'] == True:
					logging.info('CORE: AppTrace enabled.')
					app = enable_apptrace(app)

			## Execution tree + CPU time tracking
			if sys_config['hooks']['profiler']['enabled'] == True:
				import cProfile
				def profile_run(app):
					logging.info('CORE: Profiling enabled.')
					enable_jinja2_debugging()
					cProfile.runctx("run()", globals(), locals(), filename="FatCatMap.profile")
				action = profile_run ## Set our action to the profiler
	except Exception, e:
		logging.critical('CORE: CRITICAL FAILURE: Unhandled exception in main: "'+str(e)+'".')
		if config.debug:
			raise
	
	else:
		action(app)


if __name__ == '__main__':
	main()