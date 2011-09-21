""" 

	######################################## FatCatMap configuration. ########################################

"""
config = {}


## App settings
config['momentum.fatcatmap'] = {

	'version': {
		'major': 1,
		'minor': 6,
		'micro': 1,
		'build': 20110921,
		'release': 'BETA'
	}

}

## Development/debug settings
config['momentum.fatcatmap.dev'] = {

}

## Output layer settings
config['momentum.fatcatmap.output'] = { 

	'minify': False,
	'optimize': True,
	'watermark': True,
	'standalone': False,

	'appcache': {
		'enable': False,
		'manifest': 'staging-v1.5.3.appcache'
	},

	'assets':{
		'minified': False,
		'serving_mode': 'cdn', ## 'local' or 'cdn' (CDN prefixes all assets with an absolute URL)
		'cdn_prefix': ['cdn.static.labs.momentum.io', 'cdn.static.momentum.io',
						'west-us.cdn.static.fatcatmap.com', 'west-us.cdn.static.fatcatmap.org']
	}

}

## Caching
config['momentum.fatcatmap.cache'] = {

	'key_seperator': '::',
	'prefix': 'dev',
	'prefix_mode': 'explicit',
	'prefix_namespace': False,
	'namespace_seperator': '::',
	
	'adapters': {

		'fastcache': {

			'default_ttl': 600
	
		},
		
		'memcache': {

			'default_ttl': 10800
		
		}, 
		
		'backend': {

			'default_ttl': 10800

		},

		'datastore': {

			'default_ttl': 86400
		
		}
			
	}

}

config['momentum.fatcatmap.output.template_loader'] = {

	'force': True, ## Force enable template loader even on Dev server
	'debug': False,  ## Enable dev logging
	'use_memory_cache': False, ## Use handler in-memory cache for template source
	'use_memcache': False, ## Use Memcache API for template source

}

# FCM Pipelines Configuration
config['momentum.fatcatmap.pipelines'] = {

    'debug': False, # Enable basic serverlogs
	'logging': {
	
		'enable': False, # Enable the pipeline logging subsystem
		'mode': 'serverlogs', # 'serverlogs', 'xmpp' or 'channel'
		'channel': '', # Default channel to send to (admin channels are their email addresses, this can be overridden on a per-pipeline basis in the dev console)
		'jid': '', # Default XMPP JID to send to (this can be overridden on a per-pipeline basis in the dev console)
	
	}

}

# Graph factory
config['momentum.fatcatmap.core.graph.factory'] = {

	'debug': False, # Enable basic serverlogs

}