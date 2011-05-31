# -*- coding: utf-8 -*-
"""URL definitions."""
from tipfy import Rule
from tipfy import HandlerPrefix

rules = [

	HandlerPrefix('momentum.fatcatmap.handlers.', [
	
		## === Main URLs === ##
		Rule('/', name='landing', handler='main.Landing'),
		Rule('/map', name='map', handler='main.Map'),
		
		## === Security URLs === ##
		Rule('/login', name='auth/login', handler='security.Login'),
		Rule('/logout', name='auth/logout', handler='security.Logout'),
		Rule('/register', name='auth/register', handler='security.Register'),
		
		## === Dev URLs === ##
		Rule('/_fcm/dev', name='dev-index', handler='dev.Index'),
		Rule('/_fcm/dev/cache', name='dev-cache', handler='dev.CacheManagement'),
		Rule('/_fcm/dev/add-data', name='dev-add-data', handler='dev.AddData'),
		Rule('/_fcm/dev/default-data', name='dev-default-data', handler='dev.DefaultData'),
		Rule('/_fcm/dev/rpc-console', name='dev-rpc-console', handler='dev.RPCConsole'),
		Rule('/_fcm/dev/shell', name='dev-shell', handler='dev.WebShell'),
		
		## === Management URLs === ##
		Rule('/_fcm/manage', name='admin-index', handler='admin.Index'),
		
		## === API Services === ##
		Rule('/_api/js', endpoint='js-api', handler='api.JavascriptAPIDispatcher'),
		Rule('/_api/rpc', endpoint='rpc-api', handler='api.FatcatmapAPIDispatcher'),
		Rule('/_api/rpc/<string:service>', endpoint='rpc-api-service', handler='api.FatcatmapAPIDispatcher'),
		Rule('/_api/<string:module>', endpoint='api', handler='api.FatcatmapAPIDispatcher'),
		Rule('/_api/<string:module>/<string:service>', endpoint='api-call', handler='api.FatcatmapAPIDispatcher'),
		Rule('/_api/<string:module>/<string:service>/<string:method>', endpoint='api-call-rest', handler='api.FatcatmapAPIDispatcher'),			
		Rule('/_api/<string:module>/<string:service>/<string:method>.<string:format>', endpoint='api-request-rest-format', handler='api.FatcatmapAPIDispatcher'),

	
	])
]
