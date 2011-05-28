import logging
import inspect
import ndb
from ndb import model
from ndb import key as k
from google.appengine.ext import db


def add_prototypes():
	return []

def add_graph_artifact_types():

	from momentum.fatcatmap.models.core.schema import Schema
	from momentum.fatcatmap.models.core.schema import Property

	from momentum.fatcatmap.models.core.object import NodeType
	from momentum.fatcatmap.models.core.object import ObjectType

	from momentum.fatcatmap.models.core.relation import EdgeType

	## Models to put
	schemas = []
	properties = []
	node_types = []
	edge_types = []
	object_types = []


	########## Object Types ##########
	
	##### Person

	## Schema
	person = Schema(key=k.Key('Schema','object.natural.Person'), path=['object', 'natural', 'Person'], type='object')
	person.put()

	## Properties
	properties.append(Property(key=k.Key('Property', 'firstname', parent=person.key), type='StringProperty'))
	properties.append(Property(key=k.Key('Property', 'lastname', parent=person.key), type='StringProperty'))
	properties.append(Property(key=k.Key('Property', 'gender', parent=person.key), type='StringProperty'))
	properties.append(Property(key=k.Key('Property', 'date_of_birth', parent=person.key), type='DateProperty'))
	properties.append(Property(key=k.Key('Property', 'date_of_death', parent=person.key), type='DateProperty'))
	person.put()
		
	## Object Type
	person_object = ObjectType(key=k.Key('ObjectType', 'natural.Person'), name='Person', schema=k.Key('Schema', 'object.natural.Person'))
	person_object.put()
	
	## Node Types
	node_types.append(NodeType(key=k.Key('NodeType', 'natural.Person', parent=person_object.key), name='Person', schema=person.key, object_type=k.Key('ObjectType', 'object.natural.Person'), scope=['natural']))
	

	########## Relation Types ##########
	
	##### Friendship
	
	## Schema
	friendship = Schema(key=k.Key('Schema', 'relation.social.Friendship'), path=['relation', 'social', 'Friendship'], type='edge')
	friendship.put()
	
	## Edge Type
	edge_types.append(EdgeType(key=k.Key('EdgeType', 'social.Friendship'), name='Friendship', schema=friendship.key))
	

	keys = []
	batches_to_put = [schemas, properties, node_types, edge_types, object_types]
	for batch in batches_to_put:
		keys.extend(model.put_multi(batch))
	return keys

def add_services():

	from momentum.fatcatmap.models.core.services import ExtService
	from momentum.fatcatmap.models.core.services import ExtServiceKey

	## Sunlight Labs
	sunlight = ExtService(key_name='sunlight')
	sunlight.name = 'Sunlight Labs'
	sunlight.description = 'Non-profit providing data about legislators, committees and committee memberships, and districts.'
	sunlight.homepage = 'http://www.sunlightlabs.com'
	sunlight.put()

	## OpenSecrets
	opensecrets = ExtService(key_name='opensecrets')
	opensecrets.name = 'CRP OpenSecrets'
	opensecrets.description = 'Non-profit providing data about contributions, lobbying, and spending.'
	opensecrets.homepage = 'http://www.opensecrets.org'
	opensecrets.put()

	## Sunlight/OpenSecrets Keys
	models = []
	models.append(ExtServiceKey(sunlight, service=sunlight, key_name='s@providenceclarity.com', name='s@providenceclarity.com', value='5716fd8eb1ce418095fe402c7489281e', enforce_limits=False))
	models.append(ExtServiceKey(opensecrets, service=opensecrets, key_name='s@providenceclarity.com', name='s@providenceclarity.com', value='254615061689494a6ef579d65d08fb70', enforce_limits=False))

	## Other Political Services
	models.append(ExtService(key_name='bioguide', name='BioGuide', homepage='http://bioguide.congress.gov/', description='Official bio information for members of Congress.'))
	models.append(ExtService(key_name='votesmart', name='VoteSmart', homepage='http://www.votesmart.org/', description='Non-profit Project VoteSmart provides diverse information about legislators and political actions.'))
	models.append(ExtService(key_name='fec', name='Federal Elections Commission', homepage='http://www.fec.gov/', description='US Federal Elections Commission.'))
	models.append(ExtService(key_name='govtrack', name='Govtrack', homepage='http://www.govtrack.us/', description='Non-profit GovTrack provides information about legislation and legislative actions.'))
	models.append(ExtService(key_name='eventful', name='Eventful', homepage='http://www.eventful.com/', description='Eventful provides information about local events.'))
	models.append(ExtService(key_name='congresspedia', name='Congresspedia', homepage='http://www.opencongress.org/', description='OpenCongress provides wiki-style information about legislators and political actions.'))
	models.append(ExtService(key_name='twitter', name='Twitter', homepage='http://www.twitter.com/', description='Social micro-blogging service.'))
	models.append(ExtService(key_name='youtube', name='YouTube', homepage='http://www.youtube.com/', description='Social video-sharing service.'))
	models.append(ExtService(key_name='facebook', name='Facebook', homepage='http://www.facebook.com', description='Social interaction service.'))
	models.append(ExtService(key_name='freebase', name='Freebase', homepage='http://www.freebase.com/', description='An open graph of information.'))
	models.append(ExtService(key_name='wikipedia', name='Wikipedia', homepage='http://www.wikipedia.org', description='An open, wiki-style database of information.'))
	models.append(ExtService(key_name='opencalais', name='OpenCalais', homepage='http://www.opencalais.com', description='A service that converts plaintext to structured and linked data.'))
	models.append(ExtService(key_name='googlenews', name='Google News', homepage='http://news.google.com', description='Aggregates news stories and publications from journalistic organizations.'))
	models.append(ExtService(key_name='uscongress', name='U.S. Congress', homepage='http://www.congress.gov', description='Official website of the US Congress.'))
	models.append(ExtService(key_name='ussenate', name='U.S. Senate', homepage='http://www.senate.gov', description='Official website of the US Senate.'))
	models.append(ExtService(key_name='ushouse', name='U.S. House of Representatives', homepage='http://www.house.gov', description='Official website of the US House of Representatives.'))

	return db.put(models)+[sunlight, opensecrets]



