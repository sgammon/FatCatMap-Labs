{% if script_tag %}
<script type="text/javascript">
{% endif %}

// Initliaze user object
window.fatcatmap.user = {
	
	current_user: "{{ api.users.current_user() }}",
	is_user_admin: "{{ api.users.is_user_admin() }}",
	login_url: "{{ api.users.create_login_url('/') }}",
	logout_url: "{{ api.users.create_logout_url('/') }}"

};
	
// Initialize RPC object
window.fatcatmap.rpc = {
	
	base_rpc_uri: '{{ link('rpc-api', mode='internal') }}',
	api: {
		
		data: {
			base_uri: '{{ link('rpc-api-service', service='data') }}',
			methods: ['get', 'retrieveGraphObject', 'retrieveNative', 'retrieveMedia']
		},
		
		query: {
			base_uri: '{{ link('rpc-api-service', service='query') }}',
			methods: ['search', 'gql']
		},
		
		graph: {
			base_uri: '{{ link('rpc-api-service', service='graph') }}',
			methods: ['construct', 'constructFromNode', 'constructFromObject']
		},
		
		charts: {
			base_uri: '{{ link('rpc-api-service', service='charts') }}',
			methods: ['generate', 'generateFromSeries']
		},
		
		session: {
			base_uri: '{{ link('rpc-api-service', service='session') }}',
			methods: ['init', 'authenticate', 'checkin']
		}
		
	},
	
	lastRequest: null,
	lastFailure: null,
	lastResponse: null,
	action_prefix: null,
	history: {},
	used_ids: [],
		
	generateRPCHint: function (api, method, api_object) {
			
		return function (args, callbacks, async)
		{	
			if (typeof(async) == 'undefined')
			{
				async = false;
			}
			// RPC hint fulfills request by default
			return fatcatmap.rpc.fullfillRPCRequest(api_object,

					// Pass default request to API request factory
					fatcatmap.rpc.adapters.api[api].request(
						
						// Generate default request
						fatcatmap.rpc.createRPCRequest({

							// Request Object
							method: method,
							params: args,
							api: api,
							opts: {},
							async: async
						
						})
					),

					{
						// Callbacks
						success: function (response)
						{
							api_object.adapter.response(response, callbacks);
						},
						failure: function (failure)
						{
							fatcatmap.rpc.adapters.error(failure, callbacks);
						}
					}
			);
		}	
	},
	
	_assembleRPCURL: function (method, api, prefix, base_uri)
	{
		if ((typeof(api) == 'undefined' || api == null) && (typeof(base_uri) == 'undefined' || base_uri == null))
		{
			throw "RPC Error: must specify either an API or base URI to generate an RPC URL.";
		}
		else
		{
			if(typeof(base_uri) == 'undefined' || base_uri == null)  // We have been passed an explicit base_uri...
			{
				base_uri = window.fatcatmap.rpc.api[api].base_uri;
			}

			if(typeof(prefix) != 'undefined' && prefix != null) // We have been passed a prefix...
			{
				return [prefix+base_uri, method].join('.');
			}
			else // No prefix...
			{
				return [base_uri, method].join('.');
			}
		}
	},
	
	provisionRequestID: function ()
	{
		if(this.used_ids.length > 0)
		{
			id = Math.max.apply(this, this.used_ids)+1;
			this.used_ids.push(id);
			return id
		}
		else
		{
			this.used_ids.push(1);
			return 1
		}
	},
	
	createRPCRequest: function _buildFCMRPC(config)
	{
		// Build request object
		request = {

			// Top level request params
			params: {},
			action: null,
			method: null,
			api: null,
			base_uri: null,

			// Envelope for the AJAX call
			envelope: {
				id: this.provisionRequestID(),				
				opts: {},
				agent: {}
			},
			
			// Parameters for the AJAX call
			ajax: {
				async: false,
				cache: true,
				global: true,				
				http_method: 'POST',
				crossDomain: false,
				ifModified: false,
				dataType: 'json'
			},
						
			// Compile into param set for communication with ProtoRPC
			payload: function makePayload()
			{
				_payload = {};
				for (key in request.params)
				{
					_payload[key] = request.params[key];
				}
				_payload.id = request.envelope.id;
				_payload.opts = request.envelope.opts;
				_payload.agent = request.envelope.agent;
				return _payload
			}
		};
		
		// Allow config values to override
		for (key in config)
		{
			if(key in request)
			{
				request[key] = config[key]; // async, api, method, action, params, base_uri
			}
			else if (key == 'opts')
			{
				request.envelope.opts = config.opts;
			}
			else if (key == 'agent')
			{
				request.envelope.agent = config.agent;
			}
		}
		
		return request;
	},
	
	fullfillRPCRequest: function _initiateFCMRPC(config, request, callbacks)
	{

		fatcatmap.rpc.lastRequest = request;
		fatcatmap.rpc.history[request.envelope.id] = {request:request, config: config, callbacks: callbacks};
		
		if (request.action == null)
		{
			if (request.method == null)
			{
				throw "RPC Error: Request must specify a method.";
			}

			if (request.base_uri == null)
			{
				if (request.api == null)
				{
					throw "RPC Error: Request must have an API or explicit BASE_URI.";
				}
				else
				{
					request.action = this._assembleRPCURL(request.method, request.api, this.action_prefix);
				}
			}
			else
			{
				request.action = this._assembleRPCURL(request.method, null, this.action_prefix, request.base_uri);
			}
			
		}
		
		// Make AJAX call to fullfill RPC
		xhr = $.ajax({
			
			url: request.action,
			data: JSON.stringify(request.params),
			async: request.ajax.async,
			cache: request.ajax.cache,
			global: request.ajax.global,
			type: request.ajax.http_method,
			crossDomain: request.ajax.crossDomain,
			dataType: request.ajax.dataType,
			processData: false,
			ifModified: request.ajax.ifModified,
			contentType: 'application/json',
						
			beforeSend: function prepareXHR(xhr, settings)
			{
				fatcatmap.rpc.history[request.envelope.id].xhr = xhr;
				return xhr				
			},
			
			error: function xhrError(xhr, status, error)
			{
				fatcatmap.rpc.lastFailure = data;
				fatcatmap.rpc.history[request.envelope.id].xhr = xhr;
				fatcatmap.rpc.history[request.envelope.id].status = status;
				fatcatmap.rpc.history[request.envelope.id].failure = error;
				callbacks.failure(data);
			},
			
			success: function xhrSuccess(data, status, xhr)
			{
				fatcatmap.rpc.lastResponse = data;
				fatcatmap.rpc.history[request.envelope.id].xhr = xhr;				
				fatcatmap.rpc.history[request.envelope.id].status = status;
				fatcatmap.rpc.history[request.envelope.id].response = data;
				callbacks.success(data);
			},
			
			complete: function finishXHR(xhr, status)
			{
				fatcatmap.rpc.history[request.envelope.id].xhr = xhr;
				fatcatmap.rpc.history[request.envelope.id].status = status;
			},			
			
			statusCode: {

				404: function () {
					alert('RPC 404: Could not resolve RPC action URI.');
				},
				
				403: function () {
					alert('RPC 403: You are not authorized to access the data for this page.');
				},
				
				500: function () {
					alert('RPC 500: Woops! Something went wrong inside the server. Please try again.');
				}
				
			}
			
		});
		
		return {id: request.envelope.id, request: request, xhr: xhr};
	},
	
};

// Initialize Sys Object
_PLATFORM_VERSION = "{{ sys.version }}";

{% if sys.dev %}
// Drop in server environment (DEV ONLY)
fatcatmap.dev.environment = {
	{% for key, value in sys.environ.items() %}
	{{ key }}: "{{ value }}",
	{% endfor %}
};
{% endif %}

{% if script_tag %}
</script>
{% endif %}