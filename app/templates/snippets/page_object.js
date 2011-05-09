{% if script_tag %}
<script type="text/javascript">
{% endif %}

	// Initialize FCM object
var fatcatmap = {page:{}, sys:{}, dev:{}, user:{}, rpc:{}};

// Initialize Page object
fatcatmap.page = {};

// Initliaze user object
fatcatmap.user = {
	
	current_user: "{{ api.users.current_user() }}",
	is_user_admin: "{{ api.users.is_user_admin() }}",
	login_url: "{{ api.users.create_login_url('/') }}",
	logout_url: "{{ api.users.create_logout_url('/') }}"

};
	
// Initialize RPC object
fatcatmap.rpc = {
	
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
	
	history: [],
	lastRequest: null,
	lastFailure: null,
	lastResponse: null,
	
	makeRPCRequest: function _generateFCMRPC(request, callbacks)
	{
		alert(request.base_uri);
		alert(request.method);
		alert(request.params);
		alert(request.opts);
		alert(request.success);
		alert(request.failure);
		
		request.params['opts'] = request.opts;
		fatcatmap.rpc.lastRequest = request;
		$.jsonRPC.setup({endPoint: request.base_uri+'.'+request.method});
		$.jsonRPC.request('drawFromNode', request.async, request.params,{

				success: function(response)
				{
					fatcatmap.rpc.lastResponse(response);
					fatcatmap.rpc.history.push({request: request, response: response});
					callbacks.success(response);
				},
				
				error: function(response)
				{
					fatcatmap.rpc.lastFailure(failure);
					fatcatmap.rpc.history.push({request: request, failure: response});
					callbacks.failure(response);
				}

		});
		
	},
	
};

// Initialize Sys Object
fatcatmap.sys = {
	version: "{{ sys.version }}",
	drivers: {			
		registry: {},
		register: function _registerSystemDriver(module, name, initialized, callback)
		{
			if(typeof(fatcatmap.sys.drivers.registry[module]) == 'undefined')
			{
				fatcatmap.sys.drivers.registry[module] = {};
			}
			fatcatmap.sys.drivers.registry[module][name] = {
				initialized: initialized,
				registered: true,
				init_callback: callback
			};
			callback();
		}
	}
};

{% if sys.dev %}
// Initialize Dev Object
fatcatmap.dev = {
	environ: {
		{% for key, value in sys.environ.items() %}
		{{ key }}: "{{ value }}",
		{% endfor %}
	}
};
{% endif %}

{% if script_tag %}
</script>
{% endif %}