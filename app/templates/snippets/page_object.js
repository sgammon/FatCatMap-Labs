{% if script_tag %}
<script type="text/javascript">
{% endif %}

	// Initialize FCM object
	var fatcatmap = {page:{}, sys:{}, dev:{}, user:{}, rpc:{}};

	// Initialize Page object
	fatcatmap.page = {};
		
	// Initialize RPC object
	fatcatmap.rpc = {
		
		base_rpc_uri: '{{ link('rpc-api', mode='internal') }}',
		api: {
			
			data: {
				base_uri: '{{ link('rpc-api-service', service='data') }}',
				adapter: apiAdapters.api.data,
				methods: ['get', 'retrieveGraphObject', 'retrieveNative', 'retrieveMedia']
			},
			
			query: {
				base_uri: '{{ link('rpc-api-service', service='query') }}',
				adapter: apiAdapters.api.query,
				methods: ['search', 'gql']
			},
			
			graph: {
				base_uri: '{{ link('rpc-api-service', service='graph') }}',
				adapter: apiAdapters.api.graph,
				methods: ['construct', 'constructFromNode', 'constructFromObject']
			},
			
			charts: {
				base_uri: '{{ link('rpc-api-service', service='charts') }}',
				adapter: apiAdapters.api.charts,
				methods: ['generate', 'generateFromSeries']
			},
			
			session: {
				base_uri: '{{ link('rpc-api-service', service='session') }}',
				adapter: apiAdapters.api.session,
				methods: ['init', 'authenticate', 'checkin']
			}
			
		},
		
		makeRPCRequest: function _generateFCMRPC(base_uri, method, params, opts, success, failure)
		{
			
		},
		
	};

	{% if dev %}
	// Initialize Sys Object
	fatcatmap.sys = {};

	// Initialize Dev Object
	fatcatmap.dev = {};
	{% endif %}

{% if script_tag %}
</script>
{% endif %}