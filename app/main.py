# -*- coding: utf-8 -*-
"""WSGI app setup."""
import os
import sys
import config

if 'lib' not in sys.path:
	# Add lib as primary libraries directory, with fallback to lib/dist
	# and optionally to lib/dist.zip, loaded using zipimport.
	sys.path[0:0] = ['lib', 'lib/dist', 'lib/dist.zip']

from tipfy import Tipfy
from urls import get_rules


def enable_appstats(app):
	
	""" Utility function that enables appstats middleware."""
	
	from google.appengine.ext.appstats.recording import \
		appstats_wsgi_middleware
	app.wsgi_app = appstats_wsgi_middleware(app.wsgi_app)


def enable_jinja2_debugging():

	"""Enables blacklisted modules that help Jinja2 debugging."""

	if not debug:
		return

	# Enables better debugging info for errors in Jinja2 templates.
	from google.appengine.tools.dev_appserver import HardenedModulesHook
	HardenedModulesHook._WHITE_LIST_C_MODULES += ['_ctypes', 'gestalt']

debug = config.debug
sys_config = config.config.get('momentum.fatcatmap.system')

app = Tipfy(rules=get_rules(), config=config.config, debug=debug)

if debug:
	enable_jinja2_debugging()

if sys_config.get('hooks', False) != False:
	if sys_config['hooks'].get('appstats', False) != False:
		if sys_config['hooks']['appstats']['enabled'] == True:
			logging.info('CORE: AppStats enabled.')		
			enable_appstats(app)

def main():
	# Run the app.
	enable_jinja2_debugging()
	app.run()

if sys_config.get('hooks', False) != False:
	if sys_config['hooks'].get('profiler', False) != False:
		if sys_config['hooks']['profiler']['enabled'] == True:
			import cProfile
			def main():
				logging.info('CORE: Profiling enabled.')
				enable_jinja2_debugging()
				cProfile.runctx("app.run()", globals(), locals(), filename="FatCatMap.profile")

if __name__ == '__main__':
	main()