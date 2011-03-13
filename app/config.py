# -*- coding: utf-8 -*-
""" Tipfy configuration. """
config = {}
config['tipfy'] = {

	'apps_installed':[
		'momentum.fatcatmap'
	],

}

""" FatCatMap Configuration """
config['momentum.fatcatmap'] = {

	'enable_hooks':{
		'appstats':False
	}

}

# Pipelines Configuration
config['momentum.fatcatmap.pipelines'] = {

    'debug': True

}
