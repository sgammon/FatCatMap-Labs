{% if script_tag %}
<script type="text/javascript">
{% endif %}

window.fatcatmap.rpc.api.factory('data', '/_api/rpc/data', ['get', 'retrieveGraphObject', 'retrieveNative', 'retriveAsset'])
window.fatcatmap.rpc.api.factory('query', '/_api/rpc/query', ['search','gql','autocomplete'])
window.fatcatmap.rpc.api.factory('graph', '/_api/rpc/graph', ['construct', 'constructFromNode', 'constructFromObject'])
window.fatcatmap.rpc.api.factory('charts', '/_api/rpc/charts', ['generate', 'generateFromSeries'])
window.fatcatmap.rpc.api.factory('session', '/_api/rpc/session', ['init', 'authenticate', 'checkin'])

// Initliaze user object
window.fatcatmap.user.setUserInfo({
	
	{% if api.users.current_user() != none %}
		current_user: "{{ api.users.current_user() }}",
		is_user_admin: "{{ api.users.is_user_admin() }}",
	{% else %}
		current_user: null,
		is_user_admin: false,
	{% endif %}
	login_url: "{{ api.users.create_login_url('/') }}",
	logout_url: "{{ api.users.create_logout_url('/') }}"

});

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