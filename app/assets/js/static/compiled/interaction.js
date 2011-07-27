(function() {
  var InteractiveWidget, RouteController;
  var __hasProp = Object.prototype.hasOwnProperty, __extends = function(child, parent) {
    for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; }
    function ctor() { this.constructor = child; }
    ctor.prototype = parent.prototype;
    child.prototype = new ctor;
    child.__super__ = parent.prototype;
    return child;
  };
  RouteController = (function() {
    function RouteController() {
      RouteController.__super__.constructor.apply(this, arguments);
    }
    __extends(RouteController, Backbone.Router);
    return RouteController;
  })();
  InteractiveWidget = (function() {
    function InteractiveWidget(name, path, config) {
      this.name = name;
      this.path = path;
      this.config = config;
    }
    return InteractiveWidget;
  })();
}).call(this);
