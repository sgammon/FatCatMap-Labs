# -*- coding: utf-8 -*-
"""URL definitions."""
from tipfy import Rule
from tipfy import HandlerPrefix

rules = [

	HandlerPrefix('momentum.fatcatmap.handlers.', [
	
		Rule('/', name='hello-world', handler='main.Landing')
	
	])
]
