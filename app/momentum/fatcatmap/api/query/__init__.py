import ndb
from ndb import key
from ndb import model

from google.appengine.ext import db
from google.appengine.api import datastore
from google.appengine.api import datastore_types
from google.appengine.api import datastore_errors

from momentum.services import remote

from momentum.fatcatmap.api.data import DataAPIService

from momentum.fatcatmap.api.query import exceptions
from momentum.fatcatmap.api import FatCatMapAPIService

from momentum.fatcatmap.messages import data as Data
from momentum.fatcatmap.messages import query as Query


class QueryAPIService(FatCatMapAPIService):

	""" Remote Query API: Exposes a service for raw GQL and db/ndb.Query access. """

	## 1: Class Variables
	query = None
	cursors = None
	config_path = 'services.query.config'


	## 2: Internal Methods
	def buildQuery(self, query=None, filters=[], orders=[]):

		''' Build a query and prepare it to be run. '''

		pass

		
	def considerQueryOptions(self, options):

		''' Merge in a Query's options once it has been built. '''
		
		pass
		
		
	def catchQueryExceptions(self, callback, *args, **kwargs):
		
		''' Run a function and catch all relevant datastore errors. '''
		
		try:
			result = callback(*args, **kwargs)
			
		except datastore_errors.BadFilterError, e:
			raise exceptions.InvalidFilter(str(e))
			
		except datastore_errors.BadPropertyError, e:
			raise exceptions.InvalidProperty(str(e))
			
		except datastore_errors.BadArgumentError, e:
			raise exceptions.InvalidArgument(str(e))
			
		except datastore_errors.BadQueryError, e:
			raise exceptions.InvalidQuery(str(e))
			
		except datastore_errors.Error, e:
			raise exceptions.InternalQueryAPIException(str(e))
			
		else:
			return result
	
	
	## 3: Remote Methods
	@remote.method(Query.SearchRequest, Query.SearchResponse)
	def search(self, request):
		pass
		
	@remote.method(Query.QueryRequest, Query.QueryResponse)
	def query(self, request):
		pass
		
	@remote.method(Query.GQLRequest, Query.QueryResponse)
	def gql(self, request):

		if request.gql is not None:
			
			options = {}
			gql_index = request.gql.split(' ')
			if gql_index[1] == '*':
				options['keys_only'] = False
				gql_index[1] = '__key__' ## we can't ever return full models using GQL...
			else:
				options['keys_only'] = True
				
			matching_keys = self.catchQueryExceptions(db.GqlQuery, ' '.join(gql_index))


			compiled_objects = []
			if options['keys_only'] is False:
				records = datastore.Get(records)
				for key, record in zip(matching_keys, records):
					if isinstance(record, datastore.Entity):
						parent = key.parent()
						if parent is not None:
							parent = str(parent)
						k_key = Data.DatastoreKey(encoded=str(key), parent=parent)
						k_object = Data.DatastoreObject(key=k_key)
						compiled_objects.append(DataAPIService.convert_entity_to_message(record, k_object))
					elif key is None:
						compiled_objects.append(None)					
			else:
				for key in matching_keys:
					if isinstance(key, db.Key):
						parent = key.parent()
						if parent is not None:
							parent = str(parent)
						k_key = Data.DatastoreKey(encoded=str(key), parent=parent)
						compiled_objects.append(Data.DatastoreObject(key=key))
					elif key is None:
						compiled_objects.append(None)
			
			return Query.QueryResponse(results=Query.QueryResults(objects=compiled_objects, count=len(compiled_objects)))
			
		else:
			raise exceptions.EmptyGQL("Must provide a GQL string to execute.")
		
	@remote.method(Query.AutocompleteRequest, Query.AutocompleteResponse)
	def autocomplete(self, request):
		pass