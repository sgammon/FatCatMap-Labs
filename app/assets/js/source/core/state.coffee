## CoffeeScript - FCM State Management Framework
class CoreStateAPI extends CoreAPI
	
	constructor: (@fcm) ->
		
		@events =
			
			registry: []
			callchain: {}
			history: []
			
			registerEvent: (name) =>
				@events.registry.push(name)
				@events.callchain[name] = []
				
				if @fcm.dev.debug.eventlog is true
					@fcm.dev.verbose('EventLog', "Event Registered: "+name)
				
				return @
				
			registerHook: (_event, fn, once) ->
				if typeof once is null
					once = false
				try
					calltask =
						executed: false
						callback: (context) ->
							return fn(context)
						runonce: one
					@callchain[_event].push(calltask)
					
			triggerEvent: (_event, context) =>
				
				if @fcm.dev.debug.eventlog is true
					console.log("[EventLog] Event Triggered: "+_event, context || '{no context}')
									
				if typeof @events.callchain[_event] isnt null
					if @events.callchain[_event].length > 0
						for calltask in @events.callchain[_event]
							if @events.callchain[_event][calltask].executed is true and @events.callchain[_event][calltask].runonce is true
								continue
							else
								try
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
								finally
									@events.history.push(result_calltask)
									@events.callchain[_event][calltask].executed = true
									
		@session = {}
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
				@fcm.state.events.triggerEvent('REGISTER_ELEMENT', context)

				return @events.registry[id]
				
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
