_localStorageDriver = {
	
	state: {initialized: false, registered: false},
	api: {},	
	
};


function _localStorageInitCallback()
{
	_localStorageDriver.state.registered = true;
}

function _localStorageInit() { fatcatmap.sys.drivers.register('storage', 'local', _localStorageDriver.api, true, _localStorageInitCallback); _localStorageDriver.state.initialized = true; }