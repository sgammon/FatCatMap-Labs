# -*- coding: utf-8 -*-
from momentum.core.handler import MomentumHandler

# Handler Mixins
from momentum.fatcatmap.core.api.output.assets import AssetsMixin
from momentum.fatcatmap.core.api.output.live import LiveServicesMixin
from momentum.fatcatmap.core.api.output.sessions import SessionsMixin



class WebHandler(MomentumHandler, AssetsMixin, LiveServicesMixin, SessionsMixin):
		
	''' Abstract parent-class to any handler that responds to a request from a web browser. '''
	
	configPath = 'momentum.fatcatmap'
	

	def _bindRuntimeTemplateContext(self):

		''' Bind utility functions to the template variable space. '''

		params = self.context

		# Extra config
		params['user'] = self.api.users.get_current_user()
		params['util']['config']['fcm'] = self._sysConfig

		# Bind AssetMixin functions
		params['assets'] = {}
		params['assets']['script'] = self.script_url
		params['assets']['style'] = self.style_url
		params['assets']['url'] = self.asset_url
		params['assets']['image'] = self.img_url
		
		# Page Parameters
		params['page'] = {}
		params['page']['ie'] = False
		params['page']['mobile'] = False
		params['page']['manifest'] = False
		params['page']['optimized'] = False
		params['page']['elements'] = {
			'errorNotice': False,
			'infoNotice': False,
			'generalNotice': False,
			'successNotice': False
		}
		try:
			params['page']['watermark'] = int(self.request.args.get('_w', 0)) or self._outputConfig['watermark']
		except Exception:
			params['page']['watermark'] = True
			
		try:
			params['page']['standalone'] = int(self.request.args.get('_s', 0)) or self._outputConfig['standalone']
		except Exception:
			params['page']['standalone'] = False
		
		# Optimized (bundled) assets
		if self._outputConfig['optimize'] == True and self.request.args.get('_op', '1') != '0':
			params['page']['optimize'] = True
			
		# IE and Mobile flags
		if self.uagent is not None:
			if 'browser' in self.uagent:
				if 'name' in self.uagent['browser']:
					if self.uagent['browser']['name'].lower() in ['msie', 'internet explorer', 'trident']:
						params['page']['ie'] = True
					elif self.uagent['browser']['name'].lower() in ['android', 'safari', 'iphone', 'ipad']:
						params['page']['mobile'] = True
		
		# Appcaching
		if self._outputConfig['appcache']['enable'] == True or self.request.args.get('_ac', False) == True:
				params['page']['manifest'] = self._outputConfig['appcache']['manifest']
				
		# Bind Live Services (channel functions)
		params['live'] = {
			
			'get_lib': self.getChannelLib,
			'get_channel': self.getLiveChannel
			
		}
		
		return params
	