import logging
from ndb import model as n

from ProvidenceClarity.adapters import ProvidenceClarityAdapter


# ==== Indexing Operation Interface ==== #
class IndexAdapter(ProvidenceClarityAdapter):

	''' @todo: prettify this block
		FatCatMap Indexer:
		
			Author: Sam Gammon <sam@momentum.io>
		
			This class serves as an abstract parent class and interface specification for
			type-specific indexing operations. Type-based subclasses (like StringIndexer)
			from the m.f.core.api.indexer.types module extend this class.
	'''
	
	_entries = {}
		
	#### Util Methods ####
	def __init__(self, *args, **kwargs):
		super(IndexAdapter, self).__init__(*args, **kwargs)
		
	def _clear(self):
		self._input = None
		self._entries = {}
		
	def _getInput(self, _input):
		return self._input
		
	def _setEntries(self, entries):
		self._entries = entries
	
	def _getEntries(self):
		return self._entries
		
	def _encounterEntry(self, key, entry=None):
		if key not in self._entries:
			self._entries[key] = {}
		else:
			self._entries[key]['model'] = entry

		
	#### Low-Level Methods (Overridden by indexer subclasses) ####
	def prepareInput(self, _input):
		''' Receives input and sanitizes/prepares it to be tokenized and otherwise processed. '''
		return _input
	
	def tokenizeInput(self, _input):
		''' Receives prepared input and returns a list of tokens extracted. '''
		return [_input]
		
	def filterToken(self, _token):
		''' Receives one token at a time. Must return True if the token is to be kept, False otherwise. '''
		return True
	
	def prepareToken(self, _token):
		''' Receives one token at a time. Must return a prepared/sanitized version of the token appropriate for resolving an index. '''
		return _token
		
	def expandToken(self, _token):
		''' Receives one token at a time. Must return a list of *additional items only* to be considered as values of the token. '''
		return (_token, [])
		
	def resolveIndex(self, _token):
		''' Receives one token at a time. Converts a token to a query or key of an index entry. Returning False aborts that entry. '''
		entry, values = _token
		return (entry, None, values)


	#### Low-Level Methods ####
	def _firstPhaseIter(self):
		for t in self.tokenizeInput(self.prepareInput(self.get_input())):
			yield t
	
	def _secondPhaseIter(self):
		for t, v in map(self.expandToken, map(self.prepareToken, filter(self.filterToken, self.get_input()))):
			yield (t, v)

	
	#### Mid-Level Methods ####
	def _entryListForValue(self, value=None):
		
		if value is None:
			if self.get_input() is None:
				raise exceptions.EmptyInput()
			else:
				value = self.get_input()
		else:
			self.set_input(value)
		
		self.set_input(self.tokenizeInput(self.prepareInput(self.get_input())))
		self.set_input([i for i in filter(self.filterToken, self.get_input())])
		self.set_input([i for i in map(self.prepareToken, self.get_input())])
		
		# 2: Expand tokens and resolve indexes
		self.set_input([(i, v) for i, v in map(self.expandToken, self.get_input())])
				
		return self.get_input()
		
	def _entryIterForValue(self, value=None):
		
		if value is None:
			if self.get_input() is None:
				raise exceptions.EmptyInput()
			else:
				value = self.get_input()
		else:
			self.set_input(value)
		
		# 1: Prepare & tokenize input, filter and prepare for expansion
		self.set_input([t for t in self._firstPhaseIter()])
		
		# 2: Iterate over second phase and yield
		for i in self._secondPhaseIter():
			yield i
		
		
	#### High-Level Methods ####
	def resolveIndexEntriesForValue(self, value=None):
		
		from momentum.fatcatmap.core.api.indexer import getModelImplClass
		
		if value is None:
			if self._getInput() is None:
				raise exceptions.EmptyInput()
			else:
				value = self._getInput()
		else:
			self.set_input(value)
			
		## Generate entries
		self.set_input([i for i in self._entryIterForValue()])
		
		## Resolve indexes
		self._setEntries([(e, i, v) for e, i, v in map(self.resolveIndex, self.get_input())])
				
		## Prepare, tokenize, filter, expand, resolve indexes & yield
		for entry, index, values in self._getEntries():

			if isinstance(entry, (n.Key, basestring)):
				yield getModelImplClass('entry', True)(value=entry, artifacts=values)

			elif isinstance(entry, q.Query):
				pass
				## @TODO: Implement resolution of queries returned during index entry generation