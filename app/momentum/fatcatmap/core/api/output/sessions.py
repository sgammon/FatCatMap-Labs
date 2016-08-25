from momentum.fatcatmap.core.api.sessions import CoreSessionsAPI
from momentum.fatcatmap.core.api.output import HandlerMixin


class SessionsMixin(HandlerMixin):
	
	_sessions_api = CoreSessionsAPI()
	
	def getFatCatMapSession(self):
		
		if 'client' not in self.session or 'sid' not in self.session:
			if 'client' not in self.session:
				self.session['client'], self.session['sid'] = self._sessions_api.keyFactory()
			else:
				self.session['sid'] = self._sessions_api.keyFactory(self.session['client'])
				
		else:
			return self.session