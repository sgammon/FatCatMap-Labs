from momentum.fatcatmap import models as m


class Vector(m.NDBModel):
	objects = m.ndb.KeyProperty(repeated=True)
	score = m.ndb.FloatProperty()
	hints = m.ndb.KeyProperty(repeated=True)
	
	
class EdgeType(m.NDBModel):
	name = m.ndb.StringProperty()
	schema = m.ndb.KeyProperty()
	
	
class Edge(m.NDBModel):
	source = m.ndb.KeyProperty()
	target = m.ndb.KeyProperty()
	score = m.ndb.FloatProperty()
	type = m.ndb.KeyProperty()
	

class EdgeItem(m.NDBModel):
	edges = m.ndb.KeyProperty(repeated=True)
	score = m.ndb.FloatProperty()
	
	
class EdgeHint(m.NDBModel):
	node = m.ndb.KeyProperty()
	edges = m.ndb.KeyProperty(repeated=True)