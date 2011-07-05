import logging
from config import config
from werkzeug import cached_property
from momentum.fatcatmap.core.api.output import HandlerMixin

## Exception Imports
from momentum.fatcatmap.core.api.output.exceptions import AssetException
from momentum.fatcatmap.core.api.output.exceptions import InvalidAssetType
from momentum.fatcatmap.core.api.output.exceptions import InvalidAssetEntry


class CoreAssetsAPI(object):
	
	methods = ['script_url', 'style_url', 'asset_url']

	@cached_property
	def _AssetConfig(self):

		''' Grab and parse the assets config from config.py and return. '''

		return config.get('momentum.fatcatmap.assets')
		
	
	@cached_property
	def _OutputConfig(self):
		
		''' Grab and parse the output config from config.py and return. '''
		
		return config.get('momentum.fatcatmap.output')


	def script_url(self, name, module=None, prefix='static', version=None, minify=False, version_by_getvar=False, **kwargs):

		''' Return a URL for a stylesheet. '''

		return self.asset_url('js', name, module, prefix, version, minify, version_by_getvar, **kwargs)

	
	def style_url(self, name, module=None, prefix='static', version=None, minify=False, version_by_getvar=False, **kwargs):

		''' Return a URL for a stylesheet. '''

		return self.asset_url('style', name, module, prefix, version, minify, version_by_getvar, **kwargs)


	def ext_url(self, name, module=None, prefix='static', version=None, minify=False, version_by_getvar=False, **kwargs):

		''' Return a URL for a stylesheet. '''

		return self.asset_url('ext', name, module, prefix, version, minify, version_by_getvar, **kwargs)
		
	
	def asset_url(self, _type, name, module, prefix, version, minify, version_by_getvar, **kwargs):
		
		''' Return a URL for an asset, according to the current configuration. '''
		
		asset = None
		module_path = None
		
		if _type not in self._AssetConfig:
			raise InvalidAssetType, "Asset type '"+str(_type)+"' is invalid for name '"+str(name)+"' in module '"+str(module)+"'."

		# Grab config and find requested asset
		if _type in self._AssetConfig:
			if name in self._AssetConfig[_type]:
				asset = self._AssetConfig[_type][name]
			else:
				for entry in self._AssetConfig[_type]:
					if isinstance(entry, tuple):
						if entry[0] == module:
							asset = self._AssetConfig[_type][(module, entry[1])].get(name, False)
							if asset is False:
								raise InvalidAssetEntry, "Could not resolve asset '"+str(name)+"' under VALID module '"+str(module)+"'."
							module_path = entry[1]

		if asset is not None and isinstance(asset, dict):

			# Start building asset URL
			filename = []
			query_string = {}
			asset_url = ['assets', _type, prefix, module_path, ('.', filename)]
			minify = minify or self._OutputConfig.get('minify', False)
			
			
			## 1: Consider absolute assets
			if 'absolute' in asset:
				abs_url = asset.get('scheme', 'http')+'://'
				
				if minify and 'min' in asset and isinstance(asset['min'], basestring):
					return abs_url+asset.get('min')
				else:
					return asset.get('absolute')

			## 2: Consider relative assets
			else:

				## 2.1: Consider path
				if 'path' in asset:

					### Minification in path mode is a path
					if minify and 'min' in asset and isinstance(asset['min'], basestring):
						query_string['m'] = '1'
						pathspec = asset['min'].split('/')
						filename += pathspec[-1].split('.')
				
					### If there's no minification and we have a path, use it	
					else:
						pathspec = asset['path'].split('/')
						filename += pathspec[-1].split('.')
						
					### Consider version
					if version is not None or 'version' in asset:
						if version is None: version = asset['version']
						if version_by_getvar is False:
							filename.append(str(version))
						else:
							query_string['v'] = str(version)
					
					asset_url.insert(-1, ('/', pathspec[0:-1]))
			

				## 2.2: Consider no-path
				else:
					filename.append(name)
				
					### Consider version
					if version is not None or 'version' in asset:
						if version is None: version = asset['version']
						if version_by_getvar is False:
							filename.append(str(version))
						else:
							query_string['v'] = str(version)
				
					### Minification in no-path mode is a boolean (appends .min)
					if minify and 'min' in asset and isinstance(asset['min'], bool):
						query_string['m'] = '1'
						filename.append('min')
				
					### Consider explicit extension	
					if 'extension' in asset:
						filename.append(asset['extension'])					

					### Consider implicit extension
					else:
						if _type == 'style':
							filename.append('css')
						elif _type == 'js':
							filename.append('js')
				

				## 2.3: Consider arbitrary query string entries
				if len(kwargs) > 0:
					for key, value in kwargs.items():
						query_string[key] = str(value)

				logging.info('ASSET_URL: '+str(asset_url))
				logging.info('QUERY_STRING: '+str(query_string))

				## 2.4: Build relative asset URL
				if len(query_string) > 0:
					
					return reduce(lambda x, y: x+y, ['/', '/'.join(map(lambda x: isinstance(x, tuple) and x[0].join(x[1]) or x, filter(lambda x: x not in [True, False, None], asset_url))), '?', '&'.join([str(k)+'='+str(v) for k, v in query_string.items()])])
					
				else:
					return reduce(lambda x, y: x+y, ['/', '/'.join(map(lambda x: isinstance(x, tuple) and x[0].join(x[1]) or x, filter(lambda x: x not in [True, False, None], asset_url)))])
				
		else:
			if not isinstance(asset, dict):
				raise InvalidAssetEntry, "Could not resolve non-mapping asset by the name of '"+str(name)+"'. Asset value: '"+str(asset)+"'."
			
			if module not in c[_type] and name not in c[_type]:
				raise InvalidAssetEntry, "Could not resolve asset '"+str(name)+"' in module '"+str(module)+"'."
				

	def asset_url_old(self, _type, name, module=None, version=None, minify=False, version_by_getvar=False, **kwargs):

		''' Return a URL for an asset, according to the current configuration. '''

		asset = None
		c = self._AssetConfig
		o = self._OutputConfig
		
		if _type not in c:
			raise InvalidAssetType, "Asset type '"+str(_type)+"' is invalid for name '"+str(name)+"' in module '"+str(module)+"'."

		# Grab config and find requested asset
		if _type in c:
			if name in c[_type]:
				asset = c[_type][name]
			else:
				for entry in c[_type]:
					if isinstance(entry, tuple):
						if entry[0] == module:
							asset = c[_type][(module, entry[1])][name]
							module_path = entry[1]

		if asset is not None:

			# Start building the URL
			asset_url = ['assets', _type, 'static']
			filename = []
			asset_postfix = ['.']
			skip_path = False
			query_string = {}

			# 1: Start with the module
			if module is not None:
				asset_url.append(module_path)
	
			# 2: Consider output-set minification
			if o['minify'] is True or minify is True:
				
				if 'min' in asset and isinstance(asset['min'], basestring):
					asset_url.append(asset['min'])
					skip_path = True
					
				elif 'min' in asset and isinstance(asset['min'], bool) and asset['min'] is True:
					asset_postfix = asset_postfix+['min', '.']

			# 3: Consider the 'path' param
			if 'path' in asset and skip_path is not True:
				asset_url.append(asset['path'])
			else:
				# Add the name of the file if there is no path
				filename.append(name)
	
			# 4: Consider version
			if version is not None or 'version' in asset:
				if version is None: version = asset['version']
				if version_by_getvar is False:
					filename.append('-')
					filename.append(str(version))
				else:
					query_string['v'] = str(version)
	
			# 5: Add Extension
			if 'extension' in asset:
				asset_postfix.append(asset['extension'])
			else:
				if _type == 'style':
					asset_postfix.append('css')
				elif _type == 'js':
					asset_postfix.append('js')
	
			asset_url.append(reduce(lambda x, y: x+y, filename+asset_postfix)) ## Append filename to URL
		
			# 7: Consider extra query string params
			if len(kwargs) > 0:
				for k, v in kwargs.items():
					query_string[k] = str(v)

			if len(query_string) > 0:
				# Build URL and return!
				return '/'+'/'.join(asset_url)+'?'+'&'.join([str(k)+'='+str(v) for k, v in query_string.items()])
			else:
				# Build URL and return!
				return '/'+'/'.join(asset_url)
		
		else:
			if module not in c[_type] and name not in c[_type]:
				raise InvalidAssetEntry, "Could not resolve asset '"+str(name)+"' in module '"+str(module)+"'."
				
				
class AssetsMixin(CoreAssetsAPI, HandlerMixin):
	pass