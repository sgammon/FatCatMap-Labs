from momentum.fatcatmap import models as m
from momentum.fatcatmap.models.schema import Schema


class Native(m.NDBModel):

	node = m.ndb.KeyProperty()
	native = m.ndb.KeyProperty(repeated=True)