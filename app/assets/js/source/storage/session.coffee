## CoffeeScript - FCM storage driver - session storage

class SessionStorageDriver extends StorageDriver

	init: () ->
		@store = new Lawnchair {name: 'fcm-session'}, (store) ->
			$.fatcatmap.dev.log('SSB/SessionStorage', 'Driver loaded. Session store created.')
			$.fatcatmap.state.events.triggerEvent('STORAGE_DB_LOAD', {name: 'fcm-session', store: @store})

	getValueByKey: (key) ->
		
	setValueByKey: (key, value) ->
		
	deleteValueByKey: (key) ->
		
	nuke: () ->
		
	allValues: () ->

@SessionStorageDriver = new SessionStorageDriver().setup('sessionstorage', {})