def add_data_engines():

	from momentum.fatcatmap.models.core.services import ServiceWorker
	from momentum.fatcatmap.models.core.services import WorkerMethod
	from momentum.fatcatmap.models.core.services import ExtService
	from momentum.fatcatmap.models.core.services import ServicePipeline

	sunlight_service = ExtService.get_by_key_name('sunlight')
	opensecrets_service = ExtService.get_by_key_name('opensecrets')

	sunlight = ServiceWorker(key_name='sunlight', name='Sunlight Labs', worker_endpoint='worker-sunlight', service=sunlight_service, enabled=True)
	opensecrets = ServiceWorker(key_name='opensecrets', name='CRP OpenSecrets', worker_endpoint='worker-opensecrets', service=opensecrets_service, enabled=False)

	models = []
	models.append(WorkerMethod(sunlight, key_name='getLegislator', name='getLegislator', service=sunlight))
	models.append(WorkerMethod(sunlight, key_name='getLegislators', name='getLegislators', service=sunlight))

	models.append(ServicePipeline(sunlight_service, key_name='Legislator', name='Get Single Legislator', async=True, service=sunlight_service, enabled=True))
	models.append(ServicePipeline(sunlight_service, key_name='Legislators', name='Get Legislators List', service=sunlight_service, enabled=True))

	models.append(ServicePipeline(sunlight_service, key_name='Committee', name='Get Single Legislative Committee', async=True, service=sunlight_service, enabled=True))
	models.append(ServicePipeline(sunlight_service, key_name='Committees', name='Get Legislative Committees List', service=sunlight_service, enabled=True))

	return db.put(models)+[sunlight, opensecrets]



def add_political_parties():

	from momentum.fatcatmap.models.politics.party import PoliticalParty

	models = []
	models.append(PoliticalParty(key_name='D', name='Democratic Party', plural='Democrats', singular='Democrat'))
	models.append(PoliticalParty(key_name='R', name='Republican Party', plural='Republicans', singular='Republican'))
	models.append(PoliticalParty(key_name='I', name='Independent Party', plural='Independents', singular='Independent'))

	return db.put(models)


def add_election_cycles():

	from momentum.fatcatmap.models.politics.elections import ElectionCycle

	models = []
	models.append(ElectionCycle(key_name='2008', presidential_election=True))
	models.append(ElectionCycle(key_name='2010'))
	models.append(ElectionCycle(key_name='2012', presidential_election=True))

	return db.put(models)



