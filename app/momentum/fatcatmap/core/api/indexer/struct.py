from ndb import model as ndb
from google.appengine.ext import db as ldb
from ProvidenceClarity.struct.simple import SimpleStruct


class Entry(SimpleStruct):

	''' Represents a value in an index that can be mapped to datastore keys. '''

	value = list, str
	artifacts = list, str
	

class Meta(SimpleStruct):

	''' Represents an IndexMeta, which accounts for the number of times and calculated score of an artifact in an indexed target. '''

	count = int
	score = float
	attribute = str
	
	
class Mapping(SimpleStruct):

	''' Represents a mapping from an IndexEntry to a datastore key, along with meta information about the entry-key relation. '''

	entry = Entry
	value = ndb.Key, ldb.Key
	meta = list, Meta