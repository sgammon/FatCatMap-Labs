
// Map response adapters for different API services
var apiAdapters = {
	
	api: {
		
		data: {
			
			request: function dataAPIRequest(request)
			{
				
			},
			
			response: function dataAPIResponse(response)
			{
			
			}
			
		},

		query: {
			
			request: function queryAPIRequest(request)
			{
				
			},
			
			response: function queryAPIResponse(response)
			{
			
			},
			
		},
		
		graph: {
			
			request: function graphAPIRequest(request)
			{
				
			},
			
			response: function graphAPIResponse(response)
			{
			
			}
			
		},
		
		charts: {
			
			request: function chartsAPIRequest(request)
			{
				
			},
			
			response: function chartsAPIResponse(response)
			{
			
			}
			
		},
		
		session: {
			
			request: function sessionAPIRequest(request)
			{
				
			},
			
			response: function sessionAPIResponse(response)
			{
			
			}
			
		}					
			
	},
	
	error: function apiTransportError(response)
	{
		
	}
	
};

// API constructor function
function _initiateAPIFramework(page_object)
{
	if(typeof(fatcatmap) != 'undefined')
	{
		for (i in fatcatmap.rpc.api)
		{
			if ('methods' in fatcatmap['rpc']['api'][i])
			{
				for (method in fatcatmap['rpc']['api'][i]['methods'])
				{
					fatcatmap['rpc']['api'][i][method] = function (args) {
						return fatcatmap.rpc.api.makeRPCRequest(fatcatmap['rpc']['api'][i]['adapter']['request']({fatcatmap['rpc']['api'][i]['base_uri'], method, args, {}, fatcatmap['rpc']['api'][i]['adapter']['response'])
					};
				}
			}
		}
	}
}