from ndb import model as ndb
from google.appengine.ext import db as ldb
from ProvidenceClarity.struct.simple import SimpleStruct


class EntryType(SimpleStruct):

	''' Represents a type of IndexEntry. '''

	name = basestring
	indexer = basestring
	adapter = basestring
	

class Entry(SimpleStruct):

	''' Represents a value in an index that can be mapped to datastore keys. '''

	value = basestring
	artifacts = list, basestring
	

class Meta(SimpleStruct):

	''' Represents an IndexMeta, which accounts for the number of times and calculated score of an artifact in an indexed target. '''

	count = int
	score = float
	attribute = basestring
	
	
class Mapping(SimpleStruct):

	''' Represents a mapping from an IndexEntry to a datastore key, along with meta information about the entry-key relation. '''

	entry = Entry
	value = ndb.Key, ldb.Key
	meta = list, Meta