from ProvidenceClarity.struct import ProvidenceClarityStructure
from ProvidenceClarity.struct.factory import SimpleNamedTupleFactory


class SimpleStruct(object):

	_fields = None
	__slots__ = ()

	def __new__(cls, *args, **kwargs):

		''' Called when creating a new instance of SimpleStruct. This should return a NamedTuple. '''
		
		
	def __init__(cls, *args, **kwargs):

		''' Called to initiate a SimpleStruct. Should call super's init so that the NamedTuple can take args/kwargs and map them. '''