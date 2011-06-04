_sessionStorageDriver = {
	
	state: {initialized: false, registered: false},
	api: {},	
	
};


function _sessionStorageInitCallback()
{
	_sessionStorageDriver.state.registered = true;
}

function _sessionStorageInit() { fatcatmap.sys.drivers.register('storage', 'session', _sessionStorageDriver.api, true, _sessionStorageInitCallback); _sessionStorageDriver.state.initialized = true; }