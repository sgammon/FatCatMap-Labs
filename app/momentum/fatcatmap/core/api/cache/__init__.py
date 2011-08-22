import logging
import datetime
from config import config

from werkzeug import cached_property
from google.appengine.api import memcache
from google.appengine.api import namespace_manager
from momentum.fatcatmap.core.api import MomentumCoreAPI

_EMPTY_NAMESPACE = '__DEFAULT__'

_fast_cache = {}
_fragment_cache = {}


class CacheAdapter(object):
	
	''' Abstract parent class to enforce cache adapter interface. '''
	
	namespace = None

	config = None
	configPath = None
	
	@cached_property
	def cacherConfig(self):
		return config.get('momentum.fatcatmap.cache')
	
	def __init__(self, namespace=None):
		if namespace is not None:
			self.namespace = namespace
		if self.configPath is not None:
			self.config = self.cacherConfig['adapters'][self.configPath]
	
	def resolveNamespace(self, override, enable_prefix=True):
		
		_EMPTY_NAMESPACE = '__NONE__'
		
		prefix = None
		namespace = None
		
		if enable_prefix and self.cacherConfig['prefix_namespace']:
			if self.cacherConfig['prefix_mode'] == 'explicit':
				prefix = self.cacherConfig['prefix']
			elif self.cacherConfig['prefix_mode'] == 'inherit':
				prefix = namespace_manager.get_namespace()
				
		if override is None:
			if self.namespace is None:
				namespace = None
			else:
				namespace = self.namespace
		else:
			namespace = override
			
		if namespace is None and prefix is None:
			return _EMPTY_NAMESPACE
			
		elif namespace is None and prefix is not None:
			return prefix
		
		elif namespace is not None and prefix is None:
			return namespace
			
		else:
			return self.cacherConfig.get('namespace_seperator', '::').join([prefix, namespace])
				
	
	def resolveNamespace(self, override, prefix=True):
		global _EMPTY_NAMESPACE
		
		if override is not None and isinstance(override, basestring) and (prefix is False or self.cacherConfig['prefix_namespace'] is False):
			return override
		else:
			
			if prefix is False and self.cacherConfig['prefix_namespace'] is False:
				return _EMPTY_NAMESPACE
			
			elif self.cacherConfig['prefix_namespace'] is not False and prefix is False:
				if self.cacherConfig['prefix_mode'] == 'inherit':
					prefix = namespace_manager.get_namespace()
				elif self.cacherConfig['prefix_mode'] == 'explicit':
					prefix = self.cacherConfig.get('prefix', '')
				else:
					prefix = ''

				if override:
					return self.cacherConfig.get('namespace_seperator', '::').join([prefix, override])
				else:
					if self.namespace is not None:
						return self.cacherConfig.get('namespace_seperator', '::').join([prefix, self.namespace])
		return _EMPTY_NAMESPACE

	
	def getByKey(self, key, namespace=None, default_value=None):
		raise NotImplemented, 'getByKey must be implemented by CacheAdapter child classes.'
		
	def getMulti(self, keys, prefix=None, namespace=None):
		raise NotImplemented, 'getMulti must be implemented by CacheAdapter child classes.'
		
	def setByKey(self, key, value, ttl=None, namespace=None):
		raise NotImplemented, 'setByKey must be implemented by CacheAdapter child classes.'

	def setMulti(self, mapping, prefix=None, ttl=None, namespace=None):
		raise NotImplemented, 'getMulti must be implemented by CacheAdapter child classes.'
		
	def deleteByKey(self, key, namespace=None):
		raise NotImplemented, 'deleteByKey must be implemented by CacheAdapter child classes.'

	def deleteMulti(self, mapping, prefix=None, namespace=None):
		raise NotImplemented, 'getMulti must be implemented by CacheAdapter child classes.'
		
	def clearAllValues(self, namespace=None):
		raise NotImplemented, 'clearAllValues must be implemented by CacheAdapter child classes.'


