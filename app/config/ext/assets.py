"""

	###################################### Asset configuration. ######################################


"""
config = {}


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
		
		('polyfills', 'core'): { # Browser feature Polyfills
		
			'json': {'path': 'polyfills/json2.js'}, # Adds JSON support to old IE and others that don't natively support it
			'history': {'path': 'polyfills/history.js'}, # Adds support for history management to old browsers
		
		},
		
		('dev', 'util'): { # FatCatMap Developer Tools
		
			'fpsstats': {'path': 'fps_stats.js'} # Little JS snippet to enable an on-page FPS/MB counter
		
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