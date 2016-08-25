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
    __extends(IndexedDBDriver, AdvancedStorageDriver);
    function IndexedDBDriver() {
      IndexedDBDriver.__super__.constructor.apply(this, arguments);
    }
    IndexedDBDriver.prototype.init = function() {
      var adapter, idb_adapter, _i, _len, _ref;
      idb_adapter = null;
      _ref = Lawnchair.adapters;
      for (_i = 0, _len = _ref.length; _i < _len; _i++) {
        adapter = _ref[_i];
        if (adapter.adapter === 'indexed-db') {
          idb_adapter = adapter;
        }
      }
      if (idb_adapter != null) {
        return this.store = new Lawnchair({
          name: 'fcm-object',
          adapter: idb_adapter
        }, function(store) {
          $.fatcatmap.dev.log('IDB/ObjectStorage', 'Driver loaded. Object store created.');
          return $.fatcatmap.state.events.triggerEvent('STORAGE_DB_LOAD', {
            name: 'fcm-object',
            store: this.store
          });
        });
      } else {
        return $.fatcatmap.dev.log('IDB/ObjectStorage', 'Failed to resolve IndexedDB lawnchair driver.');
      }
    };
    IndexedDBDriver.prototype.save = function(db, kind, key, callbacks) {};
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
  this.IndexedDBDriver = new IndexedDBDriver().setup('objectstorage', {});
}).call(this);
