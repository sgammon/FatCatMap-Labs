## FatCatMap Object
class FatCatMap
	
	constructor: (@config)  ->
		
		## Javascript API Methods
		@api = new CoreAPIBridge
			
		## Agent Object
		@agent = new CoreAgentAPI	
		@agent.discover()
		
		## Client State Framework
		@state = new CoreStateAPI
		@state.events.registerEvent('CORE_INIT')
		@state.events.registerEvent('RPC_INIT')
		@state.events.registerEvent('API_INIT')
		@state.events.registerEvent('CORE_READY')
		@state.events.registerEvent('DRIVER_REGISTERED')
		@state.events.registerEvent('REGISTER_ELEMENT')
		@state.events.registerEvent('PLATFORM_READY')		
		
		## Users API		
		@user = new CoreUserAPI
		
		## RPC API
		@rpc = new CoreRPCAPI
		@rpc.api.factory('data', '/_api/rpc/data', ['get', 'retrieveGraphObject', 'retrieveNative', 'retriveAsset'])
		@rpc.api.factory('query', '/_api/rpc/query', ['search','gql','autocomplete'])
		@rpc.api.factory('graph', '/_api/rpc/graph', ['construct', 'constructFromNode', 'constructFromObject'])
		@rpc.api.factory('charts', '/_api/rpc/charts', ['generate', 'generateFromSeries'])
		@rpc.api.factory('session', '/_api/rpc/session', ['init', 'authenticate', 'checkin'])
		
		## SYS API
		@sys = new CoreSysAPI

		## Dev API
		@dev = new CoreDevAPI
		
		return @
		
window.fatcatmap = new FatCatMap