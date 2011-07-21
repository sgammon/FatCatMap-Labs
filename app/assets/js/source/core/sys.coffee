class CoreSysAPI extends CoreAPI
	
	constructor: (@fcm) ->
		
		@version =
			minor: null
			major: null
			release: null
		
			setVersion: (@minor, @major, @release) ->
			
		@drivers =
		
			registry: {}
		
			register: (module, name, fn, initialized, callback) ->
				if typeof @registry[module] is null
					@registry[module] = {}
				@registry[module][name] = 
					initialized: initialized
					registered: true
					hook_point: fn
					init_callback: callback
				
				## Trigger DRIVER_REGISTERED
				context =
					module: module
					name: name
					hook: fn
				
				@fcm.state.events.triggerEvent('DRIVER_REGISTERED', context)
				return
		
			resolve: (module, name) ->
				if typeof @registry[module] is null
					return false
				else
					if typeof @registry[module][name] is null
						return false
					else
						return @registry[module][name].hook_point