def add_federal_legislature():

	from momentum.fatcatmap.models.government.legislative import Legislature
	from momentum.fatcatmap.models.government.legislative import LowerLegislativeChamber
	from momentum.fatcatmap.models.government.legislative import UpperLegislativeChamber

	models = []
	congress = Legislature(key_name='us_congress',name='United States Congress', short_name='Congress', total_members=535).put()
	models.append(LowerLegislativeChamber(congress, legislature=congress, title_abbr='Rep', key_name='us_house_of_reps', name='United States House of Representatives', short_name='House of Representatives', total_members=435))
	models.append(UpperLegislativeChamber(congress, legislature=congress, title_abbr='Sen', key_name='us_senate', name='United States Senate', short_name='Senate', total_members=100))

	return db.put(models)+[congress]


def add_states():

	from momentum.fatcatmap.models.government.boundaries import USState

	models = []
	models.append(USState(key_name="AL",abbreviation="AL",fullname="Alabama",primary_display_text="Alabama",display_text=["AL","Alabama"]))
	models.append(USState(key_name="AK",abbreviation="AK",fullname="Alaska",primary_display_text="Alaska",display_text=["AK","Alaska"]))
	models.append(USState(key_name="AZ",abbreviation="AZ",fullname="Arizona",primary_display_text="Arizona",display_text=["AZ","Arizona"]))
	models.append(USState(key_name="AR",abbreviation="AR",fullname="Arkansas",primary_display_text="Arkansas",display_text=["AR","Arkansas"]))
	models.append(USState(key_name="CA",abbreviation="CA",fullname="California",primary_display_text="California",display_text=["CA","California"]))
	models.append(USState(key_name="CO",abbreviation="CO",fullname="Colorado",primary_display_text="Colorado",display_text=["CO","Colorado"]))
	models.append(USState(key_name="CT",abbreviation="CT",fullname="Connecticut",primary_display_text="Connecticut",display_text=["CT","Connecticut"]))
	models.append(USState(key_name="DE",abbreviation="DE",fullname="Delaware",primary_display_text="Delaware",display_text=["DE","Delaware"]))
	models.append(USState(key_name="FL",abbreviation="FL",fullname="Florida",primary_display_text="Florida",display_text=["FL","Florida"]))
	models.append(USState(key_name="GA",abbreviation="GA",fullname="Georgia",primary_display_text="Georgia",display_text=["GA","Georgia"]))
	models.append(USState(key_name="HI",abbreviation="HI",fullname="Hawaii",primary_display_text="Hawaii",display_text=["HI","Hawaii"]))
	models.append(USState(key_name="ID",abbreviation="ID",fullname="Idaho",primary_display_text="Idaho",display_text=["ID","Idaho"]))
	models.append(USState(key_name="IL",abbreviation="IL",fullname="Illinois",primary_display_text="Illinois",display_text=["IL","Illinois"]))
	models.append(USState(key_name="IN",abbreviation="IN",fullname="Indiana",primary_display_text="Indiana",display_text=["IN","Indiana"]))
	models.append(USState(key_name="IA",abbreviation="IA",fullname="Iowa",primary_display_text="Iowa",display_text=["IA","Iowa"]))
	models.append(USState(key_name="KS",abbreviation="KS",fullname="Kansas",primary_display_text="Kansas",display_text=["KS","Kansas"]))
	models.append(USState(key_name="KY",abbreviation="KY",fullname="Kentucky",primary_display_text="Kentucky",display_text=["KY","Kentucky"]))
	models.append(USState(key_name="LA",abbreviation="LA",fullname="Louisiana",primary_display_text="Louisiana",display_text=["LA","Louisiana"]))
	models.append(USState(key_name="ME",abbreviation="ME",fullname="Maine",primary_display_text="Maine",display_text=["ME","Maine"]))
	models.append(USState(key_name="MD",abbreviation="MD",fullname="Maryland",primary_display_text="Maryland",display_text=["MD","Maryland"]))
	models.append(USState(key_name="MA",abbreviation="MA",fullname="Massachusetts",primary_display_text="Massachusetts",display_text=["MA","Massachusetts"]))
	models.append(USState(key_name="MI",abbreviation="MI",fullname="Michigan",primary_display_text="Michigan",display_text=["MI","Michigan"]))
	models.append(USState(key_name="MN",abbreviation="MN",fullname="Minnesota",primary_display_text="Minnesota",display_text=["MN","Minnesota"]))
	models.append(USState(key_name="MS",abbreviation="MS",fullname="Mississippi",primary_display_text="Mississippi",display_text=["MS","Mississippi"]))
	models.append(USState(key_name="MO",abbreviation="MO",fullname="Missouri",primary_display_text="Missouri",display_text=["MO","Missouri"]))
	models.append(USState(key_name="MT",abbreviation="MT",fullname="Montana",primary_display_text="Montana",display_text=["MT","Montana"]))
	models.append(USState(key_name="NE",abbreviation="NE",fullname="Nebraska",primary_display_text="Nebraska",display_text=["NE","Nebraska"]))
	models.append(USState(key_name="NV",abbreviation="NV",fullname="Nevada",primary_display_text="Nevada",display_text=["NV","Nevada"]))
	models.append(USState(key_name="NH",abbreviation="NH",fullname="New Hampshire",primary_display_text="New Hampshire",display_text=["NH","New Hampshire"]))
	models.append(USState(key_name="NJ",abbreviation="NJ",fullname="New Jersey",primary_display_text="New Jersey",display_text=["NJ","New Jersey"]))
	models.append(USState(key_name="NM",abbreviation="NM",fullname="New Mexico",primary_display_text="New Mexico",display_text=["NM","New Mexico"]))
	models.append(USState(key_name="NY",abbreviation="NY",fullname="New York",primary_display_text="New York",display_text=["NY","New York"]))
	models.append(USState(key_name="NC",abbreviation="NC",fullname="North Carolina",primary_display_text="North Carolina",display_text=["NC","North Carolina"]))
	models.append(USState(key_name="ND",abbreviation="ND",fullname="North Dakota",primary_display_text="North Dakota",display_text=["ND","North Dakota"]))
	models.append(USState(key_name="OH",abbreviation="OH",fullname="Ohio",primary_display_text="Ohio",display_text=["OH","Ohio"]))
	models.append(USState(key_name="OK",abbreviation="OK",fullname="Oklahoma",primary_display_text="Oklahoma",display_text=["OK","Oklahoma"]))
	models.append(USState(key_name="OR",abbreviation="OR",fullname="Oregon",primary_display_text="Oregon",display_text=["OR","Oregon"]))
	models.append(USState(key_name="PA",abbreviation="PA",fullname="Pennsylvania",primary_display_text="Pennsylvania",display_text=["PA","Pennsylvania"]))
	models.append(USState(key_name="RI",abbreviation="RI",fullname="Rhode Island",primary_display_text="Rhode Island",display_text=["RI","Rhode Island"]))
	models.append(USState(key_name="SC",abbreviation="SC",fullname="South Carolina",primary_display_text="South Carolina",display_text=["SC","South Carolina"]))
	models.append(USState(key_name="SD",abbreviation="SD",fullname="South Dakota",primary_display_text="South Dakota",display_text=["SD","South Dakota"]))
	models.append(USState(key_name="TN",abbreviation="TN",fullname="Tennessee",primary_display_text="Tennessee",display_text=["TN","Tennessee"]))
	models.append(USState(key_name="TX",abbreviation="TX",fullname="Texas",primary_display_text="Texas",display_text=["TX","Texas"]))
	models.append(USState(key_name="UT",abbreviation="UT",fullname="Utah",primary_display_text="Utah",display_text=["UT","Utah"]))
	models.append(USState(key_name="VT",abbreviation="VT",fullname="Vermont",primary_display_text="Vermont",display_text=["VT","Vermont"]))
	models.append(USState(key_name="VA",abbreviation="VA",fullname="Virginia",primary_display_text="Virginia",display_text=["VA","Virginia"]))
	models.append(USState(key_name="WA",abbreviation="WA",fullname="Washington",primary_display_text="Washington",display_text=["WA","Washington"]))
	models.append(USState(key_name="WV",abbreviation="WV",fullname="West Virginia",primary_display_text="West Virginia",display_text=["WV","West Virginia"]))
	models.append(USState(key_name="WI",abbreviation="WI",fullname="Wisconsin",primary_display_text="Wisconsin",display_text=["WI","Wisconsin"]))
	models.append(USState(key_name="WY",abbreviation="WY",fullname="Wyoming",primary_display_text="Wyoming",display_text=["WY","Wyoming"]))

	return db.put(models)


all_functions = [add_prototypes, add_services, add_data_engines, add_political_parties, add_election_cycles, add_federal_legislature, add_states, add_graph_artifact_types]