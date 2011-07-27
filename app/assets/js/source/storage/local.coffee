## CoffeeScript - FCM storage driver - local

class LocalStorageDriver extends StorageDriver
	
	getValueByKey: (key) ->
		
	setValueByKey: (key, value) ->
		
	deleteValueByKey: (key) ->
		
	nuke: () ->
		
	allValues: () ->
		
		
class SessionStorageDriver extends StorageDriver
	
	getValueByKey: (key) ->
		
	setValueByKey: (key, value) ->
		
	deleteValueByKey: (key) ->
		
	nuke: () ->
		
	allValues: () ->
		

LocalStorageDriver('localstorage', {})
SessionStorageDriver('sessionstorage', {})