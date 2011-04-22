from ProvidenceClarity.struct import ProvidenceClarityStructure
from ProvidenceClarity.struct.factory import SimpleStructFactory


class SimpleStruct(object):
	
	''' Abstract base class for a simple structure used somewhere in Providence/Clarity. Mutable, serializable, and low-footprint. '''
	
	__slots__ = []
	__metaclass__ = SimpleStructFactory

	def __init__(self, *args, **kwargs):

		''' Called to initiate a SimpleStruct. Should call super's init so that the NamedTuple can take args/kwargs and map them. '''
		
		if len(args) > 0:
			for param, arg in zip(self.__slots__[0:len(args)], args):
				p_key, p_type = param
				if isinstance(arg, p_type):
					setattr(self, arg, p_key)
				else:
					raise AttributeError('Type error encountered assigning value "'+str(arg)+'" to param name "'+str(p_key)+'" on struct "'+self.__name__+'".')
					
			for param, arg in kwargs.items():
				if param in [k for k, v in self.__slots__]:
					if isinstance(v, dict(self.__slots__)[k]):
						setattr(self, k, v)
					else:
						raise AttributeError('Type error encountered assigning value "'+str(arg)+'" to param name "'+str(p_key)+'" on struct "'+self.__name__+'".')
						
						
	def __getattr__(self, name):
		if name in [k for k, v in self.__slots__]:
			return super(SimpleStruct, self).__getattr__(name)
		else:
			pass ## RAISE EXCEPTION