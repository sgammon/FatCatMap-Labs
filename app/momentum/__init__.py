# -*- coding: utf-8 -*-
import os
import config
import simplejson

# Tipfy Imports
from tipfy import RequestHandler, Response
from tipfyext.jinja2 import Jinja2Mixin

# ProtoRPC Imports
from protorpc import remote

# App Engine Imports
from google.appengine.api import oauth
from google.appengine.api import users
from google.appengine.api import backends
from google.appengine.api import namespace_manager

# Output Mixin Imports
from momentum.fatcatmap.core.api.output.assets import AssetsMixin


class MomentumHandler(RequestHandler, AssetsMixin, Jinja2Mixin):

	''' Top-level parent class for request handlers based in Tipfy. '''
	
	configPath = None
	minify = False
	response = Response
	
	baseHeaders = {
		
		'X-Platform': 'Providence/Clarity-Embedded', # Indicate the platform that is serving this request
		'X-Powered-By': 'Google App Engine/1.5.0', # Indicate the SDK version
		'X-UA-Compatible': 'IE=edge,chrome=1' # Enable compatibility with Chrome Frame, and force IE to render with the latest engine

	}
	
	def render(self, path, content_type='text/html', headers={}, **kwargs):

		''' Return a response containing a rendered Jinja template. '''
	
		template_context = {
			## Create empty template context...
			'user': users.get_current_user()
		}
		
		response_headers = {}
		for key, value in self.baseHeaders.items():
			response_headers[key] = value
		if len(headers) > 0:
			for key, value in headers.items():
				response_headers[key] = value
		
		# Consider kwargs
		if len(kwargs) > 0:
			for k, v in kwargs.items():
				template_context[k] = v
		
		params = self._bindTemplateFunctions(template_context, self._outputConfig())
		
		minify = unicode

		if self._outputConfig()['minify'] is True:
			import slimmer
			if content_type == 'text/html':
				minify = slimmer.html_slimmer
			elif content_type == 'text/javascript':
				from slimmer.js_function_slimmer import slim as slimjs
				minify = slimjs
			elif content_type == 'text/css':
				minify = slimmer.css_slimmer
		
		return self.response(response=minify(self.render_template(path, **template_context)), content_type=content_type, headers=[(key, value) for key, value in response_headers.items()])
				

	def _bindTemplateFunctions(self, params, output_cfg):

		''' Bind utility functions to the template variable space. '''

		# Bind Tipfy & util functions
		params['link'] = self.url_for
		params['config'] = config.config.get
		params['environ'] = os.environ.get
		
		# System Config
		sys_config = config.config.get(self.configPath)
		params['sys'] = {}
		params['sys']['dev'] = config.debug
		params['sys']['output'] = output_cfg		
		params['sys']['environ'] = os.environ
		params['sys']['version'] = str(sys_config['version']['major'])+'.'+str(sys_config['version']['minor'])+' '+str(sys_config['version']['release'])

		# Bind AssetMixin functions
		params['script_url'] = self.script_url
		params['style_url'] = self.style_url
		params['asset_url'] = self.style_url
		
		# Page Parameters
		params['page'] = {}
		params['page']['manifest'] = False
		params['page']['watermark'] = self._outputConfig()['watermark']
		params['page']['standalone'] = self._outputConfig()['standalone']
			
		# Appcaching
		if self._outputConfig()['appcache']['enable'] == True:
			params['page']['manifest'] = self._outputConfig()['appcache']['manifest']
		
		# Bind App Engine functions
		params['api'] = {
			'oauth': oauth,
			'users': {
				'is_user_admin': users.is_current_user_admin,
				'current_user': users.get_current_user,
				'create_login_url': users.create_login_url,				
				'create_logout_url': users.create_logout_url,
			},
			'backends': backends,
			'multitenancy': namespace_manager
		}
		
		return params
		

	def _outputConfig(self):
		return config.config.get(self.configPath+'.output')
		
		
class MomentumService(remote.Service):
	
	''' Top-level parent class for ProtoRPC-based API services. '''
	
	state = {}
	config = {}

	def __init__(self):
		self.config = config.config.get('momentum.services')

	def initialize_request_state(self, state):
		self.state = state