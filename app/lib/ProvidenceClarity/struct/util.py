from ProvidenceClarity.struct.core import Struct

class DictProxy(Struct):
	
	''' Handy little object that takes a dict and makes it accessible via var[item] and var.item formats. Also handy for caching. '''
	
	## Init
	def fillStructure(self, struct=None, **kwargs):
		if struct is not None:
			if isinstance(struct, dict):
				for k, v in struct.items():
					setattr(self, k, v)
			elif isinstance(struct, list):
				for k, v in struct:
					setattr(self, k, v)
		if len(kwargs) > 0:
			for k, v in kwargs.items():
				setattr(self, k, v)
			
	def __getitem__(self, name):
		if name in self.__dict__:
			return getattr(self, name)
		else:
			return default
		
	def __setitem__(self, name, value):
		setattr(self, name, value)
			
	def __delitem__(self, name):
		if name in self._entries:
			del self._entries[name]
			
	## Utiliy Methods
	def items(self):
		return [(k, v) for k, v in self.__dict__.items()]
		
		
class ConfigurableStruct(object):
	
	_config = {}
	
	def bind_config(self, config={}, **kwargs):
		if isinstance(config, dict) and len(config) > 0:
			self._config = config
		if len(kwargs) > 0:
			for k, v in kwargs.items():
				self._config[k] = v
		return self
				
	def set_config(self, config, **kwargs):
		return self.bind_config(config, **kwargs)
				
	def getConfig(self, key=None, default=KeyError):
		if key is None:
			return _config
		else:
			if key in self._config:
				return key
			if isinstance(default, Exception):
				raise default
			else:
				return default