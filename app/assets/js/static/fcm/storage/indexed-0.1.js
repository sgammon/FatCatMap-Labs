_idbDriver = {
	
	state: {initialized: false, registered: false},
	
};


function _idbInitCallback()
{
	_idbDriver.state.registered = true;
}

function _indexedDBInit() { fatcatmap.sys.drivers.register('storage', 'indexeddb', true, _idbInitCallback); _idbDriver.state.initialized = true; }