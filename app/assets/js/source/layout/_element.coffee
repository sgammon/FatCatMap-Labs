class LayoutElement

	id: null
	state: {}
	config: {}
	classes: []
	element: null
	defaults: null	
	selector: null
	registered: false
	
	## Low-Level Methods
	constructor: (@selector, @config={}) ->
		
	register: (@id) ->
		return
		
	_setState: (key, value) ->
		@state[key] = value
		return @
		
	_getState: (key, default_value=null) ->
		if @state[key] is undefined
			return default_value
		else
			return @state[key]
		
	_deleteState: (key) ->
		delete @state[key]
		
	_loadState: (@state, @classes) ->
		@_refreshState()
		
	_flushState: ->
		finalState = 
			state: @state
			classes: @classes
		return finalState
		
	_refreshState: ->
		for classname in @classes
			@get().addClass(classname)


	## Mid-Level Methods
	get: ->
		if @element is null
			@element = $(@selector)
		return @element
	
	addClass: (classname) ->
		@classes.push(classname)
		@get().addClass(classname)
		return @
		
	removeClass: (classname) ->
		if classname in @classes
			@classes.remove(classname)
		@get().removeClass(classname)
		return @
		
	toggleClass: (classname) ->
		if classname in @classes
			@classes.remove(classname)
		else
			@classes.push(classname)
		@get().toggleClass(classname)				
		return @

	
	## High-Level Methods
	hide: (duration, easing, callback) ->
		@_setState('visible', false)
		@get().hide(duration, easing, callback)
		return @
		
	show: (duration, easing, callback) ->
		@_setState('visible', true)
		@get().show(duration, easing, callback)
		
	showhide: (duration, easing, callback) ->
		if @_getState('visible', false) isnt false
			@get().hide(duration, easing, callback)
		else
			@get().show(duration, easing, callback)
		return @
	
	css: (properties) ->
		@get().css(properties)
		return @
		
	animate: (properties, options={}) ->
		@get().animate(properties, options)
		return @
		
		
if window?
	window.LayoutElement = LayoutElement