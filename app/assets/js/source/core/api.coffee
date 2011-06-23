## Core API Bride
class CoreAPIBridge extends CoreAPI

	constructor: ->

		## Storage API
		@storage =

			## Local Storage Interface
			local:

				_driver: null

				_resolveDriver: ->
					@_driver = window.fatcatmap.sys.drivers.resolve('storage', 'local')

				getValue: (key) ->
					if @_driver isnt null
						return @_driver.getValueByKey(key)
					else
						return false

				setValue: (key, value) ->
					if @_driver isnt null
						return @_driver.setValueByKey(key, value)
					else
						return false

				clearValues: ->
					if @_driver isnt null
						return @_driver.allValues()
					else
						return false

			## Session Storage Interface
			session:

				_driver: null

				_resolveDriver: ->
					@_driver = window.fatcatmap.sys.drivers.resolve('storage', 'session')

				getValue: (key) ->
					if @_driver isnt null
						return @_driver.getValueByKey(key)
					else
						return false

				setValue: (key, value) ->
					if @_driver isnt null
						return @_driver.setValueByKey(key, value)
					else
						return false

				clearValues: ->
					if @_driver isnt null
						return @_driver.allValues()
					else
						return false

			## IndexedDB Interface	
			object:

				_driver: null

				_resolveDriver: ->
					@_driver = window.fatcatmap.sys.drivers.resolve('storage', 'object')

				getValue: (key) ->
					if @_driver isnt null
						return @_driver.getValueByKey(key)
					else
						return false

				setValue: (key, value) ->
					if @_driver isnt null
						return @_driver.setValueByKey(key, value)
					else
						return false

				clearValues: ->
					if @_driver isnt null
						return @_driver.allValues()
					else
						return false

			## WebSQL Interface
			sql:

				_driver: null

				_resolveDriver: ->
					@_driver = window.fatcatmap.sys.drivers.resolve('storage', 'sql')

				getValue: (key) ->
					if @_driver isnt null
						return @_driver.getValueByKey(key)
					else
						return false

				setValue: (key, value) ->
					if @_driver isnt null
						return @_driver.setValueByKey(key, value)
					else
						return false

				clearValues: ->
					if @_driver isnt null
						return @_driver.allValues()
					else
						return false

		## Layout API
		@layout =
			
			register: (id, element) ->
				element.register(id)
				return fatcatmap.state.elements.register(id, element)

		## Visualizer API
		@visualizer = {}