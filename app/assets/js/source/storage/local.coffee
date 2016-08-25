## CoffeeScript - FCM storage driver - local

class LocalStorageDriver extends StorageDriver

	init: () ->
		@store = new Lawnchair {name: 'fcm-base'}, (store) ->
			$.fatcatmap.dev.log('LSB/LocalStorage', 'Driver loaded. Local store created.')
			$.fatcatmap.state.events.triggerEvent('STORAGE_DB_LOAD', {name: 'fcm-base', store: @store})
	
	getValueByKey: (key) ->
		
	setValueByKey: (key, value) ->
		
	deleteValueByKey: (key) ->
		
	nuke: () ->
		
	allValues: () ->

@LocalStorageDriver = new LocalStorageDriver().setup('localstorage', {})