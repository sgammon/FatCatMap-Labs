## FatCatMap Object
class FatCatMap
	
	constructor: (@config)  ->
		
		## Dev API
		@dev = new CoreDevAPI(@)

		## Sys API
		@sys = new CoreSysAPI(@)

		## Agent API
		@agent = new CoreAgentAPI(@)
		@agent.discover()

		## State API
		@state = new CoreStateAPI(@)
		@state.events.registerEvent 'RPC_READY'
		@state.events.registerEvent 'API_READY'
		@state.events.registerEvent 'CORE_READY'
		@state.events.registerEvent 'DRIVER_REGISTERED'
		@state.events.registerEvent 'REGISTER_ELEMENT'
		@state.events.registerEvent 'PLATFORM_READY'
		
		@state.events.triggerEvent 'GLOBAL_ACTIVITY'
		@state.events.registerHook 'PLATFORM_READY', => @state.events.triggerEvent 'GLOBAL_ACTIVITY_FINISH'
		
		## Model API
		@model = new CoreModelAPI(@)

		## Javascript API Methods
		@api = new CoreAPIBridge(@)
				
		## Users API
		@user = new CoreUserAPI(@)
		
		## RPC API
		@rpc = new CoreRPCAPI(@)
		
		## Live API
		@live = new CoreLiveAPI(@)
		
		return @


window.fatcatmap = new FatCatMap()
if $?
	$.extend(fatcatmap: window.fatcatmap)
window.fatcatmap.state.events.triggerEvent 'CORE_READY'