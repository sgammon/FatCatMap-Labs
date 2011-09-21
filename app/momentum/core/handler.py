# -*- coding: utf-8 -*-
import os
import ndb
import config
import hashlib
import logging
import pipeline
import werkzeug

try:
	import json
except ImportError:
	try:
		import simplejson as json
	except ImportError:
		logging.critical('No compatible JSON adapter found.')

import httpagentparser

# Tipfy Imports
from tipfy import Request
from tipfy import Response
from tipfy import RequestHandler
from tipfyext.jinja2 import Jinja2Mixin
from tipfy.sessions import SessionMiddleware

# Providence/Clarity Imports
from ProvidenceClarity.struct.util import DictProxy
from ProvidenceClarity.struct.util import ObjectProxy
from ProvidenceClarity.struct.util import CallbackProxy

_api_cache = {}


def _loadAPIModule(entry):
	
	''' Callback to lazy-load an API module in tuple(path, item) format. '''
	
	global _api_cache

	if entry not in _api_cache:
		path, name = entry
		mod = __import__(path, globals(), locals(), [name])
		_api_cache[entry] = getattr(mod, name)
		
	return _api_cache[entry]
	
_apibridge = CallbackProxy(_loadAPIModule, {

	'db': ('google.appengine.ext', 'db'),
	'xmpp': ('google.appengine.api', 'xmpp'),
	'mail': ('google.appengine.api', 'mail'),
	'oauth': ('google.appengine.api', 'oauth'),
	'users': ('google.appengine.api', 'users'),
	'images': ('google.appengine.api', 'images'),
	'channel': ('google.appengine.api', 'channel'),
	'backends': ('google.appengine.api', 'backends'),
	'memcache': ('google.appengine.api', 'memcache'),
	'urlfetch': ('google.appengine.api', 'urlfetch'),
	'blobstore': ('google.appengine.ext', 'blobstore'),
	'taskqueue': ('google.appengine.api', 'taskqueue'),
	'capabilities': ('google.appengine.api', 'capabilities'),
	'identity': ('google.appengine.api', 'app_identity'),
	'multitenancy': ('google.appengine.api', 'namespace_manager'),
	'matcher': ('google.appengine.api', 'prospective_search')

})


class MomentumHandler(RequestHandler, Jinja2Mixin):

	''' Top-level parent class for request handlers based in Tipfy. '''
	
	## 1: Class variables
	configPath = None
	minify = unicode
	response = Response
	uagent = {}
	
	## 2: Sessions, auth, etc middleware
	middleware = [SessionMiddleware()]

	## 3: Shortcuts
	api = _apibridge

	ext = DictProxy({
	
		'ndb': ndb,
		'pipelines': pipeline,
	
	})
		
	## 4: HTTP Headers included in every response
	baseHeaders = {
		
		'X-Platform': 'Providence/Clarity-Embedded', # Indicate the platform that is serving this request
		'X-Powered-By': 'Google App Engine/1.5.1', # Indicate the SDK version
		'X-UA-Compatible': 'IE=edge,chrome=1' # Enable compatibility with Chrome Frame, and force IE to render with the latest engine

	}
	
	## 5: Base template context
	baseContext = {
	
		## Python functions
		'all': all, 'any': any,
		'int': int, 'str': str,
		'len': len, 'map': map,
		'max': max, 'min': min,
		'zip': zip, 'bool': bool,
		'list': list, 'dict': dict,
		'tuple': tuple, 'range': range,
		'round': round, 'slice': slice,
		'xrange': xrange, 'filter': filter,
		'reduce': reduce, 'sorted': sorted,
		'unicode': unicode,	'reversed': reversed,
		'isinstance': isinstance, 'issubclass': issubclass,
	
		## Utility stuff
		'util': {

			'env': os.environ,
			'config': {
				'get': config.config.get,
				'debug': config.debug,
				'hooks': config.config
			},
			'converters': {
				'json': json
			}
		},
		
		## API Shortcuts
		'api': {
		
			'users': {
				'is_current_user_admin': _apibridge.users.is_current_user_admin,
				'current_user': _apibridge.users.get_current_user,
				'create_login_url': _apibridge.users.create_login_url,
				'create_logout_url': _apibridge.users.create_logout_url
			},
			'backends': _apibridge.backends,
			'multitenancy': _apibridge.multitenancy
		
		}
			
	}
	

	## 4: Internal methods
	@werkzeug.cached_property
	def config(self):
		return config.config

	@werkzeug.cached_property
	def _sysConfig(self):
		return config.config.get(self.configPath)

	@werkzeug.cached_property
	def _outputConfig(self):
		return config.config.get(self.configPath+'.output')


	@werkzeug.cached_property
	def _bindBaseContext(self):
		
		''' Bind base values that are only available at runtime, but not in the context of a particular request. '''

		context = self.context
		
		# start with base values above
		context = self.baseContext
		
		
		context['link'] = self.url_for
		context['page'] = {}
		
		context['sys'] = {
			'version': str(self._sysConfig['version']['major'])+'.'+str(self._sysConfig['version']['minor'])+' '+str(self._sysConfig['version']['release'])
		}
		return context
		
	def _bindRuntimeTemplateContext(self):

		''' Bind variables to the template context related to the current request context. '''

		raise NotImplementedError("_bindRuntimeTemplateContext is not implemented in %s." % str(self.__class__))

	def _setcontext(self, *args, **kwargs):
		
		''' Take a data structure (list of tuples, dict, or kwargs) and assign the appropriate k, v to the template context. '''
		
		if len(kwargs) > 0:
			for k, v in kwargs.items():
				self.context[k] = v
		
		if len(args) > 0:
			for arg in args:
				if isinstance(arg, list):
					if isinstance(arg[0], tuple):
						for k, v in arg:
							self.context[k] = v
				elif isinstance(arg, dict):
					for k, v in arg.items():
						self.context[k] = v
		return
		

	## 5: Public methods		
	def render(self, path, context={}, elements={}, content_type='text/html', headers={}, **kwargs):

		''' Return a response containing a rendered Jinja template. Create a session if one doesn't exist. '''
		
		if isinstance(self.context, dict) and len(self.context) > 0:
			tmp_context = self.context
			self.context = self._bindBaseContext
			map(self._setcontext, tmp_context)
		else:
			self.context = self._bindBaseContext			
		
		# Parse useragent
		if self.request.headers.get('user-agent', None) is not None:
			try:
				self.uagent = httpagentparser.detect(s)
			except Exception:
				pass
		
		# Build response HTTP headers
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
		
		# Bind runtime-level template context
		try:
			self._bindRuntimeTemplateContext()
		except NotImplementedError, e:
			if config.debug:
				raise
			else:
				pass
			
		# Read minification config + setup minification handler
		if self._outputConfig.get('minify', False) is True:
			try:
				import slimmer
				if content_type == 'text/html':
					self.minify = slimmer.html_slimmer
				elif content_type == 'text/javascript':
					from slimmer.js_function_slimmer import slim as slimjs
					self.minify = slimjs
				elif content_type == 'text/css':
					self.minify = slimmer.css_slimmer

			except ImportError, e:
				self.log.warning('Failed to import minification package "slimmer".')
				if config.debug:
					raise
			
			except AttributeError, e:
				self.log.warning('Could not resolve minification handler.')
				if config.debug:
					raise
					
			except Exception, e:
				if config.debug:
					raise
				
		## Bind elements
		map(self._setcontext, elements)
		
		return self.response(response=self.minify(self.render_template(path, **self.context)), content_type=content_type, headers=[(key, value) for key, value in response_headers.items()])