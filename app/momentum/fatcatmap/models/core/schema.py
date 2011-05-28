from momentum.fatcatmap import models as m


class Property(m.NDBModel):
	name = m.ndb.StringProperty()
	type = m.ndb.StringProperty(choices=m.property_classes(True))


class Schema(m.NDBModel):
	type = m.ndb.KeyProperty(choices=['node', 'edge', 'object'])
	path = m.ndb.StringProperty(repeated=True)
	properties = m.ndb.StructuredProperty(Property, repeated=True)