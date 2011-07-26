""" 

	######################################## FatCatMap configuration. ########################################

"""
config = {}


## App settings
config['momentum.fatcatmap'] = {

	'version': {
		'major': 1,
		'minor': 3,
		'micro': 20110724,
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
		
		'datastore': {

			'default_ttl': 86400
		
		}
	
	}

}

config['momentum.fatcatmap.output.template_loader'] = {

	'force': True, ## Force enable template loader even on Dev server
	'debug': True,  ## Enable dev logging
	'use_memory_cache': False, ## Use handler in-memory cache for template source
	'use_memcache': False, ## Use Memcache API for template source

}

# FCM Pipelines Configuration
config['momentum.fatcatmap.pipelines'] = {

    'debug': True, # Enable basic serverlogs
	'logging': {
	
		'enable': True, # Enable the pipeline logging subsystem
		'mode': 'serverlogs', # 'serverlogs', 'xmpp' or 'channel'
		'channel': '', # Default channel to send to (admin channels are their email addresses, this can be overridden on a per-pipeline basis in the dev console)
		'jid': '', # Default XMPP JID to send to (this can be overridden on a per-pipeline basis in the dev console)
	
	}

}