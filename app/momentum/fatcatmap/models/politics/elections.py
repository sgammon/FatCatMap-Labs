from momentum.fatcatmap import models as m


class ElectionCycle(m.FCMModel):
    presidential_election = m.db.BooleanProperty(default=False)