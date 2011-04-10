from momentum.fatcatmap import models as m


class IndexMappingMeta(m.NDBModel):
	
	score = m.ndb.FloatProperty()
	count = m.ndb.IntegerProperty()
	property = m.ndb.StringProperty()


class IndexMapping(m.NDBModel):

	entry = m.ndb.KeyProperty()
	value = m.ndb.KeyProperty()
 	meta = m.ndb.StructuredProperty(IndexMappingMeta, repeated=True)