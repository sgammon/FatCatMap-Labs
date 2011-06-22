## CoffeeScript - FCM RPC Framework
class RPCAPI
	
	constructor: (@name, @base_uri, @methods, @config) ->
		if @methods.length > 0
			for method in @methods
				@[method] = (params={}, callbacks={}, async=false, opts={}) ->
					return @makeRPCRequest(method, params, opts, async).fulfill(callbacks)
		
	makeRPCRequest: (method, params, opts, async) ->
		if method in @methods
			return fatcatmap.rpc.api.createRPCRequest({
				
				method: method
				api: @name
				params: params || {}
				opts: opts || {}
				async: async || false
				
			})
		
	__noSuchMethod__: (id, args) ->
		if method in @methods
			return fatcatmap.rpc.createRPCRequest({
				
				method: method
				api: @name
				params: args[0..args.length-2] || {}
				opts: args[-1] || {}
				async: args[-2] || false
				
			})


class RPCAdapter
	
	constructor: (@name) ->
		
	request: (request) ->
		return request
		
	response: (response, callbacks) ->
		if 'success' in callbacks
			fatcatmap.rpc.adapters.makeCallback(response, callbacks.success)


class RPCRequest
	
	params = {}
	action = null
	method = null
	api = null
	base_uri = null
	
	envelope:
		id: null
		opts: {}
		agent: {}
		
	ajax:
		async: false
		cache: true
		global: true
		http_method: 'POST'
		crossDomain: false
		ifModified: false
		dataType: 'json'

	constructor: (id, opts, agent) ->
		@envelope.id = id
		@envelope.opts = opts
		@envelope.agent = agent
		
	fulfill: (callbacks, config...) ->
		return fatcatmap.rpc.api.fulfillRPCRequest(config, @, @ajax.async)
		
	setOpts: (opts) ->
		@envelope.opts = opts
		
	setAgent: (agent) ->
		@envelope.agent = agent
		
	setAction: (action) ->
		@action = action
		
	setMethod: (method) ->
		@method = method
		
	setAPI: (method) ->
		@api = api
		
	setBaseURI: (uri) ->
		@base_uri = uri
		
	setParams: (params={}) ->
		@params = params
			
	payload: ->
		_payload =
			id: @envelope.id
			opts: @envelope.opts
			agent: @envelope.agent
		for key, value of @params
			_payload[key] = value

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
					
			_assembleRPCURL: (method, api, prefix, base_uri) ->
				if typeof api is null and typeof base_uri is null
					throw "RPC Error: must specify either an API or base URI to generate an RPC endpoint."
				else
					if typeof base_uri is null
						base_uri = fatcatmap.rpc.api[api].base_uri

					if typeof prefix isnt null
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
				
				for key, value of config
					if key in request
						request[key] = value
					else if key is 'opts'
						request.setOpts(value)
					else if key is 'agent'
						request.setAgent(value)
						
				return request
				
			fulfillRPCRequest: (config, request, callbacks) ->
				@lastRequest = request
				@history[request.envelope.id] =
					request: request
					config: config
					callbacks: callbacks
					
				if request.action is null
					if request.method is null
						throw "RPC Error: Request must specify at least an action or method."
					if request.base_uri is null
						if request.api is null
							throw "RPC Error: Request must have an API or explicity BASE_URI."
						else
							request.action = @_assembleRPCURL(request.method, request.api, @action_prefix)
					else
						request.action = @_assembleRPCURL(request.method, null, @action_prefix, request.base_uri)
						
				xhr = $.ajax({
				
					url: request.action
					data: JSON.stringify request.params
					async: request.ajax.async
					cache: request.ajax.cache
					global: request.ajax.global
					type: request.ajax.http_method
					crossDomain: request.ajax.crossDomain
					dataType: request.ajax.dataType
					processData: false
					ifModified: request.ajax.ifModified
					contentType: 'application/json'
					
					beforeSend: (xhr, settings) ->
						fatcatmap.rpc.history[request.envelope.id].xhr = xhr;
						return xhr
						
					error: (xhr, status, error) ->
						fatcatmap.rpc.lastFailure = error
						fatcatmap.rpc.history[request.envelope.id].xhr = xhr
						fatcatmap.rpc.history[request.envelope.id].status = status
						fatcatmap.rpc.history[request.envelope.id].failure = error
						callbacks.failure(data)
						
					success: (data, status, xhr) ->
						fatcatmap.rpc.lastResponse = data
						fatcatmap.rpc.history[request.envelope.id].xhr = xhr
						fatcatmap.rpc.history[request.envelope.id].status = status
						fatcatmap.rpc.history[request.envelope.id].response = data
						callbacks.success(data)
						
					complete: (xhr, status) ->
						fatcatmap.rpc.history[request.envelope.id].xhr = xhr
						fatcatmap.rpc.history[request.envelope.id].status = status
						
					statusCode:
						
						404: ->
							alert 'RPC 404: Could not resolve RPC action URI.'
							
						403: ->
							alert 'RPC 403: Not authorized to access the specified endpoint.'
							
						500: ->
							alert 'RPC 500: Woops! Something went wrong. Please try again.'
				
				})
				
				return {id: request.envelope.id, request: request, xhr: xhr}
						

		@adapters =
			
			data: new RPCAdapter('data')
			query: new RPCAdapter('query')
			graph: new RPCAdapter('graph')
			charts: new RPCAdapter('charts')
			session: new RPCAdapter('session')
			frame: new RPCAdapter('frame')
		
		@ext = null