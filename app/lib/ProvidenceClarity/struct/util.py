

class ProvidenceClarityDictProxy(object):
	
	''' Handy little object that takes a dict and makes it accessible via var[item] and var.item formats. Also handy for caching. '''
	
	_entries = {}
	
	## Init
	def __init__(self, struct=None, **kwargs):
		if struct is not None:
			if isinstance(struct, dict):
				for k, v in struct.items():
					self._entries[k] = v
			elif isinstance(struct, list):
				for k, v in struct:
					self._entries[k] = v
		if len(kwargs) > 0:
			for k, v in kwargs.items():
				self._entries[k] = v
	
	## Getters
	def __getattr__(self, name, default=False):
		if name in self._entries:
			return self._entries[name]
		else:
			return default
			
	def __getitem__(self, name, default=False):
		if name in self._entries:
			return self._entries[name]
		else:
			return default
	
	## Setters
	def __setattr__(self, name, value):
		self._entries[name] = value
		
	def __setitem__(self, name, value):
		self._entries[name] = value
		
	## Deleters
	def __delattr__(self, name):
		if name in self._entries:
			del self._entries[name]
			
	def __delitem__(self, name):
		if name in self._entries:
			del self._entries[name]
			
	## Utiliy Methods
	def items(self):
		return [(k, v) for k, v in self._entries.items()]