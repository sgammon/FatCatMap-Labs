"""

	###################################### Asset configuration. ######################################


"""
config = {}


# Installed Assets
config['momentum.fatcatmap.assets'] = {

	'debug': False, ## Output log messages about what's going on.
	'verbose': False, ## Raise debug-level messages to 'info'.

	# JavaScript Libraries & Includes
	'js': {

		### FatCatMap Platform Scripts ####
		('fatcatmap', 'compiled'): {
		
			'fcm': {}, # init, framework, and client-side platform code
			'layout': {}, # contains code for manipulating page layout			
			'interaction': {}, # contains code for charting, visualization & graphing
			'geo': {'path': 'plugins/geo.js'}, # contains code for geo-detection and geo-operations
			'workers': {'path': 'plugins/workers.js'}, # contains code for splitting intense tasks to workers
			'storage': {'path': 'storage.js'}, # contains code for interfacing with browser-local storage
	
		},


		### Core Dependencies ###
		('core', 'core'): {
		
			'backbone': {'min': True}, # Backbone.JS - site MVC core
			'underscore': {'min': True}, # Underscore - fantastic JS toolkit
			'amplify': {'min': True}, # AmplifyJS - for request, local storage + pubsub management
			'modernizr': {'min': True}, # Modernizr - browser polyfill + compatibility testing
			'yepnope': {'min': True} # YepNope: conditional async script loader
		
		},	
		

		### FatCatMap Local Storage Drivers ###
		('storage', 'compiled'): {
		
			'sql': {'path': 'storage/sql.js'}, # Web SQL Database driver
			'indexed': {'path': 'storage/object.js'}, # IndexedDB Database driver
			'session': {'path': 'storage/session.js'}, # SessionStorage driver
			'local': {'path': 'storage/local.js'} # LocalStorage driver
		
		},


		### Browser feature Polyfills ###
		('polyfills', 'core'): { 
		
			'json': {'path': 'polyfills/json2.js'}, # Adds JSON support to old IE and others that don't natively support it
			'history': {'path': 'polyfills/history.js'}, # Adds support for history management to old browsers
		
		},
		

		### FatCatMap Developer Tools ###
		('dev', 'util'): {
		
			'fps_stats': {} # Little JS snippet to enable an on-page FPS/MB counter
		
		},						
				

		### jQuery Core & Plugins ###
		('jquery', 'jquery'): { 
		
			'core': {'path': 'core/jquery.js', 'min': 'core/jquery.min.js'}, # jQuery Core
			'ui': {'path': 'ui/jqui.js', 'min': 'ui/jqui.min.js'}, # jQuery UI
			'tipsy': {'path': 'ui/tipsy.js'}, # Effect for slick, animated tooltips
			'masonry': {'path': 'ui/masonry.min.js'}, # Special easy-on-the-eye layout styling
			'fancybox': {'path': 'ui/fancybox.min.js'}, # Quick + clean lightbox-style dialogs
			'easing': {'path': 'core/interaction/easing.min.js'}, # Easing transitions for smoother animations
			'mousewheel': {'path': 'core/interaction/mousewheel.min.js'} # jQuery plugin for mousewheel events + interactions
			
		},
		

		### D3: Data Driven Diagrams ###	
		('d3', 'd3'): {
		
			'core': {'path': 'd3.js'}, # D3 Core Library
			'behavior': {'path': 'd3.behavior.js'}, # D3 Behaviors
			'chart': {'path': 'd3.chart.js'}, # D3 Charting
			'csv': {'path': 'd3.csv.js'}, # D3 CSV Parsing
			'geo': {'path': 'd3.geo.js'}, # D3 Geo-related functions
			'geom': {'path': 'd3.geom.js'}, # D3 Geo-map related functions
			'layout': {'path': 'd3.layout.js'}, # D3 Layout
			'time': {'path': 'd3.time.js'} # D3 Time/Date based functions
		
		},
				

		### FatCatMap Interaction Libraries ###
		('vis', 'interaction'): {

			'protovis': {'min': True}, # Stanford Protovis: JS Visualization
		
		},

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