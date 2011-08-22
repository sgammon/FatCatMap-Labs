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
					@storage.local._driver = fcm.sys.drivers.resolve('localstorage')

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
					@storage.session._driver = fcm.sys.drivers.resolve('sessionstorage')

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
				_db: null
				_driver: null


				## === Internal Methods === ##
				_resolveDriver: =>
					@storage.object._driver = @fcm.sys.drivers.resolve('objectstorage')
					
				_setDB: (event) ->
					@_db = event.target.result
				
				_unsetDB: (event) ->
					@_db = null
					
				_dbError: (event) =>
					fcm.dev.error('Storage', 'Error encountered in OBJECT storage.', event)


				## === Database Operations === ##
				db:
					
					## Load or create a database by name
					load: (name, success, error) =>
						if @storage.object._driver isnt null						
							fcm.state.events.triggerEvent('STORAGE_DB_LOAD', type: 'object', name: name)

							dbLoadSuccess: (event) =>
								@storage.object._setDB(event)
								success(event.target.db)
							
							dbLoadError: (event) =>
								@storage.object._dbError(event)
								error(event)

							request = @storage.object._driver.openDatabase(name, success: dbLoadSuccess, error: dbLoadError)
							return request
						else
							return null
						
					## Delete the loaded database
					delete: (success, error) =>
						if @storage.object._driver isnt null
							if @storage.object._db isnt null
								fcm.state.events.triggerEvent('STORAGE_DB_DELETE', type: 'object', db: @storage.object._db)
						
								dbDeleteSuccess: (event) =>
									@storage.object._unsetDB(event)
									success(event)
							
								dbDeleteError: (event) =>
									@storage.object._dbError(event)
									error(event)
						
								request = @storage.object._driver.deleteDatabase(@storage.object._db, success: dbDeleteSuccess, error: dbDeleteError)
								return request
							else
								fcm.dev.error('Storage', 'Cannot delete database before it is loaded.')
								throw "Must open a database before it can be deleted."
						else
							return null
					
					## Set the loaded database's version
					setVersion: (version, success, error) =>
						if @storage.object._driver isnt null
							if @storage.object._db isnt null
								fcm.state.events.triggerEvent('STORAGE_DB_SETVERSION', type: 'object', version: version, db: @storage.object._db)
							
								dbSetVersionSuccess: (event) =>
									success(event)
								
								dbSetVersionError: (event) =>
									error(event)
							
								request = @storage.object._driver.setDatabaseVersion(@storage.object._db, version, success: dbSetVersionSuccess, error: dbSetVersionError)
								return request
							else
								fcm.dev.error('Storage', 'Cannot set database version before it is loaded.')
								throw "Must open a database before its version can be set."
						else
							return null
						
					## Close the loaded database
					close: (success, error) =>
						if @storage.object._driver isnt null
							if @storage.object._db isnt null							
								fcm.state.events.triggerEvent('STORAGE_DB_CLOSE', type: 'object', db: @storage.object.db)
								
								dbCloseSuccess: (event) =>
									success(event)
									
								dbCloseError: (event) =>
									error(event)
									
								request = @storage.object._driver.closeDatabase(@storage.object._db, success: dbCloseSuccess, error: dbCloseError)
								return request
							else
								fcm.dev.error('Storage', 'Cannot close database before it is loaded.')
								throw "Must open a database before it can be closed."
						else
							return null
							

				## === Collection Operations === ##
				collection:
					
					## Creates a collection (in the IndexedDB spec, it's called an ObjectStore)
					create: (name, key_path=null, auto_increment=true, success=null, error=null) =>
						if @storage.object._driver isnt null
							if @storage.object._db isnt null
								fcm.state.events.triggerEvent('STORAGE_COLLECION_CREATE', type: 'object', db: @storage.object._db)
								
								collectionCreateSuccess: (event) =>
									if success isnt null
										success(event)
								
								collectionCreateError: (event) =>
									if error isnt null
										error(event)
										
								request = @storage.object._driver.createCollection(@storage.object._db, name, key_path, auto_increment, success: collectionCreateSuccess, error: collectionCreateError)
								return request
							else
								fcm.dev.error('Storage', 'Cannot call createCollection before loadDB.')
								throw "Must open a database before creating a collection."
						else
							return null
						
					## Deletes a collection
					delete: (name, success=null, error=null) =>
						if @storage.object._driver isnt null
							if @storage.object._db isnt null
								fcm.state.events.triggerEvent('STORAGE_COLLECTION_DELETE', type: 'object', name: name, db: @storage.object._db)
								
								collectionDeleteSuccess: (event) =>
									if success isnt null
										success(event)
										
								collectionDeleteError: (event) =>
									if error isnt null
										error(event)
								
								request = @storage.object._driver.deleteCollection(@storage.object._db, name, success: collectionDeleteSuccess, error: collectionDeleteError)
								return request
							else
								fcm.dev.error('Storage', 'Cannot call deleteCollection before loadDB.')
								throw "Must open a database before deleting a collection."
						else
							return null
							
					## Clears a collection of all stored values
					clear: (name, success=null, error=null) =>
						if @storage.object._driver isnt null
							if @storage.object._db isnt null
								fcm.state.events.triggerEvent('STORAGE_COLLECTION_CLEAR', type: 'object', name: name, db: @storage.object._db)

								collectionClearSuccess: (event) =>
									if success isnt null
										success(event)

								collectionClearError: (event) =>
									if error isnt null
										error(event)

								request = @storage.object._driver.clearCollection(@storage.object._db, name, success: collectionDeleteSuccess, error: collectionDeleteError)
								return request
							else
								fcm.dev.error('Storage', 'Cannot call clearCollection before loadDB.')
								throw "Must open a database before clearing a collection."
						else
							return null							


				## === General Operations === ##

				## Get an IDB object by key & kind (collection name)
				get: (kind, key, success=null, error=null) =>
					if @storage.object._driver isnt null
						if @storage.object._db isnt null
							fcm.state.events.triggerEvent('STORAGE_READ', type: 'object', mode: 'key', collection: kind, db: @storage.object._db, key: key)
							
							entityGetSuccess: (event) =>
								if success isnt null
									success(event)
									
							entityGetError: (event) =>
								if error isnt null
									error(event)
									
							request = @storage.object._driver.getValueByKey(@storage.object._db, kind, key, success: entityGetSuccess, error: entityGetError)
							return request
						else
							fcm.dev.error('Storage', 'Cannot call get before loadDB.')
							throw "Must open a database connection before keys can be retrieved."
					else
						return null

				## Add a value by kind & key (only if it doesn't exist - see put() for overwrite)
				add: (value, kind, key=null, success=null, error=null) =>
					if @storage.object._driver isnt null
						if @storage.object._db isnt null
							fcm.state.events.triggerEvent('STORAGE_WRITE', type: 'object', mode: 'add', collection: kind, db: @storage.object._db, key: key)

							entityAddSuccess: (event) =>
								if success isnt null
									success(event)

							entityAddError: (event) =>
								if error isnt null
									error(event)

							request = @storage.object._driver.addValueByKey(@storage.object._db, kind, key, value, success: entityAddSuccess, error: entityAddError)
							return request
						else
							fcm.dev.error('Storage', 'Cannot call add before loadDB.')
							throw "Must open a database connection before keys can be added."
					else
						return null
						
				## Store a value by kind & key (regardless of whether it already exists)		
				put: (value, kind, key=null, success=null, error=null) =>
					if @storage.object._driver isnt null
						if @storage.object._db isnt null
							fcm.state.events.triggerEvent('STORAGE_WRITE', type: 'object', mode: 'put', collection: kind, db: @storage.object._db, key: key)

							entityPutSuccess: (event) =>
								if success isnt null
									success(event)

							entityPutError: (event) =>
								if error isnt null
									error(event)

							request = @storage.object._driver.setValueByKey(@storage.object._db, kind, key, value, success: entityPutSuccess, error: entityPutError)
							return request
						else
							fcm.dev.error('Storage', 'Cannot call get before loadDB.')
							throw "Must open a database connection before keys can be retrieved."
					else
						return null				
				
				## Delete a value by kind & key
				delete: (kind, key, success=null, error=null) =>
					if @storage.object._driver isnt null
						if @storage.object._db isnt null
							fcm.state.events.triggerEvent('STORAGE_DELETE', type: 'object', collection: kind, db: @storage.object._db, key: key)
							
							entityDeleteSuccess: (event) =>
								if success isnt null
									success(event)
							
							entityDeleteError: (event) =>
								if error isnt null
									error(event)
									
							request = @storage.object._driver.deleteByKey(@storage.object._db, kind, key, success: entityDeleteSuccess, error: entityDeleteError)
							return request
					else
						return false


			## 4: SQL Storage
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