from momentum.fatcatmap import models as m

from momentum.fatcatmap.models.politics.party import PoliticalParty
from momentum.fatcatmap.models.government.boundaries import USState
from momentum.fatcatmap.models.government.boundaries import District
	

#### ==== Legislature Models ==== ####
class Legislature(m.FCMPolyModel):
    name = m.db.StringProperty()
    short_name = m.db.StringProperty()
    total_members = m.db.IntegerProperty()

class StateLegislature(Legislature):
    state = m.db.ReferenceProperty(USState, collection_name='legislature')


#### ==== Legislative House Models ==== ####
class LegislativeChamber(m.FCMPolyModel):
    name = m.db.StringProperty()
    short_name = m.db.StringProperty()
    title_abbr = m.db.StringProperty()
    legislature = m.db.ReferenceProperty(Legislature, collection_name='houses')
    total_members = m.db.IntegerProperty()

class UpperLegislativeChamber(LegislativeChamber):
    pass

class LowerLegislativeChamber(LegislativeChamber):
    pass


#### ==== District/Seat Models ==== ####
class UpperChamberDistrict(District):
    seniority = m.db.StringProperty(choices=['junior','senior'])
    chamber = m.db.ReferenceProperty(UpperLegislativeChamber, collection_name='districts')

class LowerChamberDistrict(District):
    number = m.db.IntegerProperty()
    chamber = m.db.ReferenceProperty(LowerLegislativeChamber, collection_name='districts')


#### ==== Legislator ==== ####
class Legislator(m.FCMPolyModel):
	office = m.db.PostalAddressProperty()
	in_office = m.db.BooleanProperty()
	webform = m.db.StringProperty()
	website = m.db.StringProperty()
	fax = m.db.PhoneNumberProperty()
	phone = m.db.PhoneNumberProperty()
	district = m.db.ReferenceProperty(District, collection_name='legislators')	
	party = m.db.ReferenceProperty(PoliticalParty, collection_name='legislators')
	chamber = m.db.ReferenceProperty(LegislativeChamber, collection_name='legislators')

class StateLegislator(Legislator):
	state = m.db.ReferenceProperty(USState, collection_name='state_legislators')