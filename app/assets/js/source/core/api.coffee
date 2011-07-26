## Core API Bride
class CoreAPIBridge extends CoreAPI

	constructor: (@fcm) ->

		## Storage API
		@storage =

			## Local Storage Interface
			local:

				_driver: null

				_resolveDriver: =>
					@_driver = @fcm.sys.drivers.resolve('localstorage')

				getValue: (key) =>
					if @_driver isnt null
						return @_driver.getValueByKey(key)
					else
						return false

				setValue: (key, value) =>
					if @_driver isnt null
						return @_driver.setValueByKey(key, value)
					else
						return false

				clearValues: =>
					if @_driver isnt null
						return @_driver.allValues()
					else
						return false

			## Session Storage Interface
			session:

				_driver: null

				_resolveDriver: ->
					@_driver = @fcm.sys.drivers.resolve('sessionstorage')

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
					@_driver = @fcm.sys.drivers.resolve('objectstorage')

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
					@_driver = @fcm.sys.drivers.resolve('sqlstorage')

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
			
			register: (id, element) =>
				element.register(id)
				return @fcm.state.elements.register(id, element)

		## Visualizer API
		@visualizer = {}