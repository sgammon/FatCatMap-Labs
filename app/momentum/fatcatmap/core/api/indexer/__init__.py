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
	
	def _loadAdapter(self, type=None, value=None):
		
		''' Loads the appropriate IndexAdapter according to the type or value passed in. '''

		global _types
		if _type in _types:
			pass
	
	@t.tasklet
	def _commit(self):
		pass

	def _flushDatastoreCaches(self):

		# Flush runtime-level cache
		global _indexer_cache
		_indexer_cache = {'read':[], 'write':[], 'delete':[]}
		
		# Flush object-level cache
		self._read_cache = []
		self._write_cache = []
		self._delete_cache = []
		
		return
	
	
	### Low-Level Methods ###	
	def _findIndexEntry(self):
		pass

	def _createIndexEntry(self):
		pass
		
	def _findIndexMapping(self):
		pass
		
	def _createIndexMapping(self):
		pass

	def _findIndexMeta(self):
		pass
		
	def _createIndexMeta(self):
		pass
		
		
	### Mid-Level Methods ###
	def _resolveIndexEntry(self):
		pass
		
	def _resolveIndexMapping(self):
		pass
		
	def _resolveIndexMeta(self):
		pass
	
	
	### High-Level Methods ###
	def writeIndexMap(self, entries):
		pass
		
	def commit(self):
		pass
		
	def mapIndexesForValue(self, value):
		pass