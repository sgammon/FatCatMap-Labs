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
		'momentum.fatcatmap'
	],

}
config['tipfy.sessions'] = {

	'secret_key':'ASKLdjOF)H#*@G@)*GCJDBUVF(!&Gouhf981g27gd2G@H)'

}


""" 

	########## FatCatMap configuration. ##########

"""
config['momentum.fatcatmap'] = {

	'version': {
		'major': 0,
		'minor': 2,
		'release': 'ALPHA',
	}

}

config['momentum.fatcatmap.system'] = {

	'hooks': {
		'appstats': {'enabled': False},
		'profiler': {'enabled': False}
	}

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
			'navigation': {'version': 0.2} # Contains code to animate and fade the top navigation pulldown
		
		},
		
		('jquery', 'jquery'): { # jQuery Core & Plugins
		
			'core': {'path': 'core/jquery.full.1.5.js'}, # jQuery Core
			'rpc': {'path': 'rpc/jquery.rpc.2.0.js'}, # JSON RPC
			'ui': {'path': 'ui/jquery.ui-1.8.9.full.js'}, # jQuery UI
			'tools': {'path': 'tools/jquery.tools.min.js'}, # Giant jQuery swiss army knife
			'indexeddb': {'path': 'core/jquery.indexeddb.1.1-full.js'}, # Indexed DB interface
			'tipsy': {'path': 'ui/jquery.tipsy.js'}, # Effect for slick, animated tooltips
			'meerkat': {'path': 'ui/jquery.meerkat.js'}, # Effect for smooth slide-in content zones
			'uniform': {'path': 'ui/jquery.uniform.js'}, # Form styling
			'masonry': {'path': 'ui/jquery.masonry.js'} # Special easy-on-the-eye layout styling
			
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
			'layout': {'version': 0.4}, # Styles for FCM's layouts. Not page-specific.
			'forms': {'version': 0.2}, # Styles forms on FCM. Links to sprite skins.
			'mobile': {'version': 0.3}, # HTML5 Boilerplate's stylesheet for mobile devices
			'visualizer': {'version': 0.2} # Styles for the FCM visualizer
		
		}
	
	},
	
	# Other Assets
	'ext': {
	 },

}

# Output 


# Pipelines Configuration
config['momentum.fatcatmap.pipelines'] = {

    'debug': True

}
