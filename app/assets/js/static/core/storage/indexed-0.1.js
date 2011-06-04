_idbDriver = {
	
	state: {initialized: false, registered: false},
	api: {},
	
};


function _idbInitCallback()
{
	_idbDriver.state.registered = true;
}

function _indexedDBInit() { fatcatmap.sys.drivers.register('storage', 'object', _idbDriver.api, false, _idbInitCallback); _idbDriver.state.initialized = false; }