from config import config
from momentum.fatcatmap.core.api.output import HandlerMixin

## Exception Imports
from momentum.fatcatmap.core.api.output.exceptions import AssetException
from momentum.fatcatmap.core.api.output.exceptions import InvalidAssetType
from momentum.fatcatmap.core.api.output.exceptions import InvalidAssetEntry


class AssetsMixin(HandlerMixin):
	
	methods = ['script_url', 'style_url', 'asset_url']
	

	def _getAssetConfig(self):

		''' Grab and parse the assets config from config.py and return. '''

		return config.get('momentum.fatcatmap.assets')		


	def script_url(self, name, module=None, version=None, minify=False, version_by_getvar=False, **kwargs):

		''' Return a URL for a stylesheet. '''

		return self.asset_url('js', name, module, version, minify, version_by_getvar, **kwargs)

	
	def style_url(self, name, module=None, version=None, minify=False, version_by_getvar=False, **kwargs):

		''' Return a URL for a stylesheet. '''

		return self.asset_url('style', name, module, version, minify, version_by_getvar, **kwargs)
		
	
	def asset_url(self, _type, name, module=None, version=None, minify=False, version_by_getvar=False, **kwargs):

		''' Return a URL for an asset, according to the current configuration. '''

		asset = None
		c = self._getAssetConfig()		
		
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
			query_string = {}

			# 1: Start with the module
			if module is not None:
				asset_url.append(module_path)
	
			# 2: Consider the 'path' param
			if 'path' in asset:
				asset_url.append(asset['path'])

			else:
				# 3: Add the name of the file
				filename = name
	
				# 4: Consider version
				if version is not None:
					if version_by_getvar is False:
						filename += '-'+str(version)
					else:
						query_string['v'] = str(version)
				elif 'version' in asset:
					if version_by_getvar is False:
						filename += '-'+str(asset['version'])
					else:
						query_string['v'] = str(asset['version'])
		
				# 5: Add Extension
				if 'extension' in asset:
					filename += '.'+asset['extension']
				else:
					if _type == 'style':
						filename += '.css'
					elif _type == 'js':
						filename += '.js'
		
					asset_url.append(filename)
	
			# 6: Consider minification
			if minify is not False:
				query_string['m'] = 1
	
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