from protorpc import messages

from momentum.fatcatmap.messages import data as Data
from momentum.services.core.fields.variant import VariantField


# ==== Query requests ==== #
class QueryOptions(messages.Message):

	## Query Config ##
	keys_only = messages.BooleanField(1, default=False)
	count_only = messages.BooleanField(2, default=False)
	ancestor = messages.StringField(3, default=None)
	deadline = messages.IntegerField(4, default=10)
	limit = messages.IntegerField(5, default=25)
	offset = messages.IntegerField(6, default=0)

	## Paging ##
	paging = messages.BooleanField(7, default=False)
	page = messages.IntegerField(8, default=1)
	items_per_page = messages.IntegerField(9, default=25)
	
	## Prefetching & Cursors ##
	prefetch = messages.BooleanField(10, default=False)
	cursors = messages.BooleanField(11, default=False)
	start_cursor = messages.StringField(12, default=None)
	end_cursor = messages.StringField(13, default=None)
	
	
class GQLRequest(messages.Message):

	gql = messages.StringField(1)
	options = messages.MessageField(QueryOptions, 2)	
	
	
class QueryRequest(messages.Message):
	
	class Filter(messages.Message):
		
		name = messages.StringField(1)
		
		class FilterOperator(messages.Enum):
			
			EQUALS = 1
			NOTEQUALS = 2
			GREATERTHAN = 3
			LESSTHAN = 4
		
		operator = messages.EnumField(FilterOperator, 2, repeated=True)
		value = VariantField(3)

	class Order(messages.Message):

		name = messages.StringField(1)

		class OrderDirectionOperator(messages.Enum):
		
			ASC = 1
			DSC = 2
			
		direction = messages.EnumField(OrderDirectionOperator, 2)
		
	filters = messages.MessageField(Filter, 1, repeated=True)
	orders = messages.MessageField(Order, 2, repeated=True)
	options = messages.MessageField(QueryOptions, 3)
	
	
class SearchRequest(messages.Message):

	terms = messages.StringField(1)
	scope = messages.StringField(2, repeated=True)
	
	
class AutocompleteRequest(messages.Message):

	fragment = messages.StringField(1)
	scope = messages.StringField(2, repeated=True)
	
	
# ==== Query responses ==== #
class QueryResponse(messages.Message):
	
	class QueryResults(messages.Message):
		
		count = messages.IntegerField(1)
		total = messages.IntegerField(2)
		objects = messages.MessageField(Data.DatastoreObject, 3, repeated=True)
		
	results = messages.MessageField(QueryResults, 1)
	
	
class SearchResponse(messages.Message):

	class SearchResult(messages.Message):
		
		href = messages.StringField(1)
		score = messages.FloatField(2)
		heading = messages.StringField(3)
		description = messages.StringField(4)
	
	count = messages.IntegerField(1)
	total = messages.IntegerField(2)
	results = messages.MessageField(SearchResult, 3, repeated=True)
	
	
class AutocompleteResponse(messages.Message):

	class AutocompleteFragment(messages.Message):

		class AutocompleteResult(messages.Message):
		
			href = messages.StringField(1)
			score = messages.FloatField(2)
			text = messages.StringField(3)
		
		count = messages.IntegerField(1)
		fragment = messages.StringField(2)
		reuslts = messages.MessageField(AutocompleteResult, 3, repeated=True)
		
	count = messages.IntegerField(1)
	fragments = messages.MessageField(AutocompleteFragment, 2, repeated=True)