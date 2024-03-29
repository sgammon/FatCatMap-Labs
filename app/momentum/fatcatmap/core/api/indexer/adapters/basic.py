import string
from momentum.fatcatmap.core.api.indexer.util import NLTKGateway
from momentum.fatcatmap.core.api.indexer.adapter import IndexAdapter


class StringIndexer(IndexAdapter):

	def prepareInput(self, _input):
		''' Receives input and sanitizes/prepares it to be tokenized and otherwise processed. '''
		return unicode(_input).lower()
	
	def tokenizeInput(self, _input):
		''' Receives prepared input and returns a list of tokens extracted. '''
		return [t for t in NLTKGateway().word_tokenizer.tokenize(_input)]
		
	def filterToken(self, _token):
		''' Receives one token at a time. Must return True if the token is to be kept, False otherwise. '''
		return len(_token) > 3
	
	def prepareToken(self, _token):
		''' Receives one token at a time. Must return a prepared/sanitized version of the token appropriate for resolving an index. '''
		return reduce(lambda x, y: x+y, [char for char in filter(lambda c: c not in string.punctuation, _token)])
		
	def expandToken(self, _token):
		''' Receives one token at a time. Must return a list of *additional items only* to be considered as values of the token. '''
		return (_token, [NLTKGateway().stemmer.stem(_token)])
		
	def resolveIndex(self, _token):
		''' Receives one token at a time. Converts a token to a query or key of an index entry. Returning False aborts that entry. '''
		entry, values = _token
		return (entry, entry, values)



class NumericIndexer(IndexAdapter):

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

	
	
class DateTimeIndexer(IndexAdapter):

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