

class MomentumAPIService(object):
	pass
	
	
def CallResponder(func):

	def decorated(self, *args, **kwargs):
		result = func(self, *args, **kwargs)
		self.result = result
	return decorated		
	
	
def QueryResponder(func):

	def decorated(self, query={}, *args, **kwargs):

		## Retrieve 'mode' parameter
		mode = self.request.args.get('mode', False)
		if mode is False:
			self.request.form.get('mode', False)
			if mode is False:
				if mode in kwargs:
					mode = kwargs['mode']

		## Check for query params
		query_params = {}
		if isinstance(query, list):
			for entry in query:
				## @TODO: Add sorting here
				query_params[entry['name']] = entry['value']
			query = query_params

		## Get result of function call
		result = func(self, *args, **kwargs)

		## If it's a query, fetch results according to params and return
		if isinstance(result, (db.Query)):

			if 'keys_only' in query:
				result.keys_only = True


			## == Run Query
			query_result = self.runQuery(result, limit=query.get('limit'), offset=query.get('offset'))

			self.result['data_count'] = query_result['count']
			self.result['data'] = query_result['data']
			self.result['cursor'] = query_result['cursor']

			return self.BuildAPIResponse()

		else:
			self.result = result

   	return decorated