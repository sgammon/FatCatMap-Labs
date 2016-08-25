## CoffeeScript - FCM State Management Framework
class CoreStateAPI extends CoreAPI
	
	constructor: (fcm) ->
		
		@ui =
			
			indicators:
				
				globalIndicatorQueue: 0
				currentGlobalProgress: 0

				startSpinner: () ->
					if @globalIndicatorQueue == 0
						$('#globalActivityIndicator').animate({opacity: 1}).removeClass('hidden')
					@globalIndicatorQueue++
					
				stopSpinner: () ->
					@globalIndicatorQueue--
					if @globalIndicatorQueue == 0
						$('#globalActivityIndicator').animate({opacity: 0}, 'fast', -> $(@).addClass('hidden'))
					
				setGlobalProgressBar: (progress) ->
					if not progress?
						progress = @currentGlobalProgress + 10
						
					if progress >= 100
						$('#globalProgress').animate({width: $('#toploader').width()}, () ->

							$('#globalProgress').css({width: 0})	
						)
						
					else
						$('#globalProgress').animate({width: $('#toploader').width() * (progress / 100)})
						
					@currentGlobalProgress = progress
		
		@events =
			
			registry: []
			callchain: {}
			history: []
			
			registerEvent: (name) =>
				@events.registry.push(name)
				@events.callchain[name] = []
				
				if fcm.dev.debug.eventlog is true
					fcm.dev.verbose('EventLog', "Event Registered: "+name)
				
				return @
				
			registerHook: (_event, fn, once) =>
								
				if typeof once is null
					once = false
				calltask =
					executed: false
					callback: (context) ->
						return fn(context)
					runonce: once
				@events.callchain[_event].push(calltask)
				if fcm.dev.debug.verbose is true
					fcm.dev.eventlog("Hook Registered", fn, "on event", _event)
					
			triggerEvent: (_event, context) =>
				
				fcm.dev.eventlog("Event Triggered", _event, context || '{no context}')
									
				if typeof @events.callchain[_event] isnt null
					if @events.callchain[_event].length > 0
						for calltask of @events.callchain[_event]
							if @events.callchain[_event][calltask].executed is true and @events.callchain[_event][calltask].runonce is true
								continue
							else
								try
									if fcm.dev.debug.eventlog is true and fcm.dev.debug.verbose is true
										fcm.dev.eventlog("Callchain", calltask, @events.callchain[_event])
									result = @events.callchain[_event][calltask].callback(context)
									result_calltask =
										event: _event
										context: context
										task: @events.callchain[_event][calltask]
										result: result
								catch error
									result_calltask =
										event: _event
										context: context
										task: @events.callchain[_event][calltask]
										error: error
									fcm.dev.error('Events', 'Calltask failed with error: ', error, result_calltask)
								finally
									@events.history.push(result_calltask)
									@events.callchain[_event][calltask].executed = true
									
		@session =
		
			_id: null
			_token: null
			_tokenHistory: []
			
			getID: () ->
				if @_id?
					return @_id
				else
					return false
					
			init: (id, token) ->
				@_id = id
				@_token = token
				@_tokenHistory.push(token)
				
			renew: (token) ->
				@_token = token
				@_tokenHistory.push(token)
			

		@local = {}
		
		@elements =
			
			registry: {}
						
			get: (id) ->
				return @registry[id]
					
			scan: ->
				$('[data-element]').each(
					buildElement: (index, element) ->
						@register( element.attr('data-element'),
							@factory(element.attr('data-element'), '#'+element.attr('id'), element.attr('data-element-type') or null)
						)
				)
				
				return @
						
			factory: (id, selector, type='LayoutElement', config={}) ->
				if type is null
					_type = LayoutElement
					
				if type is 'LayoutElement'
					_type = LayoutElement

				else if type is 'Panel'
					_type = Panel
					
				else if type is 'SuperPanel'
					_type = SuperPanel
					
				else if type is 'Navigation'
					_type = Navigation
					
				return new _type(id, selector, config)
					
			
			register: (id, element) =>
				@events.registry[id] = element

				## Trigger REGISTER_ELEMENT event
				context =
					id: id
					element: element
				fcm.state.events.triggerEvent('REGISTER_ELEMENT', context)

				return @elements.registry[id]
				
			_setState: (id, key, value) ->
				if @registry[id] isnt null
					@registry[id]._setState(key, value)
				return @
				
			_getState: (id, key, default_value=null) ->
				if @registry[id] isnt null
					return @registry[id]._getState(key, default_value)
				else
					return default_value
				
			_loadState: (id, state) ->
				if @registry[id] is null
					throw "Must register element before setting state!"
				else
					@registry[id]._loadState(state)
				return @

		### === Register State Events === ###
		
		# Session events
		@events.registerEvent('SESSION_INIT')
		@events.registerEvent('SESSION_RENEW')
		@events.registerEvent('SESSION_CHECKIN')
		@events.registerEvent('SESSION_EXPIRE')

		# Activity events
		@events.registerEvent('GLOBAL_ACTIVITY')
		@events.registerEvent('GLOBAL_ACTIVITY_FINISH')
				
		@events.registerHook('GLOBAL_ACTIVITY', => @ui.indicators.startSpinner())
		@events.registerHook('GLOBAL_ACTIVITY_FINISH', => @ui.indicators.stopSpinner())