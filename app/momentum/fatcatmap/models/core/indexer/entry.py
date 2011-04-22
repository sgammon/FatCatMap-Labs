from momentum.fatcatmap import models as m


class IndexEntryType(m.NDBModel):
	
	# default=['momentum','fatcatmap','core','api','indexer','adapters','DefaultEntryAdapter']
	
	name = m.ndb.StringProperty()
	indexer = m.ndb.StringProperty(choices=['meta','organic','semantic','relation'], default='organic')
	adapter = m.ndb.StringProperty(repeated=True)


class IndexEntry(m.NDBModel):

	type = m.ndb.KeyProperty()
	value = m.ndb.StringProperty(repeated=True)
	artifacts = m.ndb.StringProperty(repeated=True)