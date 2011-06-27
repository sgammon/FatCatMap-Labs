# -*- coding: utf-8 -*-
import os
import datetime

config = {}

## Check if we're running the app server
debug = os.environ.get('SERVER_SOFTWARE', '').startswith('Dev')


""" 

	######################################## Tipfy configuration. ########################################

"""
config['tipfy'] = {

	# Basic Config Values
	#'server_name': 'localhost:8080' if debug == True else 'spi.wirestone.staging.ext.providenceclarity.com',

	# Installed middleware modules
	'middleware': [

	    # Display Midleware
	    #'tipfy.ext.i18n.I18nMiddleware',  ## Enables automatic string translations based on locale of user

	    # Debugging Middleware
	    'tipfy.ext.debugger.DebuggerMiddleware',  ## Enable debugger. It will be loaded only when executed from the dev environment.
	    'tipfy.ext.appstats.AppstatsMiddleware',  ## Enable for good code profiling information
    
	    # FCM Middleware
	    'momentum.fatcatmap.core.middleware.multitenancy.AppVersionNamespacingMiddleware',  ## Restricts the app to accessing services in the appropriate namespace.
    
	],

	'apps_installed':[
		'momentum.platform', ## The Momentum backend behind the data analysis and magic that powers FatCatMap
		'momentum.fatcatmap' ## The FCM frontend responsible for making that data accessible and useful
	],

}
config['tipfy.sessions'] = {

	'secret_key':'ASDkljgdo*(#G!(CDSOICBD&V!OCXVVBIUB#V*C&VLSAXCX212e122d1))'

}
config['tipfyext.jinja2'] = {

	'templates_dir': 'templates', ## Root directory for template storage
	'templates_compiled_target': None, ##  Compiled templates directory
	'force_use_compiled': False, ## Force Jinja to use compiled templates, even on the Dev server

	'environment_args': { ## Jinja constructor arguments
		'optimized': True,	## 
	    'autoescape': True, ## Global Autoescape. BE CAREFUL WITH THIS.
	    'extensions': ['jinja2.ext.autoescape', 'jinja2.ext.with_'],
	},

	'after_environment_created': 'momentum.fatcatmap.core.output.fcmOutputEnvironmentFactory', ## Map to the core output factory

}


""" 

	######################################## Core configuration. ########################################

"""
## System Config
config['momentum.system'] = {

	'hooks': {
		'appstats': {'enabled': False},
		'apptrace': {'enabled': False},
		'profiler': {'enabled': False}
	}

}

## Global Services Cfg
config['momentum.services'] = {

	'logging': True,
	'hooks': {
		'appstats': {'enabled': False},
		'apptrace': {'enabled': False},
		'profiler': {'enabled': False}
	}

}



"""

	###################################### Platform configuration. ######################################


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

	######################################## FatCatMap configuration. ########################################

"""

## App settings
config['momentum.fatcatmap'] = {

	'version': {
		'major': 1,
		'minor': 1,
		'micro': 20110623,
		'release': 'ALPHA'
	}

}

## Development/debug settings
config['momentum.fatcatmap.dev'] = {

}

## Output layer settings
config['momentum.fatcatmap.output'] = { 

	'minify': False,
	'watermark': True,
	'standalone': False,

	'appcache': {
		'enable': False,
		'manifest': 'scaffolding-v1.1.manifest'
	},

	'assets':{
		'optimize': False,
		'compiled': True,
	}

}

config['momentum.fatcatmap.output.template_loader'] = {

	'force': True, ## Force enable template loader even on Dev server
	'debug': True,  ## Enable dev logging
	'use_memory_cache': False, ## Use handler in-memory cache for template source
	'use_memcache': False, ## Use Memcache API for template source

}


