
// Map response adapters for different API services
var apiAdapters = {
	
	api: {
		
		data: {
			
			request: function dataAPIRequest(request)
			{
				return request
			},
			
			response: function dataAPIResponse(response, callbacks)
			{
				if ('success' in callbacks)
				{
					apiAdapters.makeCallback(response, callbacks.success)
				}			
			}
			
		},

		query: {
			
			request: function queryAPIRequest(request)
			{
				return request
			},
			
			response: function queryAPIResponse(response, callbacks)
			{
				if ('success' in callbacks)
				{
					apiAdapters.makeCallback(response, callbacks.success)					
				}			
			},
			
		},
		
		graph: {
			
			request: function graphAPIRequest(request)
			{
				return request
			},
			
			response: function graphAPIResponse(response, callbacks)
			{
				if ('success' in callbacks)
				{
					apiAdapters.makeCallback(response, callbacks.success)					
				}			
			}
			
		},
		
		charts: {
			
			request: function chartsAPIRequest(request)
			{
				return request
			},
			
			response: function chartsAPIResponse(response, callbacks)
			{
				if ('success' in callbacks)
				{
					apiAdapters.makeCallback(response, callbacks.success)					
				}			
			}
			
		},
		
		session: {
			
			request: function sessionAPIRequest(request)
			{
				return request
			},
			
			response: function sessionAPIResponse(response, callbacks)
			{
				if ('success' in callbacks)
				{
					apiAdapters.makeCallback(response, callbacks.success);
				}
			}
			
		},
		
		output: {
			
			request: function outputAPIRequest(request)
			{
				return request
			},
			
			response: function outputAPIResponse(response, callbacks)
			{
				if ('success' in callbacks)
				{
					apiAdapters.makeCallback(response, callbacks.success);
				}
			}
			
		}
			
	},
	
	error: function apiTransportError(failure, callbacks)
	{
		if ('failure' in callbacks)
		{
			callbacks.failure(failure);
		}
		else
		{
			alert('Unhandled exception in API request.');
		}
	},
	
	makeCallback: function _callResponder(response, callback)
	{
		if(typeof(callback) == 'function')
		{
			callback(response);
		}
	}
	
};

// API constructor function
function _initiateAPIFramework(page_object)
{
	// If the page has loaded...
	if(typeof(page_object) != 'undefined')
	{
		// Loop over the API's provided...
		for (i in page_object.rpc.api)
		{
			// For each method in each API...
			if ('methods' in page_object['rpc']['api'][i])
			{
				// Link up the adapter (from above)
				page_object['rpc']['api'][i]['adapter'] = apiAdapters['api'][i];
				
				// Create a framework function for calling the method
				for (method_i in page_object['rpc']['api'][i]['methods'])
				{
					method = page_object['rpc']['api'][i]['methods'][method_i];
					if ('failure' in page_object['rpc']['api'][i]['adapter'])
					{
						page_object['rpc']['api'][i][method] = function (args, callbacks, async) {
							if (typeof(async) == 'undefined')
							{
								async = false;
							}
							return page_object.rpc.makeRPCRequest(
								page_object['rpc']['api'][i]['adapter']['request']({
									
									base_uri: page_object['rpc']['api'][i]['base_uri'],
									method: method,
									params: args,
									opts: {},
									responder: function (response) {
										page_object['rpc']['api'][i]['adapter']['response'](response, callbacks);
									},
									failure: function (failure) {
										page_object['rpc']['api'][i]['adapter']['failure'](failure, callbacks);
									}
									
								}));
						};
					}
					else
					{
						page_object['rpc']['api'][i][method] = function (args, callbacks, async) {
							if (typeof(async) == 'undefined')
							{
								async = false;
							}	
							return page_object.rpc.makeRPCRequest(
								page_object['rpc']['api'][i]['adapter']['request']({
									base_uri: page_object['rpc']['api'][i]['base_uri'],
									method: method,
									params: args,
									opts: {},
									responder: function (response) {
										page_object['rpc']['api'][i]['adapter']['response'](response, callbacks);
									},
									failure: function (failure) {
										apiAdapters.error(failure, callbacks);
									}
								}));
						};						
					}
				}
			}
		}
	}
}