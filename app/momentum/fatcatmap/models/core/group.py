from momentum.fatcatmap import models as m
from momentum.fatcatmap.models.schema import Schema


class Group(m.NDBModel):
	schema = m.ndb.KeyProperty()