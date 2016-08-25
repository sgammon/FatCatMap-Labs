# -*- coding: utf-8 -*-
import os
import sys
import logging
import datetime
import bootstrap

if 'lib' not in sys.path or 'lib/distlib' not in sys.path:
	bootstrap.MomentumBootstrapper.prepareImports()

_config = {}
_compiled_config = None

## Check if we're running the app server
debug = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')


""" 

	######################################## Tipfy configuration. ########################################

"""
_config['webapp2'] = {

	# Basic Config Values
	#'server_name': 'localhost:8080' if debug == True else 'spi.wirestone.staging.ext.providenceclarity.com',

	'apps_installed':[
		'momentum.fatcatmap' ## The FCM frontend responsible for making that data accessible and useful
	],

}
_config['webapp2_extras.sessions'] = {

	'secret_key':'ASDkljgdo*(#G!(CDSOICBD&V!OCXVVBIUB#V*C&VLSAXCX212e122d1))',
    'default_backend': 'datastore',
    'cookie_name':     'fcmsession',
    'session_max_age': None,
    'cookie_args': {
        'max_age':     86400,
        #'domain':      '*',
        'path':        '/',
        'secure':      False,
        'httponly':    False,
    }	

}
_config['webapp2_extras.jinja2'] = {

	'template_path': 'templates/source', ## Root directory for template storage
	'compiled_path': 'templates.compiled', ##  Compiled templates directory
	'force_compiled': True, ## Force Jinja to use compiled templates, even on the Dev server

	'environment_args': { ## Jinja constructor arguments
		'optimized': True,	## 
	    'autoescape': True, ## Global Autoescape. BE CAREFUL WITH THIS.
	    'extensions': ['jinja2.ext.autoescape', 'jinja2.ext.with_', 'jinja2.ext.i18n'],
	},

}


""" 

	######################################## Core configuration. ########################################

"""
## System Config
_config['momentum.system'] = {

	'debug': False, # System-level debug messages

	'hooks': { # System-level Developer's Hooks
		'appstats': {'enabled': False}, # AppStats RPC optimization + analysis tool
		'apptrace': {'enabled': False}, # AppTrace memory usage optimization + analysis tool
		'profiler': {'enabled': False}  # Python profiler for CPU cycle/efficiency optimization + analysis
	},
	
	'include': [ # Extended configuration files to include
		('platform', 'config.ext.platform'), # FCM/Momentum Platform config
		('fatcatmap', 'config.ext.fatcatmap'), # FCM Site (Tipfy-layer) config
		('services', 'config.ext.services'), # Global + site services (RPC/API) config
		('assets', 'config.ext.assets') # Asset manangement layer config
	]

}

def systemLog(message, _type='debug'):
	global debug
	global _config
	if _config['momentum.system']['debug'] is True or _type in ('error', 'critical'):
		prefix = '[CORE_SYSTEM]: '		
		if _type == 'debug' or debug is True:
			logging.debug(prefix+message)
		elif _type == 'info':
			logging.info(prefix+message)
		elif _type == 'error':
			logging.error(prefix+message)
		elif _type == 'critical':
			logging.critical(prefix+message)


def readConfig(config=_config):
	global _compiled_config
	from webapp2 import import_string	
	if _compiled_config is not None:
		return _compiled_config
	else:
		if config['momentum.system'].get('include', False) is not False and len(config['momentum.system']['include']) > 0:
			systemLog('Considering system config includes...')
			for name, configpath in config['momentum.system']['include']:
				systemLog('Checking include "'+str(name)+'" at path "'+str(configpath)+'".')
				try:
					for key, cfg in import_string('.'.join(configpath.split('.')+['config'])).items():
						config[key] = cfg
				except Exception, e:
					systemLog('Encountered exception of type "'+str(e.__class__)+'" when trying to parse config include "'+str(name)+'" at path "'+str(configpath))
					if debug:
						raise
					else:
						continue
		if len(config) > 0 and _compiled_config is None:
			_compiled_config = config
				
		return config
	
config = readConfig(_config)