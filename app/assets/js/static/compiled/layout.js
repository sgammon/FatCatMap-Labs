(function() {
  var Dialog, LayoutElement, Navigation, Panel, Sidebar, SuperBar, SuperFooter, SuperPanel;
  var __hasProp = Object.prototype.hasOwnProperty, __extends = function(child, parent) {
    for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; }
    function ctor() { this.constructor = child; }
    ctor.prototype = parent.prototype;
    child.prototype = new ctor;
    child.__super__ = parent.prototype;
    return child;
  }, __bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; };
  LayoutElement = (function() {
    __extends(LayoutElement, Backbone.View);
    function LayoutElement() {
      LayoutElement.__super__.constructor.apply(this, arguments);
    }
    LayoutElement.prototype.id = null;
    LayoutElement.prototype.name = null;
    LayoutElement.prototype.state = {};
    LayoutElement.prototype.config = {};
    LayoutElement.prototype.classes = [];
    LayoutElement.prototype.element = null;
    LayoutElement.prototype.defaults = null;
    LayoutElement.prototype.selector = null;
    LayoutElement.prototype.registered = false;
    LayoutElement.prototype.register = function(name) {
      this.name = name;
    };
    return LayoutElement;
  })();
  if (typeof window !== "undefined" && window !== null) {
    window.LayoutElement = LayoutElement;
    window.Layout = {};
  }
  Panel = (function() {
    __extends(Panel, LayoutElement);
    function Panel() {
      Panel.__super__.constructor.apply(this, arguments);
    }
    Panel.prototype.nothing = function() {};
    return Panel;
  })();
  SuperPanel = (function() {
    __extends(SuperPanel, LayoutElement);
    function SuperPanel() {
      SuperPanel.__super__.constructor.apply(this, arguments);
    }
    SuperPanel.prototype.nothing = function() {};
    return SuperPanel;
  })();
  SuperBar = (function() {
    __extends(SuperBar, SuperPanel);
    function SuperBar() {
      SuperBar.__super__.constructor.apply(this, arguments);
    }
    SuperBar.prototype.initialize = function() {
      $(this.el).hover(__bind(function() {
        return $(this.el).animate({
          opacity: 1.0
        });
      }, this), __bind(function() {
        return $(this.el).animate({
          opacity: 0.8
        });
      }, this));
      this.el = $(this.id);
    };
    return SuperBar;
  })();
  SuperFooter = (function() {
    __extends(SuperFooter, SuperPanel);
    function SuperFooter() {
      SuperFooter.__super__.constructor.apply(this, arguments);
    }
    SuperFooter.prototype.initialize = function() {
      $(this.el).hover(__bind(function() {
        return $(this.el).animate({
          opacity: 0.8
        });
      }, this), __bind(function() {
        return $(this.el).animate({
          opacity: 0.5
        });
      }, this));
      this.$('#bottomFcmBranding a').hover(__bind(function() {
        return this.$('#bottomFcmBranding a div').addClass('brandingHover');
      }, this), __bind(function() {
        return this.$('#bottomFcmBranding a div').removeClass('brandingHover');
      }, this));
    };
    return SuperFooter;
  })();
  Sidebar = (function() {
    __extends(Sidebar, LayoutElement);
    function Sidebar(id, config) {
      this.id = id;
      this.el = $(this.id);
      this.state = {
        hidden: false,
        locked: false,
        folded: false,
        unfolded: false,
        maximized: false
      };
      this.config = {
        maximizable: false,
        folded_width: 40,
        unfolded_width: $('body').width() * .25,
        maximized_width: $('body').width() * .70
      };
      if (config != null) {
        _.extend(this.config, config);
      }
      this.$('.enabled.expandButton').click(__bind(function(event) {
        return this.unfold();
      }, this));
      this.$('.enabled.closeButton').click(__bind(function(event) {
        return this.fold();
      }, this));
      this.hide = __bind(function(animate) {
        if (animate == null) {
          animate = true;
        }
        if (this.state.hidden === false) {
          this.state.hidden = true;
          if (animate === true) {
            $(this.el).animate({
              opacity: 0
            }, __bind(function() {
              return $(this.el).addClass('hidden');
            }, this));
          } else {
            $(this.el).addClass('hidden');
          }
        }
        return this.state.hidden;
      }, this);
      this.unhide = __bind(function(animate) {
        if (animate == null) {
          animate = true;
        }
        if (this.state.hidden === true) {
          this.state.hidden = false;
          if (animate === true) {
            $(this.el).animate({
              opacity: 1
            }, __bind(function() {
              return $(this.el).removeClass('hidden');
            }, this));
          } else {
            $(this.el).removeClass('hidden');
          }
        }
        return this.state.hidden;
      }, this);
      this.lock = __bind(function() {
        this.state.locked = true;
        this.$('.expandButton').removeClass('enabled').unbind('click');
        return this.state.locked;
      }, this);
      this.unlock = __bind(function() {
        this.state.locked = false;
        this.$('.expandButton').addClass('enabled').click(__bind(function() {
          return this.unfold();
        }, this));
        return this.state.locked;
      }, this);
      this.fold = __bind(function() {
        this.state.folded = true;
        this.state.unfolded = false;
        this.state.maximized = false;
        this.hideContent();
        if (this.$('.closeButton').hasClass('multiButton')) {
          this.$('.closeButton').removeClass('closeButton').addClass('expandButton');
          this.$('.closeMultiButton').removeClass('enabled').addClass('hidden');
          this.$('.expandMultiButton').addClass('enabled').removeClass('hidden');
        } else {
          if (!this.$('.closeButton').hasClass('hidden')) {
            this.$('.closeButton').addClass('hidden');
          }
        }
        if (!this.$('.expandButton').hasClass('enabled') && this.state.locked !== true) {
          this.$('.expandButton').addClass('enabled');
        }
        this.$('.enabled.expandButton').unbind('click').click(__bind(function(event) {
          return this.unfold();
        }, this));
        return $(this.el).addClass('folded').removeClass('unfolded').animate({
          width: this.config.folded_width
        });
      }, this);
      this.unhideContent = __bind(function() {
        return this.$('.panelWrapper').animate({
          opacity: 1
        }).removeClass('hidden');
      }, this);
      this.hideContent = __bind(function() {
        return this.$('.panelWrapper').animate({
          opacity: 0
        }).addClass('hidden');
      }, this);
      this.unfold = __bind(function() {
        this.state.folded = false;
        this.state.unfolded = true;
        this.state.maximized = false;
        $(this.el).addClass('unfolded').removeClass('folded').animate({
          width: this.config.unfolded_width
        });
        this.unhideContent();
        $('.enabled.closeButton').removeClass('hidden');
        if (this.config.maximizable !== false) {
          return this.$('.enabled.expandButton').unbind('click').click(__bind(function(event) {
            console.log('maximize called');
            return this.maximize();
          }, this));
        } else {
          if (this.$('.expandButton').hasClass('multiButton')) {
            this.$('.expandMultiButton').addClass('hidden');
            this.$('.closeMultiButton').removeClass('hidden');
            this.$('.expandButton').removeClass('expandButton').addClass('closeButton');
            return this.$('.closeButton').unbind('click').click(__bind(function() {
              return this.fold();
            }, this));
          } else {
            return this.$('.enabled.expandButton').removeClass('enabled');
          }
        }
      }, this);
      this.minimize = __bind(function() {
        this.$('.enabled.minimizeButton').removeClass('enabled').addClass('hidden');
        this.$('.expandButton').addClass('enabled').removeClass('hidden');
        return this.unfold();
      }, this);
      this.maximize = __bind(function() {
        this.state.folded = false;
        this.state.unfolded = true;
        this.state.maximized = true;
        this.$('.enabled.expandButton').removeClass('enabled').addClass('hidden');
        this.$('.minimizeButton').removeClass('hidden').addClass('enabled').unbind('click').click(__bind(function(ev) {
          return this.minimize();
        }, this));
        return $(this.el).addClass('maximized').removeClass('unfolded').animate({
          width: this.config.maximized_width
        });
      }, this);
    }
    return Sidebar;
  })();
  window.Layout.Panel = Panel;
  window.Layout.Sidebar = Sidebar;
  window.Layout.SuperBar = SuperBar;
  window.Layout.SuperPanel = SuperPanel;
  window.Layout.SuperFooter = SuperFooter;
  Dialog = (function() {
    __extends(Dialog, LayoutElement);
    function Dialog() {
      Dialog.__super__.constructor.apply(this, arguments);
    }
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
  window.Layout.Dialog = Dialog;
  Navigation = (function() {
    var pane_class;
    __extends(Navigation, LayoutElement);
    function Navigation() {
      Navigation.__super__.constructor.apply(this, arguments);
    }
    pane_class = '.navPane';
    Navigation.prototype.register = function(id) {
      this.id = id;
      $(this.selector).hover(function() {
        $(this.selector).animate({
          opacity: 1.0
        });
      }, function() {
        $(this.selector).animate({
          opacity: 0.8
        });
      });
      $('.SupernavLink').click(function() {
        var current_pane, expanded, navref;
        navref = $(this).attr('data-navref');
        current_pane = $('#topnav').attr('data-currentpane');
        if (current_pane !== null || current_pane !== void 0) {
          $('.navpane#' + current_pane + 'Pane').addClass('hidden');
        }
        $('#topnav').attr('data-currentpane', navref);
        expanded = $('#contentHeader').attr('data-expanded');
        if (expanded === null || expanded === void 0 || expanded !== 'true') {
          $('#contentHeader').slideDown().removeClass('hidden');
          $('#contentHeader').attr('data-expanded', 'true');
        }
        return $('.navpane#' + navref + 'Pane').removeClass('hidden');
      });
      return $('.foldNavigation').click(function() {
        var current_pane, navref;
        navref = this.getAttribute('data-navref');
        current_pane = $('#topnav').attr('data-currentpane');
        if (current_pane !== null || current_pane !== void 0) {
          $('#topnav').removeAttr('data-currentpane');
        }
        $('#contentHeader').slideUp();
        return $('#contentHeader').removeAttr('data-expanded');
      });
    };
    return Navigation;
  })();
  window.Layout.Navigation = Navigation;
}).call(this);
