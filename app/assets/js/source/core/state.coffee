## CoffeeScript - FCM State Management Framework
class CoreStateAPI extends CoreAPI
	
	constructor: ->
		
		@events =
			
			registry: []
			callchain: {}
			history: []
			
			registerEvent: (name) ->
				@registry.push(name)
				@callchain[name] = []
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
					
			triggerEvent: (_event, context) ->
				if typeof @callchain[_event] isnt null
					if @callchain[_event].length > 0
						for calltask in @callchain[_event]
							if @callchain[_event][calltask].executed is true and @callchain[_event][calltask].runonce is true
								continue
							else
								try
									result = @callchain[_event][calltask].callback(context)
									result_calltask =
										event: _event
										context: context
										task: @callchain[_event][calltask]
										result: result
								catch error
									result_calltask =
										event: _event
										context: context
										task: @callchain[_event][calltask]
										error: error
								finally
									@history.push(result_calltask)
									@callchain[_event][calltask].executed = true
									
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
					
			
			register: (id, element) ->
				@registry[id] = element
				return @registry[id]
				
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
