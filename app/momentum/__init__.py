# -*- coding: utf-8 -*-
import os
import config
import slimmer
from slimmer.js_function_slimmer import slim as slimjs

# Tipfy Imports
from tipfy import RequestHandler, Response
from tipfyext.jinja2 import Jinja2Mixin

# ProtoRPC Imports
from protorpc import remote

# App Engine Imports
from google.appengine.api import users

# Output Mixin Imports
from momentum.fatcatmap.core.api.output.assets import AssetsMixin


class MomentumHandler(RequestHandler, AssetsMixin, Jinja2Mixin):
	
	configPath = None
	minify = False
	response = Response
	
	def render(self, path, content_type='text/html', headers={}, **kwargs):

		''' Return a response containing a rendered Jinja template. '''
	
		template_context = {
			## Create empty template context...
			'user': users.get_current_user()
		}
		
		# Consider kwargs
		if len(kwargs) > 0:
			for k, v in kwargs.items():
				template_context[k] = v
		
		params = self._bindTemplateFunctions(template_context, self._outputConfig())
		
		minify = unicode
		minify = unicode

		if self._outputConfig()['minify'] is True:
			if content_type == 'text/html':
				minify = slimmer.html_slimmer
			elif content_type == 'text/javascript':
				minify = slimjs
			elif content_type == 'text/css':
				minify = slimmer.css_slimmer
		
		return self.response(response=minify(self.render_template(path, **template_context)), content_type=content_type, headers=headers)
				

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
		
		# Bind App Engine functions
		params['api'] = {'users':{}}
		params['api']['users']['current_user'] = users.get_current_user
		params['api']['users']['is_user_admin'] = users.is_current_user_admin
		params['api']['users']['create_login_url'] = users.create_login_url
		params['api']['users']['create_logout_url'] = users.create_logout_url
		
		return params
		

	def _outputConfig(self):
		return config.config.get(self.configPath+'.output')
		
		
class MomentumService(remote.Service):
	
	state = {}
	config = {}

	def __init__(self):
		self.config = config.config.get('momentum.services')

	def initialize_request_state(self, state):
		self.state = state