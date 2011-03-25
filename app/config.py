# -*- coding: utf-8 -*-
""" Tipfy configuration. """
config = {}
config['tipfy'] = {

	'apps_installed':[
		'momentum.fatcatmap'
	],

}
config['tipfy.sessions'] = {
	'secret_key':'ASKLdjOF)H#*@G@)*GCJDBUVF(!&Gouhf981g27gd2G@H)'
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
