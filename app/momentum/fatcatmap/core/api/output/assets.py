from config import config
from momentum.fatcatmap.core.api.output import HandlerMixin


class AssetsMixin(HandlerMixin):
	
	methods = ['script_url', 'style_url', 'asset_url']
	

	def _getAssetConfig(self):

		''' Grab and parse the assets config from config.py and return. '''

		return config.get('momentum.fatcatmap.assets')		


	def script_url(self, name, module=None, version=None, minify=False, **kwargs):

		''' Return a URL for a stylesheet. '''

		return self.asset_url('js', name, module, version, minify, **kwargs)

	
	def style_url(self, name, module=None, version=None, minify=False, **kwargs):

		''' Return a URL for a stylesheet. '''

		return self.asset_url('style', name, module, version, minify, **kwargs)
		
	
	def asset_url(self, _type, name, module=None, version=None, minify=False, **kwargs):

		''' Return a URL for an asset, according to the current configuration. '''

		asset = None
		assert _type in ['style', 'js', 'ext'] # Only three modules right now...

		# Grab config and find requested asset
		c = self._getAssetConfig()
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
				filename = name+'-'
	
				# 4: Consider version
				if version is not None:
					filename += str(version)
				elif 'version' in asset:
					filename += str(asset['version'])
		
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
		
				# Build URL and return!
				return '/'+'/'.join(asset_url)+'?'+'&'.join([str(k)+'='+str(v) for k, v in query_string.items()])
	
			# Build URL and return!
			return '/'+'/'.join(asset_url)
		
		else:
			raise KeyError