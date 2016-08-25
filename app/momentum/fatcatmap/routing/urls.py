# -*- coding: utf-8 -*-
"""URL definitions."""
from webapp2 import Route
from webapp2_extras.routes import HandlerPrefixRoute

rules = [

	HandlerPrefixRoute('momentum.fatcatmap.handlers.', [
	
		## === Main URLs === ##
		Route('/', name='landing', handler='content.map.MapLanding'),
		Route('/offline', name='offline', handler='main.Offline'),

		## === Security URLs === ##
		HandlerPrefixRoute('security.', [

			Route('/login', name='auth/login', handler='Login'),
			Route('/logout', name='auth/logout', handler='Logout'),
			Route('/register', name='auth/register', handler='Register'),		
		
		]),

		## === Content Sections == ##
		HandlerPrefixRoute('content.', [

			Route('/map', name='map:landing', handler='map.MapLanding'),
			Route('/browse', name='browse:landing', handler='browse.BrowseLanding'),
			Route('/search', name='search:landing', handler='search.SearchLanding'),
			Route('/interact', name='interact:landing', handler='interact.InteractLanding'),
			Route('/visualize', name='visualize:landing', handler='visualize.VisualizeLanding')
		
		]),
		
		## === Site: About FCM === ##
		HandlerPrefixRoute('site.about.', [

			Route('/about', name='about:landing', handler='Landing'),
			Route('/about/bias', name='about:bias', handler='Bias'),
			Route('/about/mission', name='about:mission', handler='Mission'),
			Route('/about/technology', name='about:poweredby', handler='PoweredBy')
		
		]),

		## === Site: Help (bug reporter, help topics, 'ask a question') === ##
		HandlerPrefixRoute('site.help.', [

			Route('/help', name='help:landing', handler='Landing'),
			Route('/help/ask', name='help:ask', handler='AskQuestion'),
			Route('/help/faq', name='help:faq', handler='FAQ'),
			Route('/help/topics', name='help:topics:list', handler='ListTopics'),		
			Route('/help/topic/<string:key>', name='help:topic', handler='ViewTopic'),		
			Route('/help/terminology', name='help:terminology', handler='Terminology'),
			Route('/help/something-broke', name='help:bugreporter', handler='ReportBug')
		
		]),
		
		## === Site: Legal (privacy policy, source data, terms of service) === ##
		HandlerPrefixRoute('site.legal.', [		

			Route('/legal', name='legal:landing', handler='Landing'),
			Route('/legal/data', name='legal:sourcedata', handler='Data'),
			Route('/legal/terms', name='legal:terms', handler='Terms'),
			Route('/legal/privacy', name='legal:privacy', handler='Privacy')
			
		]),
		
		## === User URLs === ##
		HandlerPrefixRoute('user.', [

			Route('/me', name='user:landing', handler='Landing'),
			Route('/me/inbox', name='user:inbox', handler='Inbox'),
			Route('/me/stats', name='user:stats', handler='Stats'),
			Route('/me/profile', name='user:profile', handler='Profile'),
			Route('/me/history', name='user:history', handler='History'),
			Route('/me/account', name='user:account', handler='Account'),
			Route('/me/settings', name='settings:landing', handler='Settings')

		]),
		
		## === Dev URLs === ##
		HandlerPrefixRoute('dev.', [

			Route('/_fcm/dev', name='dev-index', handler='Index'),
			Route('/_fcm/dev/cache', name='dev-cache', handler='CacheManagement'),
			Route('/_fcm/dev/add-data', name='dev-add-data', handler='AddData'),
			Route('/_fcm/dev/default-data', name='dev-default-data', handler='DefaultData'),
			Route('/_fcm/dev/rpc-console', name='dev-rpc-console', handler='RPCConsole'),
			Route('/_fcm/dev/shell', name='dev-shell', handler='WebShell')

		]),
		
		## === Management URLs === ##
		Route('/_fcm/manage', name='admin-index', handler='admin.Index'),
		
		## === Worker URLs === ##
		HandlerPrefixRoute('workers.', [
				
			Route('/_fcm/workers', name='workers', handler='Main'),
			Route('/_fcm/workers/warmup/<routine>', name='warmup-worker', handler='cache.Warmup'),
			Route('/_fcm/workers/fetch/ext/<routine>', name='fetch-worker', handler='fetch.FetchExternal'),

			# Scheduler Workers
			HandlerPrefixRoute('scheduler.', [

				Route('/_fcm/workers/scheduler', name='scheduler-worker', handler='Main'),
				Route('/_fcm/workers/scheduler/tick', name='scheduler-tick', handler='Tick'),
				Route('/_fcm/workers/scheduler/callback', name='scheduler-callback', handler='Callback'),
				Route('/_fcm/workers/scheduler/next', name='scheduler-next', handler='Next'),
				Route('/_fcm/workers/scheduler/status', name='scheduler-status', handler='Status')
				
			]),
			
			# Crawler Workers
			HandlerPrefixRoute('crawler.', [
			
				Route('/_fcm/workers/crawler', name='crawler-worker', handler='Main'),
			
			]),
			
			# Analyzer Workers
			HandlerPrefixRoute('analyzer.', [
			
				Route('/_fcm/workers/analyzer', name='analyzer-worker', handler='Main'),
			
			])
			
		]),
		
		## === API Services === ##
		HandlerPrefixRoute('api.', [		

			Route('/_api/js', name='js-api', handler='JavascriptAPIDispatcher'),
			Route('/_api/rpc', name='rpc-api', handler='FatcatmapAPIDispatcher'),
			Route('/_api/rpc/<service>', name='rpc-api-service', handler='FatcatmapAPIDispatcher'),

			Route('/_api/<module>', name='api', handler='FatcatmapAPIDispatcher'),
			Route('/_api/<module>/<service>', name='api-call', handler='FatcatmapAPIDispatcher'),
			Route('/_api/<module>/<service>/<method>', name='api-call-rest', handler='FatcatmapAPIDispatcher'),			
			Route('/_api/<module>/<service>/<method>.<format>', name='api-request-rest-format', handler='FatcatmapAPIDispatcher')
			
		])

	
	])
]
