from momentum.fatcatmap import models as m


class Property(m.NDBModel):
	name = m.ndb.StringProperty()
	type = m.ndb.StringProperty(choices=m.property_classes(True))
	repeated = m.ndb.BooleanProperty(default=False)


class Schema(m.NDBModel):
	type = m.ndb.StringProperty(choices=['node', 'edge', 'object'])
	path = m.ndb.StringProperty(repeated=True)
	properties = m.ndb.LocalStructuredProperty(Property, repeated=True)
	artifact_types = m.ndb.KeyProperty(repeated=True)
	classpath = m.ndb.StringProperty()