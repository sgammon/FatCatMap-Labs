"""

	###################################### Services configuration. ######################################


"""
config = {}


## Global Services
config['momentum.services'] = {

	'logging': True,

	'hooks': {
		'appstats': {'enabled': False},
		'apptrace': {'enabled': False},
		'profiler': {'enabled': False}
	},

	'middleware': [

		('authentication', {
		
			'enabled': True,
			'debug': True,
			'path': 'momentum.services.middleware.security.AuthenticationMiddleware',
			'args': {
			
			}
		
		}),
		
		('monitoring', {
		
			'enabled': True,
			'debug': True,
			'path': 'momentum.services.middleware.audit.MonitoringMiddleware',
			'args': {
			
			}			
		
		}),
		
		('authorization', {
		
			'enabled': True,
			'debug': True,
			'path': 'momentum.services.middleware.security.AuthorizationMiddleware',
			'args': {
			
			}			
		
		}),
		
		('caching', {
		
			'enabled': True,
			'debug': True,
			'path': 'momentum.services.middleware.caching.CachingMiddleware',
			'args': {
			
			}
		
		})

	],
	
	## Configuration profiles that can be assigned to services
	'middleware_config': {
	
		## Response + data caching middleware
		'caching': {
		
			'profiles': {
			
				## No caching
				'none': {
					
					'localize': False,					
					'default_ttl': None, ## Default Time-to-Live for cached items
					
					'activate': {
						'local': False, ## Local browser-side caching, if supported
						'request': False, ## Caching of full API responses by hashed API requests
						'internal': False ## Caching inside the remote service object
					}
				
				},
			
			
				## Cache things as they are pulled/used by clients
				'lazy': {
					
					'localize': False,
					'default_ttl': 60,
				
					'activate': {
						'local': False,
						'request': True,
						'internal': True
					},

				},
				
				## Cache things as they are used, but set low timeouts to avoid stale data
				'safe': {
				
					'localize': False,
					'default_ttl': 60,
					
					'activate': {
						'local': False,
						'request': False,
						'internal': True
					}
				
				},
				
				## Cache things before they are accessed, predictively, and with long timeouts
				'aggressive': {

					'localize': False,				
					'default_ttl': 120,
					
					'activate': {
						'local': True,
						'request': True,
						'internal': True
					}
				
				}
			
			},
			
			'default_profile': 'none' ## Default caching profile for APIs that don't specify one
		
		},
		
		## Security and permissions enforcement middleware
		'security': {
			
			'profiles': {
			
				## APIs with no security features
				'none': {
				
					'expose': 'all', ## Whether to expose existence of this API to javascript clients
					
					## Client authentication
					'authentication': {
						'enabled': False
					},
					
					## Client authorization
					'authorization': {
						'enabled': False
					}
				
				},
				
				## APIs marked public
				'public': {
				
					'expose': 'all',
					
					'authentication': {
						'enabled': False,
						'mode': None
					},
					
					'authorization': {
						'enabled': False,
						'mode': None
					}
				
				},
				
				## APIs marked private
				'private': {
				
					'expose': 'admin',
					
					'authentication': {
						'enabled': False,
						'mode': None
					},
					
					'authorization': {
						'enabled': False,
						'mode': None
					}
				
				}
			
			},
			
			'default_profile': 'public'
		
		},
		
		## Recording and logging middleware
		'recording': {
		
			'profiles': {
			
				'none': {
					'mode': None
				},
				
				'minimal': {
					'mode': None
				},
				
				'full': {
					'mode': None
				},
				
				'debug': {
					'mode': None
				}
			
			},
		
		},
	
	},
	
	### Default config values
	'defaults': {
	
		'module': {},
		'service': {
		
			'config': {
				'caching': 'none',
				'security': 'none',
				'recording': 'none'
			},
			
			'args': {
			
			}
		
		}
	
	},

}



# FCM Services
config['momentum.fatcatmap.services'] = {

	'enabled': True, ## Disable API services system wide
	'logging': True, ## Logging for service request handling

	# Module-level (default) config (NOT IMPLEMENTED YET)
	'config': {
	
		'url_prefix': '/_api/rpc', ## Prefix for all service invocation URLs
	
	},

	# Installed API's
	'services': {
	
		## Debug, development, uptime, etc methods for infrastructure/testing/monitoring use
		'system': {
			'enabled': True,
			'service': 'momentum.fatcatmap.api.system.SystemAPIService',
			'methods': ['echo', 'hello'],
			
			'config': {
				'caching': 'none',
				'security': 'none',
				'recording': 'none'
			}
		},
	
		## For creating/updating/retrieving userspace data
		'data': {
			'enabled': True,
			'service': 'momentum.fatcatmap.api.data.DataAPIService',
			'methods': ['get', 'create', 'update', 'delete', 'sync', 'preload', 'getObject', 'getNative', 'getAsset', 'putAsset'],

			'config': {
				'caching': 'none',
				'security': 'none',
				'recording': 'none'
			}
		},
		
		## Recursively generates structures suitable for graphing
		'graph': {
			'enabled': True,
			'service': 'momentum.fatcatmap.api.graph.GraphAPIService',
			'methods': ['construct', 'constructFromNode', 'constructFromObject'],

			'config': {
				'caching': 'aggressive',
				'security': 'none',
				'recording': 'none'
			}
		},
		
		## Assembles full HTML or JSON template views for natives/other data
		'frame': {
			'enabled': True,
			'service': 'momentum.fatcatmap.api.frame.FrameAPIService',
			'methods': ['render', 'renderWidget', 'renderDialog'],

			'config': {
				'caching': 'none',
				'security': 'none',
				'recording': 'none'				
			}
		},
		
		## Exposes methods to query and search userland data
		'query': {
			'enabled': True,
			'service': 'momentum.fatcatmap.api.query.QueryAPIService',
			'methods': ['search', 'gql', 'quickSearch'],

			'config': {
				'caching': 'none',
				'security': 'none',
				'recording': 'none'				
			}
		},
		
		## Assembles data structures suitable for visualizations.
		'charts': {
			'enabled': True,
			'service': 'momentum.fatcatmap.api.charts.ChartsAPIService',
			'methods': ['generate', 'generateFromSeries'],		

			'config': {
				'caching': 'none',
				'security': 'none',
				'recording': 'none'				
			}
		},
		
		## Allows a user to establish and manage a persistent session
		'session': {
			'enabled': True,
			'service': 'momentum.fatcatmap.api.session.SessionAPIService',
			'methods': ['init', 'authenticate', 'checkin'],

			'config': {
				'caching': 'none',
				'security': 'none',
				'recording': 'none'				
			}
		}
		
	} ## End services

} ## End services


# Graph API
config['momentum.fatcatmap.services.graph'] = {
	
	'debug': True
	
}