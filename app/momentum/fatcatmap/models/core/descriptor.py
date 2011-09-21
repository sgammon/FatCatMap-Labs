from momentum.fatcatmap import models as m


class Descriptor(m.FCMPolyModel):

	ttl = None

	target = m.ldb.StringProperty()

	stale = m.ldb.BooleanProperty(default=False)
	created = m.ldb.DateTimeProperty(auto_now_add=True)
	modified = m.ldb.DateTimeProperty(auto_now=True)