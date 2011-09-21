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


		### Core Dependencies ###
		('core', 'core'): {

			'config': {
				'version_mode': 'getvar',
				'bundle': 'dependencies.bundle.min.js'
			},
			
			'assets': {
				'dependencies': {'version': 0.1}, # compiled version of all the following			
				'data': {'min': True, 'version': '0.4.1'}, # Data.JS - beta duplicate site MVC core
				'backbone': {'min': True, 'version': '0.5.1'}, # Backbone.JS - site MVC core
				'amplify': {'min': True, 'version': '1.0.0'}, # AmplifyJS - for request, local storage + pubsub management
				'modernizr': {'min': True, 'version': '2.0'}, # Modernizr - browser polyfill + compatibility testing
				'yepnope': {'min': True, 'version': '1.0.1'}, # YepNope: conditional async script loader
				'lawnchair': {'version': '0.6.3'}, # Lawnchair: Client-side persistent storage
				'zeroclipboard': {'min': False, 'version': '1.0.7'} # ZeroClipboard: Universal copy-to-clipboard
			}
		
		},
		
		### FatCatMap Platform Scripts ###
		('fatcatmap', 'compiled'): {

			'config': {
				'version_mode': 'getvar',
				'bundle': 'core.bundle.min.js'
			},

			'assets': {
				'base': {'min': True, 'version': 0.1}, # milk (mustasche for coffee), _underscore, _root
				'fcm': {'min': True, 'version': 0.1}, # init, framework, and client-side platform code
				'layout': {'min': True, 'version': 0.1}, # contains code for manipulating page layout
				'interaction': {'min': True, 'version': 0.1} # contains code for charting, visualization & graphing
			}
	
		},
		
		### FatCatMap Site Scripts ###
		('site', 'compiled/site'): {
		
			'config': {
				'min': True,
				'version_mode': 'getvar'
			},
			
			'assets': {
				'browse': {'min': True, 'version': 0.1}, # content section: data browser
				'search': {'min': True, 'version': 0.1}, # content section: data search
				'map': {'min': True, 'version': 0.1}, # content section: data mapping
				'interact': {'min': True, 'version': 0.1}, # content section: social interaction
				'visualize': {'min': True, 'version': 0.1}, # content section: data visualization				
			}
		
		},
		
		### FatCatMap Local Storage Drivers ###
		('storage', 'compiled/storage'): {
			
			'config': {
				'version_mode': 'getvar'
			},
			
			'assets': {
				'combined': {'min': True, 'version': 0.1},
				'local': {'min': True, 'version': 0.1},
				'object': {'min': True, 'version': 0.1}
			},
			
		},

		### FatCatMap 3rd Party Storage Drivers ###
		('ext-storage', 'core/storage'): {

			'config': {
				'version_mode': 'getvar',
				'bundle': 'storage.bundle.min.js'			
			},
	
			'assets': {
				'websql': {'min': False, 'version': 0.1}, # Web SQL plugin for Lawnchair
				'indexeddb': {'min': False, 'version': 0.1}, # IndexedDB plugin for Lawnchair
			}
		
		},

		### FatCatMap Platform Plugins ###
		('plugins', 'compiled/plugins'): {

			'config': {
				'version_mode': 'getvar',
				'bundle': 'plugins.bundle.min.js'			
			},
			
			'assets': {
				'geo': {'min': True, 'version': 0.1}, # contains code for geo-detection and geo-operations
				'workers': {'min': True, 'version': 0.1}, # contains code for splitting intense tasks to workers
			}
		
		},

		### Browser feature Polyfills ###
		('polyfills', 'core/polyfills'): { 

			'config': {
				'version_mode': 'getvar',
				'bundle': 'polyfills.bundle.min.js'
			},
			
			'assets': {
				'json2': {'min': True}, # Adds JSON support to old IE and others that don't natively support it
				'history': {'min': True}, # Adds support for history management to old browsers
				'rgbcolor': {'min': True}, # Adds support for RGB color for CanVG
				'canvg': {'min': True} # Renders SVG over canvas (good for &droid)
			}

		},
		
		### FatCatMap Developer Tools ###
		('dev', 'util'): {

			'config': {
				'bundle': 'util.bundle.min.js'
			},

			'assets': {
				'fps_stats': {} # Little JS snippet to enable an on-page FPS/MB counter
			}
		
		},						
				
		### jQuery Core & Plugins ###
		('jquery', 'jquery'): { 
		
			'config': {
				'version_mode': 'getvar',				
				'bundle': 'jquery.bundle.min.js'
			},
			
			'assets': {
				'core': {'name': 'jquery', 'min': True, 'version': '1.6.1'}, # jQuery Core
				'easing': {'path': 'interaction/easing.min.js'}, # Easing transitions for smoother animations
				'mousewheel': {'path': 'interaction/mousewheel.min.js'} # jQuery plugin for mousewheel events + interactions
			}
			
		},
		
		### jQuery UI & Plugins ###
		('jquery-ui', 'jquery/ui'): {

			'config': {
				'min': True,
				'version_mode': 'getvar',
				'bundle': 'jquery.ui.bundle.min.js'				
			},
			
			'assets': {
				'jqui': {'min': True, 'version': '1.8.9'}, # jQuery UI
				'tipsy': {'min': True, 'version': '1.0.0a'}, # Effect for slick, animated tooltips
				'masonry': {'min': True, 'version': '1.3.2'}, # Special easy-on-the-eye layout styling
				'fancybox': {'min': True, 'version': '1.3.4'}, # Quick + clean lightbox-style dialogs
				'animate-enhanced': {'min': True, 'version': '0.76'} # Replaces jQuery animate() with CSS3 animations
			}
		
		},
		
		### Zepto Core & Plugins ###
		('zepto', 'zepto'): {

			'config': {
				'min': False,
				'version_mode': 'getvar',
				'bundle': 'zepto.bundle.min.js'
			},

			'assets': {
				'core': {'name': 'zepto'}, # Zepto Core
				'ajax': {}, # Ajax shim
				'assets': {}, # Assets API
				'detect': {}, # Feature detection
				'event': {}, # Event framework
				'fx': {}, # Effects framework
				'gesture': {}, # Gestures framework
				'polyfill': {}, # Feature polyfill for mobile
				'touch': {} # Touch events support
			}
		
		},
		
		### D3: Data Driven Diagrams ###	
		('d3', 'd3'): {
		
			'config': {
				'version_mode': 'getvar',
				'bundle': 'd3.bundle.min.js'
			},
		
			'assets': {
				'core': {'name': 'd3.fcm', 'min': True} # D3 Core Library
			}
		
		},
				
		### FatCatMap Interaction Libraries ###
		('vis', 'interaction'): {

			'config': {
				'version_mode': 'getvar'
			},

			'assets': {
				'protovis': {'min': True}, # Stanford Protovis: JS Visualization			
			}
		
		},

		'belated_png': {'path': 'util/dd_belatedpng.js'} # Belated PNG fix
	
	},


	# Cascading Style Sheets
	'style': {
		
		# Compiled (SASS) FCM Stylesheets
		('compiled', 'compiled'): {
		
			'config': {
				'min': True,
				'version_mode': 'getvar'
			},
		
			'assets': {
				'fcm': {'version': 0.1}, # compiled version of all the following
				'main': {'version': 0.3}, # reset, main, layout, forms
				'interaction': {'version': 0.1}, # visualizer, charts
				'ie': {'version': 0.1}, # fixes for internet explorer (grrr...)
				'print': {'version': 0.1} # proper format for printing
			}
		
		},
		
		# Content-section specific stylesheets
		('site', 'compiled/site'): {
		
			'config': {
				'min': True,
				'version_mode': 'getvar'
			},
			
			'assets': {
				'browse': {'version': 0.1}, # content section: data browser
				'search': {'version': 0.1}, # content section: data search
				'map': {'version': 0.1}, # content section: data mapping
				'interact': {'version': 0.1}, # content section: social interaction
				'visualize': {'version': 0.1}, # content section: data visualization				
			}
		
		},
		
		# Static FCM Stylesheets
		('core', 'fcm'): {
			
			'config': {
				'min': False,
				'version_mode': 'filename'
			},
			
			'assets': {
				'fonts': {'version': 0.3},
				'mobile': {'version': 0.2},
				'plugins': {'version': 0.1}
			}
			
		}
	
	},

	
	# Other Assets
	'ext': {
	 },
	
}