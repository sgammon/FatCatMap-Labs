(function() {
  var AdvancedStorageDriver, CoreAPI, CoreAPIBridge, CoreAgentAPI, CoreDevAPI, CoreLiveAPI, CoreModelAPI, CoreRPCAPI, CoreStateAPI, CoreSysAPI, CoreUserAPI, FatCatMap, LocalModel, ModelCollection, RPCAPI, RPCAdapter, RPCRequest, RemoteModel, SiteSection, StorageDriver;
  var __bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; }, __hasProp = Object.prototype.hasOwnProperty, __extends = function(child, parent) {
    for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; }
    function ctor() { this.constructor = child; }
    ctor.prototype = parent.prototype;
    child.prototype = new ctor;
    child.__super__ = parent.prototype;
    return child;
  }, __slice = Array.prototype.slice, __indexOf = Array.prototype.indexOf || function(item) {
    for (var i = 0, l = this.length; i < l; i++) {
      if (this[i] === item) return i;
    }
    return -1;
  };
  CoreAPI = (function() {
    function CoreAPI(name, path, config) {
      this.name = name;
      this.path = path;
      this.config = config;
    }
    return CoreAPI;
  })();
  CoreDevAPI = (function() {
    __extends(CoreDevAPI, CoreAPI);
    function CoreDevAPI(fcm) {
      this.verbose = __bind(this.verbose, this);
      this.error = __bind(this.error, this);
      this.eventlog = __bind(this.eventlog, this);
      this.log = __bind(this.log, this);
      this.setDebug = __bind(this.setDebug, this);      this.config = {};
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
              setInterval(function() {
                return stats.update();
              }, 1000 / 60);
            },
            hide: function(selector) {
              $('#js_fps_stats').hide();
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
    CoreDevAPI.prototype.setDebug = function(debug) {
      this.debug = debug;
      return console.log("[CoreDev] Debug has been set.", this.debug);
    };
    CoreDevAPI.prototype.log = function() {
      var context, message, module;
      module = arguments[0], message = arguments[1], context = 3 <= arguments.length ? __slice.call(arguments, 2) : [];
      if (!(context != null)) {
        context = '{no context}';
      }
      if (this.debug.logging === true) {
        console.log.apply(console, ["[" + module + "] INFO: " + message].concat(__slice.call(context)));
      }
    };
    CoreDevAPI.prototype.eventlog = function() {
      var context, sublabel;
      sublabel = arguments[0], context = 2 <= arguments.length ? __slice.call(arguments, 1) : [];
      if (!(context != null)) {
        context = '{no context}';
      }
      if (this.debug.eventlog === true) {
        console.log.apply(console, ["[EventLog] " + sublabel].concat(__slice.call(context)));
      }
    };
    CoreDevAPI.prototype.error = function() {
      var context, message, module;
      module = arguments[0], message = arguments[1], context = 3 <= arguments.length ? __slice.call(arguments, 2) : [];
      if (this.debug.logging === true) {
        console.log.apply(console, ["[" + module + "] ERROR: " + message].concat(__slice.call(context)));
      }
    };
    CoreDevAPI.prototype.verbose = function() {
      var context, message, module;
      module = arguments[0], message = arguments[1], context = 3 <= arguments.length ? __slice.call(arguments, 2) : [];
      if (this.debug.verbose === true) {
        this.log.apply(this, [module, message].concat(__slice.call(context)));
      }
    };
    return CoreDevAPI;
  })();
  CoreSysAPI = (function() {
    __extends(CoreSysAPI, CoreAPI);
    function CoreSysAPI(fcm) {
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
        register: __bind(function(module, name, hook, preference, initialized, callback) {
          var context;
          if (!(this.drivers.registry[module] != null)) {
            this.drivers.registry[module] = {};
          }
          this.drivers.registry[module][name] = {
            initialized: initialized,
            preference: preference,
            registered: true,
            hook_point: hook,
            init_callback: callback
          };
          context = {
            module: module,
            name: name,
            hook: hook
          };
          fcm.state.events.triggerEvent('DRIVER_REGISTERED', context);
        }, this),
        resolve: function(module, name) {
          var cp, option, option_name, preference, selection, _default;
          if (!(this.registry[module] != null)) {
            return false;
          } else {
            if (name != null) {
              if (!(this.registry[module][name] != null)) {
                return false;
              } else {
                return this.registry[module][name].hook_point;
              }
            } else {
              _default = null;
              selection = null;
              preference = 0;
              for (option_name in this.registry[module]) {
                option = this.registry[module][option_name];
                if (option.preference != null) {
                  if (typeof option.preference === 'function') {
                    if (typeof $ !== "undefined" && $ !== null) {
                      cp = option.preference($.fatcatmap);
                    } else {
                      cp = option.preference(window.fatcatmap);
                    }
                  } else {
                    cp = option.preference;
                  }
                  if (cp !== null && typeof cp !== 'boolean') {
                    if (cp > preference) {
                      selection = option;
                    }
                  } else {
                    if (cp === false) {
                      continue;
                    } else if (cp === true) {
                      selection = option;
                    } else {
                      continue;
                    }
                  }
                } else {
                  _default = option;
                }
              }
              if (selection !== null) {
                return selection.hook_point;
              } else {
                if (_default !== null) {
                  return _default.hook_point;
                } else {
                  return null;
                }
              }
            }
          }
        }
      };
    }
    return CoreSysAPI;
  })();
  CoreAgentAPI = (function() {
    __extends(CoreAgentAPI, CoreAPI);
    function CoreAgentAPI(fcm) {
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
      if (index === -1) {} else {
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
  CoreStateAPI = (function() {
    __extends(CoreStateAPI, CoreAPI);
    function CoreStateAPI(fcm) {
      this.ui = {
        indicators: {
          globalIndicatorQueue: 0,
          currentGlobalProgress: 0,
          startSpinner: function() {
            if (this.globalIndicatorQueue === 0) {
              $('#globalActivityIndicator').animate({
                opacity: 1
              }).removeClass('hidden');
            }
            return this.globalIndicatorQueue++;
          },
          stopSpinner: function() {
            this.globalIndicatorQueue--;
            if (this.globalIndicatorQueue === 0) {
              return $('#globalActivityIndicator').animate({
                opacity: 0
              }, 'fast', function() {
                return $(this).addClass('hidden');
              });
            }
          },
          setGlobalProgressBar: function(progress) {
            if (!(progress != null)) {
              progress = this.currentGlobalProgress + 10;
            }
            if (progress >= 100) {
              $('#globalProgress').animate({
                width: $('#toploader').width()
              }, function() {
                return $('#globalProgress').css({
                  width: 0
                });
              });
            } else {
              $('#globalProgress').animate({
                width: $('#toploader').width() * (progress / 100)
              });
            }
            return this.currentGlobalProgress = progress;
          }
        }
      };
      this.events = {
        registry: [],
        callchain: {},
        history: [],
        registerEvent: __bind(function(name) {
          this.events.registry.push(name);
          this.events.callchain[name] = [];
          if (fcm.dev.debug.eventlog === true) {
            fcm.dev.verbose('EventLog', "Event Registered: " + name);
          }
          return this;
        }, this),
        registerHook: __bind(function(_event, fn, once) {
          var calltask;
          if (typeof once === null) {
            once = false;
          }
          calltask = {
            executed: false,
            callback: function(context) {
              return fn(context);
            },
            runonce: once
          };
          this.events.callchain[_event].push(calltask);
          if (fcm.dev.debug.verbose === true) {
            return fcm.dev.eventlog("Hook Registered", fn, "on event", _event);
          }
        }, this),
        triggerEvent: __bind(function(_event, context) {
          var calltask, result, result_calltask, _results;
          fcm.dev.eventlog("Event Triggered", _event, context || '{no context}');
          if (typeof this.events.callchain[_event] !== null) {
            if (this.events.callchain[_event].length > 0) {
              _results = [];
              for (calltask in this.events.callchain[_event]) {
                if (this.events.callchain[_event][calltask].executed === true && this.events.callchain[_event][calltask].runonce === true) {
                  continue;
                } else {
                  try {
                    if (fcm.dev.debug.eventlog === true && fcm.dev.debug.verbose === true) {
                      fcm.dev.eventlog("Callchain", calltask, this.events.callchain[_event]);
                    }
                    result = this.events.callchain[_event][calltask].callback(context);
                    result_calltask = {
                      event: _event,
                      context: context,
                      task: this.events.callchain[_event][calltask],
                      result: result
                    };
                  } catch (error) {
                    result_calltask = {
                      event: _event,
                      context: context,
                      task: this.events.callchain[_event][calltask],
                      error: error
                    };
                    fcm.dev.error('Events', 'Calltask failed with error: ', error, result_calltask);
                  } finally {
                    this.events.history.push(result_calltask);
                    this.events.callchain[_event][calltask].executed = true;
                  }
                }
              }
              return _results;
            }
          }
        }, this)
      };
      this.session = {
        _id: null,
        _token: null,
        _tokenHistory: [],
        getID: function() {
          if (this._id != null) {
            return this._id;
          } else {
            return false;
          }
        },
        init: function(id, token) {
          this._id = id;
          this._token = token;
          return this._tokenHistory.push(token);
        },
        renew: function(token) {
          this._token = token;
          return this._tokenHistory.push(token);
        }
      };
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
        register: __bind(function(id, element) {
          var context;
          this.events.registry[id] = element;
          context = {
            id: id,
            element: element
          };
          fcm.state.events.triggerEvent('REGISTER_ELEMENT', context);
          return this.elements.registry[id];
        }, this),
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
      /* === Register State Events === */
      this.events.registerEvent('SESSION_INIT');
      this.events.registerEvent('SESSION_RENEW');
      this.events.registerEvent('SESSION_CHECKIN');
      this.events.registerEvent('SESSION_EXPIRE');
      this.events.registerEvent('GLOBAL_ACTIVITY');
      this.events.registerEvent('GLOBAL_ACTIVITY_FINISH');
      this.events.registerHook('GLOBAL_ACTIVITY', __bind(function() {
        return this.ui.indicators.startSpinner();
      }, this));
      this.events.registerHook('GLOBAL_ACTIVITY_FINISH', __bind(function() {
        return this.ui.indicators.stopSpinner();
      }, this));
    }
    return CoreStateAPI;
  })();
  LocalModel = (function() {
    __extends(LocalModel, Backbone.Model);
    function LocalModel() {
      LocalModel.__super__.constructor.apply(this, arguments);
    }
    LocalModel.prototype._type = function() {
      return 'local';
    };
    return LocalModel;
  })();
  RemoteModel = (function() {
    __extends(RemoteModel, Backbone.Model);
    function RemoteModel() {
      RemoteModel.__super__.constructor.apply(this, arguments);
    }
    RemoteModel.prototype._type = function() {
      return 'remote';
    };
    return RemoteModel;
  })();
  ModelCollection = (function() {
    __extends(ModelCollection, Backbone.Collection);
    function ModelCollection() {
      ModelCollection.__super__.constructor.apply(this, arguments);
    }
    ModelCollection.prototype._noop = function() {};
    return ModelCollection;
  })();
  CoreModelAPI = (function() {
    __extends(CoreModelAPI, CoreAPI);
    function CoreModelAPI(fcm) {
      window.Models = {};
      fcm.state.events.registerEvent('MODEL_DEFINE');
      fcm.state.events.registerEvent('MODEL_SYNC');
      fcm.state.events.registerEvent('ENTITY_CREATE');
      fcm.state.events.registerEvent('ENTITY_PUT');
      fcm.state.events.registerEvent('ENTITY_GET');
      fcm.state.events.registerEvent('ENTITY_DELETE');
      this.local = {
        schema: {}
      };
      this.remote = {
        schema: {}
      };
      this.sync = {
        _backboneSync: __bind(function(method, model, options) {
          var config, error, failure_callback, success, success_callback;
          success = options[0], error = options[1], config = 3 <= options.length ? __slice.call(options, 2) : [];
          switch (method) {
            case "create":
              fcm.state.events.triggerEvent('ENTITY_CREATE', {
                model: model,
                options: options
              });
              return fcm.rpc.api.data.create({
                object: model
              }).fulfill({
                success: success_callback,
                failure: failure_callback
              }, config);
            case "read":
              fcm.state.events.triggerEvent('ENTITY_GET', {
                model: model,
                options: options
              });
              success_callback = options[0], failure_callback = options[1], config = 3 <= options.length ? __slice.call(options, 2) : [];
              return fcm.rpc.api.data.get({
                key: model.id
              }).fulfill({
                success: success_callback,
                failure: failure_callback
              }, config);
            case "update":
              fcm.state.events.triggerEvent('ENTITY_PUT', {
                model: model,
                options: options
              });
              success_callback = options[0], failure_callback = options[1], config = 3 <= options.length ? __slice.call(options, 2) : [];
              return fcm.rpc.api.data.update({
                key: model.id,
                object: model.toJSON()
              }).fulfill({
                success: success_callback,
                failure: failure_callback
              }, config);
            case "delete":
              fcm.state.events.triggerEvent('ENTITY_DELETE', {
                model: model,
                options: options
              });
              success_callback = options[0], failure_callback = options[1], config = 3 <= options.length ? __slice.call(options, 2) : [];
              return fcm.rpc.api.data["delete"]({
                key: model.id
              }).fulfill({
                success: success_callback,
                failure: failure_callback
              }, config);
            default:
              return fcm.rpc.dev.error('Model', 'Backbone bridge model sync got an unrecognized method.', {
                method: method,
                model: model,
                options: options
              });
          }
        }, this)
      };
      Backbone.sync = this.sync;
    }
    return CoreModelAPI;
  })();
  window.LocalModel = LocalModel;
  window.RemoteModel = RemoteModel;
  window.ModelCollection = ModelCollection;
  CoreAPIBridge = (function() {
    __extends(CoreAPIBridge, CoreAPI);
    function CoreAPIBridge(fcm) {
      fcm.state.events.registerEvent('STORAGE_READ');
      fcm.state.events.registerEvent('STORAGE_WRITE');
      fcm.state.events.registerEvent('STORAGE_CLEAR');
      fcm.state.events.registerEvent('STORAGE_DELETE');
      fcm.state.events.registerEvent('STORAGE_DB_LOAD');
      fcm.state.events.registerEvent('STORAGE_DB_CLOSE');
      fcm.state.events.registerEvent('STORAGE_DB_QUERY');
      fcm.state.events.registerEvent('STORAGE_DB_CREATE');
      fcm.state.events.registerEvent('STORAGE_DB_DELETE');
      fcm.state.events.registerEvent('STORAGE_DB_SETVERSION');
      fcm.state.events.registerEvent('STORAGE_DB_TRANSACTION');
      fcm.state.events.registerEvent('STORAGE_COLLECTION_CLEAR');
      fcm.state.events.registerEvent('STORAGE_COLLECTION_CREATE');
      fcm.state.events.registerEvent('STORAGE_COLLECTION_DELETE');
      this.storage = {
        local: {
          _driver: null,
          _resolveDriver: __bind(function() {
            return this.storage.local._driver = $.fatcatmap.sys.drivers.resolve('localstorage');
          }, this),
          get: __bind(function(key) {
            if (this.storage.local._driver !== null) {
              fcm.state.events.triggerEvent('STORAGE_READ', {
                type: 'local',
                mode: 'key',
                key: key
              });
              return this.storage.local._driver.getValueByKey(key);
            } else {
              return null;
            }
          }, this),
          set: __bind(function(key, value) {
            if (this.storage.local._driver !== null) {
              fcm.state.events.triggerEvent('STORAGE_WRITE', {
                type: 'local',
                key: key,
                value: value
              });
              return this.storage.local._driver.setValueByKey(key, value);
            } else {
              return null;
            }
          }, this),
          "delete": __bind(function(key) {
            if (this.storage.local._driver !== null) {
              fcm.state.events.triggerEvent('STORAGE_DELETE', {
                type: 'local',
                key: key
              });
              return this.storage.local._driver.deleteByKey(key);
            } else {
              return null;
            }
          }, this),
          clear: __bind(function() {
            if (this.storage.local._driver !== null) {
              fcm.state.events.triggerEvent('STORAGE_CLEAR', {
                type: 'local'
              });
              return this._driver.nuke();
            } else {
              return null;
            }
          }, this),
          all: __bind(function() {
            if (this.storage.local._driver !== null) {
              fcm.state.events.triggerEvent('STORAGE_READ', {
                type: 'local',
                mode: 'all'
              });
              return this.storage.local._driver.allValues();
            } else {
              return null;
            }
          }, this)
        },
        session: {
          _driver: null,
          _resolveDriver: __bind(function() {
            return this.storage.session._driver = $.fatcatmap.sys.drivers.resolve('sessionstorage');
          }, this),
          get: __bind(function(key) {
            if (this.storage.session._driver !== null) {
              fcm.state.events.triggerEvent('STORAGE_READ', {
                type: 'session',
                mode: 'key',
                key: key
              });
              return this.storage.session._driver.getValueByKey(key);
            } else {
              return null;
            }
          }, this),
          set: __bind(function(key, value) {
            if (this.storage.session._driver !== null) {
              fcm.state.events.triggerEvent('STORAGE_WRITE', {
                type: 'session',
                key: key,
                value: value
              });
              return this.storage.session._driver.setValueByKey(key, value);
            } else {
              return null;
            }
          }, this),
          "delete": __bind(function(key) {
            if (this.storage.session._driver !== null) {
              this.fcm.state.events.triggerEvent('STORAGE_DELETE', {
                type: 'session',
                key: key
              });
              return this.storage.session._driver.deleteByKey(key);
            } else {
              return null;
            }
          }, this),
          clear: __bind(function() {
            if (this.storage.session._driver !== null) {
              fcm.state.events.triggerEvent('STORAGE_CLEAR', {
                type: 'session'
              });
              return this.storage.session._driver.nuke();
            } else {
              return null;
            }
          }, this),
          all: __bind(function() {
            if (this.storage.session._driver !== null) {
              fcm.state.events.triggerEvent('STORAGE_READ', {
                type: 'session',
                mode: 'all'
              });
              return this.storage.session._driver.allValues();
            } else {
              return null;
            }
          }, this)
        },
        object: {
          _driver: null,
          _resolveDriver: __bind(function() {
            return this.storage.object._driver = $.fatcatmap.sys.drivers.resolve('objectstorage');
          }, this),
          _dbError: __bind(function(event) {
            return fcm.dev.error('Storage', 'Error encountered in OBJECT storage.', event);
          }, this),
          get: __bind(function() {
            var args, _ref;
            args = 1 <= arguments.length ? __slice.call(arguments, 0) : [];
            if (this._driver != null) {
              this._resolveDriver();
            }
            return (_ref = this._driver).get.apply(_ref, args);
          }, this),
          keys: __bind(function() {
            var args, _ref;
            args = 1 <= arguments.length ? __slice.call(arguments, 0) : [];
            if (this._driver != null) {
              this._resolveDriver();
            }
            return (_ref = this._driver).keys.apply(_ref, args);
          }, this),
          batch: __bind(function() {
            var args, _ref;
            args = 1 <= arguments.length ? __slice.call(arguments, 0) : [];
            if (this._driver != null) {
              this._resolveDriver();
            }
            return (_ref = this._driver).batch.apply(_ref, args);
          }, this),
          save: __bind(function() {
            var args, _ref;
            args = 1 <= arguments.length ? __slice.call(arguments, 0) : [];
            if (this._driver != null) {
              this._resolveDriver();
            }
            return (_ref = this._driver).save.apply(_ref, args);
          }, this),
          exists: __bind(function() {
            var args, _ref;
            args = 1 <= arguments.length ? __slice.call(arguments, 0) : [];
            if (this._driver != null) {
              this._resolveDriver();
            }
            return (_ref = this._driver).exists.apply(_ref, args);
          }, this),
          each: __bind(function() {
            var args, _ref;
            args = 1 <= arguments.length ? __slice.call(arguments, 0) : [];
            if (this._driver != null) {
              this._resolveDriver();
            }
            return (_ref = this._driver).each.apply(_ref, args);
          }, this),
          all: __bind(function() {
            var args, _ref;
            args = 1 <= arguments.length ? __slice.call(arguments, 0) : [];
            if (this._driver != null) {
              this._resolveDriver();
            }
            return (_ref = this._driver).all.apply(_ref, args);
          }, this),
          remove: __bind(function() {
            var args, _ref;
            args = 1 <= arguments.length ? __slice.call(arguments, 0) : [];
            if (this._driver != null) {
              this._resolveDriver();
            }
            return (_ref = this._driver).remove.apply(_ref, args);
          }, this),
          nuke: __bind(function() {
            var args, _ref;
            args = 1 <= arguments.length ? __slice.call(arguments, 0) : [];
            if (this._driver != null) {
              this._resolveDriver();
            }
            return (_ref = this._driver).nuke.apply(_ref, args);
          }, this)
        }
      };
      this.layout = {
        register: __bind(function(id, element) {
          element.register(id);
          return fcm.state.elements.register(id, element);
        }, this),
        render: __bind(function(id, element) {}, this),
        renderTemplate: __bind(function() {
          var context, id;
          id = arguments[0], context = 2 <= arguments.length ? __slice.call(arguments, 1) : [];
        }, this)
      };
      fcm.state.events.registerEvent('MAP_REGISTERED');
      fcm.state.events.registerEvent('MAP_DATA_CHANGE');
      fcm.state.events.registerEvent('MAP_NODE_ADDED');
      fcm.state.events.registerEvent('MAP_EDGE_ADDED');
      fcm.state.events.registerEvent('MAP_DRAW');
      fcm.state.events.registerEvent('MAP_SHIFT_ORIGIN');
      this.visualizer = {
        graph: {
          currentGraph: null,
          register: function(currentGraph) {
            this.currentGraph = currentGraph;
          },
          showMore: function(node) {
            var list, neighbors;
            $('#nodeDetails #node_label').text(node.label);
            $('#nodeDetails #node_kind').text(node.kind);
            list = '';
            neighbors = this.currentGraph.index.neighbors_by_node[node.key.encoded];
            _.each(neighbors, __bind(function(neighbor) {
              return list += '<li><a href="#">' + neighbor.label + '</a></li>';
            }, this));
            return $('#nodeDetails #node_outgoing_edges').html(list);
          }
        }
      };
    }
    return CoreAPIBridge;
  })();
  CoreUserAPI = (function() {
    __extends(CoreUserAPI, CoreAPI);
    function CoreUserAPI(fcm) {
      fcm.state.events.registerEvent('USER_CHANGE');
      this.current_user = null;
      this.is_user_admin = null;
      this.login_url = null;
      this.logout_url = null;
    }
    CoreUserAPI.prototype.setUserInfo = function(user_properties) {
      var context, fcm;
      context = {};
      if (user_properties['current_user'] !== null) {
        this.current_user = user_properties['current_user'];
        context.current_user = this.current_user;
      }
      if (user_properties['is_user_admin'] !== null) {
        this.is_user_admin = user_properties['is_user_admin'];
        context.is_user_admin = this.is_user_admin;
      }
      if (user_properties['login_url'] !== null) {
        this.login_url = user_properties['login_url'];
        context.login_url = this.login_url;
      }
      if (user_properties['logout_url'] !== null) {
        this.logout_url = user_properties['logout_url'];
        context.logout_url = this.logout_url;
      }
      if (typeof $ !== "undefined" && $ !== null) {
        fcm = $.fatcatmap;
      } else {
        fcm = window.fatcatmap;
      }
      return fcm.state.events.triggerEvent('USER_CHANGE', context);
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
          this[method] = this._buildRPCMethod(method, base_uri, config);
        }
      }
    }
    RPCAPI.prototype._buildRPCMethod = function(method, base_uri, config) {
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
          var fcm, request;
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
          if (typeof $ !== "undefined" && $ !== null) {
            fcm = $.fatcatmap;
          } else {
            fcm = window.fatcatmap;
          }
          request = fcm.rpc.api.createRPCRequest({
            method: method,
            api: api,
            params: params || {},
            opts: opts || {},
            async: async || false
          });
          if (callbacks !== null) {
            return request.fulfill(callbacks);
          } else {
            return request;
          }
        }, this)(params, callbacks, async, opts);
      }, this);
      if (typeof $ !== "undefined" && $ !== null) {
        $.fatcatmap.rpc.registerAPIMethod(api, method, base_uri, config);
      } else {
        window.fatcatmap.rpc.registerAPIMethod(api, method, base_uri, config);
      }
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
        dataType: 'json',
        contentType: 'application/json'
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
      var callbacks, config, defaultFailureCallback, defaultSuccessCallback;
      callbacks = arguments[0], config = 2 <= arguments.length ? __slice.call(arguments, 1) : [];
      if (!(callbacks != null ? callbacks.success : void 0)) {
        defaultSuccessCallback = __bind(function(context) {
          return $.fatcatmap.dev.log('RPC', 'RPC succeeded but had no success callback.', this);
        }, this);
        callbacks.success = defaultSuccessCallback;
      }
      if (!(callbacks != null ? callbacks.failure : void 0)) {
        defaultFailureCallback = __bind(function(context) {
          return $.fatcatmap.dev.error('RPC', 'RPC failed but had no failure callback.', this);
        }, this);
        callbacks.failure = defaultFailureCallback;
      }
      return window.fatcatmap.rpc.api.fulfillRPCRequest(config, this, callbacks);
    };
    RPCRequest.prototype.setAsync = function(async) {
      var _ref, _ref2;
      if ((_ref = this.ajax) != null) {
        if ((_ref2 = _ref.async) == null) {
          _ref.async = async;
        }
      }
      return this;
    };
    RPCRequest.prototype.setOpts = function(opts) {
      var _ref, _ref2;
      if ((_ref = this.envelope) != null) {
        if ((_ref2 = _ref.opts) == null) {
          _ref.opts = opts;
        }
      }
      return this;
    };
    RPCRequest.prototype.setAgent = function(agent) {
      var _ref, _ref2;
      if ((_ref = this.envelope) != null) {
        if ((_ref2 = _ref.agent) == null) {
          _ref.agent = agent;
        }
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
    __extends(CoreRPCAPI, CoreAPI);
    function CoreRPCAPI(fcm) {
      var original_xhr;
      fcm.state.events.registerEvent('RPC_CREATE');
      fcm.state.events.registerEvent('RPC_FULFILL');
      fcm.state.events.registerEvent('RPC_SUCCESS');
      fcm.state.events.registerEvent('RPC_ERROR');
      fcm.state.events.registerEvent('RPC_COMPLETE');
      fcm.state.events.registerEvent('RPC_PROGRESS');
      if (window.amplify != null) {
        fcm.dev.verbose('RPC', 'AmplifyJS detected. Registering.');
        fcm.sys.drivers.register('transport', 'amplify', window.amplify, true, true);
      }
      this.base_rpc_uri = '/_api/rpc';
      original_xhr = $.ajaxSettings.xhr;
      this.internals = {
        transports: {
          xhr: {
            factory: __bind(function() {
              var req;
              req = original_xhr();
              if (req) {
                if (typeof req.addEventListener === 'function') {
                  req.addEventListener("progress", __bind(function(ev) {
                    return $.fatcatmap.state.events.triggerEvent('RPC_PROGRESS', {
                      event: ev
                    });
                  }, this), false);
                }
              }
              return req;
            }, this)
          }
        }
      };
      $.ajaxSetup({
        global: true,
        xhr: __bind(function() {
          return this.internals.transports.xhr.factory();
        }, this)
      });
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
        decodeRPCResponse: function(data, status, xhr, success, error) {
          return success(data, status);
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
          if (typeof $ !== "undefined" && $ !== null) {
            $.fatcatmap.dev.log('RPC', 'New Request', request, config);
          } else {
            window.fatcatmap.dev.log('RPC', 'New Request', request, config);
          }
          request.setAction(this._assembleRPCURL(request.method, request.api, this.action_prefix, this.base_rpc_uri));
          return request;
        },
        fulfillRPCRequest: function(config, request, callbacks) {
          var context;
          if (typeof $ !== "undefined" && $ !== null) {
            $.fatcatmap.dev.log('RPC', 'Fulfill', config, request, callbacks);
          } else {
            window.fatcatmap.dev.log('RPC', 'Fulfill', config, request, callbacks);
          }
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
          context = {
            config: config,
            request: request,
            callbacks: callbacks
          };
          fcm.state.events.triggerEvent('RPC_FULFILL', context);
          (function(request, callbacks) {
            var amplify, fatcatmap, xhr, xhr_action, xhr_settings;
            fatcatmap = window.fatcatmap;
            xhr_settings = {
              resourceId: request.api + '.' + request.method,
              url: request.action,
              data: JSON.stringify(request.payload()),
              async: request.ajax.async,
              global: request.ajax.global,
              type: request.ajax.http_method,
              crossDomain: request.ajax.crossDomain,
              dataType: request.ajax.dataType,
              processData: false,
              ifModified: request.ajax.ifModified,
              contentType: request.ajax.contentType,
              beforeSend: __bind(function(xhr, settings) {
                fatcatmap.rpc.api.history[request.envelope.id].xhr = xhr;
                if (callbacks != null) {
                  if (typeof callbacks.status === "function") {
                    callbacks.status('beforeSend');
                  }
                }
                return xhr;
              }, this),
              error: __bind(function(xhr, status, error) {
                if (callbacks != null) {
                  if (typeof callbacks.status === "function") {
                    callbacks.status('error');
                  }
                }
                fatcatmap.dev.error('RPC', 'Error: ', {
                  error: error,
                  status: status,
                  xhr: xhr
                });
                fatcatmap.rpc.api.lastFailure = error;
                fatcatmap.rpc.api.history[request.envelope.id].xhr = xhr;
                fatcatmap.rpc.api.history[request.envelope.id].status = status;
                fatcatmap.rpc.api.history[request.envelope.id].failure = error;
                context = {
                  xhr: xhr,
                  status: status,
                  error: error
                };
                fatcatmap.state.events.triggerEvent('RPC_ERROR', context);
                fcm.state.events.triggerEvent('RPC_COMPLETE', context);
                return callbacks != null ? typeof callbacks.failure === "function" ? callbacks.failure(error) : void 0 : void 0;
              }, this),
              success: __bind(function(data, status, xhr) {
                if (data.status === 'ok') {
                  if (callbacks != null) {
                    if (typeof callbacks.status === "function") {
                      callbacks.status('success');
                    }
                  }
                  fatcatmap.dev.log('RPC', 'Success', data, status, xhr);
                  fatcatmap.rpc.api.lastResponse = data;
                  fatcatmap.rpc.api.history[request.envelope.id].xhr = xhr;
                  fatcatmap.rpc.api.history[request.envelope.id].status = status;
                  fatcatmap.rpc.api.history[request.envelope.id].response = data;
                  context = {
                    xhr: xhr,
                    status: status,
                    data: data
                  };
                  fcm.state.events.triggerEvent('RPC_SUCCESS', context);
                  fcm.state.events.triggerEvent('RPC_COMPLETE', context);
                  fatcatmap.dev.verbose('RPC', 'Success callback', callbacks);
                  return callbacks != null ? typeof callbacks.success === "function" ? callbacks.success(data.response.content, data.response.type, data) : void 0 : void 0;
                } else if (data.status === 'failure') {
                  if (callbacks != null) {
                    if (typeof callbacks.status === "function") {
                      callbacks.status('error');
                    }
                  }
                  fatcatmap.dev.error('RPC', 'Error: ', {
                    error: error,
                    status: status,
                    xhr: xhr
                  });
                  fatcatmap.rpc.api.lastFailure = error;
                  fatcatmap.rpc.api.history[request.envelope.id].xhr = xhr;
                  fatcatmap.rpc.api.history[request.envelope.id].status = status;
                  fatcatmap.rpc.api.history[request.envelope.id].failure = error;
                  context = {
                    xhr: xhr,
                    status: status,
                    error: error
                  };
                  fatcatmap.state.events.triggerEvent('RPC_ERROR', context);
                  fcm.state.events.triggerEvent('RPC_COMPLETE', context);
                  return callbacks != null ? typeof callbacks.failure === "function" ? callbacks.failure(error) : void 0 : void 0;
                }
              }, this),
              statusCode: {
                404: function() {
                  fatcatmap.dev.error('RPC', 'HTTP/404', 'Could not resolve RPC action URI.');
                  return fatcatmap.state.events.triggerEvent('RPC_ERROR', {
                    message: 'RPC 404: Could not resolve RPC action URI.',
                    code: 404
                  });
                },
                403: function() {
                  fatcatmap.dev.error('RPC', 'HTTP/403', 'Not authorized to access the specified endpoint.');
                  return fatcatmap.state.events.triggerEvent('RPC_ERROR', {
                    message: 'RPC 403: Not authorized to access the specified endpoint.',
                    code: 403
                  });
                },
                500: function() {
                  fatcatmap.dev.error('RPC', 'HTTP/500', 'Internal server error.');
                  return fatcatmap.state.events.triggerEvent('RPC_ERROR', {
                    message: 'RPC 500: Woops! Something went wrong. Please try again.',
                    code: 500
                  });
                }
              }
            };
            amplify = fatcatmap.sys.drivers.resolve('transport', 'amplify');
            if ((amplify != null) && amplify === !false) {
              fatcatmap.dev.verbose('RPC', 'Fulfilling with AmplifyJS adapter.');
              xhr_action = amplify.request;
              xhr = xhr_action(xhr_settings);
            } else {
              fatcatmap.dev.verbose('RPC', 'Fulfilling with AJAX adapter.');
              xhr = $.ajax(xhr_settings);
            }
            return fatcatmap.dev.verbose('RPC', 'Resulting XHR: ', xhr);
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
      fcm.state.events.registerHook('RPC_FULFILL', function() {
        return $.fatcatmap.state.events.triggerEvent('GLOBAL_ACTIVITY');
      });
      fcm.state.events.registerHook('RPC_COMPLETE', function() {
        return $.fatcatmap.state.events.triggerEvent('GLOBAL_ACTIVITY_FINISH');
      });
      fcm.state.events.registerHook('RPC_PROGRESS', function(event) {
        return console.log('progress', event);
      });
    }
    CoreRPCAPI.prototype.registerAPIMethod = function(api, name, base_uri, config) {
      var amplify, base_settings, fcm, resourceId;
      if (typeof $ !== "undefined" && $ !== null) {
        fcm = $.fatcatmap;
      } else {
        fcm = window.fatcatmap;
      }
      amplify = fcm.sys.drivers.resolve('transport', 'amplify');
      if (amplify !== false) {
        fcm.dev.log('RPCAPI', 'Registering request procedure "' + api + '.' + name + '" with AmplifyJS.');
        resourceId = api + '.' + name;
        base_settings = {
          type: 'POST',
          dataType: 'json',
          contentType: 'application/json',
          url: this.api._assembleRPCURL(name, api, null, base_uri),
          decoder: this.api.decodeRPCResponse
        };
        if (config.caching != null) {
          if (config.caching === true) {
            base_settings.caching = 'persist';
          }
          return amplify.request.define(resourceId, "ajax", base_settings);
        } else {
          return amplify.request.define(resourceId, "ajax", base_settings);
        }
      }
    };
    return CoreRPCAPI;
  })();
  window.RPCAPI = RPCAPI;
  window.RPCAdapter = RPCAdapter;
  window.RPCRequest = RPCRequest;
  SiteSection = (function() {
    function SiteSection(name, path, config) {
      this.name = name;
      this.path = path;
      this.config = config;
    }
    return SiteSection;
  })();
  CoreLiveAPI = (function() {
    __extends(CoreLiveAPI, CoreAPI);
    function CoreLiveAPI(fcm) {
      this.fcm = fcm;
      this.onClose = __bind(this.onClose, this);
      this.onError = __bind(this.onError, this);
      this.onMessage = __bind(this.onMessage, this);
      this.onOpen = __bind(this.onOpen, this);
      this.dispatch = __bind(this.dispatch, this);
      this.listen = __bind(this.listen, this);
      this.openChannel = __bind(this.openChannel, this);
      this.defaultLiveFailureHandler = __bind(this.defaultLiveFailureHandler, this);
      this.defaultLiveSuccessHandler = __bind(this.defaultLiveSuccessHandler, this);
      this.fcm.state.events.registerEvent('CHANNEL_OPEN');
      this.fcm.state.events.registerEvent('CHANNEL_MESSAGE');
      this.fcm.state.events.registerEvent('CHANNEL_ERROR');
      this.fcm.state.events.registerEvent('CHANNEL_CLOSE');
      this.token = null;
      this.channel = null;
      this.socket = null;
      this.handlers = {
        _registry: {
          "default": this.defaultLiveHandler
        },
        add: function(type, callback) {
          this.registry[type] = callback;
        },
        remove: function(type) {
          this.registry[type] = null;
        },
        resolve: function(type) {
          if (__indexOf.call(this.registry, type) >= 0) {
            return this.registry[type];
          } else {
            return false;
          }
        },
        handle: function(type, data) {
          return this.registry[type](data);
        }
      };
    }
    CoreLiveAPI.prototype.defaultLiveSuccessHandler = function() {
      var message, _ref;
      message = 1 <= arguments.length ? __slice.call(arguments, 0) : [];
      (_ref = this.fcm.dev.debug).log.apply(_ref, ['CoreLive', 'Live API received unhandled successful push message.'].concat(__slice.call(message)));
    };
    CoreLiveAPI.prototype.defaultLiveFailureHandler = function() {
      var message, _ref;
      message = 1 <= arguments.length ? __slice.call(arguments, 0) : [];
      (_ref = this.fcm.dev.debug).log.apply(_ref, ['CoreLive', 'Live API received unhandled push message failure.'].concat(__slice.call(message)));
    };
    CoreLiveAPI.prototype.openChannel = function(token) {
      var _ref;
      this.token = token;
      this.fcm.dev.debug.log('CoreLive', 'Opening channel.', this.token);
      try {
        this.channel = typeof goog !== "undefined" && goog !== null ? (_ref = goog.appengine) != null ? new _ref.Channel(this.token) : void 0 : void 0;
        this.socket = this.channel.open();
        this.socket.onopen = this.onOpen;
        this.socket.onmessage = this.onMessage;
        this.socket.onerror = this.onError;
        this.socket.onclose = this.onClose;
      } catch (error) {
        this.fcm.dev.debug.error('CoreLive', 'Encountered error preparing live channel.', error);
        return {
          channel: false,
          socket: false
        };
      }
      return {
        channel: channel,
        socket: socket
      };
    };
    CoreLiveAPI.prototype.listen = function(token) {
      var channel, socket, _ref;
      if (this.channel === null && this.socket === null) {
        _ref = this.openChannel(token), channel = _ref.channel, socket = _ref.socket;
        if ((channel != null) && (socket != null)) {
          return this.fcm.state.events.registerHook('CHANNEL_OPEN', this.dispatch);
        }
      }
    };
    CoreLiveAPI.prototype.dispatch = function(message) {
      if (message.status === 'ok') {
        if (this.handlers.resolve(message.response.type)) {
          return this.handlers.handle(message.response.type, message);
        } else {
          this.defaultLiveSuccessHandler(message);
        }
      } else {
        if (this.handlers.resolve(message.response.type)) {
          return this.handlers.handle(message.error.type, message);
        } else {
          this.defaultLiveFailureHandler(message);
        }
      }
    };
    CoreLiveAPI.prototype.onOpen = function() {
      this.fcm.dev.debug.log('CoreLive', 'Channel is ready to receive live messages.');
      return this.fcm.state.events.triggerEvent('CHANNEL_OPEN');
    };
    CoreLiveAPI.prototype.onMessage = function(message) {
      this.fcm.dev.debug.verbose('CoreLive', 'Channel message received.', message);
      return this.fcm.state.events.triggerEvent('CHANNEL_MESSAGE', message);
    };
    CoreLiveAPI.prototype.onError = function(error) {
      this.fcm.dev.debug.error('CoreLive', 'Encountered channel error.', error);
      return this.fcm.state.events.triggerEvent('CHANNEL_ERROR', error);
    };
    CoreLiveAPI.prototype.onClose = function() {
      this.fcm.dev.debug.log('CoreLive', 'Channel has been closed.');
      return this.fcm.state.events.triggerEvent('CHANNEL_CLOSE');
    };
    return CoreLiveAPI;
  })();
  StorageDriver = (function() {
    var name, store;
    function StorageDriver() {}
    name = 'StorageDriver';
    store = {};
    StorageDriver.prototype.setup = function(name, config) {
      this.name = name;
      this.config = config;
      return $.fatcatmap.sys.drivers.register(this.name, 'native', typeof this.init === "function" ? this.init() : void 0, 999, true);
    };
    StorageDriver.prototype.getValueByKey = function(store, key) {};
    StorageDriver.prototype.setValueByKey = function(store, key, value) {};
    StorageDriver.prototype.addValueByKey = function(store, key, value) {};
    StorageDriver.prototype.deleteByKey = function(store, key) {};
    StorageDriver.prototype.nuke = function() {};
    StorageDriver.prototype.allValues = function() {};
    return StorageDriver;
  })();
  AdvancedStorageDriver = (function() {
    __extends(AdvancedStorageDriver, StorageDriver);
    function AdvancedStorageDriver() {
      AdvancedStorageDriver.__super__.constructor.apply(this, arguments);
    }
    AdvancedStorageDriver.prototype.openDatabase = function(name, callbacks) {};
    AdvancedStorageDriver.prototype.deleteDatabase = function(name, callbacks) {};
    AdvancedStorageDriver.prototype.setDatabaseVerison = function(db, version, callbacks) {};
    AdvancedStorageDriver.prototype.closeDatabase = function(db, callbacks) {};
    AdvancedStorageDriver.prototype.createCollection = function(db, name, key_path, auto_increment, callbacks) {};
    AdvancedStorageDriver.prototype.deleteCollection = function(db, name, callbacks) {};
    AdvancedStorageDriver.prototype.clearCollection = function(db, name, callbacks) {};
    return AdvancedStorageDriver;
  })();
  this.StorageDriver = StorageDriver;
  this.AdvancedStorageDriver = AdvancedStorageDriver;
  FatCatMap = (function() {
    function FatCatMap(config) {
      this.config = config;
      this.dev = new CoreDevAPI(this);
      this.sys = new CoreSysAPI(this);
      this.agent = new CoreAgentAPI(this);
      this.agent.discover();
      this.state = new CoreStateAPI(this);
      this.state.events.registerEvent('RPC_READY');
      this.state.events.registerEvent('API_READY');
      this.state.events.registerEvent('CORE_READY');
      this.state.events.registerEvent('DRIVER_REGISTERED');
      this.state.events.registerEvent('REGISTER_ELEMENT');
      this.state.events.registerEvent('PLATFORM_READY');
      this.state.events.triggerEvent('GLOBAL_ACTIVITY');
      this.state.events.registerHook('PLATFORM_READY', __bind(function() {
        return this.state.events.triggerEvent('GLOBAL_ACTIVITY_FINISH');
      }, this));
      this.model = new CoreModelAPI(this);
      this.api = new CoreAPIBridge(this);
      this.user = new CoreUserAPI(this);
      this.rpc = new CoreRPCAPI(this);
      this.live = new CoreLiveAPI(this);
      return this;
    }
    return FatCatMap;
  })();
  window.fatcatmap = new FatCatMap();
  if (typeof $ !== "undefined" && $ !== null) {
    $.extend({
      fatcatmap: window.fatcatmap
    });
  }
  window.fatcatmap.state.events.triggerEvent('CORE_READY');
}).call(this);
