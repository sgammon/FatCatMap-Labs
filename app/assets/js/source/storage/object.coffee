class IndexedDBDriver extends AdvancedStorageDriver

	init: () ->
		idb_adapter = null
		for adapter in Lawnchair.adapters
			if adapter.adapter == 'indexed-db'
				idb_adapter = adapter
		if idb_adapter?
			@store = new Lawnchair {name: 'fcm-object', adapter: idb_adapter}, (store) ->
				$.fatcatmap.dev.log('IDB/ObjectStorage', 'Driver loaded. Object store created.')
				$.fatcatmap.state.events.triggerEvent('STORAGE_DB_LOAD', {name: 'fcm-object', store: @store})
		else
			$.fatcatmap.dev.log('IDB/ObjectStorage', 'Failed to resolve IndexedDB lawnchair driver.')

	save: (db, kind, key, callbacks) ->
		
	setValueByKey: (db, kind, key, value, callbacks) ->
		
	addValueByKey: (db, kind, key, value, callbacks) ->
		
	deleteValueByKey: (db, kind, key, callbacks) ->
		
	openDatabase: (name, callbacks) ->
		
	deleteDatabase: (db, callbacks) ->
		
	setDatabaseVersion: (db, version, callbacks) ->
		
	closeDatabase: (db, callbacks) ->
		
	createCollection: (db, name, key_path, auto_increment, callbacks) ->
		
	deleteCollection: (db, name) ->
		
	clearCollection: (db, name) ->
		
		
@IndexedDBDriver = new IndexedDBDriver().setup('objectstorage', {})