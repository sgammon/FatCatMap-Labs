from momentum.services.flags import ServiceFlag


class Cacheable(ServiceFlag):

	def execute(self, *args, **kwargs):
		return self.execute_remote()


class LocalCacheable(ServiceFlag):

	def execute(self):
		pass

	
class MemCacheable(ServiceFlag):

	def execute(self):
		pass