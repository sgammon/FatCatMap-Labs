# -*- coding: utf-8 -*-
"""URL definitions."""
from webapp2 import Route
from webapp2_extras.routes import HandlerPrefixRoute

rules = [

	HandlerPrefixRoute('momentum.fatcatmap.handlers.', [
	
		## === Main URLs === ##
		Route('/', name='landing', handler='content.map.MapLanding'),
		Route('/offline', name='offline', handler='main.Offline'),

		## === Content Sections == ##
		Route('/map', name='map:landing', handler='content.map.MapLanding'),
		Route('/browse', name='browse:landing', handler='content.browse.BrowseLanding'),
		Route('/search', name='search:landing', handler='content.search.SearchLanding'),
		Route('/interact', name='interact:landing', handler='content.interact.InteractLanding'),
		Route('/visualize', name='visualize:landing', handler='content.visualize.VisualizeLanding'),
		
		## === Site: About FCM === ##
		Route('/about', name='about:landing', handler='site.about.Landing'),
		Route('/about/bias', name='about:bias', handler='site.about.Bias'),
		Route('/about/mission', name='about:mission', handler='site.about.Mission'),
		Route('/about/technology', name='about:poweredby', handler='site.about.PoweredBy'),

		## === Site: Help (bug reporter, help topics, 'ask a question') === ##
		Route('/help', name='help:landing', handler='site.help.Landing'),
		Route('/help/ask', name='help:ask', handler='site.help.AskQuestion'),
		Route('/help/faq', name='help:faq', handler='site.help.FAQ'),
		Route('/help/topics', name='help:topics:list', handler='site.help.ListTopics'),		
		Route('/help/topic/<string:key>', name='help:topic', handler='site.help.ViewTopic'),		
		Route('/help/terminology', name='help:terminology', handler='site.help.Terminology'),
		Route('/help/something-broke', name='help:bugreporter', handler='site.help.ReportBug'),
		
		## === Site: Legal (privacy policy, source data, terms of service) === ##
		Route('/legal', name='legal:landing', handler='site.legal.Landing'),
		Route('/legal/data', name='legal:sourcedata', handler='site.legal.Data'),
		Route('/legal/terms', name='legal:terms', handler='site.legal.Terms'),
		Route('/legal/privacy', name='legal:privacy', handler='site.legal.Privacy'),
		
		## === User URLs === ##
		Route('/me', name='user:landing', handler='user.Landing'),
		Route('/me/inbox', name='user:inbox', handler='user.Inbox'),
		Route('/me/stats', name='user:stats', handler='user.Stats'),
		Route('/me/profile', name='user:profile', handler='user.Profile'),
		Route('/me/history', name='user:history', handler='user.History'),
		Route('/me/account', name='user:account', handler='user.Account'),
		Route('/me/settings', name='settings:landing', handler='user.Settings'),
		
		## === Security URLs === ##
		Route('/login', name='auth/login', handler='security.Login'),
		Route('/logout', name='auth/logout', handler='security.Logout'),
		Route('/register', name='auth/register', handler='security.Register'),
		
		## === Dev URLs === ##
		Route('/_fcm/dev', name='dev-index', handler='dev.Index'),
		Route('/_fcm/dev/cache', name='dev-cache', handler='dev.CacheManagement'),
		Route('/_fcm/dev/add-data', name='dev-add-data', handler='dev.AddData'),
		Route('/_fcm/dev/default-data', name='dev-default-data', handler='dev.DefaultData'),
		Route('/_fcm/dev/rpc-console', name='dev-rpc-console', handler='dev.RPCConsole'),
		Route('/_fcm/dev/shell', name='dev-shell', handler='dev.WebShell'),
		
		## === Management URLs === ##
		Route('/_fcm/manage', name='admin-index', handler='admin.Index'),
		
		## === API Services === ##
		Route('/_api/js', name='js-api', handler='api.JavascriptAPIDispatcher'),
		Route('/_api/rpc', name='rpc-api', handler='api.FatcatmapAPIDispatcher'),
		Route('/_api/rpc/<string:service>', name='rpc-api-service', handler='api.FatcatmapAPIDispatcher'),

		Route('/_api/<string:module>', name='api', handler='api.FatcatmapAPIDispatcher'),
		Route('/_api/<string:module>/<string:service>', name='api-call', handler='api.FatcatmapAPIDispatcher'),
		Route('/_api/<string:module>/<string:service>/<string:method>', name='api-call-rest', handler='api.FatcatmapAPIDispatcher'),			
		Route('/_api/<string:module>/<string:service>/<string:method>.<string:format>', name='api-request-rest-format', handler='api.FatcatmapAPIDispatcher'),

	
	])
]
