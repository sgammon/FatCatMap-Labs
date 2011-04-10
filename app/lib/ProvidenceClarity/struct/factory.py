from ProvidenceClarity.struct.core import NamedTuple

## == For the 'Simple' struct type
class SimpleNamedTupleFactory(type):
	
	'''
	
		=====================================================
		| Providence/Clarity Structures: Simple Named Tuple |
		=====================================================
		This class creates a named tuple at runtime out of an easily-definable OOP-based 'Struct' schema.
		The SimpleStruct class uses this as a factory for producing the named tuples at runtime.
	
		Advantages of the Simple Named Tuple:
		--1: Serializable without any special code
		--2: Can be unpacked, and is hashable (extends tuple)
		--4: Easier on memory than a full class inheritance path
	
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