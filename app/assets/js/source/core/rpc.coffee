## CoffeeScript - FCM RPC Framework
class RPCAPI
	
	constructor: (@name, @base_uri, @methods, @config) ->

		if @methods.length > 0
			for method in @methods
				@[method] = @_buildRPCMethod(method)
				
				
	_buildRPCMethod: (method) ->
		api = @name
		rpcMethod = (params={}, callbacks=null, async=false, opts={}) =>
			do (params={}, callbacks={}, async=false, opts={}) =>
				request = window.fatcatmap.rpc.api.createRPCRequest({
			
					method: method
					api: api
					params: params || {}
					opts: opts || {}
					async: async || false
			
				})
				
				if callbacks?
					return request.fulfill(callbacks)
				else
					return request
		
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

		if id?
			@envelope.id = id
		if opts?
			@envelope.opts = opts
		if agent?
			@envelope.agent = agent
		
	fulfill: (callbacks, config...) ->
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
	
	constructor: ->

		@base_rpc_uri = '/_api/rpc'
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
				
				console.log('[RPC] Request: ', request, config)
				request.setAction(@_assembleRPCURL(request.method, request.api, @action_prefix, @base_rpc_uri))
						
				return request
				
			fulfillRPCRequest: (config, request, callbacks) ->

				console.log('[RPC] Fulfill: ', config, request, callbacks)
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
				
				do (request, callbacks) ->
					@request = request
					@callbacks = callbacks
					@fatcatmap = window.fatcatmap
					
					xhr = $.ajax({
			
						url: @request.action
						data: JSON.stringify @request.payload()
						async: @request.ajax.async
						cache: @request.ajax.cache
						global: @request.ajax.global
						type: @request.ajax.http_method
						crossDomain: @request.ajax.crossDomain
						dataType: @request.ajax.dataType
						processData: false
						ifModified: @request.ajax.ifModified
						contentType: 'application/json'
				
						beforeSend: (xhr, settings) =>
							@fatcatmap.rpc.api.history[@request.envelope.id].xhr = xhr;
							return xhr
					
						error: (xhr, status, error) =>
							console.log('[RPC] Error: ', data, status, xhr)
							@fatcatmap.rpc.api.lastFailure = error
							@fatcatmap.rpc.api.history[@request.envelope.id].xhr = xhr
							@fatcatmap.rpc.api.history[@request.envelope.id].status = status
							@fatcatmap.rpc.api.history[@request.envelope.id].failure = error
							@callbacks.failure(data)
					
						success: (data, status, xhr) =>
							console.log('[RPC] Success: ', data, status, xhr)
							@fatcatmap.rpc.api.lastResponse = data
							@fatcatmap.rpc.api.history[@request.envelope.id].xhr = xhr
							@fatcatmap.rpc.api.history[@request.envelope.id].status = status
							@fatcatmap.rpc.api.history[@request.envelope.id].response = data
							@callbacks.success(data)
					
						complete: (xhr, status) =>
							@fatcatmap.rpc.api.history[@request.envelope.id].xhr = xhr
							@fatcatmap.rpc.api.history[@request.envelope.id].status = status
					
						statusCode:
					
							404: ->
								console.log('[RPC]: 404')
								alert 'RPC 404: Could not resolve RPC action URI.'
						
							403: ->
								console.log('[RPC]: 403')
								alert 'RPC 403: Not authorized to access the specified endpoint.'
						
							500: ->
								console.log('[RPC]: 500')							
								alert 'RPC 500: Woops! Something went wrong. Please try again.'
			
					})
				
				return {id: request.envelope.id, request: request}
						

		@adapters =
			
			data: new RPCAdapter('data')
			query: new RPCAdapter('query')
			graph: new RPCAdapter('graph')
			charts: new RPCAdapter('charts')
			session: new RPCAdapter('session')
			frame: new RPCAdapter('frame')
		
		@ext = null
		
		
window.RPCAPI = RPCAPI
window.RPCAdapter = RPCAdapter
window.RPCRequest = RPCRequest