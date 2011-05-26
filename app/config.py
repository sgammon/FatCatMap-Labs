# -*- coding: utf-8 -*-
import os
import datetime

config = {}

## Check if we're running the app server
debug = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')


""" 

	########## Tipfy configuration. ##########

"""
config['tipfy'] = {

	# Basic Config Values
	#'server_name': 'localhost:8080' if debug == True else 'spi.wirestone.staging.ext.providenceclarity.com',

	# Installed middleware modules
	'middleware': [

	    # Display Midleware
	    #'tipfy.ext.i18n.I18nMiddleware',  ## Enables automatic string translations based on locale of user

	    # Debugging Middleware
	    #'tipfy.ext.debugger.DebuggerMiddleware',  ## Enable debugger. It will be loaded only when executed from the dev environment.
	    #'tipfy.ext.appstats.AppstatsMiddleware',  ## Enable for good code profiling information
    
	    # FCM Middleware
	    'momentum.fatcatmap.core.middleware.multitenancy.AppVersionNamespacingMiddleware',  ## Restricts the app to accessing services in the appropriate namespace.
    
	],

	'apps_installed':[
		'momentum.platform',
		'momentum.fatcatmap'
	],

}
config['tipfy.sessions'] = {

	'secret_key':'ASKLdjOF)H#*@G@)*GCJDBUVF(!&Gouhf981g27gd2G@H)'

}
config['tipfyext.jinja2'] = {

	'templates_dir': 'templates', ## Root directory for template storage
	'templates_compiled_target': None, ##  Compiled templates directory
	'force_use_compiled': False, ## Force Jinja to use compiled templates, even on the Dev server

	'environment_args': { ## Jinja constructor arguments
		'optimized': False,	
	    'autoescape': True,
	    'extensions': ['jinja2.ext.autoescape', 'jinja2.ext.with_'],
	},

	'after_environment_created': 'momentum.fatcatmap.core.output.fcmOutputEnvironmentFactory',

}


###### ===== System Config ===== #####
config['momentum.system'] = {

	'hooks': {
		'appstats': {'enabled': False},
		'profiler': {'enabled': False}
	}

}

config['momentum.services'] = {

	'logging': True

}



"""

	########## Platform configuration. ##########


"""
config['momentum.platform'] = {

	'version': {
		'major': 0,
		'minor': 1,
		'micro': 20110523,
		'release': 'DEV'
	}

}

config['momentum.platform.output'] = { 

}




""" 

	########## FatCatMap configuration. ##########

"""
config['momentum.fatcatmap'] = {

	'version': {
		'major': 0,
		'minor': 4,
		'micro': 20110526,
		'release': 'ALPHA'
	}

}

config['momentum.fatcatmap.dev'] = {

}

config['momentum.fatcatmap.output'] = { 

	'minify': False,
	'assets':{
		'optimize': False,
		'compiled': False, 
	}

}

config['momentum.fatcatmap.output.template_loader'] = {

	'force': True, ## Force enable template loader even on Dev server
	'debug': True,  ## Enable dev logging
	'use_memory_cache': False, ## Use handler in-memory cache for template bytecode
	'use_memcache': False, ## Use Memcache API for template bytecode

}

# Installed Assets
config['momentum.fatcatmap.assets'] = {

	# JavaScript Libraries & Includes
	'js': {
	
		('core', 'fcm'): { # FatCatMap Scripts
		
			'init': {'version': 0.2}, # Contains code to animate and fade the top navigation pulldown		
			'rpc': {'version': 0.2}, # Contains code to aid remote RPCs from javascript.
			'graph': {'version': 0.2}, # Holds code used by the layout and Protovis to construct graph visualizations
			'plugins': {'version': 0.2}, # Contains code to animate and fade the top navigation pulldown
			'layout': {'version': 0.2} # Contains code to animate and fade the top navigation pulldown
		
		},
		
		('storage', 'fcm'): { # FatCatMap Storage Drivers
		
			'sql': {'path': 'storage/sql-0.1.js'}, # Web SQL Database driver
			'indexed': {'path': 'storage/indexed-0.1.js'}, # IndexedDB Database driver
			'session': {'path': 'storage/session-0.1.js'}, # SessionStorage driver
			'local': {'path': 'storage/local-0.1.js'} # LocalStorage driver
		
		},
		
		('polyfills', 'fcm'): {
		
			'json': {'path': 'polyfills/json2.js'}, # Adds JSON support to old IE and others that don't natively support it
			'history': {'path': 'polyfills/history.js'}, # Adds support for history management to old browsers
		
		},
		
		('jquery', 'jquery'): { # jQuery Core & Plugins
		
			'core': {'path': 'core/jquery.full.1.5.js'}, # jQuery Core
			'rpc': {'path': 'rpc/jquery.rpc.2.0.js'}, # JSON RPC
			'ui': {'path': 'ui/jquery.ui-1.8.9.full.js'}, # jQuery UI
			'indexeddb': {'path': 'core/storage/jquery.indexeddb.1.1-full.js'}, # Indexed DB interface
			'websql': {'path': 'core/storage/jquery.sql.0.8a.min.js'}, # WebSQL interface
			'tipsy': {'path': 'ui/jquery.tipsy.js'}, # Effect for slick, animated tooltips
			'uniform': {'path': 'ui/jquery.uniform.js'}, # Form styling
			'masonry': {'path': 'ui/jquery.masonry.js'} # Special easy-on-the-eye layout styling
			
		},
		
		('compiled', 'min'): { # Compiled Scripts
		
			'core': {'version': 0.1}, # contains core, rpc, ui
			'plugins': {'version': 0.1} # contains ui, storage adapters, tipsy, uniform, masonry
		
		},
		
		'protovis': {'path': 'protovis/protovis-d3.2.js'}, # Stanford Protovis: JS Visualization Library
		'modernizr': {'path': 'modernizr/modernizr-1.7.min.js'}, # Modernizr: Checks browser compatibility
		'yepnope': {'path': 'yepnope/yepnope-1.0.1-min.js'}, # YepNope: conditional script loader with Modernizr integration
		'belated_png': {'path': 'util/dd_belatedpng.js'} # Belated PNG fix
	
	},

	# Cascading Style Sheets
	'style': {
		
		('core', 'fcm'): { # FatCatMap Stylesheets
		
			'main': {'version': 0.3}, # Boilerplate stuff and reusable, site-wide CSS classes.
			'reset': {'version': 0.2}, # Standard CSS reset stylesheet.
			'fonts': {'version': 0.1}, # Standard CSS reset stylesheet.			
			'layout': {'version': 0.4}, # Styles for FCM's layouts. Not page-specific.
			'forms': {'version': 0.2}, # Styles forms on FCM. Links to sprite skins.
			'mobile': {'version': 0.3}, # HTML5 Boilerplate's stylesheet for mobile devices
			'visualizer': {'version': 0.2} # Styles for the FCM visualizer
		
		},
		
		('compiled', 'min'): { # Compiled FCM Stylesheets
		
			'core': {'version': 0.1}, # reset, main, fonts, layout, forms, mobile + visualizer
			'plugins': {'version': 0.1} # tipsy, uniform, masonry, jquery ui
		
		}
	
	},
	
	# Other Assets
	'ext': {
	 },
	
}

# Output 


# Services
config['momentum.fatcatmap.services'] = {

	'logging': True,

}


# Pipelines Configuration
config['momentum.fatcatmap.pipelines'] = {

    'debug': True

}
