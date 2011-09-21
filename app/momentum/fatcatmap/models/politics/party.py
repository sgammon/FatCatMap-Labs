from momentum.fatcatmap import models as m

class PoliticalParty(m.FCMModel):
	name = m.db.StringProperty()
	plural = m.db.StringProperty()
	singular = m.db.StringProperty()