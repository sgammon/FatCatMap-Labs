## Core API Bride
class CoreAPIBridge extends CoreAPI

	constructor: (fcm) ->

		## ========== Register events ========== ##
		
		# Storage API
		fcm.state.events.registerEvent('STORAGE_READ')		
		fcm.state.events.registerEvent('STORAGE_WRITE')
		fcm.state.events.registerEvent('STORAGE_CLEAR')
		fcm.state.events.registerEvent('STORAGE_DELETE')		
		fcm.state.events.registerEvent('STORAGE_DB_LOAD')
		fcm.state.events.registerEvent('STORAGE_DB_CLOSE')		
		fcm.state.events.registerEvent('STORAGE_DB_QUERY')		
		fcm.state.events.registerEvent('STORAGE_DB_CREATE')
		fcm.state.events.registerEvent('STORAGE_DB_DELETE')
		fcm.state.events.registerEvent('STORAGE_DB_SETVERSION')		
		fcm.state.events.registerEvent('STORAGE_DB_TRANSACTION')
		fcm.state.events.registerEvent('STORAGE_COLLECTION_CLEAR')
		fcm.state.events.registerEvent('STORAGE_COLLECTION_CREATE')
		fcm.state.events.registerEvent('STORAGE_COLLECTION_DELETE')


		## ========== FatCatMap Storage API ========== ##
		@storage =

			## 1: Local Storage
			local:

				_driver: null

				_resolveDriver: =>
					@storage.local._driver = $.fatcatmap.sys.drivers.resolve('localstorage')

				## Get a LocalStorage value by key
				get: (key) =>
					if @storage.local._driver isnt null
						fcm.state.events.triggerEvent('STORAGE_READ', type: 'local', mode: 'key', key: key)						
						return @storage.local._driver.getValueByKey(key)
					else
						return null
						
				## Set a LocalStorage value by key
				set: (key, value) =>
					if @storage.local._driver isnt null
						fcm.state.events.triggerEvent('STORAGE_WRITE', type: 'local', key: key, value: value)						
						return @storage.local._driver.setValueByKey(key, value)
					else
						return null
						
				## Delete a LocalStorage value by key
				delete: (key) =>
					if @storage.local._driver isnt null
						fcm.state.events.triggerEvent('STORAGE_DELETE', type: 'local', key: key)
						return @storage.local._driver.deleteByKey(key)
					else
						return null

				## Clear LocalStorage of all values
				clear: =>
					if @storage.local._driver isnt null
						fcm.state.events.triggerEvent('STORAGE_CLEAR', type: 'local')
						return @_driver.nuke()
					else
						return null
						
				## Return all values stored in LocalStorage
				all: =>
					if @storage.local._driver isnt null
						fcm.state.events.triggerEvent('STORAGE_READ', type: 'local', mode: 'all')
						return @storage.local._driver.allValues()
					else
						return null

			## 2: Session Storage
			session:

				_driver: null

				_resolveDriver: =>
					@storage.session._driver = $.fatcatmap.sys.drivers.resolve('sessionstorage')

				## Get a SessionStorage value by key
				get: (key) =>
					if @storage.session._driver isnt null
						fcm.state.events.triggerEvent('STORAGE_READ', type: 'session', mode: 'key', key: key)
						return @storage.session._driver.getValueByKey(key)
					else
						return null

				## Set a SessionStorage value by key
				set: (key, value) =>
					if @storage.session._driver isnt null
						fcm.state.events.triggerEvent('STORAGE_WRITE', type: 'session', key: key, value: value)						
						return @storage.session._driver.setValueByKey(key, value)
					else
						return null
				
				## Delete a SessionStorage value by key
				delete: (key) =>
					if @storage.session._driver isnt null
						@fcm.state.events.triggerEvent('STORAGE_DELETE', type: 'session', key: key)
						return @storage.session._driver.deleteByKey(key)
					else
						return null

				## Clear SessionStorage of all values
				clear: =>
					if @storage.session._driver isnt null
						fcm.state.events.triggerEvent('STORAGE_CLEAR', type: 'session')
						return @storage.session._driver.nuke()
					else
						return null

				## Return all values stored in SessionStorage
				all: =>
					if @storage.session._driver isnt null
						fcm.state.events.triggerEvent('STORAGE_READ', type: 'session', mode: 'all')
						return @storage.session._driver.allValues()
					else
						return null


			## 3: IndexedDB Storage
			object:

				## === Internal Properties === ##
				_driver: null


				## === Internal Methods === ##
				_resolveDriver: =>
					@storage.object._driver = $.fatcatmap.sys.drivers.resolve('objectstorage')
					
				_dbError: (event) =>
					fcm.dev.error('Storage', 'Error encountered in OBJECT storage.', event)
							

				## === General Operations === ##

				get: (args...) =>
					if @_driver?
						@_resolveDriver()
					return @_driver.get(args...)

				keys: (args...) =>
					if @_driver?
						@_resolveDriver()
					return @_driver.keys(args...)

				batch: (args...) =>
					if @_driver?
						@_resolveDriver()
					return @_driver.batch(args...)
					
				save: (args...) =>
					if @_driver?
						@_resolveDriver()
					return @_driver.save(args...)					

				exists: (args...) =>
					if @_driver?
						@_resolveDriver()
					return @_driver.exists(args...)

				each: (args...) =>
					if @_driver?
						@_resolveDriver()
					return @_driver.each(args...)
						
				all: (args...) =>
					if @_driver?
						@_resolveDriver()
					return @_driver.all(args...)
				
				remove: (args...) =>
					if @_driver?
						@_resolveDriver()
					return @_driver.remove(args...)

				nuke: (args...) =>
					if @_driver?
						@_resolveDriver()
					return @_driver.nuke(args...)


		## ========== FatCatMap Layout API ========== ##
		@layout =
			
			register: (id, element) =>
				element.register(id)
				return fcm.state.elements.register(id, element)
				
			render: (id, element) =>
				return
				
			renderTemplate: (id, context...) =>
				return


		## ========== FatCatMap Visualizer API ========== ##
		fcm.state.events.registerEvent('MAP_REGISTERED')
		fcm.state.events.registerEvent('MAP_DATA_CHANGE')
		fcm.state.events.registerEvent('MAP_NODE_ADDED')
		fcm.state.events.registerEvent('MAP_EDGE_ADDED')
		fcm.state.events.registerEvent('MAP_DRAW')
		fcm.state.events.registerEvent('MAP_SHIFT_ORIGIN')
		
		@visualizer =
		
			graph:
				
				currentGraph: null
					
				register: (@currentGraph) ->
				
				showMore: (node) ->
					
					$('#nodeDetails #node_label').text(node.label)
					$('#nodeDetails #node_kind').text(node.kind)

					list = ''
					
					neighbors = @currentGraph.index.neighbors_by_node[node.key.encoded]
					
					_.each( neighbors, (neighbor) =>
						list += '<li><a href="#">'+neighbor.label+'</a></li>'
					)
					
					$('#nodeDetails #node_outgoing_edges').html(list);