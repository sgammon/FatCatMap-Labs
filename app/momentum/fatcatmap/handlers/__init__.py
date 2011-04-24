# -*- coding: utf-8 -*-
import os
import config

# Tipfy Imports
from tipfy import RequestHandler, Response
from tipfyext.jinja2 import Jinja2Mixin

# App Engine Imports
from google.appengine.api import users

# Output Mixin Imports
from momentum.fatcatmap.core.api.output.assets import AssetsMixin


class WebHandler(RequestHandler, AssetsMixin, Jinja2Mixin):
		
	response = Response


	def render(self, path, **kwargs):
	
		''' Return a response containing a rendered Jinja template. '''
	
		template_context = {
			## Create empty template context...
			'user': users.get_current_user()
		}
		
		# Consider kwargs
		if len(kwargs) > 0:
			for k, v in kwargs.items():
				template_context[k] = v
		
		params = self._bindTemplateFunctions(template_context)
		return self.render_response(path, **template_context)
				

	def _bindTemplateFunctions(self, params):

		''' Bind utility functions to the template variable space. '''

		# Bind Tipfy & util functions
		params['link'] = self.url_for
		params['config'] = config.config.get
		params['environ'] = os.environ.get

		# Bind AssetMixin functions
		params['script_url'] = self.script_url
		params['style_url'] = self.style_url
		params['asset_url'] = self.style_url
		
		# Bind App Engine functions
		params['current_user'] = users.get_current_user
		params['is_user_admin'] = users.is_current_user_admin
		params['create_login_url'] = users.create_login_url
		params['create_logout_url'] = users.create_logout_url
		
		return params