# FCM Services
config['momentum.fatcatmap.services'] = {

	'enabled': True, ## Disable API services system wide
	'logging': True, ## Logging for service request handling

	# Module-level (default) config (NOT IMPLEMENTED YET)
	'config': {
	
		'url_prefix': '/_api/rpc', ## Prefix for all service invocation URLs
	
		## Response + data caching middleware
		'caching': {
		
			'profiles': {
			
				'lazy': {},
				'safe': {},
				'aggressive': {}
			
			},
			'default_profile': 'safe'
		
		},
		
		## Security and permissions enforcement middleware
		'security': {
			
			'profiles': {
			
				'public': {},
				'private': {}
			
			},
			'default_profile': 'public'
		
		},
		
		## Recording and logging middleware
		'recording': {
		},
	
	},

	# Installed API's
	'services': {
	
		## For creating/updating/retrieving userspace data
		'data': {
			'enabled': True,
			'service': 'momentum.fatcatmap.api.data.DataAPIService',
			'methods': ['get', 'sync', 'preload', 'getObject', 'getNative', 'getAsset', 'putAsset'],
			'config': {
				'caching': 'safe',
				'security': 'public'
			}
		},
		
		## Recursively generates structures suitable for graphing
		'graph': {
			'enabled': True,
			'service': 'momentum.fatcatmap.api.graph.GraphAPIService',
			'methods': ['construct', 'constructFromNode', 'constructFromObject'],
			'config': {
				'caching': 'safe',
				'security': 'public'
			}
		},
		
		## Assembles full HTML or JSON template views for natives/other data
		'frame': {
			'enabled': True,
			'service': 'momentum.fatcatmap.api.frame.FrameAPIService',
			'methods': ['render', 'renderWidget', 'renderDialog'],
			'config': {
				'caching': 'safe',
				'security': 'public'
			}
		},
		
		## Exposes methods to query and search userland data
		'query': {
			'enabled': True,
			'service': 'momentum.fatcatmap.api.query.QueryAPIService',
			'methods': ['search', 'gql', 'quickSearch'],
			'config': {
				'caching': 'safe',
				'security': 'public'
			}
		},
		
		## Assembles data structures suitable for visualizations.
		'charts': {
			'enabled': True,
			'service': 'momentum.fatcatmap.api.charts.ChartsAPIService',
			'methods': ['generate', 'generateFromSeries'],		
			'config': {
				'caching': 'safe',
				'security': 'public'
			}
		},
		
		## Allows a user to establish and manage a persistent session
		'session': {
			'enabled': True,
			'service': 'momentum.fatcatmap.api.session.SessionAPIService',
			'methods': ['init', 'authenticate', 'checkin'],
			'config': {
				'caching': 'safe',
				'security': 'public'
			}
		}	
	}

}

