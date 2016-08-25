from momentum.platform.core.security import SecurityMiddleware

	
class LoginRequiredMiddleware(SecurityMiddleware):

	def pre_dispatch(self, handler):
		return _enforce_fcm_security(handler, 'login', self.authConfig)

	
	
class UserRequiredMiddleware(SecurityMiddleware):

	def pre_dispatch(self, handler):
		return _enforce_fcm_security(handler, 'user', self.authConfig)

	
	
class AdminRequiredMiddleware(SecurityMiddleware):

	def pre_dispatch(self, handler):
		return _enforce_fcm_security(handler, 'admin', self.authConfig)



def _enforce_fcm_security():
	pass