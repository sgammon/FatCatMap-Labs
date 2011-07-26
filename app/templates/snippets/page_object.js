{% if script_tag %}
<script type="text/javascript">
{% endif %}

fatcatmap = window.fatcatmap;

{% if services %}
	{% for service, action, config, opts in services %}	
		fatcatmap.rpc.api.factory('{{ service }}', '{{ action }}', [{% for method in config.methods %}'{{ method }}',{% endfor %}], {% autoescape false %}{{ util.converters.json.dumps(opts) }}{% endautoescape %});
	{% endfor %}
	
		fatcatmap.state.events.triggerEvent('API_READY');
{% endif %}

// Initliaze user object
fatcatmap.user.setUserInfo({
	
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

fatcatmap.dev.setDebug({logging: true, eventlog: true, verbose: true});
{% endif %}

{% if script_tag %}
</script>
{% endif %}