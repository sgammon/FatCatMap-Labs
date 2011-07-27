class CoreDevAPI extends CoreAPI

	constructor: (fcm) ->

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
						return
						
					hide: (selector) ->
						$('#js_fps_stats').hide()
						return
		
		@debug =
			logging: true
			eventlog: true
			verbose: true
			
			
	setDebug: (@debug) =>
		console.log("[CoreDev] Debug has been set.", @debug)
		
	log: (module, message, context...) =>
		if not context?
			context = '{no context}'
		if @debug.logging is true
			console.log "["+module+"] INFO: "+message, context...
		return
			
	error: (module, message, context...) =>
		if @debug.logging is true
			console.log "["+module+"] ERROR: "+message, context...
		return
			
	verbose: (module, message, context...) =>
		if @debug.verbose is true
			@log(module, message, context...)
		return