# -*- coding: utf-8 -*-
config = {}




""" 

	########## Tipfy configuration. ##########

"""
config['tipfy'] = {

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

	'enable_hooks':{
		'appstats':False
	}

}

config['momentum.fatcatmap.system'] = {



}

# Installed Assets
config['momentum.fatcatmap.assets'] = {

	# JavaScript Libraries & Includes
	'js': {
	
		('core', 'fcm'): { # FatCatMap Scripts
		
			'init': {'version': 0.1}, # Contains code to animate and fade the top navigation pulldown		
			'graph': {'version': 0.1}, # Holds code used by the layout and Protovis to construct graph visualizations
			'plugins': {'version': 0.1}, # Contains code to animate and fade the top navigation pulldown
			'navigation': {'version': 0.1} # Contains code to animate and fade the top navigation pulldown
		
		},
		
		('jquery', 'jquery'): { # jQuery Core & Plugins
		
			'core': {'path': 'core/jquery.full.1.5.js'}, # jQuery Core
			'rpc': {'path': 'rpc/jquery.rpc.2.0.js'}, # JSON RPC
			'ui': {'path': 'ui/jquery.ui-1.8.9.full.js'} # jQuery UI
		
		},
		
		'protovis': {'path': 'protovis/protovis-d3.2.js'}, # Stanford Protovis: JS Visualization Library
		'modernizr': {'path': 'modernizr/modernizr-1.7.min.js'}, # Modernizr: Checks browser compatibility
		'belated_png': {'path': 'util/dd_belatedpng.js'}
	
	},

	# Cascading Style Sheets
	'style': {
		
		('core', 'fcm'): { # FatCatMap Stylesheets
		
			'main': {'version': 0.2}, # Boilerplate stuff and reusable, site-wide CSS classes.
			'reset': {'version': 0.1}, # Standard CSS reset stylesheet.
			'layout': {'version': 0.2}, # Styles for FCM's layouts. Not page-specific.
			'mobile': {'version': 0.2}, # HTML5 Boilerplate's stylesheet for mobile devices
			'visualizer': {'version': 0.1} # Styles for the FCM visualizer
		
		}
	
	},
	
	# Other Assets
	'ext': {
	 },

}

# Pipelines Configuration
config['momentum.fatcatmap.pipelines'] = {

    'debug': True

}
