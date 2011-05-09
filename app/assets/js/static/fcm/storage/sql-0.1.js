_sqlDriver = {
	
	state: {initialized: false, registered: false},
	
};


function _sqlInitCallback()
{
	_sqlDriver.state.registered = true;
}

function _webSQLInit() { fatcatmap.sys.drivers.register('storage', 'websql', true, _sqlInitCallback); _sqlDriver.state.initialized = true; }