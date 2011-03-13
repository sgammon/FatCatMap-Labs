from momentum.fatcatmap import models as m


class ObjectType(m.NDBModel):
	name = m.ndb.StringProperty()
	schema = m.ndb.KeyProperty()


class Object(m.NDBModel):
	type = m.ndb.KeyProperty()
	last_modified = m.ndb.StringProperty()
	last_healthcheck = m.ndb.StringProperty()
	

class NodeType(m.NDBModel):
	name = m.ndb.StringProperty()
	schema = m.ndb.KeyProperty()
	object_type = m.ndb.KeyProperty()
	
	
class Node(m.NDBModel):
	type = m.ndb.KeyProperty()
	label = m.ndb.StringProperty()
	scope = m.ndb.StringProperty(repeated=True)