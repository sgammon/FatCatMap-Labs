# -*- coding: utf-8 -*-
"""URL definitions."""
from tipfy import Rule
from tipfy import HandlerPrefix

rules = [

	HandlerPrefix('momentum.fatcatmap.handlers.', [
	
		## === Main URLs === ##
		Rule('/', name='landing', handler='main.Landing'),
		Rule('/offline', name='offline', handler='main.Offline'),

		## === Content Sections == ##
		Rule('/map', name='map:landing', handler='content.map.MapLanding'),
		Rule('/browse', name='browse:landing', handler='content.browse.BrowseLanding'),
		Rule('/search', name='search:landing', handler='content.search.SearchLanding'),
		Rule('/interact', name='interact:landing', handler='content.interact.InteractLanding'),
		Rule('/visualize', name='visualize:landing', handler='content.visualize.VisualizeLanding'),
		
		## === Site: About FCM === ##
		Rule('/about', name='about:landing', handler='site.about.Landing'),
		Rule('/about/bias', name='about:bias', handler='site.about.Bias'),
		Rule('/about/mission', name='about:mission', handler='site.about.Mission'),
		Rule('/about/technology', name='about:poweredby', handler='site.about.PoweredBy'),

		## === Site: Help (bug reporter, help topics, 'ask a question') === ##
		Rule('/help', name='help:landing', handler='site.help.Landing'),
		Rule('/help/ask', name='help:ask', handler='site.help.AskQuestion'),
		Rule('/help/faq', name='help:faq', handler='site.help.FAQ'),
		Rule('/help/topics', name='help:topics:list', handler='site.help.ListTopics'),		
		Rule('/help/topic/<string:key>', name='help:topic', handler='site.help.ViewTopic'),		
		Rule('/help/terminology', name='help:terminology', handler='site.help.Terminology'),
		Rule('/help/something-broke', name='help:bugreporter', handler='site.help.ReportBug'),
		
		## === Site: Legal (privacy policy, source data, terms of service) === ##
		Rule('/legal', name='legal:landing', handler='site.legal.Landing'),
		Rule('/legal/data', name='legal:sourcedata', handler='site.legal.Data'),
		Rule('/legal/terms', name='legal:terms', handler='site.legal.Terms'),
		Rule('/legal/privacy', name='legal:privacy', handler='site.legal.Privacy'),
		
		## === User URLs === ##
		Rule('/me', name='user:landing', handler='user.Landing'),
		Rule('/me/inbox', name='user:inbox', handler='user.Inbox'),
		Rule('/me/stats', name='user:stats', handler='user.Stats'),
		Rule('/me/profile', name='user:profile', handler='user.Profile'),
		Rule('/me/history', name='user:history', handler='user.History'),
		Rule('/me/account', name='user:account', handler='user.Account'),
		Rule('/me/settings', name='settings:landing', handler='user.Settings'),
		
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
