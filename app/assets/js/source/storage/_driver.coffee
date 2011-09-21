class StorageDriver
	
	name = 'StorageDriver'
	store = {}
		
	setup: (@name, @config) ->
		$.fatcatmap.sys.drivers.register(@name, 'native', @init?(), 999, true)	
	
	getValueByKey: (store, key) ->
		
	setValueByKey: (store, key, value) ->
		
	addValueByKey: (store, key, value) ->
		
	deleteByKey: (store, key) ->
		
	nuke: () ->
		
	allValues: () ->
		
		
class AdvancedStorageDriver extends StorageDriver
	
	openDatabase: (name, callbacks) ->
		
	deleteDatabase: (name, callbacks) ->
	
	setDatabaseVerison: (db, version, callbacks) ->
		
	closeDatabase: (db, callbacks) ->
		
	createCollection: (db, name, key_path, auto_increment, callbacks) ->
		
	deleteCollection: (db, name, callbacks) ->
		
	clearCollection: (db, name, callbacks) ->
		

## Exports
@StorageDriver = StorageDriver
@AdvancedStorageDriver = AdvancedStorageDriver