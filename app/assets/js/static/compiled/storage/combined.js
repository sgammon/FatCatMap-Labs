(function() {
  var IndexedDBDriver, LocalStorageDriver, SessionStorageDriver;
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
