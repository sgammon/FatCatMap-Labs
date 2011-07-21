# -*- coding: utf-8 -*-
import os
import config
import hashlib
import logging
import simplejson

# ProtoRPC Imports
from protorpc import remote

# Tipfy Imports
from tipfy import RequestHandler, Response
from tipfyext.jinja2 import Jinja2Mixin

from tipfy.i18n import I18nMiddleware
from tipfy.sessions import SessionMiddleware

# App Engine Imports
from google.appengine.api import oauth
from google.appengine.api import users
from google.appengine.api import backends
from google.appengine.api import namespace_manager

# Handler Mixins
from momentum.fatcatmap.core.api.output.assets import AssetsMixin
from momentum.fatcatmap.core.api.output.live import LiveServicesMixin
from momentum.fatcatmap.core.api.output.sessions import SessionsMixin


class MomentumHandler(RequestHandler, Jinja2Mixin, AssetsMixin, LiveServicesMixin, SessionsMixin):

	''' Top-level parent class for request handlers based in Tipfy. '''
	
	configPath = None
	config = config.config
	minify = False
	response = Response
	
	middleware = [SessionMiddleware(), I18nMiddleware()]
	
	baseHeaders = {
		
		'X-Platform': 'Providence/Clarity-Embedded', # Indicate the platform that is serving this request
		'X-Powered-By': 'Google App Engine/1.5.1', # Indicate the SDK version
		'X-UA-Compatible': 'IE=edge,chrome=1' # Enable compatibility with Chrome Frame, and force IE to render with the latest engine

	}		
	
	
	def render(self, path, context={}, elements={}, content_type='text/html', headers={}, **kwargs):

		''' Return a response containing a rendered Jinja template. Create a session if one doesn't exist. '''
	
		self.context['user'] = users.get_current_user()
		self.context['session'] = self.getFatCatMapSession()		
		
		
		response_headers = {}
		for key, value in self.baseHeaders.items():
			response_headers[key] = value
		if len(headers) > 0:
			for key, value in headers.items():
				response_headers[key] = value
		
		# Consider kwargs
		if len(kwargs) > 0:
			for k, v in kwargs.items():
				self.context[k] = v
		
		params = self._bindTemplateFunctions(self.context, self._outputConfig())
		
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
				
		## Bind elements
		for element, config in elements.items():
			self.context['page']['elements'][element] = config
		
		return self.response(response=minify(self.render_template(path, **self.context)), content_type=content_type, headers=[(key, value) for key, value in response_headers.items()])
				

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
		params['page']['elements'] = {
			'errorNotice': False,
			'infoNotice': False,
			'generalNotice': False,
			'successNotice': False
		}
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
		
		# Bind Live Services (channel functions)
		params['live'] = {
			
			'get_lib': self.getChannelLib,
			'get_channel': self.getLiveChannel
			
		}
		
		return params
		

	def _outputConfig(self):
		return config.config.get(self.configPath+'.output')