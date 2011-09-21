from momentum.fatcatmap import models as m

from momentum.fatcatmap.models.core import object as o
from momentum.fatcatmap.models.core import relation as r


class ConstructedGraph(m.NDBModel):
	
	origin = m.ndb.KeyProperty()
	limit = m.ndb.IntegerProperty()
	degree = m.ndb.IntegerProperty()
	
	nodes = m.ndb.LocalStructuredProperty(o.Node, repeated=True)
	edges = m.ndb.LocalStructuredProperty(r.Edge, repeated=True)
	hints = m.ndb.LocalStructuredProperty(r.EdgeHint, repeated=True)