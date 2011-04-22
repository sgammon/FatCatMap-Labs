from ProvidenceClarity.struct.core import Record
from ProvidenceClarity.struct.core import NamedTuple


## == For the 'Simple' struct type
class SimpleStructFactory(type):
	
	'''
	
		========================================================
		| Providence/Clarity Structures: Simple Struct Factory |
		========================================================
		This class creates a named tuple at runtime out of an easily-definable OOP-based 'Struct' schema. The
		SimpleStruct class uses this as a factory for producing the named, tailored structures at runtime.
	
		Advantages of the Simple Named Tuple:
		--1: Serializable without any special code
		--2: Can be unpacked, and is hashable (extends tuple)
		--3: Easier on memory than a full class inheritance path
	
	'''
	
	def __new__(cls, name, bases, _dict):

		if object in bases and name == 'SimpleStruct':
			return type.__new__(cls, name, bases, _dict)
		
		else:
			_fields = [(k, v) for k, v in filter(lambda x: x[0][0] != '_' and True or False, _dict.items())]
			_dict['__slots__'] = [str(k) for k, v in _fields]
			#_dict['__metaclass__'] = cls._spawnStruct
			return type.__new__(cls, name, bases, _dict)
			
	@classmethod
	def _spawnStruct(cls, name, bases, _dict):
		pass


## == For the 'Immutable' struct type
class ImmutableStructFactory(type):

	'''

		===========================================================
		| Providence/Clarity Structures: Immutable Struct Factory |
		===========================================================
		This class creates a named tuple at runtime out of an easily-definable OOP-based 'Struct' schema. The
		SimpleStruct class uses this as a factory for producing the named (immutable) tuples at runtime.

		Advantages of the Simple Named Tuple:
		--1: Serializable without any special code
		--2: Can be unpacked, and is hashable (extends tuple)
		--3: Easier on memory than a full class inheritance path

	'''

	def __new__(cls, name, bases, _dict):

		print ''
		print 'FACTORY: '
		print '----------------------------'
		print '== cls: '+str(cls)
		print '== name: '+str(name)
		print '== bases: '+str(bases)
		print '== dict: '+str(_dict)
		print ''

		return NamedTuple(name, bases, _dict)



## == For the 'Complex' struct type
class ComplexDictionaryFactory(type):

	'''
	
		=====================================================
		| Providence/Clarity Structures: Complex Dictionary |
		=====================================================
		This class creates a modified dictionary at runtime out of an easily-definable OOP-based 'Struct'
		schema. The ComplexStruct class uses this as a factory for producing the dictionary at runtime.
	
		Advantages of the Complex Dictionary:
		--1: Properties can be accessed with dot or subscript syntax
		--2: Properties can be defined at runtime in the constructor
		--4: Resulting objects can have methods and properties (like an object)
	
	'''
	
	pass