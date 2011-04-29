# == NLTK Imports == #
from nltk.stem.porter import PorterStemmer
from nltk.tokenize.punkt import PunktWordTokenizer
from nltk.tokenize.punkt import PunktSentenceTokenizer

# == Module Cache == #
_stemmer = None
_word_tokenizer = None
_sentence_tokenizer = None


class NLTKGateway(object):
	
	''' Simple object-oriented gateway to NLTK assets. '''

	extensions = {
	
		'stemmer': (_stemmer, PorterStemmer),
		'word_tokenizer': (_word_tokenizer, PunktWordTokenizer),
		'sentence_tokenizer': (_sentence_tokenizer, PunktSentenceTokenizer)
	
	}

	def __init__(self, **kwargs):
		for name, value in self.extensions.items():
			_cached_global, extension = value
			if _cached_global is None:
				_cached_global = extension()
			setattr(self, name, _cached_global)