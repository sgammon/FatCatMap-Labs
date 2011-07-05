(function() {
  var Dialog, Navigation, Panel, Sidebar, SuperBar, SuperFooter, SuperPanel;
  var __hasProp = Object.prototype.hasOwnProperty, __extends = function(child, parent) {
    for (var key in parent) { if (__hasProp.call(parent, key)) child[key] = parent[key]; }
    function ctor() { this.constructor = child; }
    ctor.prototype = parent.prototype;
    child.prototype = new ctor;
    child.__super__ = parent.prototype;
    return child;
  };
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
  SuperBar = (function() {
    function SuperBar() {
      SuperBar.__super__.constructor.apply(this, arguments);
    }
    __extends(SuperBar, SuperPanel);
    SuperBar.prototype.register = function(id) {
      this.id = id;
      $('#momentumSuperbar').hover(function() {
        return $('#momentumSuperbar').animate({
          opacity: 1.0
        });
      }, function() {
        return $('#momentumSuperbar').animate({
          opacity: 0.8
        });
      });
    };
    return SuperBar;
  })();
  SuperFooter = (function() {
    function SuperFooter() {
      SuperFooter.__super__.constructor.apply(this, arguments);
    }
    __extends(SuperFooter, SuperPanel);
    SuperFooter.prototype.register = function(id) {
      this.id = id;
      $('#momentumSuperfooter').hover(function() {
        return $('#momentumSuperfooter').animate({
          opacity: 0.8
        });
      }, function() {
        return $('#momentumSuperfooter').animate({
          opacity: 0.5
        });
      });
      $('#bottomFcmBranding a').hover(function() {
        return $('#bottomFcmBranding a div').addClass('brandingHover');
      }, function() {
        return $('#bottomFcmBranding a div').removeClass('brandingHover');
      });
    };
    return SuperFooter;
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
  window.Panel = Panel;
  window.Sidebar = Sidebar;
  window.SuperBar = SuperBar;
  window.SuperPanel = SuperPanel;
  window.SuperFooter = SuperFooter;
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
  Navigation = (function() {
    var pane_class;
    function Navigation() {
      Navigation.__super__.constructor.apply(this, arguments);
    }
    __extends(Navigation, LayoutElement);
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
  window.Navigation = Navigation;
}).call(this);
