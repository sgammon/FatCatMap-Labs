from momentum.fatcatmap import models as m
from momentum.fatcatmap.models.schema import Schema


class Object(m.NDBModel):
	schema = m.ndb.KeyProperty()
	
	
class Node(m.NDBModel):
	label = m.ndb.StringProperty()
	scope = m.ndb.StringProperty(repeated=True)
	schema = m.ndb.KeyProperty()