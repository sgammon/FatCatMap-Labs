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
	
	history: [],
	lastRequest: null,
	lastFailure: null,
	lastResponse: null,
	
	generateRPCHint: function (api, method, api_object) {
			
		return function (args, callbacks, async)
		{	
			if (typeof(async) == 'undefined')
			{
				async = false;
			}
			return fatcatmap.rpc.makeRPCRequest(api_object, {

						// Request Object
						method: method,
						params: args,
						opts: {},
						async: async
						
					},

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
	
	
	makeRPCRequest: function _generateFCMRPC(config, request, callbacks)
	{
		request.params['opts'] = request.opts;
		fatcatmap.rpc.lastRequest = request;
		$.FatCatMapRPC.setup({endPoint: config.base_uri+'.'+request.method});
		$.FatCatMapRPC.request(request.method, request.async, request.params,{

				success: function internalRPCSuccessCallback(response)
				{
					fatcatmap.rpc.lastResponse = response;
					fatcatmap.rpc.history.push({request: request, response: response});
					callbacks.success(response);
				},
				
				error: function internalRPCFailureCallback(response)
				{
					fatcatmap.rpc.lastFailure = response;
					fatcatmap.rpc.history.push({request: request, failure: response});
					callbacks.failure(response);
				}

		});
		
	},
	
};

// Initialize Sys Object
_PLATFORM_VERSION = "{{ sys.version }}";

{% if sys.dev %}
// Initialize Dev Object
fatcatmap.dev = {
	environment: {
		{% for key, value in sys.environ.items() %}
		{{ key }}: "{{ value }}",
		{% endfor %}
	}
};
{% endif %}

{% if script_tag %}
</script>
{% endif %}