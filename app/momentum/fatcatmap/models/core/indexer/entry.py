from momentum.fatcatmap import models as m


class IndexEntryType(m.NDBModel):
	
	name = db.StringProperty()
	indexer = db.StringProperty(choices=['meta','organic','semantic','relation'])
	adapter = db.StringListProperty(default=['momentum','fatcatmap','core','api','indexer','adapters','DefaultEntryAdapter'])


class IndexEntry(m.NDBModel):

	type = m.ndb.KeyProperty()
	value = m.ndb.StringProperty(repeated=True)
	artifacts = m.ndb.StringProperty(repeated=True)