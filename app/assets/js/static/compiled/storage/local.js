(function() {
  var LocalStorageDriver, SessionStorageDriver;
  var __hasProp = Object.prototype.hasOwnProperty, __extends = function(child, parent) {
    for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; }
    function ctor() { this.constructor = child; }
    ctor.prototype = parent.prototype;
    child.prototype = new ctor;
    child.__super__ = parent.prototype;
    return child;
  };
  LocalStorageDriver = (function() {
    function LocalStorageDriver() {
      LocalStorageDriver.__super__.constructor.apply(this, arguments);
    }
    __extends(LocalStorageDriver, StorageDriver);
    LocalStorageDriver.prototype.getValueByKey = function(key) {};
    LocalStorageDriver.prototype.setValueByKey = function(key, value) {};
    LocalStorageDriver.prototype.deleteValueByKey = function(key) {};
    LocalStorageDriver.prototype.nuke = function() {};
    LocalStorageDriver.prototype.allValues = function() {};
    return LocalStorageDriver;
  })();
  SessionStorageDriver = (function() {
    function SessionStorageDriver() {
      SessionStorageDriver.__super__.constructor.apply(this, arguments);
    }
    __extends(SessionStorageDriver, StorageDriver);
    SessionStorageDriver.prototype.getValueByKey = function(key) {};
    SessionStorageDriver.prototype.setValueByKey = function(key, value) {};
    SessionStorageDriver.prototype.deleteValueByKey = function(key) {};
    SessionStorageDriver.prototype.nuke = function() {};
    SessionStorageDriver.prototype.allValues = function() {};
    return SessionStorageDriver;
  })();
  LocalStorageDriver('localstorage', {});
  SessionStorageDriver('sessionstorage', {});
}).call(this);
