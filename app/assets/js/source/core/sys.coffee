class CoreSysAPI extends CoreAPI
	
	constructor: ->
		
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
		
			resolve: (module, name) ->
				if typeof @registry[module] is null
					return false
				else
					if typeof @registry[module][name] is null
						return false
					else
						return @registry[module][name].hook_point

						
class CoreDevAPI extends CoreAPI

	constructor: ->

		@config = {}
		@environment = {}

		@performance =
			tools:
				fpsstats:
					show: (selector) ->
						
						stats = new Stats()
						stats.domElement.style.position = 'absolute'
						stats.domElement.style.left = '50px'
						stats.domElement.style.top = '50px'
						stats.domElement.style.opacity = 0.7
						stats.domElement.id = 'js_fps_stats'
						
						console.log('stats', stats)

						$('body').append(stats.domElement)

						setInterval(

							->
							    stats.update()

						, 1000 / 60 );
						
					hide: (selector) ->
						$('#js_fps_stats').hide()
		
		@debug =
			logging: true
			eventlog: true
			verbose: true