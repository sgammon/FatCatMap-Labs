/* ====== User-Agent Parser ====== */
var UserAgent = {
	init: function () {
		this.browser = this.searchString(this.dataBrowser) || "An unknown browser";
		this.version = this.searchVersion(navigator.userAgent)
			|| this.searchVersion(navigator.appVersion)
			|| "an unknown version";
		this.OS = this.searchString(this.dataOS) || "an unknown OS";
		if(this.browser == 'iPod/iPhone' || this.browser == 'Android')
		{
			this.type = 'mobile';
			this.mobile = true;
		}
		else
		{
			this.type = 'desktop';
			this.mobile = false;
		}
	},
	searchString: function (data) {
		for (var i=0;i<data.length;i++)	{
			var dataString = data[i].string;
			var dataProp = data[i].prop;
			this.versionSearchString = data[i].versionSearch || data[i].identity;
			if (dataString) {
				if (dataString.indexOf(data[i].subString) != -1)
					return data[i].identity;
			}
			else if (dataProp)
				return data[i].identity;
		}
	},
	searchVersion: function (dataString) {
		var index = dataString.indexOf(this.versionSearchString);
		if (index == -1) return;
		return parseFloat(dataString.substring(index+this.versionSearchString.length+1));
	},
	dataBrowser: [
		{
			string: navigator.userAgent,
			subString: "Chrome",
			identity: "Chrome"
		},
		{ 	string: navigator.userAgent,
			subString: "OmniWeb",
			versionSearch: "OmniWeb/",
			identity: "OmniWeb"
		},
		{
			string: navigator.vendor,
			subString: "Apple",
			identity: "Safari",
			versionSearch: "Version"
		},
		{
			prop: window.opera,
			identity: "Opera"
		},
		{
			string: navigator.vendor,
			subString: "iCab",
			identity: "iCab"
		},
		{
			string: navigator.vendor,
			subString: "KDE",
			identity: "Konqueror"
		},
		{
			string: navigator.userAgent,
			subString: "Firefox",
			identity: "Firefox"
		},
		{
			string: navigator.vendor,
			subString: "Camino",
			identity: "Camino"
		},
		{		// for newer Netscapes (6+)
			string: navigator.userAgent,
			subString: "Netscape",
			identity: "Netscape"
		},
		{
			string: navigator.userAgent,
			subString: "MSIE",
			identity: "Explorer",
			versionSearch: "MSIE"
		},
		{
			string: navigator.userAgent,
			subString: "Gecko",
			identity: "Mozilla",
			versionSearch: "rv"
		},
		{ 		// for older Netscapes (4-)
			string: navigator.userAgent,
			subString: "Mozilla",
			identity: "Netscape",
			versionSearch: "Mozilla"
		}
	],
	dataOS : [
		{
			string: navigator.platform,
			subString: "Win",
			identity: "Windows"
		},
		{
			string: navigator.platform,
			subString: "Mac",
			identity: "Mac"
		},
		{
			   string: navigator.userAgent,
			   subString: "iPhone",
			   identity: "iPhone/iPod"
	    },
		{
			string: navigator.platform,
			subString: "Linux",
			identity: "Linux"
		}
	]

};

/* ====== FATCATMAP INIT ====== */
function _platformInit()
{
	
	page_object = {
		api: {}, // Holds JS-API code for interacting with all the services below
		agent: {}, // Holds information initialized about the browser/client environment
		state: {}, // Holds information about the state of FCM and the current page
		user: {}, // Holds information about the current user (including history and permissions)
		rpc: {}, // Manages a convenient framework for querying FCM API's easily from javascript
		sys: {}, // Holds configuration and environment information for the FCM internals
		dev: {} // Contains debug and server environment stuff (if a user is an admin or we're on the dev server)
	};
		
	// Initialize API property
	page_object.api = {
		storage: {},
		layout: {},
		visualizer: {}
	};
	
	// Set up agent property
	UserAgent.init();
	page_object.agent = {
		platform: {
			os: UserAgent.OS,
			type: UserAgent.type,
			vendor: navigator.vendor,
			product: navigator.product,
			browser: UserAgent.browser,
			version: UserAgent.version,
			flags: {
				mobile: UserAgent.mobile,
				webkit: $.browser.webkit,
				msie: $.browser.msie,
				opera: $.browser.opera,
				mozilla: $.browser.mozilla
			}
		},
		capabilities: {
			cookies: navigator.cookieEnabled,
			ajax: $.support.ajax,
			canvas: Modernizr.canvas,
			geolocation: Modernizr.geolocation,
			svg: Modernizr.svg,
			workers: Modernizr.webworkers,
			history: Modernizr.history,
			sockets: Modernizr.websockets,
			storage: {
				local: Modernizr.localStorage,
				session: Modernizr.sessionStorage,
				websql: Modernizr.websqldatabase,
				indexeddb: Modernizr.indexeddb
			}
		}
	};

	// Initialize page state property
	page_object.state = {
		events: {},
		page: {}
	};

	// Initialize user property
	page_object.user = {
		current_user: null,
		is_user_admin: null,
		login_url: null,
		logout_url: null
	};	
	
	// Initialize RPC property
	page_object.rpc = {
		api: {},
		security: {}
	};
	
	// Initialize system property
	page_object.sys = {

		version: {
			
			minor: null,
			major: null,
			release: null,
			setVersion: function setSysVersion(minor, major, release)
			{
				fatcatmap.sys.version.minor = minor;
				fatcatmap.sys.version.major = major;
				fatcatmap.sys.version.release = release;
			}
			
		},
		
		
		drivers: {
			
			registry: {},
			register: function _registerSystemDriver(module, name, initialized, callback)
			{
				if(typeof(window.fatcatmap.sys.drivers.registry[module]) == 'undefined')
				{
					window.fatcatmap.sys.drivers.registry[module] = {};
				}
				window.fatcatmap.sys.drivers.registry[module][name] = {
					initialized: initialized,
					registered: true,
					init_callback: callback
				};
				callback();
			}
			
		}
				
	};

	// Initialize dev/debug property
	page_object.dev = {
		config: {},
		environment: {},
		performance: {},
		debug: {}
	};
	
	return page_object
}

// Initialize global fatcatmap variable
var fatcatmap = _platformInit();