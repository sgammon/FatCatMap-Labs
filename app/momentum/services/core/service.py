import config
import logging
import werkzeug

from protorpc import remote


## Top-Level Service Class
class MomentumService(remote.Service):
	
	''' Top-level parent class for ProtoRPC-based API services. '''
	
	handler = None
	middleware = {}
	state = {'request': {}, 'opts': {}, 'service': {}}
	config = {'global': {}, 'module': {}, 'service': {}}

	@werkzeug.cached_property
	def globalConfig(self):
		return config.config.get('momentum.services')
		
	def __init__(self, *args, **kwargs):
		super(MomentumService, self).__init__(*args, **kwargs)
		
	def initiate_request_state(self, state):
		super(MomentumService, self).initiate_request_state(state)

	def _initializeMomentumService(self):

		##### ==== Step 1: Copy over global, module, and service configuration ==== ####
		
		## Copy global config
		self.config['global'] = self.globalConfig
		
		## Module configuration
		if hasattr(self, 'moduleConfigPath'):
			self.config['module'] = config.config.get(getattr(self, 'moduleConfigPath', '__null__'), {})

			## If we have a module + service config path, pull it from the module's branch
			if hasattr(self, 'configPath'):
				path = getattr(self, 'configPath').split('.')
				if len(path) > 0:
					fragment = self.config['module']
					for i in xrange(0, len(path)-1):
						if path[i] in fragment:
							fragment = fragment[path[i]]
					if isinstance(fragment, dict):
						self.config['service'] = fragment

		## No module configuration
		else:
			## Copy over default module config
			self.config['module'] = self.config['global']['defaults']['module']
			
			## If we have a service config path but no module config path...
			if hasattr(self, 'configPath'):
				## Try importing it as a top-level namespace
				toplevel = config.config.get(self.configPath, None)
				if toplevel is None:
					## If that doesn't work, copy it over from defaults...
					self.config['service'] = self.config['global']['defaults']['service']
				else:
					self.config['service'] = toplevel
					
			else:
				## If we have nothing, copy over defaults...
				self.config['service'] = self.config['global']['defaults']['service']
				

		##### ==== Step 2: Check for an initialize hook ==== ####
		if hasattr(self, 'initialize'):
			self.initialize()
		
	def _setstate(self, key, value):
		self.state['service'][key] = value
		
	def _getstate(self, key, default):
		if key in self.state['service']:
			return self.state['service'][key]
		else: return default
		
	def _delstate(self, key):
		if key in self.state['service']:
			del self.state['service'][key]
		
	def __setitem__(self, key, value):
		self._setstate(key, value)
		
	def __getitem__(self, key):
		return self._getstate(key, None)
		
	def __delitem__(self, key):
		self._delstate(key)

	def __repr__(self):
		return '<MomentumService::'+'.'.join(self.__module__.split('.')+[self.__class__.__name__])+'>'
		
	def setflag(self, name, value):
		if self.handler is not None:
			return self.handler.setflag(name, value)
		
	def getflag(self, name):
		if self.handler is not None:
			return self.handler.getflag(name)