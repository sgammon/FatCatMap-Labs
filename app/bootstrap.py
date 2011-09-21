import sys

if 'lib' not in sys.path:
	# Add lib as primary libraries directory, with fallback to lib/dist
	# and optionally to lib/dist.zip, loaded using zipimport.
	sys.path[0:0] = ['lib', 'lib/dist', 'lib/dist.zip']
	

class MomentumBootstrapper(object):

	@classmethod
	def prepareImports(cls):
		if 'lib' not in sys.path:
			sys.path[0:0] = ['lib', 'lib/dist', 'lib/dist.zip']
		return cls
			
	@classmethod
	def prepareTipfy(cls):
		from tipfy import Tipfy
		import config
		return (Tipfy, config.config)