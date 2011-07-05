(function() {
  var CoreAPI, CoreAPIBridge, CoreAgentAPI, CoreDevAPI, CoreRPCAPI, CoreStateAPI, CoreSysAPI, CoreUserAPI, FatCatMap, InteractiveWidget, LayoutElement, RPCAPI, RPCAdapter, RPCRequest, SiteSection;
  var __hasProp = Object.prototype.hasOwnProperty, __extends = function(child, parent) {
    for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; }
    function ctor() { this.constructor = child; }
    ctor.prototype = parent.prototype;
    child.prototype = new ctor;
    child.__super__ = parent.prototype;
    return child;
  }, __bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; }, __indexOf = Array.prototype.indexOf || function(item) {
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
        cookies: navigator.cookieEnabled,
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
      this.layout = {
        register: function(id, element) {
          element.register(id);
          return fatcatmap.state.elements.register(id, element);
        }
      };
      this.visualizer = {};
    }
    __extends(CoreAPIBridge, CoreAPI);
    return CoreAPIBridge;
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
      this.performance = {
        tools: {
          fpsstats: {
            show: function(selector) {
              var stats;
              stats = new Stats();
              stats.domElement.style.position = 'absolute';
              stats.domElement.style.left = '50px';
              stats.domElement.style.top = '50px';
              stats.domElement.style.opacity = 0.7;
              stats.domElement.id = 'js_fps_stats';
              console.log('stats', stats);
              $('body').append(stats.domElement);
              return setInterval(function() {
                return stats.update();
              }, 1000 / 60);
            },
            hide: function(selector) {
              return $('#js_fps_stats').hide();
            }
          }
        }
      };
      this.debug = {
        logging: true,
        eventlog: true,
        verbose: true
      };
    }
    __extends(CoreDevAPI, CoreAPI);
    return CoreDevAPI;
  })();
  CoreUserAPI = (function() {
    function CoreUserAPI() {
      this.current_user = null;
      this.is_user_admin = null;
      this.login_url = null;
      this.logout_url = null;
    }
    __extends(CoreUserAPI, CoreAPI);
    CoreUserAPI.prototype.setUserInfo = function(user_properties) {
      if (user_properties['current_user'] !== null) {
        this.current_user = user_properties['current_user'];
      }
      if (user_properties['is_user_admin'] !== null) {
        this.is_user_admin = user_properties['is_user_admin'];
      }
      if (user_properties['login_url'] !== null) {
        this.login_url = user_properties['login_url'];
      }
      if (user_properties['logout_url'] !== null) {
        return this.logout_url = user_properties['logout_url'];
      }
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
          this[method] = this._buildRPCMethod(method);
        }
      }
    }
    RPCAPI.prototype._buildRPCMethod = function(method) {
      var api, rpcMethod;
      api = this.name;
      rpcMethod = __bind(function(params, callbacks, async, opts) {
        if (params == null) {
          params = {};
        }
        if (callbacks == null) {
          callbacks = null;
        }
        if (async == null) {
          async = false;
        }
        if (opts == null) {
          opts = {};
        }
        return __bind(function(params, callbacks, async, opts) {
          var request;
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
          request = window.fatcatmap.rpc.api.createRPCRequest({
            method: method,
            api: api,
            params: params || {},
            opts: opts || {},
            async: async || false
          });
          if (callbacks != null) {
            return request.fulfill(callbacks);
          } else {
            return request;
          }
        }, this)(params, callbacks, async, opts);
      }, this);
      return rpcMethod;
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
        return window.fatcatmap.rpc.adapters.makeCallback(response, callbacks.success);
      }
    };
    return RPCAdapter;
  })();
  RPCRequest = (function() {
    function RPCRequest(id, opts, agent) {
      this.params = {};
      this.action = null;
      this.method = null;
      this.api = null;
      this.base_uri = null;
      this.envelope = {
        id: null,
        opts: {},
        agent: {}
      };
      this.ajax = {
        async: false,
        cache: true,
        global: true,
        http_method: 'POST',
        crossDomain: false,
        ifModified: false,
        dataType: 'json'
      };
      if (id != null) {
        this.envelope.id = id;
      }
      if (opts != null) {
        this.envelope.opts = opts;
      }
      if (agent != null) {
        this.envelope.agent = agent;
      }
    }
    RPCRequest.prototype.fulfill = function() {
      var callbacks, config;
      callbacks = arguments[0], config = 2 <= arguments.length ? __slice.call(arguments, 1) : [];
      return window.fatcatmap.rpc.api.fulfillRPCRequest(config, this, callbacks);
    };
    RPCRequest.prototype.setAsync = function(async) {
      var _ref, _ref2;
      if ((_ref = this.ajax) != null) {
                if ((_ref2 = _ref.async) != null) {
          _ref2;
        } else {
          _ref.async = async;
        };
      }
      return this;
    };
    RPCRequest.prototype.setOpts = function(opts) {
      var _ref, _ref2;
      if ((_ref = this.envelope) != null) {
                if ((_ref2 = _ref.opts) != null) {
          _ref2;
        } else {
          _ref.opts = opts;
        };
      }
      return this;
    };
    RPCRequest.prototype.setAgent = function(agent) {
      var _ref, _ref2;
      if ((_ref = this.envelope) != null) {
                if ((_ref2 = _ref.agent) != null) {
          _ref2;
        } else {
          _ref.agent = agent;
        };
      }
      return this;
    };
    RPCRequest.prototype.setAction = function(action) {
      this.action = action;
      return this;
    };
    RPCRequest.prototype.setMethod = function(method) {
      this.method = method;
      return this;
    };
    RPCRequest.prototype.setAPI = function(api) {
      this.api = api;
      return this;
    };
    RPCRequest.prototype.setBaseURI = function(base_uri) {
      this.base_uri = base_uri;
      return this;
    };
    RPCRequest.prototype.setParams = function(params) {
      this.params = params != null ? params : {};
      return this;
    };
    RPCRequest.prototype.payload = function() {
      var _payload;
      _payload = {
        id: this.envelope.id,
        opts: this.envelope.opts,
        agent: this.envelope.agent,
        request: {
          params: this.params,
          method: this.method,
          api: this.api
        }
      };
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
          if (api == null) {
            api = null;
          }
          if (prefix == null) {
            prefix = null;
          }
          if (base_uri == null) {
            base_uri = null;
          }
          if (api === null && base_uri === null) {
            throw "[RPC] Error: Must specify either an API or base URI to generate an RPC endpoint.";
          } else {
            if (base_uri === null) {
              base_uri = window.fatcatmap.rpc.api[api].base_uri;
            }
            if (prefix !== null) {
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
          var request;
          request = new RPCRequest(this.provisionRequestID());
          if (config.api != null) {
            request.setAPI(config.api);
          }
          if (config.method != null) {
            request.setMethod(config.method);
          }
          if (config.agent != null) {
            request.setAgent(config.agent);
          }
          if (config.opts != null) {
            request.setOpts(config.opts);
          }
          if (config.base_uri != null) {
            request.setBaseURI(config.base_uri);
          }
          if (config.params != null) {
            request.setParams(config.params);
          }
          if (config.async != null) {
            request.setAsync(config.async);
          }
          console.log('[RPC] Request: ', request, config);
          request.setAction(this._assembleRPCURL(request.method, request.api, this.action_prefix, this.base_rpc_uri));
          return request;
        },
        fulfillRPCRequest: function(config, request, callbacks) {
          console.log('[RPC] Fulfill: ', config, request, callbacks);
          this.lastRequest = request;
          this.history[request.envelope.id] = {
            request: request,
            config: config,
            callbacks: callbacks
          };
          if (request.action === null) {
            if (request.method === null) {
              throw "[RPC] Error: Request must specify at least an action or method.";
            }
            if (request.base_uri === null) {
              if (request.api === null) {
                throw "[RPC] Error: Request must have an API or explicity BASE_URI.";
              } else {
                request.action = this._assembleRPCURL(request.method, request.api, this.action_prefix);
              }
            } else {
              request.action = this._assembleRPCURL(request.method, null, this.action_prefix, request.base_uri);
            }
          }
          if (request.action === null || request.action === void 0) {
            throw '[RPC] Error: Could not determine RPC action.';
          }
          (function(request, callbacks) {
            var xhr;
            this.request = request;
            this.callbacks = callbacks;
            this.fatcatmap = window.fatcatmap;
            return xhr = $.ajax({
              url: this.request.action,
              data: JSON.stringify(this.request.payload()),
              async: this.request.ajax.async,
              cache: this.request.ajax.cache,
              global: this.request.ajax.global,
              type: this.request.ajax.http_method,
              crossDomain: this.request.ajax.crossDomain,
              dataType: this.request.ajax.dataType,
              processData: false,
              ifModified: this.request.ajax.ifModified,
              contentType: 'application/json',
              beforeSend: __bind(function(xhr, settings) {
                this.fatcatmap.rpc.api.history[this.request.envelope.id].xhr = xhr;
                return xhr;
              }, this),
              error: __bind(function(xhr, status, error) {
                console.log('[RPC] Error: ', data, status, xhr);
                this.fatcatmap.rpc.api.lastFailure = error;
                this.fatcatmap.rpc.api.history[this.request.envelope.id].xhr = xhr;
                this.fatcatmap.rpc.api.history[this.request.envelope.id].status = status;
                this.fatcatmap.rpc.api.history[this.request.envelope.id].failure = error;
                return this.callbacks.failure(data);
              }, this),
              success: __bind(function(data, status, xhr) {
                console.log('[RPC] Success: ', data, status, xhr);
                this.fatcatmap.rpc.api.lastResponse = data;
                this.fatcatmap.rpc.api.history[this.request.envelope.id].xhr = xhr;
                this.fatcatmap.rpc.api.history[this.request.envelope.id].status = status;
                this.fatcatmap.rpc.api.history[this.request.envelope.id].response = data;
                return this.callbacks.success(data);
              }, this),
              complete: __bind(function(xhr, status) {
                this.fatcatmap.rpc.api.history[this.request.envelope.id].xhr = xhr;
                return this.fatcatmap.rpc.api.history[this.request.envelope.id].status = status;
              }, this),
              statusCode: {
                404: function() {
                  console.log('[RPC]: 404');
                  return alert('RPC 404: Could not resolve RPC action URI.');
                },
                403: function() {
                  console.log('[RPC]: 403');
                  return alert('RPC 403: Not authorized to access the specified endpoint.');
                },
                500: function() {
                  console.log('[RPC]: 500');
                  return alert('RPC 500: Woops! Something went wrong. Please try again.');
                }
              }
            });
          })(request, callbacks);
          return {
            id: request.envelope.id,
            request: request
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
  window.RPCAPI = RPCAPI;
  window.RPCAdapter = RPCAdapter;
  window.RPCRequest = RPCRequest;
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
        get: function(id) {
          return this.registry[id];
        },
        scan: function() {
          $('[data-element]').each({
            buildElement: function(index, element) {
              return this.register(element.attr('data-element'), this.factory(element.attr('data-element'), '#' + element.attr('id'), element.attr('data-element-type') || null));
            }
          });
          return this;
        },
        factory: function(id, selector, type, config) {
          var _type;
          if (type == null) {
            type = 'LayoutElement';
          }
          if (config == null) {
            config = {};
          }
          if (type === null) {
            _type = LayoutElement;
          }
          if (type === 'LayoutElement') {
            _type = LayoutElement;
          } else if (type === 'Panel') {
            _type = Panel;
          } else if (type === 'SuperPanel') {
            _type = SuperPanel;
          } else if (type === 'Navigation') {
            _type = Navigation;
          }
          return new _type(id, selector, config);
        },
        register: function(id, element) {
          this.registry[id] = element;
          return this.registry[id];
        },
        _setState: function(id, key, value) {
          if (this.registry[id] !== null) {
            this.registry[id]._setState(key, value);
          }
          return this;
        },
        _getState: function(id, key, default_value) {
          if (default_value == null) {
            default_value = null;
          }
          if (this.registry[id] !== null) {
            return this.registry[id]._getState(key, default_value);
          } else {
            return default_value;
          }
        },
        _loadState: function(id, state) {
          if (this.registry[id] === null) {
            throw "Must register element before setting state!";
          } else {
            this.registry[id]._loadState(state);
          }
          return this;
        }
      };
    }
    __extends(CoreStateAPI, CoreAPI);
    return CoreStateAPI;
  })();
  LayoutElement = (function() {
    LayoutElement.prototype.id = null;
    LayoutElement.prototype.state = {};
    LayoutElement.prototype.config = {};
    LayoutElement.prototype.classes = [];
    LayoutElement.prototype.element = null;
    LayoutElement.prototype.defaults = null;
    LayoutElement.prototype.selector = null;
    LayoutElement.prototype.registered = false;
    function LayoutElement(selector, config) {
      this.selector = selector;
      this.config = config != null ? config : {};
    }
    LayoutElement.prototype.register = function(id) {
      this.id = id;
    };
    LayoutElement.prototype._setState = function(key, value) {
      this.state[key] = value;
      return this;
    };
    LayoutElement.prototype._getState = function(key, default_value) {
      if (default_value == null) {
        default_value = null;
      }
      if (this.state[key] === void 0) {
        return default_value;
      } else {
        return this.state[key];
      }
    };
    LayoutElement.prototype._deleteState = function(key) {
      return delete this.state[key];
    };
    LayoutElement.prototype._loadState = function(state, classes) {
      this.state = state;
      this.classes = classes;
      return this._refreshState();
    };
    LayoutElement.prototype._flushState = function() {
      var finalState;
      finalState = {
        state: this.state,
        classes: this.classes
      };
      return finalState;
    };
    LayoutElement.prototype._refreshState = function() {
      var classname, _i, _len, _ref, _results;
      _ref = this.classes;
      _results = [];
      for (_i = 0, _len = _ref.length; _i < _len; _i++) {
        classname = _ref[_i];
        _results.push(this.get().addClass(classname));
      }
      return _results;
    };
    LayoutElement.prototype.get = function() {
      if (this.element === null) {
        this.element = $(this.selector);
      }
      return this.element;
    };
    LayoutElement.prototype.addClass = function(classname) {
      this.classes.push(classname);
      this.get().addClass(classname);
      return this;
    };
    LayoutElement.prototype.removeClass = function(classname) {
      if (__indexOf.call(this.classes, classname) >= 0) {
        this.classes.remove(classname);
      }
      this.get().removeClass(classname);
      return this;
    };
    LayoutElement.prototype.toggleClass = function(classname) {
      if (__indexOf.call(this.classes, classname) >= 0) {
        this.classes.remove(classname);
      } else {
        this.classes.push(classname);
      }
      this.get().toggleClass(classname);
      return this;
    };
    LayoutElement.prototype.hide = function(duration, easing, callback) {
      this._setState('visible', false);
      this.get().hide(duration, easing, callback);
      return this;
    };
    LayoutElement.prototype.show = function(duration, easing, callback) {
      this._setState('visible', true);
      return this.get().show(duration, easing, callback);
    };
    LayoutElement.prototype.showhide = function(duration, easing, callback) {
      if (this._getState('visible', false) !== false) {
        this.get().hide(duration, easing, callback);
      } else {
        this.get().show(duration, easing, callback);
      }
      return this;
    };
    LayoutElement.prototype.css = function(properties) {
      this.get().css(properties);
      return this;
    };
    LayoutElement.prototype.animate = function(properties, options) {
      if (options == null) {
        options = {};
      }
      this.get().animate(properties, options);
      return this;
    };
    return LayoutElement;
  })();
  if (typeof window !== "undefined" && window !== null) {
    window.LayoutElement = LayoutElement;
  }
  InteractiveWidget = (function() {
    function InteractiveWidget(name, path, config) {
      this.name = name;
      this.path = path;
      this.config = config;
    }
    return InteractiveWidget;
  })();
  SiteSection = (function() {
    function SiteSection(name, path, config) {
      this.name = name;
      this.path = path;
      this.config = config;
    }
    return SiteSection;
  })();
  FatCatMap = (function() {
    function FatCatMap(config) {
      this.config = config;
      this.api = new CoreAPIBridge;
      this.agent = new CoreAgentAPI;
      this.agent.discover();
      this.state = new CoreStateAPI;
      this.state.events.registerEvent('CORE_INIT');
      this.state.events.registerEvent('RPC_INIT');
      this.state.events.registerEvent('API_INIT');
      this.state.events.registerEvent('CORE_READY');
      this.state.events.registerEvent('DRIVER_REGISTERED');
      this.state.events.registerEvent('REGISTER_ELEMENT');
      this.state.events.registerEvent('PLATFORM_READY');
      this.user = new CoreUserAPI;
      this.rpc = new CoreRPCAPI;
      this.sys = new CoreSysAPI;
      this.dev = new CoreDevAPI;
      return this;
    }
    return FatCatMap;
  })();
  window.fatcatmap = new FatCatMap();
}).call(this);
