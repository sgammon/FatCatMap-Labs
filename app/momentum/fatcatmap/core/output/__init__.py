"""

Core: Output

Responsible for the task of finding and compiling templates to be sent to the browser.
Two levels of caching are implemented here - in-memory handler caching and memcache.

According to settings in the config.py, this module will attempt to load compiled
template code from the handler first, memcache second, and at last resort will compile
the template and store it in the cache.

-sam (<sam@momentum.io>)

"""

import os
import base64
import pprint
import config
import logging
import datetime
import timesince
import simplejson
import byteconvert

from google.appengine.ext import db
from google.appengine.api import memcache

from werkzeug import cached_property

from tipfyext.jinja2 import Environment as JEnvironment
from tipfyext.jinja2 import ModuleLoader as JModuleLoader
from tipfyext.jinja2 import FileSystemLoader as JFileSystemLoader

try:
	from tipfy.ext import i18n
except (ImportError, AttributeError), e:
	i18n = None

try:
	t_data
except NameError:
	t_data = {}


# Superfast In-Memory Cache
def get_tdata_from_fastcache(name, do_log):

	''' Get template data from fastcache (instance memory). '''

	if name in t_data:
		if do_log: logging.debug('OUTPUT_LOADER: Found bytecode in fastcache memory under key \''+str(base64.b64encode(name))+'\'.')
		return t_data[name]
	else: return None
	
def set_tdata_to_fastcache(name, data, do_log):
	
	''' Save template data to fastcache (instance memory). '''
	
	t_data[name] = data
	if do_log: logging.debug('OUTPUT_LOADER: Set template \''+str(name)+'\' to fastcache memory.')
	

# Memcache API loader
def get_tdata_from_memcache(name, do_log):
	
	''' Get template data from memcache. '''
	
	data = memcache.get('Core//Output//Template-'+name)
	if data is not None:
		if do_log: logging.debug('OUTPUT_LOADER: Found bytecode in memcache under key \'tdata-'+str(name)+'\'.')
		return data
	else: return None
	
def set_tdata_to_memcache(name, data, do_log):
	
	''' Set template data to memcache. '''
	
	memcache.set('Core//Output//Template-'+name, data)
	if do_log: logging.debug('OUTPUT_LOADER: Set template \''+str(name)+'\' to memcache under key \'Core//Output//Template-'+str(name)+'\'.')
	

# Loader class
class FCMCoreOutputLoader(JFileSystemLoader):
	
	''' Loads templates and automatically inserts bytecode caching logic for both fastcache (instance memory) and memcache. '''
	
	@cached_property
	def devConfig(self):
		return config.config.get('momentum.fatcatmap.dev')
		
	@cached_property
	def loaderConfig(self):
		return config.config.get('momentum.fatcatmap.output.template_loader')

	def get_source(self, environment, name):

		# Load config
		dev = self.devConfig
		y_cfg = self.loaderConfig
		
		# Encode in Base64
		b64_name = base64.b64encode(name)

		# Debug logging
		if y_cfg.get('debug') == True: do_log = True
		else: do_log = False
		if do_log: logging.debug('OUTPUT_LOADER: FCM Template Loader received request for name \''+str(name)+'\'.')
		
		# Don't do caching if we're in dev mode
		if not config.debug or self.loaderConfig['force'] is True:

			# Try the in-memory supercache
			if y_cfg.get('use_memory_cache') == True: bytecode = get_tdata_from_fastcache(b64_name, do_log)
			else: bytecode = None
		
			if bytecode is None: # Not found in fastcache
		
				if do_log: logging.debug('OUTPUT_LOADER: Template not found in fastcache.')
			
				# Fallback to memcache
				if y_cfg.get('use_memcache') == True: bytecode = get_tdata_from_memcache(b64_name, do_log)

				# Fallback to regular loader, then cache
				if bytecode is None: # Not found in memcache
				
					if do_log: logging.debug('OUTPUT_LOADER: Template not found in memcache.')
					source = super(FCMCoreOutputLoader, self).get_source(environment, name)
				
					if y_cfg.get('use_memcache') != False:
						set_tdata_to_memcache(b64_name, source, do_log)
				
					if y_cfg.get('use_memory_cache') != False:
						set_tdata_to_fastcache(b64_name, source, do_log)
	
		else: ## In dev mode, compile everything every time
		
			source = super(FCMCoreOutputLoader, self).get_source(environment, name)
			
		# Return compiled template code
		return source
		
		
# Template Factory
def fcmOutputEnvironmentFactory(environment):

	"""Returns a prepared Jinja2 environment for FCM.

	:return:
		A ``jinja2.Environment`` instance.
	"""

	cfg = config.config.get('tipfyext.jinja2')
	templates_compiled_target = cfg.get('templates_compiled_target')
	use_compiled = not config.debug or cfg.get( 'force_use_compiled')

	if templates_compiled_target is not None and use_compiled:
		# Use precompiled templates loaded from a module or zip.
		loader = JModuleLoader(templates_compiled_target)
	else:
		# Parse templates for every new environment instances.
		loader = FCMCoreOutputLoader(cfg.get('templates_dir'))

	# Add global functions
	util = {
		'converters':{
			'timesince':timesince.timesince,
			'byteconvert':byteconvert.humanize_bytes,
			'json':simplejson
		},
		'getattr':getattr,
		'setattr':setattr,
		'pprint':pprint.pprint,
		'config':config.config,
		'len': len,
		'type': type,
		'types':{
			'str':str,
			'basestring':basestring,
			'object':object,
			'int':int,
			'long':long,
			'float':float,
			'datetime': datetime,
			'list':list,
			'dict':dict,
			'tuple':tuple,
			'appengine':{
			
				'db':{
					'key':db.Key,
					'model':db.Model
				}
			
			}
		}
	}
	
	# Set global functions
	environment.globals['util'] = util
	
	if i18n:
		# Install i18n.
		trans = i18n.get_translations
		environment.install_gettext_callables(
			lambda s: trans().ugettext(s),
			lambda s, p, n: trans().ungettext(s, p, n),
			newstyle=True)
		environment.globals.update({
			'format_date':	   i18n.format_date,
			'format_time':	   i18n.format_time,
			'format_datetime': i18n.format_datetime,
		})

	environment.loader = loader