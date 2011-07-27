(function() {
  var IndexedDBDriver;
  var __hasProp = Object.prototype.hasOwnProperty, __extends = function(child, parent) {
    for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; }
    function ctor() { this.constructor = child; }
    ctor.prototype = parent.prototype;
    child.prototype = new ctor;
    child.__super__ = parent.prototype;
    return child;
  };
  IndexedDBDriver = (function() {
    function IndexedDBDriver() {
      IndexedDBDriver.__super__.constructor.apply(this, arguments);
    }
    __extends(IndexedDBDriver, AdvancedStorageDriver);
    IndexedDBDriver.prototype.getValueByKey = function(db, kind, key, callbacks) {};
    IndexedDBDriver.prototype.setValueByKey = function(db, kind, key, value, callbacks) {};
    IndexedDBDriver.prototype.addValueByKey = function(db, kind, key, value, callbacks) {};
    IndexedDBDriver.prototype.deleteValueByKey = function(db, kind, key, callbacks) {};
    IndexedDBDriver.prototype.openDatabase = function(name, callbacks) {};
    IndexedDBDriver.prototype.deleteDatabase = function(db, callbacks) {};
    IndexedDBDriver.prototype.setDatabaseVersion = function(db, version, callbacks) {};
    IndexedDBDriver.prototype.closeDatabase = function(db, callbacks) {};
    IndexedDBDriver.prototype.createCollection = function(db, name, key_path, auto_increment, callbacks) {};
    IndexedDBDriver.prototype.deleteCollection = function(db, name) {};
    IndexedDBDriver.prototype.clearCollection = function(db, name) {};
    return IndexedDBDriver;
  })();
  IndexedDBDriver('objectstorage', {});
}).call(this);
