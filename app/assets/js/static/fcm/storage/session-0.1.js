_sessionStorageDriver = {
	
	state: {initialized: false, registered: false},
	
};


function _sessionStorageInitCallback()
{
	_sessionStorageDriver.state.registered = true;
}

function _sessionStorageInit() { fatcatmap.sys.drivers.register('storage', 'session', true, _sessionStorageInitCallback); _sessionStorageDriver.state.initialized = true; }