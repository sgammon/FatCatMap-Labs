(function() {
  var CoreAPI, CoreAPIBridge, CoreAgentAPI, CoreDevAPI, CoreLiveAPI, CoreModelAPI, CoreRPCAPI, CoreStateAPI, CoreSysAPI, CoreUserAPI, FatCatMap, InteractiveWidget, LayoutElement, LocalModel, RPCAPI, RPCAdapter, RPCRequest, RemoteModel, SiteSection;
  var __indexOf = Array.prototype.indexOf || function(item) {
    for (var i = 0, l = this.length; i < l; i++) {
      if (this[i] === item) return i;
    }
    return -1;
  }, __bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; }, __hasProp = Object.prototype.hasOwnProperty, __extends = function(child, parent) {
    for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; }
    function ctor() { this.constructor = child; }
    ctor.prototype = parent.prototype;
    child.prototype = new ctor;
    child.__super__ = parent.prototype;
    return child;
  }, __slice = Array.prototype.slice;
  CoreAPI = (function() {
    function CoreAPI(name, path, config) {
      this.name = name;
      this.path = path;
      this.config = config;
    }
    return CoreAPI;
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
  CoreDevAPI = (function() {
    function CoreDevAPI(fcm) {
      this.verbose = __bind(this.verbose, this);;
      this.error = __bind(this.error, this);;
      this.log = __bind(this.log, this);;
      this.setDebug = __bind(this.setDebug, this);;      this.config = {};
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
    __extends(CoreDevAPI, CoreAPI);
    CoreDevAPI.prototype.setDebug = function(debug) {
      this.debug = debug;
      return console.log("[CoreDev] Debug has been set.", this.debug);
    };
    CoreDevAPI.prototype.log = function() {
      var context, message, module;
      module = arguments[0], message = arguments[1], context = 3 <= arguments.length ? __slice.call(arguments, 2) : [];
      if (context != null) {
        context = '{no context}';
      }
      if (this.debug.logging === true) {
        console.log("[" + module + "] INFO: " + message, context);
      }
    };
    CoreDevAPI.prototype.error = function() {
      var context, message, module;
      module = arguments[0], message = arguments[1], context = 3 <= arguments.length ? __slice.call(arguments, 2) : [];
      if (this.debug.logging === true) {
        console.log("[" + module + "] ERROR: " + message, context);
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
    __extends(CoreSysAPI, CoreAPI);
    return CoreSysAPI;
  })();
  CoreAgentAPI = (function() {
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
  CoreStateAPI = (function() {
    function CoreStateAPI(fcm) {
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
          if (fcm.dev.debug.eventlog === true && fcm.dev.debug.verbose === true) {
            return console.log("[EventLog] Hook Registered: ", fn, "on event", _event);
          }
        }, this),
        triggerEvent: __bind(function(_event, context) {
          var calltask, result, result_calltask, _results;
          if (fcm.dev.debug.eventlog === true) {
            console.log("[EventLog] Event Triggered: " + _event, context || '{no context}');
          }
          if (typeof this.events.callchain[_event] !== null) {
            if (this.events.callchain[_event].length > 0) {
              _results = [];
              for (calltask in this.events.callchain[_event]) {
                if (this.events.callchain[_event][calltask].executed === true && this.events.callchain[_event][calltask].runonce === true) {
                  continue;
                } else {
                  try {
                    if (fcm.dev.debug.eventlog === true && fcm.dev.debug.verbose === true) {
                      console.log("[EventLog] Callchain: ", calltask, this.events.callchain[_event]);
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
        register: __bind(function(id, element) {
          var context;
          this.events.registry[id] = element;
          context = {
            id: id,
            element: element
          };
          fcm.state.events.triggerEvent('REGISTER_ELEMENT', context);
          return this.events.registry[id];
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
    }
    __extends(CoreStateAPI, CoreAPI);
    return CoreStateAPI;
  })();
  LocalModel = (function() {
    function LocalModel() {
      LocalModel.__super__.constructor.apply(this, arguments);
    }
    __extends(LocalModel, Backbone.Model);
    LocalModel.prototype._type = function() {
      return 'local';
    };
    return LocalModel;
  })();
  RemoteModel = (function() {
    function RemoteModel() {
      RemoteModel.__super__.constructor.apply(this, arguments);
    }
    __extends(RemoteModel, Backbone.Model);
    RemoteModel.prototype._type = function() {
      return 'remote';
    };
    return RemoteModel;
  })();
  CoreModelAPI = (function() {
    function CoreModelAPI(fcm) {
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
    }
    __extends(CoreModelAPI, CoreAPI);
    CoreModelAPI.prototype.sync = function(method, model, options) {
      var config, failure_callback, fcm, success_callback;
      if (typeof $ !== "undefined" && $ !== null) {
        fcm = $.fatcatmap;
      } else {
        fcm = window.fatcatmap;
      }
      switch (method) {
        case "create":
          fcm.state.events.triggerEvent('ENTITY_CREATE', {
            model: model,
            options: options
          });
          success_callback = options[0], failure_callback = options[1], config = 3 <= options.length ? __slice.call(options, 2) : [];
          return this.fcm.rpc.api.data.create({
            object: model.toJSON()
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
          return this.fcm.rpc.api.data.get({
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
          return this.fcm.rpc.api.data.update({
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
          return this.fcm.rpc.api.data["delete"]({
            key: model.id
          }).fulfill({
            success: success_callback,
            failure: failure_callback
          }, config);
      }
    };
    return CoreModelAPI;
  })();
  window.LocalModel = LocalModel;
  window.RemoteModel = RemoteModel;
  CoreAPIBridge = (function() {
    function CoreAPIBridge(fcm) {
      this.fcm = fcm;
      this.storage = {
        local: {
          _driver: null,
          _resolveDriver: __bind(function() {
            return this._driver = this.fcm.sys.drivers.resolve('localstorage');
          }, this),
          getValue: __bind(function(key) {
            if (this._driver !== null) {
              return this._driver.getValueByKey(key);
            } else {
              return false;
            }
          }, this),
          setValue: __bind(function(key, value) {
            if (this._driver !== null) {
              return this._driver.setValueByKey(key, value);
            } else {
              return false;
            }
          }, this),
          clearValues: __bind(function() {
            if (this._driver !== null) {
              return this._driver.allValues();
            } else {
              return false;
            }
          }, this)
        },
        session: {
          _driver: null,
          _resolveDriver: function() {
            return this._driver = this.fcm.sys.drivers.resolve('sessionstorage');
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
            return this._driver = this.fcm.sys.drivers.resolve('objectstorage');
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
            return this._driver = this.fcm.sys.drivers.resolve('sqlstorage');
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
        register: __bind(function(id, element) {
          element.register(id);
          return this.fcm.state.elements.register(id, element);
        }, this)
      };
      this.visualizer = {};
    }
    __extends(CoreAPIBridge, CoreAPI);
    return CoreAPIBridge;
  })();
  CoreUserAPI = (function() {
    function CoreUserAPI(fcm) {
      fcm.state.events.registerEvent('USER_CHANGE');
      this.current_user = null;
      this.is_user_admin = null;
      this.login_url = null;
      this.logout_url = null;
    }
    __extends(CoreUserAPI, CoreAPI);
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
          var fcm, request;
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
          if (callbacks != null) {
            return request.fulfill(callbacks);
          } else {
            return request;
          }
        }, this)(params, callbacks, async, opts);
      }, this);
      if (typeof $ !== "undefined" && $ !== null) {
        $.fatcatmap.rpc.registerAPIMethod(api, method, this.config);
      } else {
        window.fatcatmap.rpc.registerAPIMethod(api, method, this.config);
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
    function CoreRPCAPI(fcm) {
      fcm.state.events.registerEvent('RPC_CREATE');
      fcm.state.events.registerEvent('RPC_FULFILL');
      fcm.state.events.registerEvent('RPC_SUCCESS');
      fcm.state.events.registerEvent('RPC_ERROR');
      fcm.state.events.registerEvent('RPC_COMPLETE');
      if (window.amplify != null) {
        fcm.dev.verbose('RPC', 'AmplifyJS detected. Registering.');
        fcm.sys.drivers.register('transport', 'amplify', window.amplify, true, true);
      }
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
        decodeRPCResponse: function(data, status, xhr, success, error) {
          return success(data);
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
          var context;
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
          context = {
            config: config,
            request: request,
            callbacks: callbacks
          };
          fcm.state.events.triggerEvent('RPC_FULFILL', context);
          (function(request, callbacks) {
            var amplify, fatcatmap, xhr, xhr_settings;
            fatcatmap = window.fatcatmap;
            amplify = this.fatcatmap.sys.drivers.resolve('transport', 'amplify');
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
              contentType: 'application/json',
              beforeSend: __bind(function(xhr, settings) {
                fatcatmap.rpc.api.history[request.envelope.id].xhr = xhr;
                return xhr;
              }, this),
              error: __bind(function(xhr, status, error) {
                console.log('[RPC] Error: ', data, status, xhr);
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
                return callbacks != null ? callbacks.failure(data) : void 0;
              }, this),
              success: __bind(function(data, status, xhr) {
                console.log('[RPC] Success: ', data, status, xhr);
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
                return callbacks != null ? callbacks.success(data) : void 0;
              }, this),
              complete: __bind(function(xhr, status) {
                fatcatmap.rpc.api.history[request.envelope.id].xhr = xhr;
                fatcatmap.rpc.api.history[request.envelope.id].status = status;
                context = {
                  xhr: xhr,
                  status: status
                };
                fatcatmap.state.events.triggerEvent('RPC_COMPLETE', context);
                return callbacks != null ? callbacks.complete(xhr, status) : void 0;
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
            };
            if (!amplify) {
              fatcatmap.dev.verbose('RPC', 'Fulfilling with AJAX adapter.');
              return xhr = $.ajax(xhr_settings);
            } else {
              fatcatmap.dev.verbose('RPC', 'Fulfilling with AmplifyJS adapter.');
              return xhr = amplify.reauest(xhr_settings);
            }
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
      fcm.state.events.triggerEvent('RPC_READY');
    }
    __extends(CoreRPCAPI, CoreAPI);
    CoreRPCAPI.prototype.registerAPIMethod = function(api, name, config) {
      var amplify, fcm;
      if (typeof $ !== "undefined" && $ !== null) {
        fcm = $.fatcatmap;
      } else {
        fcm = window.fatcatmap;
      }
      amplify = fcm.sys.drivers.resolve('transport', 'amplify');
      if (amplify !== false) {
        fcm.dev.log('RPCAPI', 'Registering request procedure "' + api + '.' + name + '" with AmplifyJS.');
        if ((config.caching != null) === true) {
          return amplify.request.define(api + '.' + name, "ajax", {
            type: 'POST',
            dataType: 'json',
            cache: 'persist',
            decoder: this.api.decodeRPCResponse
          });
        } else {
          return amplify.request.define(api + '.' + name, "ajax", {
            type: 'POST',
            dataType: 'json',
            decoder: this.api.decodeRPCResponse
          });
        }
      }
    };
    return CoreRPCAPI;
  })();
  window.RPCAPI = RPCAPI;
  window.RPCAdapter = RPCAdapter;
  window.RPCRequest = RPCRequest;
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
  CoreLiveAPI = (function() {
    function CoreLiveAPI(fcm) {
      this.fcm = fcm;
      this.onClose = __bind(this.onClose, this);;
      this.onError = __bind(this.onError, this);;
      this.onMessage = __bind(this.onMessage, this);;
      this.onOpen = __bind(this.onOpen, this);;
      this.openChannel = __bind(this.openChannel, this);;
      this.fcm.state.events.registerEvent('CHANNEL_OPEN');
      this.fcm.state.events.registerEvent('CHANNEL_MESSAGE');
      this.fcm.state.events.registerEvent('CHANNEL_ERROR');
      this.fcm.state.events.registerEvent('CHANNEL_CLOSE');
      this.token = null;
      this.channel = null;
      this.socket = null;
    }
    __extends(CoreLiveAPI, CoreAPI);
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
        return this.socket.onclose = this.onClose;
      } catch (error) {
        return this.fcm.dev.debug.error('CoreLive', 'Encountered error preparing live channel.', error);
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
