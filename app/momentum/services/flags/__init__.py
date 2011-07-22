import logging

class ServiceFlag(object):
	
	args = None
	kwargs = None
	callback = None
	
	def __init__(self, *args, **kwargs):
		self.args = args
		self.kwargs = kwargs

	def __call__(self, fn):

		def wrapped(*args, **kwargs):
			self.callback = fn
			self.callback_args = args
			self.callback_kwargs = kwargs

			for n in set(dir(fn)) - set(dir(self)):
				setattr(self, n, getattr(fn, n))
		
			return self.execute(*self.args, **self.kwargs)
		
		return wrapped
		
	def execute(self, *args, **kwargs):
		return self.execute_remote()
		
	def execute_remote(self):
		return self.callback(*self.callback_args, **self.callback_kwargs)
		
	def __repr__(self):
		return self.callback