import datetime as dt
from ndb import model as ndb
from google.appengine.ext import db as ldb

# P/C Imports
from ProvidenceClarity.struct.util import ObjectProxy
from ProvidenceClarity.struct.util import ConfigurableStruct

# FCM Core Imports
from momentum.fatcatmap.core.api import MomentumCoreAPI

# Indexer API Imports
from momentum.fatcatmap.core.api.indexer import types as t
from momentum.fatcatmap.core.api.indexer.struct import Meta
from momentum.fatcatmap.core.api.indexer.struct import Entry
from momentum.fatcatmap.core.api.indexer.struct import Mapping


# ==== Type to Indexer Mappings ==== #
_types = ObjectProxy({

	str: t.basic.StringIndexingAdapter,
	int: t.basic.NumericIndexingAdapter,
	ndb.Key: t.datastore.KeyIndexingAdapter,
	ldb.Key: t.datastore.KeyIndexingAdapter,
	dt.date: t.datetime.DateTimeIndexingAdapter,
	dt.time: t.datetime.DateTimeIndexingAdapter,
	dt.datetime: t.datetime.DateTimeIndexingAdapter,

})


# ==== Indexing Operation Interface ==== #
class IndexingAdapter(ConfigurableStruct):

	''' @todo: prettify this block
		FatCatMap Indexer:
		
			Author: Sam Gammon <sam@momentum.io>
		
			This class serves as an abstract parent class and interface specification for
			type-specific indexing operations. Type-based subclasses (like StringIndexer)
			from the m.f.core.api.indexer.types module extend this class.
	'''
	
	def __init__(self, *args, **kwargs):
		super(Indexer, self).__init__(*args, **kwargs)
		
	
		

# ==== Programmatic Indexer Interface ==== #
class IndexerAPI(MomentumCoreAPI):

	''' @todo: prettify this block
		FatCatMap Indexer API:
			
			Author: Sam Gammon <sam@momentum.io>
			
			This class is instantiated to access the Core Indexer API, which specifies
			procedures for generating indexes for arbitrary, complex input data suitable
			for storage in the datastore or memcache.
	'''
	
	def __init__(self, *args, **kwargs):
		super(IndexerAPI, self).__init__(*args, **kwargs)