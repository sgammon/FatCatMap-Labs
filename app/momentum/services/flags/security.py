from momentum.services.flags import ServiceFlag


class Authorize(ServiceFlag):

	def execute(self, *args, **kwargs):
		return self.execute_remote()


class Authenticate(ServiceFlag):

	def execute(self):
		pass

	
class AdminOnly(ServiceFlag):

	def execute(self):
		pass