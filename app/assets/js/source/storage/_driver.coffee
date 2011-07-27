class StorageDriver
	
	constructor: (@name, @config) ->
		if $?
			fcm = $.fatcatmap
		else
			fcm = window.fatcatmap
		fcm.sys.drivers.register(@name, 'native', @, 999, true)
	
	getValueByKey: (key) ->
		
	setValueByKey: (key, value) ->
		
	addValueByKey: (key, value) ->
		
	deleteByKey: (key) ->
		
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
if window?
	window.StorageDriver = StorageDriver
	window.AdvancedStorageDriver = AdvancedStorageDriver