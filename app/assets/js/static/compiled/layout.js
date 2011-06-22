(function() {
  var Dialog, LayoutElement, Panel, Sidebar, SuperPanel;
  var __indexOf = Array.prototype.indexOf || function(item) {
    for (var i = 0, l = this.length; i < l; i++) {
      if (this[i] === item) return i;
    }
    return -1;
  }, __hasProp = Object.prototype.hasOwnProperty, __extends = function(child, parent) {
    for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; }
    function ctor() { this.constructor = child; }
    ctor.prototype = parent.prototype;
    child.prototype = new ctor;
    child.__super__ = parent.prototype;
    return child;
  };
  LayoutElement = (function() {
    LayoutElement.prototype.name = null;
    LayoutElement.prototype.state = {};
    LayoutElement.prototype.config = {};
    LayoutElement.prototype.classes = [];
    LayoutElement.prototype.element = null;
    LayoutElement.prototype.defaults = null;
    LayoutElement.prototype.selector = null;
    function LayoutElement(name, selector, config) {
      this.name = name;
      this.selector = selector;
      this.config = config;
    }
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
      this._setState('visibile', false);
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
  window.LayoutElement = LayoutElement;
  Panel = (function() {
    function Panel() {
      Panel.__super__.constructor.apply(this, arguments);
    }
    __extends(Panel, LayoutElement);
    Panel.prototype.nothing = function() {};
    return Panel;
  })();
  SuperPanel = (function() {
    function SuperPanel() {
      SuperPanel.__super__.constructor.apply(this, arguments);
    }
    __extends(SuperPanel, LayoutElement);
    SuperPanel.prototype.nothing = function() {};
    return SuperPanel;
  })();
  Sidebar = (function() {
    function Sidebar() {
      Sidebar.__super__.constructor.apply(this, arguments);
    }
    __extends(Sidebar, LayoutElement);
    Sidebar.prototype.fold = function() {};
    Sidebar.prototype.unfold = function() {};
    Sidebar.prototype.minimize = function() {};
    Sidebar.prototype.maximize = function() {};
    return Sidebar;
  })();
  Dialog = (function() {
    function Dialog() {
      Dialog.__super__.constructor.apply(this, arguments);
    }
    __extends(Dialog, LayoutElement);
    Dialog.prototype.defaults = {
      modal: false,
      opacity: true,
      autoScale: true
    };
    Dialog.prototype.next = function() {};
    Dialog.prototype.previous = function() {};
    Dialog.prototype.goto = function(index) {};
    Dialog.prototype.cancel = function() {};
    Dialog.prototype.resize = function() {};
    Dialog.prototype.center = function() {};
    Dialog.prototype.title = function() {};
    return Dialog;
  })();
}).call(this);
