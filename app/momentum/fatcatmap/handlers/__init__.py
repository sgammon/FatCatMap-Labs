# -*- coding: utf-8 -*-
from momentum import MomentumHandler


class WebHandler(MomentumHandler):
		
	''' Abstract parent-class to any handler that responds to a request from a web browser. '''
	
	configPath = 'momentum.fatcatmap'