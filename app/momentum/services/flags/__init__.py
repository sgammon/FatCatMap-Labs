import logging

class ServiceFlag(object):
	
	args = None
	kwargs = None
	request = None
	service = None	
	callback = None
	
	def __init__(self, *args, **kwargs):
		self.args = args
		self.kwargs = kwargs

	def __call__(self, fn):

		def wrapped(service_obj, request):

			self.callback = fn
			self.service = service_obj
			self.request = request

			for n in set(dir(fn)) - set(dir(self)):
				setattr(self, n, getattr(fn, n))
		
			return self.execute(*self.args, **self.kwargs)
		
		return wrapped
		
	def execute(self, *args, **kwargs):
		return self.execute_remote()
		
	def execute_remote(self):
		return self.callback(self.service, self.request)
		
	def __repr__(self):
		return self.callback