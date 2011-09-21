from momentum.services.flags import ServiceFlag


class Monitor(ServiceFlag):

	def execute(self, *args, **kwargs):
		return self.execute_remote()


class Debug(ServiceFlag):

	def execute(self):
		pass

	
class LogLevel(ServiceFlag):

	def execute(self):
		pass