class FastcacheAdapter(CacheAdapter):

	''' Adapter to central instance memory cache. '''
	
	configPath = 'fastcache'
	
	def getByKey(self, key, namespace=None, default_value=None):
		global _fast_cache

		namespace = self.resolveNamespace(namespace)			
		if namespace in _fast_cache:
			if key in _fast_cache[namespace]['items']:
				
				ttl = _fast_cache[namespace]['items'][key].get('ttl', self.config['default_ttl'])
				expiration = _fast_cache[namespace]['items'][key]['timestamp']+datetime.timedelta(seconds=ttl)
				
				if datetime.datetime.now() < expiration:
					_fast_cache[namespace]['meta']['hits'] += 1
					return _fast_cache[namespace]['items'][key]['value']
				else:
					del _fast_cache[namespace]['items'][key]
					return default_value

			_fast_cache[namespace]['meta']['misses'] += 1
		return default_value

	
	def getMulti(self, keys, prefix=None, namespace=None):
		global _fast_cache
		
		namespace = self.resolveNamespace(namespace)
		if namespace in _fast_cache:
			return [result for result in filter(lambda x: x == None, [self.getByKey(ck, namespace) for ck in map(lambda x: prefix != None and '::'.join([prefix+key]) or key, keys)])]
	
			
	def setByKey(self, key, value, ttl=None, namespace=None):
		global _fast_cache

		namespace = self.resolveNamespace(namespace)			
		if namespace not in _fast_cache:
			_fast_cache[namespace] = {'meta': {'items': 0, 'counters': 0, 'hits': 0, 'misses': 0}, 'items': {}, 'counters': {}}

		if key not in _fast_cache[namespace]['items']:
			_fast_cache[namespace]['meta']['items'] += 1
		
		_fast_cache[namespace]['items'][key] = {'value': value, 'timestamp': datetime.datetime.now()}
		if ttl is not None:
			_fast_cache[namespace]['items'][key]['ttl'] = ttl
				
				
	def setMulti(self, mapping, prefix=None, ttl=None, namespace=None):
		global _fast_cache

		namespace = self.resolveNamespace(namespace)
		if isinstance(mapping, dict):
			for key, value in mapping.items():
				if prefix is not None:
					key = self.cacherConfig.get('key_seperator', '::').join([prefix, key])
				self.setByKey(key, value, ttl, namespace)
		return
				

	def deleteByKey(self, key, namespace=None):
		global _fast_cache
		
		namespace = self.resolveNamespace(namespace)			
		if namespace in _fast_cache:
			if key in _fast_cache[namespace]['items']:
				_fast_cache[namespace]['meta']['items'] -= 1				
				del _fast_cache[namespace]['items'][key]		
		return
		
		
	def deleteMulti(self, mapping, prefix=None, namespace=None):
		global _fast_cache

		namespace = self.resolveNamespace(namespace)
		if isinstance(mapping, list):
			for key in mapping:
				if prefix is not None:
					key = self.cacherConfig.get('key_seperator', '::').join([prefix, key])
				self.deleteByKey(key, namespace)
		return		
		
	
	def dumpAllValues(self, namespace=False):
		global _fast_cache
		namespace = self.resolveNamespace(namespace)
		
		if namespace is False:
			return _fast_cache
		else:
			if namespace in _fast_cache:
				return _fast_cache[namespace]
		return
			
	
	def clearAllValues(self, namespace=False):
		global _fast_cache
		namespace = self.resolveNamespace(namespace)
		
		if namespace is False:
			_fast_cache = {}
		else:
			if namespace in _fast_cache:
				del _fast_cache[namespace]
		return
		
	
class MemcacheAdapter(CacheAdapter):

	''' Adapter to memcache. '''
	
	configPath = 'memcache'
	
	def getByKey(self, key, namespace=None, default_value=None):
		namespace = self.resolveNamespace(namespace)
		logging.info('GETTING KEY "'+str(key)+'" from namespace "'+str(namespace)+'"')
		result = memcache.get(key, namespace=namespace)
		logging.info('RESULT '+str(result))
		if result is not None:
			return result
		else:
			return default_value
		
	def getMulti(self, keys, prefix=None, namespace=None):
		namespace = self.resolveNamespace(namespace)
		return memcache.get_multi(keys, prefix, namespace)
		
	def setByKey(self, key, value, ttl=None, namespace=None):
		namespace = self.resolveNamespace(namespace)
		if ttl is None:
			ttl = self.config['default_ttl']
		logging.info('SETTING KEY "'+str(key)+'" to namespace "'+str(namespace)+'" to value "'+str(value)+'"')
		return memcache.set(key, value, ttl, namespace=namespace)
		
	def setMulti(self, mapping, prefix=None, ttl=None, namespace=None):
		namespace = self.resolveNamespace(namespace)
		if ttl is None:
			ttl = self.config['default_ttl']
		return memcache.set_multi(mapping, ttl, prefix, 0, namespace)
		
	def deleteByKey(self, key, namespace=None):
		namespace = self.resolveNamespace(namespace)
		return memcache.delete(key, 0, namespace)
		
	def deleteMulti(self, mapping, prefix=None, namespace=None):
		namespace = self.resolveNamespace(namespace)
		return memcache.delete_multi(mapping, 0, prefix, namespace)
		
	def clearAllValues(self, namespace=None):
		namespace = self.resolveNamespace(namespace)
		return memcache.flush_all()
	
	
class DatastoreAdapter(CacheAdapter):

	''' Adapter to datastore-based caching. '''
	
	configPath = 'datastore'



class CoreCacheAPI(MomentumCoreAPI):
	pass