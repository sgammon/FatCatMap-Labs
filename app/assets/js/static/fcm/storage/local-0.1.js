_localStorageDriver = {
	
	state: {initialized: false, registered: false},
	
};


function _localStorageInitCallback()
{
	_localStorageDriver.state.registered = true;
}

function _localStorageInit() { fatcatmap.sys.drivers.register('storage', 'local', true, _localStorageInitCallback); _localStorageDriver.state.initialized = true; }