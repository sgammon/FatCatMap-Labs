_sqlDriver = {
	
	state: {initialized: false, registered: false},
	api: {},
	
};


function _sqlInitCallback()
{
	_sqlDriver.state.registered = true;
}

function _webSQLInit() { fatcatmap.sys.drivers.register('storage', 'sql', _sqlDriver.api, false, _sqlInitCallback); _sqlDriver.state.initialized = false; }