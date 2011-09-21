## CoffeeScript - FCM RPC Framework
class RPCAPI
	
	constructor: (@name, @base_uri, @methods, @config) ->

		if @methods.length > 0
			for method in @methods
				@[method] = @_buildRPCMethod(method, base_uri, config)
				
				
	_buildRPCMethod: (method, base_uri, config) ->
		api = @name
		rpcMethod = (params={}, callbacks=null, async=false, opts={}) =>
			do (params={}, callbacks=null, async=false, opts={}) =>
				if $?
					fcm = $.fatcatmap
				else
					fcm = window.fatcatmap
				request = fcm.rpc.api.createRPCRequest({
			
					method: method
					api: api
					params: params || {}
					opts: opts || {}
					async: async || false
					
				})
				
				if callbacks isnt null
					return request.fulfill(callbacks)
				else
					return request
		
		if $?
			$.fatcatmap.rpc.registerAPIMethod(api, method, base_uri, config)
		else
			window.fatcatmap.rpc.registerAPIMethod(api, method, base_uri, config)
		return rpcMethod


class RPCAdapter
	
	constructor: (@name) ->
		
	request: (request) ->
		return request
		
	response: (response, callbacks) ->
		if 'success' in callbacks
			window.fatcatmap.rpc.adapters.makeCallback(response, callbacks.success)


class RPCRequest
	

	constructor: (id, opts, agent) ->

		@params = {}
		@action = null
		@method = null
		@api = null
		@base_uri = null

		@envelope =
			id: null
			opts: {}
			agent: {}

		@ajax =
			async: false
			cache: true
			global: true
			http_method: 'POST'
			crossDomain: false
			ifModified: false
			dataType: 'json'
			contentType: 'application/json'

		if id?
			@envelope.id = id
		if opts?
			@envelope.opts = opts
		if agent?
			@envelope.agent = agent
		
	fulfill: (callbacks, config...) ->
	
		if not callbacks?.success
			defaultSuccessCallback = (context) =>
				$.fatcatmap.dev.log('RPC', 'RPC succeeded but had no success callback.', @)
			callbacks.success = defaultSuccessCallback
		
		if not callbacks?.failure
			defaultFailureCallback = (context) =>
				$.fatcatmap.dev.error('RPC', 'RPC failed but had no failure callback.', @)
			callbacks.failure = defaultFailureCallback
	
		return window.fatcatmap.rpc.api.fulfillRPCRequest(config, @, callbacks)

	setAsync: (async) ->
		@ajax?.async ?= async
		return @

	setOpts: (opts) ->
		@envelope?.opts ?= opts
		return @
		
	setAgent: (agent) ->
		@envelope?.agent ?= agent
		return @
		
	setAction: (@action) ->
		return @
		
	setMethod: (@method) ->
		return @
		
	setAPI: (@api) ->
		return @
		
	setBaseURI: (@base_uri) ->
		return @
		
	setParams: (@params={}) ->
		return @
			
	payload: ->
		_payload =
			id: @envelope.id
			opts: @envelope.opts
			agent: @envelope.agent
			request:
				params: @params
				method: @method
				api: @api
				
		return _payload


