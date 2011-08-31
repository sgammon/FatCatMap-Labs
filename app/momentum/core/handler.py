# -*- coding: utf-8 -*-
import os
import ndb
import config
import hashlib
import logging
import pipeline
import werkzeug
import protorpc
import momentum
import mapreduce
import simplejson

# ProtoRPC Imports
from protorpc import remote

# Momentum
from momentum import core
from momentum import platform

# Momentum Core
from momentum.core import model
from momentum.core import platform

# Tipfy Imports
from tipfy import Request
from tipfy import Response
from tipfy import RequestHandler
from tipfyext.jinja2 import Jinja2Mixin
from tipfy.i18n import I18nMiddleware
from tipfy.sessions import SessionMiddleware

# Providence/Clarity Imports
import ProvidenceClarity
from ProvidenceClarity.struct.util import DictProxy
from ProvidenceClarity.struct.util import ObjectProxy

# App Engine Imports
from google.appengine.ext import db
from google.appengine.api import xmpp
from google.appengine.api import mail
from google.appengine.api import oauth
from google.appengine.api import users
from google.appengine.api import images
from google.appengine.api import channel
from google.appengine.api import backends
from google.appengine.api import memcache
from google.appengine.api import urlfetch
from google.appengine.ext import blobstore
from google.appengine.api import taskqueue
from google.appengine.api import capabilities
from google.appengine.api import app_identity
from google.appengine.api import namespace_manager
from google.appengine.api import prospective_search


class MomentumHandler(RequestHandler, Jinja2Mixin):

	''' Top-level parent class for request handlers based in Tipfy. '''
	
	## 1: Class variables
	configPath = None
	minify = unicode
	response = Response
	
	## 2: Sessions, auth, etc middleware
	middleware = [SessionMiddleware(), I18nMiddleware()]

	## 3: Shortcuts
	api = DictProxy({
	
		'db': db,
		'xmpp': xmpp,
		'mail': mail,
		'oauth': oauth,
		'users': users,
		'images': images,
		'channel': channel,
		'backends': backends,
		'memcache': memcache,
		'urlfetch': urlfetch,
		'blobstore': blobstore,
		'taskqueue': taskqueue,
		'capabilities': capabilities,
		'identity': app_identity,
		'multitenancy': namespace_manager,
		'matcher': prospective_search,
		
	})

	ext = DictProxy({
	
		'ndb': ndb,
		'protorpc': protorpc,
		'pipelines': pipeline,
		'mapreduce': mapreduce
	
	})
	
	platform = DictProxy({

		'core': momentum.core,
		'api': momentum.platform,
		'engine': ProvidenceClarity.AppBridge,
	
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
				'json': simplejson
			}
		},
		
		## API Shortcuts
		'api': {
		
			'oauth': oauth,
			'users': {
				'is_current_user_admin': users.is_current_user_admin,
				'current_user': users.get_current_user,
				'create_login_url': users.create_login_url,
				'create_logout_url': users.create_logout_url
			},
			'backends': backends,
			'multitenancy': namespace_manager
		
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