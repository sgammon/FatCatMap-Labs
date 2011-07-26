class CoreSysAPI extends CoreAPI
	
	constructor: (fcm) ->
		
		@version =
			minor: null
			major: null
			release: null
		
			setVersion: (@minor, @major, @release) ->
			
		@drivers =
		
			registry: {}
			
			register: (module, name, hook, preference, initialized, callback) =>
				if not @drivers.registry[module]?
					@drivers.registry[module] = {}
				@drivers.registry[module][name] = 
					initialized: initialized
					preference: preference
					registered: true
					hook_point: hook
					init_callback: callback
				
				## Trigger DRIVER_REGISTERED
				context =
					module: module
					name: name
					hook: hook

				fcm.state.events.triggerEvent('DRIVER_REGISTERED', context)
				return
		
			resolve: (module, name) ->
				
				## Check module existence
				if not @registry[module]?
					return false
				else
					
					## If we have the name of the driver we want to load...
					if name?
						
						## If there's no such driver...
						if not @registry[module][name]?
							return false
						
						## Load if so
						else
							return @registry[module][name].hook_point
					else
						
						_default = null					
						selection = null						
						preference = 0
						for option_name of @registry[module]
							option = @registry[module][option_name]
							
							## If no preference is defined, it's set as the new default. Thus, load drivers in the order of preference you *want*, and it'll climb the ladder.
							if option.preference?
								if typeof(option.preference) == 'function'
									if $?
										cp = option.preference($.fatcatmap)
									else
										cp = option.preference(window.fatcatmap)
								else
									cp = option.preference
									
								
								if cp isnt null and typeof(cp) isnt 'boolean'
									if cp > preference
										selection = option
								else
									if cp is false
										continue
									else if cp is true
										selection = option
									else 
										continue
							else
								_default = option

						if selection isnt null
							return selection.hook_point
						else
							if _default isnt null
								return _default.hook_point
							else
								return null