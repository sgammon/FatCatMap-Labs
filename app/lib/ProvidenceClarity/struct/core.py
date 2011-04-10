
class ProvidenceClarityStructure(object):
	
	platform = 'Providence/Clarity-v2.2-EMBEDDED-ALPHA'


class Struct(ProvidenceClarityStructure):
	
	_type = None
	
	## Init -- Accept structure fill
	def __init__(self, struct=None, **kwargs):
		if struct is not None:
			self.fillStructure(struct)
		else:
			if len(kwargs) > 0:
				self.fillStructure(**kwargs)

	@classmethod
	def _type(cls):
		return cls._type
		
	@classmethod
	def serialize(cls):
		return self.__dict__
		
	@classmethod
	def deserialize(cls, structure):
		return cls(structure)
		
	def fillStruct(self, fill, **kwargs):
		if fill is not None:
			if isinstance(fill, dict):
				for k, v in fill.items():
					self._entries[k] = v
			elif isinstance(fill, list):
				for k, v in fill:
					self._entries[k] = v
		if len(kwargs) > 0:
			for k, v in kwargs.items():
				self._entries[k] = v
				
				
class NamedTuple(tuple):

	_fields = []
	__slots__ = ()

	def __new__(cls, name, bases, _dict):
		
		print ''
		print 'TUPLE: '
		print '----------------------------'
		print '== cls: '+str(cls)
		print '== name: '+str(name)
		print '== bases: '+str(bases)
		print '== dict: '+str(_dict)
		print ''
		
		fields = []
		for key, value in _dict.items():
			if key[0] != '_':
				fields.append((key, value))
				
		print 'fields: '+str(fields)
				
		_dict['_fields'] = fields
		_dict['__slots__'] = ()
		#_dict['__metaclass__'] = type
		return type(name, (object,), _dict)
		
	def __init__(self, *args, **kwargs):

		print ''
		print 'STRUCT INIT: '
		print '----------------------------'
		print '== args: '+str(args)
		print '== kwargs: '+str(kwargs)
		print ''
		
		
	@classmethod
	def _make(cls, iterable, new=tuple.__new__, len=len):
		return new(cls, iterable)

	def __repr__(self):
		return self.__class__.__name__+'('+','.join([k+'='+str(v) for k, v in zip(self._fields, [self.__getitem__(i) for i in enumerate(self._fields)])])+')'

	def _asdict(self):
		return dict([(k, v) for k, v in zip(self._fields, [self.__getitem__(i) for i in enumerate(self._fields)])])

	def _replace(self, **kwargs):
		return self._make(map(kwargs.pop, self._fields, self))

	def __getnewargs__(self):
		return tuple(self)		