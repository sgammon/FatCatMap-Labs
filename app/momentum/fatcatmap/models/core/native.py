from momentum.fatcatmap import models as m


class Native(m.NDBModel):

	node = m.ndb.KeyProperty()
	native = m.ndb.KeyProperty(repeated=True)
	current_version = m.ndb.KeyProperty()
	
	
class EdgeNative(m.NDBModel):
	
	edge = m.ndb.KeyProperty()
	native = m.ndb.KeyProperty(repeated=True)
	current_version = m.ndb.KeyProperty()