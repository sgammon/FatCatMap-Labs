from momentum.fatcatmap import models as m

from momentum.fatcatmap.models.core.geo import Boundary


class USState(Boundary):
    fullname = m.db.StringProperty()
    abbreviation = m.db.StringProperty()


class District(Boundary):
    state = m.db.ReferenceProperty(USState, collection_name='districts')