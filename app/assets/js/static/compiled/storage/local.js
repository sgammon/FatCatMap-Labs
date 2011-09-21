(function() {
  var LocalStorageDriver;
  var __hasProp = Object.prototype.hasOwnProperty, __extends = function(child, parent) {
    for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; }
    function ctor() { this.constructor = child; }
    ctor.prototype = parent.prototype;
    child.prototype = new ctor;
    child.__super__ = parent.prototype;
    return child;
  };
  LocalStorageDriver = (function() {
    __extends(LocalStorageDriver, StorageDriver);
    function LocalStorageDriver() {
      LocalStorageDriver.__super__.constructor.apply(this, arguments);
    }
    LocalStorageDriver.prototype.init = function() {
      return this.store = new Lawnchair({
        name: 'fcm-base'
      }, function(store) {
        $.fatcatmap.dev.log('LSB/LocalStorage', 'Driver loaded. Local store created.');
        return $.fatcatmap.state.events.triggerEvent('STORAGE_DB_LOAD', {
          name: 'fcm-base',
          store: this.store
        });
      });
    };
    LocalStorageDriver.prototype.getValueByKey = function(key) {};
    LocalStorageDriver.prototype.setValueByKey = function(key, value) {};
    LocalStorageDriver.prototype.deleteValueByKey = function(key) {};
    LocalStorageDriver.prototype.nuke = function() {};
    LocalStorageDriver.prototype.allValues = function() {};
    return LocalStorageDriver;
  })();
  this.LocalStorageDriver = new LocalStorageDriver().setup('localstorage', {});
}).call(this);
