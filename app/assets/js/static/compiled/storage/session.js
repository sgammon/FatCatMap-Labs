(function() {
  var SessionStorageDriver;
  var __hasProp = Object.prototype.hasOwnProperty, __extends = function(child, parent) {
    for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; }
    function ctor() { this.constructor = child; }
    ctor.prototype = parent.prototype;
    child.prototype = new ctor;
    child.__super__ = parent.prototype;
    return child;
  };
  SessionStorageDriver = (function() {
    __extends(SessionStorageDriver, StorageDriver);
    function SessionStorageDriver() {
      SessionStorageDriver.__super__.constructor.apply(this, arguments);
    }
    SessionStorageDriver.prototype.init = function() {
      return this.store = new Lawnchair({
        name: 'fcm-session'
      }, function(store) {
        $.fatcatmap.dev.log('SSB/SessionStorage', 'Driver loaded. Session store created.');
        return $.fatcatmap.state.events.triggerEvent('STORAGE_DB_LOAD', {
          name: 'fcm-session',
          store: this.store
        });
      });
    };
    SessionStorageDriver.prototype.getValueByKey = function(key) {};
    SessionStorageDriver.prototype.setValueByKey = function(key, value) {};
    SessionStorageDriver.prototype.deleteValueByKey = function(key) {};
    SessionStorageDriver.prototype.nuke = function() {};
    SessionStorageDriver.prototype.allValues = function() {};
    return SessionStorageDriver;
  })();
  this.SessionStorageDriver = new SessionStorageDriver().setup('sessionstorage', {});
}).call(this);
