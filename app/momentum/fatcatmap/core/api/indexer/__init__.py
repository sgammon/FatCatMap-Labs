import logging
import datetime as dt

from ndb import query as q
from ndb import model as n
from ndb import context as c
from ndb import tasklets as t

from google.appengine.ext import db as ldb

# P/C Imports
from ProvidenceClarity.struct.util import DictProxy
from ProvidenceClarity.struct.util import ObjectProxy
from ProvidenceClarity.struct.util import ConfigurableStruct

# FCM Core Imports
from momentum.fatcatmap.core.api import MomentumCoreAPI

# Indexer API Imports
from momentum.fatcatmap.core.api.indexer import adapters
from momentum.fatcatmap.core.api.indexer import exceptions
from momentum.fatcatmap.core.api.indexer.struct import Meta
from momentum.fatcatmap.core.api.indexer.struct import Entry
from momentum.fatcatmap.core.api.indexer.struct import Mapping
from momentum.fatcatmap.core.api.indexer.struct import EntryType

# Indexer Model Imports
from momentum.fatcatmap.models.core.indexer.map import IndexMapping
from momentum.fatcatmap.models.core.indexer.map import IndexMappingMeta
from momentum.fatcatmap.models.core.indexer.entry import IndexEntry
from momentum.fatcatmap.models.core.indexer.entry import IndexEntryType


# === Global Cache === #
_indexer_cache = {'read':[], 'write':[], 'delete':[]}


# ==== Type to Indexer Mappings ==== #
_types = ObjectProxy({

	str: adapters.basic.StringIndexer,
	int: adapters.basic.NumericIndexer,
	n.Key: adapters.datastore.KeyIndexer,
	ldb.Key: adapters.datastore.KeyIndexer,
	dt.date: adapters.datetime.DateTimeIndexer,
	dt.time: adapters.datetime.DateTimeIndexer,
	dt.datetime: adapters.datetime.DateTimeIndexer

})


# ==== Indexing-Related Models & Structures ==== #
_models = DictProxy({

	'meta': (Meta, IndexMappingMeta),
	'entry': (Entry, IndexEntry),
	'mapping': (Mapping, IndexMapping),
	'entry_type': (EntryType, IndexEntryType)

})

def getModelImplClass(name, struct=False):
	global _models
	if name in _models:
		struct, impl_class = _models[name]
		if struct:
			return struct
		return impl_class
	else:
		raise KeyError
				

# ==== Programmatic Indexer Interface ==== #
class IndexerAPI(MomentumCoreAPI, ConfigurableStruct):

	''' @todo: prettify this block
		FatCatMap Indexer API:
			
			Author: Sam Gammon <sam@momentum.io>
			
			This class is instantiated to access the Core Indexer API, which specifies
			procedures for generating indexes for arbitrary, complex input data suitable
			for storage in the datastore or memcache.
	'''
	
	_adapter = None
	_objects = {}
	_read_cache = []	
	_write_cache = []
	_delete_cache = []
	
	### Utility Methods ###
	def __init__(self, *args, **kwargs):

		''' Indexer API initiation. '''

		# Pull in runtime-level cache
		global _indexer_cache
		
		# Set basic properties, initialize cache from previous requests
		self._adapter = None
		self._read_cache = _indexer_cache.get('read', [])
		self._write_cache = _indexer_cache.get('write', [])
		self._delete_cache = _indexer_cache.get('delete', [])
		
		super(IndexerAPI, self).__init__(*args, **kwargs)
	
	def _loadAdapter(self, _type, force=False):
		
		''' Loads the appropriate IndexAdapter according to the type or value passed in. '''

		global _types
		if self._adapter is None or force is True:
			logging.info('---Loading adapter for type: '+str(_type))
			if _type in _types:
				self._adapter = _types[_type]()
			logging.info('---Loaded adapter: '+str(self._adapter))
		return self._adapter
	
	@t.tasklet
	def _commit(self):
		
		''' Commits the mutation table to the index map (writes and deletes are actually performed). '''
		
		pass

	def _flushDatastoreCaches(self):
		
		''' Clear the runtime-level and object-level CRUD caches. '''

		# Flush runtime-level cache
		global _indexer_cache
		_indexer_cache = {'read':[], 'write':[], 'delete':[]}
		
		# Flush object-level cache
		self._read_cache = []
		self._write_cache = []
		self._delete_cache = []
		
		return
	
	
	### Low-Level Methods ###
	@tasklet.tasklet
	def _findIndexEntry(self, key=None, key_name=None, value=None, **kwargs):
		
		''' Find an index entry according to key, key name, value, or any other model property. '''
		pass
		
	def _tokensForValue(self, value):
		
		''' Processes a value with an Indexer class to resolve indexes the value should be mapped to. '''
		
		adapter = self.loadAdapter(type(value))
		for entry in adapter.resolveIndexEntriesForValue():
			yield entry

	def _createIndexEntry(self):
		
		''' Create an index entry for a given principal and value. '''
		
		pass
		
	def _findIndexMapping(self):
		
		''' Find an index mapping according to entry key and target key. '''
		
		pass
		
	def _createIndexMapping(self):
		
		''' Create a mapping between a given key and an index entry. '''
		
		pass

	def _findIndexMeta(self):
		
		''' Find meta information for an index, index entry, or index mapping. '''
		
		pass
		
	def _createIndexMeta(self):
		
		''' Create a meta information record for an index, index entry, or index mapping. '''
		
		pass
		
		
	### Mid-Level Methods ###
	def _resolveIndexEntry(self):
		
		''' Find or create an index entry by principal and value. '''
		
		pass
		
	def _resolveIndexMapping(self):
		
		''' Find or create an index mapping by entry key and target key. '''
		
		pass
		
	def _resolveIndexMeta(self):
		
		''' Find or create an index/entry/mapping meta by parent key. '''
		
		pass
	
	
	### High-Level Methods ###
	def writeIndexMapping(self, target, entry):
		
		''' Write a mapping between one entry and one target. '''
		
		pass
		
	def writeIndexMap(self, target, entries):

		''' Write a mapping between a target key and a list of appropriate index entries. '''

		pass
		
	def commit(self):
		
		''' Save buffered datastore deletes and writes to BigTable. '''
		
		pass
		
	def mapIndexesForValue(self, value):
		
		'''  '''
		
		pass