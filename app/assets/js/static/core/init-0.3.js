(function() {
  var CoreAPI, CoreAPIBridge, CoreAgentAPI, CoreDevAPI, CoreRPCAPI, CoreStateAPI, CoreSysAPI, CoreUserAPI, FatCatMap, RPCAPI, RPCAdapter, RPCRequest;
  var __hasProp = Object.prototype.hasOwnProperty, __extends = function(child, parent) {
    for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; }
    function ctor() { this.constructor = child; }
    ctor.prototype = parent.prototype;
    child.prototype = new ctor;
    child.__super__ = parent.prototype;
    return child;
  }, __indexOf = Array.prototype.indexOf || function(item) {
    for (var i = 0, l = this.length; i < l; i++) {
      if (this[i] === item) return i;
    }
    return -1;
  }, __slice = Array.prototype.slice;
  CoreAPI = (function() {
    function CoreAPI(name, path, config) {
      this.name = name;
      this.path = path;
      this.config = config;
    }
    return CoreAPI;
  })();
  CoreAPIBridge = (function() {
    function CoreAPIBridge() {
      this.storage = {
        local: {
          _driver: null,
          _resolveDriver: function() {
            return this._driver = window.fatcatmap.sys.drivers.resolve('storage', 'local');
          },
          getValue: function(key) {
            if (this._driver !== null) {
              return this._driver.getValueByKey(key);
            } else {
              return false;
            }
          },
          setValue: function(key, value) {
            if (this._driver !== null) {
              return this._driver.setValueByKey(key, value);
            } else {
              return false;
            }
          },
          clearValues: function() {
            if (this._driver !== null) {
              return this._driver.allValues();
            } else {
              return false;
            }
          }
        },
        session: {
          _driver: null,
          _resolveDriver: function() {
            return this._driver = window.fatcatmap.sys.drivers.resolve('storage', 'session');
          },
          getValue: function(key) {
            if (this._driver !== null) {
              return this._driver.getValueByKey(key);
            } else {
              return false;
            }
          },
          setValue: function(key, value) {
            if (this._driver !== null) {
              return this._driver.setValueByKey(key, value);
            } else {
              return false;
            }
          },
          clearValues: function() {
            if (this._driver !== null) {
              return this._driver.allValues();
            } else {
              return false;
            }
          }
        },
        object: {
          _driver: null,
          _resolveDriver: function() {
            return this._driver = window.fatcatmap.sys.drivers.resolve('storage', 'object');
          },
          getValue: function(key) {
            if (this._driver !== null) {
              return this._driver.getValueByKey(key);
            } else {
              return false;
            }
          },
          setValue: function(key, value) {
            if (this._driver !== null) {
              return this._driver.setValueByKey(key, value);
            } else {
              return false;
            }
          },
          clearValues: function() {
            if (this._driver !== null) {
              return this._driver.allValues();
            } else {
              return false;
            }
          }
        },
        sql: {
          _driver: null,
          _resolveDriver: function() {
            return this._driver = window.fatcatmap.sys.drivers.resolve('storage', 'sql');
          },
          getValue: function(key) {
            if (this._driver !== null) {
              return this._driver.getValueByKey(key);
            } else {
              return false;
            }
          },
          setValue: function(key, value) {
            if (this._driver !== null) {
              return this._driver.setValueByKey(key, value);
            } else {
              return false;
            }
          },
          clearValues: function() {
            if (this._driver !== null) {
              return this._driver.allValues();
            } else {
              return false;
            }
          }
        }
      };
      this.layout = {};
      this.visualizer = {};
    }
    __extends(CoreAPIBridge, CoreAPI);
    return CoreAPIBridge;
  })();
  CoreAgentAPI = (function() {
    function CoreAgentAPI() {
      this._data = {};
      this.platform = {};
      this.capabilities = {};
      this._data = {
        browsers: [
          {
            string: navigator.userAgent,
            subString: "Chrome",
            identity: "Chrome"
          }, {
            string: navigator.userAgent,
            subString: "OmniWeb",
            versionSearch: "OmniWeb/",
            identity: "OmniWeb"
          }, {
            string: navigator.vendor,
            subString: "Apple",
            identity: "Safari",
            versionSearch: "Version"
          }, {
            prop: window.opera,
            identity: "Opera"
          }, {
            string: navigator.vendor,
            subString: "iCab",
            identity: "iCab"
          }, {
            string: navigator.vendor,
            subString: "KDE",
            identity: "Konqueror"
          }, {
            string: navigator.userAgent,
            subString: "Firefox",
            identity: "Firefox"
          }, {
            string: navigator.vendor,
            subString: "Camino",
            identity: "Camino"
          }, {
            string: navigator.userAgent,
            subString: "Netscape",
            identity: "Netscape"
          }, {
            string: navigator.userAgent,
            subString: "MSIE",
            identity: "Explorer",
            versionSearch: "MSIE"
          }, {
            string: navigator.userAgent,
            subString: "Gecko",
            identity: "Mozilla",
            versionSearch: "rv"
          }, {
            string: navigator.userAgent,
            subString: "Mozilla",
            identity: "Netscape",
            versionSearch: "Mozilla"
          }
        ],
        os: [
          {
            string: navigator.platform,
            subString: "Win",
            identity: "Windows"
          }, {
            string: navigator.platform,
            subString: "Mac",
            identity: "Mac"
          }, {
            string: navigator.userAgent,
            subString: "iPhone",
            identity: "iPhone/iPod"
          }, {
            string: navigator.platform,
            subString: "Linux",
            identity: "Linux"
          }
        ]
      };
    }
    __extends(CoreAgentAPI, CoreAPI);
    CoreAgentAPI.prototype._makeMatch = function(data) {
      var prop, string, value, _i, _len, _results;
      _results = [];
      for (_i = 0, _len = data.length; _i < _len; _i++) {
        value = data[_i];
        string = value.string;
        prop = value.prop;
        this._data.versionSearchString = value.versionSearch || value.identity;
        if (string !== null) {
          if (value.string.indexOf(value.subString) !== -1) {
            return value.identity;
          }
        } else if (prop) {
          return value.identity;
        }
      }
      return _results;
    };
    CoreAgentAPI.prototype._makeVersion = function(dataString) {
      var index;
      index = dataString.indexOf(this._data.versionSearchString);
      if (index === -1) {
        ;
      } else {
        return parseFloat(dataString.substring(index + this._data.versionSearchString.length + 1));
      }
    };
    CoreAgentAPI.prototype.discover = function() {
      var browser, mobile, os, type, version;
      browser = this._makeMatch(this._data.browsers) || "unknown";
      version = this._makeVersion(navigator.userAgent) || this._makeVersion(navigator.appVersion) || "unknown";
      os = this._makeMatch(this._data.os) || "unknown";
      if (browser === 'iPod/iPhone' || browser === 'Android') {
        type = 'mobile';
        mobile = false;
      }
      this.platform = {
        os: os,
        type: type,
        vendor: navigator.vendor,
        product: navigator.product,
        browser: browser,
        version: version,
        flags: {
          mobile: mobile,
          webkit: $.browser.webkit,
          msie: $.browser.msie,
          opera: $.browser.opera,
          mozilla: $.browser.mozilla
        }
      };
      return this.capabilities = {
        cookies: navigator.cookiesEnabled,
        ajax: $.support.ajax,
        canvas: Modernizr.canvas,
        geolocation: Modernizr.geolocation,
        svg: Modernizr.svg,
        workers: Modernizr.webworkers,
        history: Modernizr.history,
        sockets: Modernizr.websockets,
        storage: {
          local: Modernizr.localstorage,
          session: Modernizr.sessionstorage,
          websql: Modernizr.websqldatabase,
          object: Modernizr.indexeddb
        }
      };
    };
    return CoreAgentAPI;
  })();
  CoreStateAPI = (function() {
    function CoreStateAPI() {
      this.events = {
        registry: [],
        callchain: {},
        history: [],
        registerEvent: function(name) {
          this.registry.push(name);
          this.callchain[name] = [];
          return this;
        },
        registerHook: function(_event, fn, once) {
          var calltask;
          if (typeof once === null) {
            once = false;
          }
          try {
            calltask = {
              executed: false,
              callback: function(context) {
                return fn(context);
              },
              runonce: one
            };
            return this.callchain[_event].push(calltask);
          } catch (_e) {}
        },
        triggerEvent: function(_event, context) {
          var calltask, result, result_calltask, _i, _len, _ref, _results;
          if (typeof this.callchain[_event] !== null) {
            if (this.callchain[_event].length > 0) {
              _ref = this.callchain[_event];
              _results = [];
              for (_i = 0, _len = _ref.length; _i < _len; _i++) {
                calltask = _ref[_i];
                if (this.callchain[_event][calltask].executed === true && this.callchain[_event][calltask].runonce === true) {
                  continue;
                } else {
                  try {
                    result = this.callchain[_event][calltask].callback(context);
                    result_calltask = {
                      event: _event,
                      context: context,
                      task: this.callchain[_event][calltask],
                      result: result
                    };
                  } catch (error) {
                    result_calltask = {
                      event: _event,
                      context: context,
                      task: this.callchain[_event][calltask],
                      error: error
                    };
                  } finally {
                    this.history.push(result_calltask);
                    this.callchain[_event][calltask].executed = true;
                  }
                }
              }
              return _results;
            }
          }
        }
      };
      this.session = {};
      this.local = {};
      this.elements = {
        registry: {},
        get: function(id) {},
        register: function(id, selector, default_config, default_state) {},
        setState: function(id, key, value) {},
        getState: function(id, key, default_value) {},
        loadState: function(id) {}
      };
    }
    __extends(CoreStateAPI, CoreAPI);
    return CoreStateAPI;
  })();
  CoreUserAPI = (function() {
    function CoreUserAPI() {
      this.current_user = null;
      this.is_user_admin = null;
      this.login_url = null;
      this.logout_url = null;
    }
    __extends(CoreUserAPI, CoreAPI);
    CoreUserAPI.prototype.setUserInfo = function(current_user, is_user_admin, login_url, logout_url) {
      this.current_user = current_user;
      this.is_user_admin = is_user_admin;
      this.login_url = login_url;
      this.logout_url = logout_url;
    };
    return CoreUserAPI;
  })();
  RPCAPI = (function() {
    function RPCAPI(name, base_uri, methods, config) {
      var method, _i, _len, _ref;
      this.name = name;
      this.base_uri = base_uri;
      this.methods = methods;
      this.config = config;
      if (this.methods.length > 0) {
        _ref = this.methods;
        for (_i = 0, _len = _ref.length; _i < _len; _i++) {
          method = _ref[_i];
          this[method] = function(params, callbacks, async, opts) {
            if (params == null) {
              params = {};
            }
            if (callbacks == null) {
              callbacks = {};
            }
            if (async == null) {
              async = false;
            }
            if (opts == null) {
              opts = {};
            }
            return this.makeRPCRequest(method, params, opts, async).fulfill(callbacks);
          };
        }
      }
    }
    RPCAPI.prototype.makeRPCRequest = function(method, params, opts, async) {
      if (__indexOf.call(this.methods, method) >= 0) {
        return fatcatmap.rpc.api.createRPCRequest({
          method: method,
          api: this.name,
          params: params || {},
          opts: opts || {},
          async: async || false
        });
      }
    };
    RPCAPI.prototype.__noSuchMethod__ = function(id, args) {
      if (__indexOf.call(this.methods, method) >= 0) {
        return fatcatmap.rpc.createRPCRequest({
          method: method,
          api: this.name,
          params: args.slice(0, (args.length - 2 + 1) || 9e9) || {},
          opts: args[-1] || {},
          async: args[-2] || false
        });
      }
    };
    return RPCAPI;
  })();
  RPCAdapter = (function() {
    function RPCAdapter(name) {
      this.name = name;
    }
    RPCAdapter.prototype.request = function(request) {
      return request;
    };
    RPCAdapter.prototype.response = function(response, callbacks) {
      if (__indexOf.call(callbacks, 'success') >= 0) {
        return fatcatmap.rpc.adapters.makeCallback(response, callbacks.success);
      }
    };
    return RPCAdapter;
  })();
  RPCRequest = (function() {
    var action, api, base_uri, method, params;
    params = {};
    action = null;
    method = null;
    api = null;
    base_uri = null;
    RPCRequest.prototype.envelope = {
      id: null,
      opts: {},
      agent: {}
    };
    RPCRequest.prototype.ajax = {
      async: false,
      cache: true,
      global: true,
      http_method: 'POST',
      crossDomain: false,
      ifModified: false,
      dataType: 'json'
    };
    function RPCRequest(id, opts, agent) {
      this.envelope.id = id;
      this.envelope.opts = opts;
      this.envelope.agent = agent;
    }
    RPCRequest.prototype.fulfill = function() {
      var callbacks, config;
      callbacks = arguments[0], config = 2 <= arguments.length ? __slice.call(arguments, 1) : [];
      return fatcatmap.rpc.api.fulfillRPCRequest(config, this, this.ajax.async);
    };
    RPCRequest.prototype.setOpts = function(opts) {
      return this.envelope.opts = opts;
    };
    RPCRequest.prototype.setAgent = function(agent) {
      return this.envelope.agent = agent;
    };
    RPCRequest.prototype.setAction = function(action) {
      return this.action = action;
    };
    RPCRequest.prototype.setMethod = function(method) {
      return this.method = method;
    };
    RPCRequest.prototype.setAPI = function(method) {
      return this.api = api;
    };
    RPCRequest.prototype.setBaseURI = function(uri) {
      return this.base_uri = uri;
    };
    RPCRequest.prototype.setParams = function(params) {
      if (params == null) {
        params = {};
      }
      return this.params = params;
    };
    RPCRequest.prototype.payload = function() {
      var key, value, _payload, _ref;
      _payload = {
        id: this.envelope.id,
        opts: this.envelope.opts,
        agent: this.envelope.agent
      };
      _ref = this.params;
      for (key in _ref) {
        value = _ref[key];
        _payload[key] = value;
      }
      return _payload;
    };
    return RPCRequest;
  })();
  CoreRPCAPI = (function() {
    function CoreRPCAPI() {
      this.base_rpc_uri = '/_api/rpc';
      this.api = {
        lastRequest: null,
        lastFailure: null,
        lastResponse: null,
        action_prefix: null,
        history: {},
        used_ids: [],
        factory: function(name, base_uri, methods, config) {
          return this[name] = new RPCAPI(name, base_uri, methods, config);
        },
        _assembleRPCURL: function(method, api, prefix, base_uri) {
          if (typeof api === null && typeof base_uri === null) {
            throw "RPC Error: must specify either an API or base URI to generate an RPC endpoint.";
          } else {
            if (typeof base_uri === null) {
              base_uri = fatcatmap.rpc.api[api].base_uri;
            }
            if (typeof prefix !== null) {
              return [prefix + base_uri, method].join('.');
            } else {
              return [base_uri, method].join('.');
            }
          }
        },
        provisionRequestID: function() {
          var id;
          if (this.used_ids.length > 0) {
            id = Math.max.apply(this, this.used_ids) + 1;
            this.used_ids.push(id);
            return id;
          } else {
            this.used_ids.push(1);
            return 1;
          }
        },
        createRPCRequest: function(config) {
          var key, request, value;
          request = new RPCRequest(this.provisionRequestID());
          for (key in config) {
            value = config[key];
            if (__indexOf.call(request, key) >= 0) {
              request[key] = value;
            } else if (key === 'opts') {
              request.setOpts(value);
            } else if (key === 'agent') {
              request.setAgent(value);
            }
          }
          return request;
        },
        fulfillRPCRequest: function(config, request, callbacks) {
          var xhr;
          this.lastRequest = request;
          this.history[request.envelope.id] = {
            request: request,
            config: config,
            callbacks: callbacks
          };
          if (request.action === null) {
            if (request.method === null) {
              throw "RPC Error: Request must specify at least an action or method.";
            }
            if (request.base_uri === null) {
              if (request.api === null) {
                throw "RPC Error: Request must have an API or explicity BASE_URI.";
              } else {
                request.action = this._assembleRPCURL(request.method, request.api, this.action_prefix);
              }
            } else {
              request.action = this._assembleRPCURL(request.method, null, this.action_prefix, request.base_uri);
            }
          }
          xhr = $.ajax({
            url: request.action,
            data: JSON.stringify(request.params),
            async: request.ajax.async,
            cache: request.ajax.cache,
            global: request.ajax.global,
            type: request.ajax.http_method,
            crossDomain: request.ajax.crossDomain,
            dataType: request.ajax.dataType,
            processData: false,
            ifModified: request.ajax.ifModified,
            contentType: 'application/json',
            beforeSend: function(xhr, settings) {
              fatcatmap.rpc.history[request.envelope.id].xhr = xhr;
              return xhr;
            },
            error: function(xhr, status, error) {
              fatcatmap.rpc.lastFailure = error;
              fatcatmap.rpc.history[request.envelope.id].xhr = xhr;
              fatcatmap.rpc.history[request.envelope.id].status = status;
              fatcatmap.rpc.history[request.envelope.id].failure = error;
              return callbacks.failure(data);
            },
            success: function(data, status, xhr) {
              fatcatmap.rpc.lastResponse = data;
              fatcatmap.rpc.history[request.envelope.id].xhr = xhr;
              fatcatmap.rpc.history[request.envelope.id].status = status;
              fatcatmap.rpc.history[request.envelope.id].response = data;
              return callbacks.success(data);
            },
            complete: function(xhr, status) {
              fatcatmap.rpc.history[request.envelope.id].xhr = xhr;
              return fatcatmap.rpc.history[request.envelope.id].status = status;
            },
            statusCode: {
              404: function() {
                return alert('RPC 404: Could not resolve RPC action URI.');
              },
              403: function() {
                return alert('RPC 403: Not authorized to access the specified endpoint.');
              },
              500: function() {
                return alert('RPC 500: Woops! Something went wrong. Please try again.');
              }
            }
          });
          return {
            id: request.envelope.id,
            request: request,
            xhr: xhr
          };
        }
      };
      this.adapters = {
        data: new RPCAdapter('data'),
        query: new RPCAdapter('query'),
        graph: new RPCAdapter('graph'),
        charts: new RPCAdapter('charts'),
        session: new RPCAdapter('session'),
        frame: new RPCAdapter('frame')
      };
      this.ext = null;
    }
    __extends(CoreRPCAPI, CoreAPI);
    return CoreRPCAPI;
  })();
  CoreSysAPI = (function() {
    function CoreSysAPI() {
      this.version = {
        minor: null,
        major: null,
        release: null,
        setVersion: function(minor, major, release) {
          this.minor = minor;
          this.major = major;
          this.release = release;
        }
      };
      this.drivers = {
        registry: {},
        register: function(module, name, fn, initialized, callback) {
          if (typeof this.registry[module] === null) {
            this.registry[module] = {};
          }
          return this.registry[module][name] = {
            initialized: initialized,
            registered: true,
            hook_point: fn,
            init_callback: callback
          };
        },
        resolve: function(module, name) {
          if (typeof this.registry[module] === null) {
            return false;
          } else {
            if (typeof this.registry[module][name] === null) {
              return false;
            } else {
              return this.registry[module][name].hook_point;
            }
          }
        }
      };
    }
    __extends(CoreSysAPI, CoreAPI);
    return CoreSysAPI;
  })();
  CoreDevAPI = (function() {
    function CoreDevAPI() {
      this.config = {};
      this.environment = {};
      this.performance = {};
      this.debug = {
        logging: true,
        eventlog: true,
        verbose: true
      };
    }
    __extends(CoreDevAPI, CoreAPI);
    return CoreDevAPI;
  })();
  FatCatMap = (function() {
    function FatCatMap(config) {
      this.config = config;
      this.api = new CoreAPIBridge;
      this.agent = new CoreAgentAPI;
      this.agent.discover();
      this.state = new CoreStateAPI;
      this.user = new CoreUserAPI;
      this.rpc = new CoreRPCAPI;
      this.rpc.api.factory('data', '/_api/rpc/data', ['get', 'retrieveGraphObject', 'retrieveNative', 'retriveAsset']);
      this.rpc.api.factory('query', '/_api/rpc/query', ['search', 'gql', 'autocomplete']);
      this.rpc.api.factory('graph', '/_api/rpc/graph', ['construct', 'constructFromNode', 'constructFromObject']);
      this.rpc.api.factory('charts', '/_api/rpc/charts', ['generate', 'generateFromSeries']);
      this.rpc.api.factory('session', '/_api/rpc/session', ['init', 'authenticate', 'checkin']);
      this.sys = new CoreSysAPI;
      this.dev = new CoreDevAPI;
      this.state.events.registerEvent('CORE_INIT');
      this.state.events.registerEvent('RPC_INIT');
      this.state.events.registerEvent('API_INIT');
      this.state.events.registerEvent('DRIVER_REGISTERED');
      this.state.events.registerEvent('REGISTER_ELEMENT');
      this.state.events.registerEvent('PLATFORM_READY');
      return this;
    }
    return FatCatMap;
  })();
  window.fatcatmap = new FatCatMap;
}).call(this);