# Installed Assets
config['momentum.fatcatmap.assets'] = {

	# JavaScript Libraries & Includes
	'js': {
	
		('core', 'core'): { # FatCatMap Scripts
		
			'init': {'version': 0.3}, # Contains code to initiate and prepare the fatcatmap object
			'rpc': {'version': 0.2}, # Contains code to integrate remote RPCs with the fatcatmap object
			'graph': {'version': 0.2}, # Holds code used by the layout and Protovis to construct graph visualizations
			'plugins': {'version': 0.2}, # Contains code for miscellaneous jQuery plugins
			'layout': {'version': 0.2} # Contains code to animate and fade the top navigation pulldown, and sidebars, etc
		
		},
		
		('storage', 'core'): { # FatCatMap Storage Drivers
		
			'sql': {'path': 'storage/sql-0.1.js'}, # Web SQL Database driver
			'indexed': {'path': 'storage/indexed-0.1.js'}, # IndexedDB Database driver
			'session': {'path': 'storage/session-0.1.js'}, # SessionStorage driver
			'local': {'path': 'storage/local-0.1.js'} # LocalStorage driver
		
		},
		
		('polyfills', 'core'): {
		
			'json': {'path': 'polyfills/json2.js'}, # Adds JSON support to old IE and others that don't natively support it
			'history': {'path': 'polyfills/history.js'}, # Adds support for history management to old browsers
		
		},
		
		('jquery', 'jquery'): { # jQuery Core & Plugins
		
			'core': {'path': 'core/jquery.full.1.5.js'}, # jQuery Core
			'ui': {'path': 'ui/jquery.ui-1.8.9.full.js'}, # jQuery UI
			'indexeddb': {'path': 'core/storage/jquery.indexeddb.1.1-full.js'}, # Indexed DB interface
			'websql': {'path': 'core/storage/jquery.sql.0.8a.min.js'}, # WebSQL interface
			'tipsy': {'path': 'ui/jquery.tipsy.js'}, # Effect for slick, animated tooltips
			'uniform': {'path': 'ui/jquery.uniform.js'}, # Form styling
			'masonry': {'path': 'ui/jquery.masonry.js'}, # Special easy-on-the-eye layout styling
			'fancybox': {'path': 'ui/jquery.fancybox.js'}, # Quick + clean lightbox-style dialogs
			'easing': {'path': 'core/interaction/jquery.easing-1.3.pack.js'}, # Easing transitions for smoother animations
			'mousewheel': {'path': 'core/interaction/jquery.mousewheel-3.0.4.pack.js'} # jQuery plugin for mousewheel events + interactions
			
		},
		
		('compiled', 'compiled'): { # Compiled Scripts
			
			'core': {'path': 'core.js'}, # init, framework, and client-side platform code
			'storage': {'path': 'storage.js'}, # contains code for interfacing with browser-local storage
			'layout': {'path': 'layout.js'}, # contains code for manipulating page layout
			'interaction': {'path': 'interaction.js'}, # contains code for charting, visualization & graphing
			'site': {'path': 'site.js'} # contains code specific to site content areas
		
		},
		
		'protovis': {'path': 'interaction/protovis-d3.2.js'}, # Stanford Protovis: JS Visualization Library
		'modernizr': {'path': 'util/modernizr-1.7.min.js'}, # Modernizr: Checks browser compatibility
		'yepnope': {'path': 'util/yepnope-1.0.1-min.js'}, # YepNope: conditional script loader with Modernizr integration
		'belated_png': {'path': 'util/dd_belatedpng.js'} # Belated PNG fix
	
	},

	# Cascading Style Sheets
	'style': {
		
		('core', 'fcm'): { # FatCatMap Stylesheets
		
			'main': {'version': 0.3}, # Boilerplate stuff and reusable, site-wide CSS classes.
			'reset': {'version': 0.2}, # Standard CSS reset stylesheet.
			'fonts': {'version': 0.2}, # Standard CSS reset stylesheet.			
			'layout': {'version': 0.4}, # Styles for FCM's layouts. Not page-specific.
			'forms': {'version': 0.2}, # Styles forms on FCM. Links to sprite skins.			
			'mobile': {'version': 0.3}, # HTML5 Boilerplate's stylesheet for mobile devices
			'plugins': {'version': 0.1}, # Styles for JS plugins that FCM uses
			'visualizer': {'version': 0.2} # Styles for the FCM visualizer
		
		},
		
		('compiled', 'compiled'): { # Compiled FCM Stylesheets
		
			'main': {'version': 0.3}, # reset, main, fonts, layout, forms, mobile + visualizer
			'print': {'version': 0.2}, # alternate print stylesheet			
			'plugins': {'version': 0.1}, # tipsy, uniform, masonry, jquery ui, etc
			'browse': {'version': 0.1}, # content section: data browser
			'search': {'version': 0.1}, # content section: data search
			'map': {'version': 0.1}, # content section: data mapping
			'interact': {'version': 0.1}, # content section: social interaction
			'visualize': {'version': 0.1}, # content section: data visualization	
		}
	
	},
	
	# Other Assets
	'ext': {
	 },
	
}


# FCM Pipelines Configuration
config['momentum.fatcatmap.pipelines'] = {

    'debug': True

}