## Core RPC API
class CoreRPCAPI extends CoreAPI
	
	constructor: (fcm) ->

		## Register FCM events
		fcm.state.events.registerEvent('RPC_CREATE')
		fcm.state.events.registerEvent('RPC_FULFILL')
		fcm.state.events.registerEvent('RPC_SUCCESS')
		fcm.state.events.registerEvent('RPC_ERROR')
		fcm.state.events.registerEvent('RPC_COMPLETE')
		fcm.state.events.registerEvent('RPC_PROGRESS')
		
		## Use amplify, if we can
		if window.amplify?
			fcm.dev.verbose('RPC', 'AmplifyJS detected. Registering.')
			fcm.sys.drivers.register('transport', 'amplify', window.amplify, true, true)

		@base_rpc_uri = '/_api/rpc'
		
		
		## Set up request internals
		original_xhr = $.ajaxSettings.xhr
		
		@internals =
		
			transports:
				
				xhr:
					factory: () =>
						req = original_xhr()
						if req
							if typeof req.addEventListener == 'function'
								req.addEventListener("progress", (ev) =>
										$.fatcatmap.state.events.triggerEvent('RPC_PROGRESS', {event: ev})
								, false)
						return req
						
		$.ajaxSetup(
			
			global: true			
			xhr: () =>
				return @internals.transports.xhr.factory()

		)
		
		@api =
			
			lastRequest: null
			lastFailure: null
			lastResponse: null
			action_prefix: null
			history: {}
			used_ids: []
			
			factory: (name, base_uri, methods, config) ->
				@[name] = new RPCAPI(name, base_uri, methods, config)
					
			_assembleRPCURL: (method, api=null, prefix=null, base_uri=null) ->
				if api is null and base_uri is null
					throw "[RPC] Error: Must specify either an API or base URI to generate an RPC endpoint."
				else
					if base_uri is null ## if we're working with an API, get the base URI
						base_uri = window.fatcatmap.rpc.api[api].base_uri

					if prefix isnt null
						return [prefix+base_uri, method].join('.')
					else
						return [base_uri, method].join('.')
						
			provisionRequestID: ->
				if @used_ids.length > 0
					id = Math.max.apply(@, @used_ids)+1
					@used_ids.push(id)
					return id
				else
					@used_ids.push(1)
					return 1
											
			decodeRPCResponse: (data, status, xhr, success, error) ->
				success(data, status)
					
			createRPCRequest: (config) ->

				request = new RPCRequest(@provisionRequestID())

				if config.api?
					request.setAPI(config.api)

				if config.method?
					request.setMethod(config.method)

				if config.agent?
					request.setAgent(config.agent)

				if config.opts?
					request.setOpts(config.opts)

				if config.base_uri?
					request.setBaseURI(config.base_uri)

				if config.params?
					request.setParams(config.params)

				if config.async?
					request.setAsync(config.async)
				
				if $?
					$.fatcatmap.dev.log('RPC', 'New Request', request, config)
				else
					window.fatcatmap.dev.log('RPC', 'New Request', request, config)
				
				request.setAction(@_assembleRPCURL(request.method, request.api, @action_prefix, @base_rpc_uri))
						
				return request
				
			fulfillRPCRequest: (config, request, callbacks) ->

				if $?
					$.fatcatmap.dev.log('RPC', 'Fulfill', config, request, callbacks)
				else
					window.fatcatmap.dev.log('RPC', 'Fulfill', config, request, callbacks)

				@lastRequest = request

				@history[request.envelope.id] =
					request: request
					config: config
					callbacks: callbacks

				if request.action is null
					if request.method is null
						throw "[RPC] Error: Request must specify at least an action or method."
					if request.base_uri is null
						if request.api is null
							throw "[RPC] Error: Request must have an API or explicity BASE_URI."
						else
							request.action = @_assembleRPCURL(request.method, request.api, @action_prefix)
					else
						request.action = @_assembleRPCURL(request.method, null, @action_prefix, request.base_uri)

				if request.action is null or request.action is undefined
					throw '[RPC] Error: Could not determine RPC action.'
					
				context =
					config: config
					request: request
					callbacks: callbacks
				fcm.state.events.triggerEvent('RPC_FULFILL', context)
				
				do (request, callbacks) ->
					fatcatmap = window.fatcatmap
					
					xhr_settings =
						resourceId: request.api+'.'+request.method
						url: request.action
						data: JSON.stringify request.payload()
						async: request.ajax.async
						global: request.ajax.global
						type: request.ajax.http_method
						crossDomain: request.ajax.crossDomain
						dataType: request.ajax.dataType
						processData: false
						ifModified: request.ajax.ifModified
						contentType: request.ajax.contentType
			
						beforeSend: (xhr, settings) =>
							fatcatmap.rpc.api.history[request.envelope.id].xhr = xhr;
							callbacks?.status?('beforeSend')
							return xhr
				
						error: (xhr, status, error) =>
							callbacks?.status?('error')
							fatcatmap.dev.error('RPC', 'Error: ', {error: error, status: status, xhr: xhr})
							fatcatmap.rpc.api.lastFailure = error
							fatcatmap.rpc.api.history[request.envelope.id].xhr = xhr
							fatcatmap.rpc.api.history[request.envelope.id].status = status
							fatcatmap.rpc.api.history[request.envelope.id].failure = error
						
							context =
								xhr: xhr
								status: status
								error: error
								
							fatcatmap.state.events.triggerEvent('RPC_ERROR', context)
							fcm.state.events.triggerEvent('RPC_COMPLETE', context)			
							callbacks?.failure?(error)
				
						success: (data, status, xhr) =>

							if data.status == 'ok'
								callbacks?.status?('success')
								fatcatmap.dev.log('RPC', 'Success', data, status, xhr)
								fatcatmap.rpc.api.lastResponse = data
								fatcatmap.rpc.api.history[request.envelope.id].xhr = xhr
								fatcatmap.rpc.api.history[request.envelope.id].status = status
								fatcatmap.rpc.api.history[request.envelope.id].response = data

								context =
									xhr: xhr
									status: status
									data: data
								fcm.state.events.triggerEvent('RPC_SUCCESS', context)
								fcm.state.events.triggerEvent('RPC_COMPLETE', context)

								fatcatmap.dev.verbose('RPC', 'Success callback', callbacks)
							
								callbacks?.success?(data.response.content, data.response.type, data)
							
							else if data.status == 'failure'
								callbacks?.status?('error')
								fatcatmap.dev.error('RPC', 'Error: ', {error: error, status: status, xhr: xhr})
								fatcatmap.rpc.api.lastFailure = error
								fatcatmap.rpc.api.history[request.envelope.id].xhr = xhr
								fatcatmap.rpc.api.history[request.envelope.id].status = status
								fatcatmap.rpc.api.history[request.envelope.id].failure = error
						
								context =
									xhr: xhr
									status: status
									error: error
								
								fatcatmap.state.events.triggerEvent('RPC_ERROR', context)
								fcm.state.events.triggerEvent('RPC_COMPLETE', context)			
								callbacks?.failure?(error)

				
						statusCode:
				
							404: ->
								fatcatmap.dev.error('RPC', 'HTTP/404', 'Could not resolve RPC action URI.')
								fatcatmap.state.events.triggerEvent('RPC_ERROR', message: 'RPC 404: Could not resolve RPC action URI.', code: 404)
					
							403: ->
								fatcatmap.dev.error('RPC', 'HTTP/403', 'Not authorized to access the specified endpoint.')
								fatcatmap.state.events.triggerEvent('RPC_ERROR', message: 'RPC 403: Not authorized to access the specified endpoint.', code: 403)
					
							500: ->
								fatcatmap.dev.error('RPC', 'HTTP/500', 'Internal server error.')
								fatcatmap.state.events.triggerEvent('RPC_ERROR', message: 'RPC 500: Woops! Something went wrong. Please try again.', code: 500)
				
					amplify = fatcatmap.sys.drivers.resolve('transport', 'amplify')
					if amplify? and amplify is not false
						fatcatmap.dev.verbose('RPC', 'Fulfilling with AmplifyJS adapter.')
						xhr_action = amplify.request
						xhr = xhr_action(xhr_settings)
					else
						fatcatmap.dev.verbose('RPC', 'Fulfilling with AJAX adapter.')
						xhr = $.ajax(xhr_settings)
						
					fatcatmap.dev.verbose('RPC', 'Resulting XHR: ', xhr)
					
				return {id: request.envelope.id, request: request}
						

		@adapters =
			
			data: new RPCAdapter('data')
			query: new RPCAdapter('query')
			graph: new RPCAdapter('graph')
			charts: new RPCAdapter('charts')
			session: new RPCAdapter('session')
			frame: new RPCAdapter('frame')
		
		@ext = null
		
		fcm.state.events.registerHook 'RPC_FULFILL', -> $.fatcatmap.state.events.triggerEvent 'GLOBAL_ACTIVITY'
		fcm.state.events.registerHook 'RPC_COMPLETE', -> $.fatcatmap.state.events.triggerEvent 'GLOBAL_ACTIVITY_FINISH'
		fcm.state.events.registerHook 'RPC_PROGRESS', (event) -> console.log('progress', event)
		
	registerAPIMethod: (api, name, base_uri, config) ->
		if $?
			fcm = $.fatcatmap
		else
			fcm = window.fatcatmap
		amplify = fcm.sys.drivers.resolve('transport', 'amplify')
		if amplify isnt false
			fcm.dev.log('RPCAPI', 'Registering request procedure "'+api+'.'+name+'" with AmplifyJS.')

			resourceId = api+'.'+name
			base_settings =
				type: 'POST'
				dataType: 'json'
				contentType: 'application/json'
				url: @api._assembleRPCURL(name, api, null, base_uri)
				decoder: @api.decodeRPCResponse

			if config.caching?
				if config.caching == true
					base_settings.caching = 'persist'
				amplify.request.define(resourceId, "ajax", base_settings)
			else
				amplify.request.define(resourceId, "ajax", base_settings)

		
		
window.RPCAPI = RPCAPI
window.RPCAdapter = RPCAdapter
window.RPCRequest = RPCRequest