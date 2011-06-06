# FatCatMap Labs - Code Documentation

##Change Log

**Sun, June 05 2011 software version tag 1.1-ALPHA**
- Installed Blueprint plugins (buttons, link icons, print, ie, liquid layout and forms)
- Committing Coffee structure for the first time
- Browsing to nodes on the graph now works, though it's through synchronous pageloads
- Adjusted sizing and apportioning of instances to backends
- Added more compiled assets (see blueprint plugins), along with asset entries in config.py
- Added a special 'elements' property to the render function, for activating/overriding page elements
- Added easy-to-trigger global warning/notice messages from the new 'elements' special handler property
- Moved some content sections to having their own "layout" that they can inherit from
- Better configuration for SASS/Compass - automagically doing images now

**Sat, June 04 2011**

- We're now completely on the SASS bandwagon! See assets/style/source.
- Created 'scaffolding' appcache manifest for deployment to production
- Created production + labs version of the app.yaml
- Fixed bugs in the output loader when caching was enabled
- Fixed visual and layout bugs (mostly with opacity)
- Structural components there for coffeescript
- Scaled up a few of the backends

**Thu, June 02 2011 major release version tag 1-alpha**

- The platform is nearing a place where it can be used. Along with the new version tag:
- Created this changelog (finally)
- Added content to static error pages
- some git spring cleaning
- including some new FCM graphics
- a meaninfgul README
- cleaned up configuration and app.yaml files (with comments)
- a whole bunch of new debug and dev tools.
- removed old JSONRPC/JSONRPCDispatcher code (completely using ProtoRPC now)
- installed AppTrace and AppStats
- installed a warmup script
- added a directory for platform docs

**Tue, May 31 2011**

- Installed Fancybox
- Installed jQuery easing and mousewheel plugins
- testing out new striped background
- new functionality to inject a manifest attribute for offline caching
- repackaged 'content' handlers into subpackages of momentum.fatcatmap.handlers (along with matching template directory structure)
- moved news explorer to Visualize section
- added 'site' URLs and matching handlers (sections for about, legal, help, etc)
- added better momentum menu context links
- Added new asset handlers and a skip block to the app.yaml
- stability and readability improvements to the JavaScript API
- middleware layer for AppStats enabled and seperately configurable for the services (ProtoRPC) and main site (Tipfy) layers
- made small tweaks to templates, including a link from the 'mapper' header on each page to the map

**Mon, May 30 2011**

- New wireframe on main.Landing for a 'News Explorer'
- Moved all font dependencies to local style/fonts folder for accurate dev server testing
- Added FCM header icons for browse, search, etc
- Small interface tweaks and bug fixes

**Sat, May 28 2011**

- Moved ProtoRPC to buildout process
- moved NDB back to app root
- added node/edge type recognition to recursive Grapher
- added scripting to add base Edge/Node/Object types and related Schema items

**Thu, May 26 2011**

- New interface for inbox messages (replaces Notiications concept)
- branding/version/dev watermark placed at the bottom of the page
- Stability and cohesiveness improvements to the JavaScript API
- rewritten AJAX RPC mechanism (without reliance on JSONRPC for jQuery)
- new custom template loader (momentum.fatcatmap.core.output) with template source caching in fastcache (instance memory) and memcache
- new JS layout code written to maximize page sidebars
- new graph JS written to browse to a node

**Wed, May 25 2011**

- ProtoRPC structure for APIs now in place,
- JavaScript API is functional and performing RPCs
- new favicon and logo
- new handlers and code space for backends (momentum.platform)
- unified classes at the top level (MomentumHandler, MomentumService)

**Fri, May 13 2011**

- New JavaScript API (alpha) with plumbing for easy RPC/API calls
- JS codespace for visualization control/page control
- abstracted interfaces to local browser resources like storage and SVG
- added config values to control minification, optimization, and location of script assets
- Yep/Nope code added to parallelize and control JS loading, along with Modernizr for feature detection

**Sun, May 08 2011**

- Working Tipsy-based tooltips
- config entries for assets manager (allows programmatic activation/deactivation of minification, optimization, and switching to compiled assets)
- piping laid (but not yet connected) for the new JS API

**Tue, May 03 2011**

- Added a ton of JavaScript libraries
- automatic library loading with YepNope
- and starting in on the details pane/settings pane sidebars

**Sat, April 30 2011**

- More reliable Struct framework. Tested with args, kwargs, and __slots__
- Working interface to the Indexer.
- Update to NDB, update to ProtoRPC
- working indexer adapter parent class
- Indexer correctly makes use of Indexers and yields Entry SimpleStructs)
- struct framework updated and improved
- beginning support for ImmutableStructs and ComplexStructs.

**Fri, April 29 2011**

- Installed ProtoRPC
- created a script to automatically update appropriate Google Code libs
- working StringIndexer with proper indexer inheritance tree

**Sat, April 24 2011**

- Cleaned up Git repository (hopefully)
- re-wrote front end base template using the HTML5 Boilerplate
- created AssetsMixin for easy URL construction to link to assets in templates
- cleaned up assets folder and linked properly in config.py

**Fri, April 22 2011**

- Installed newer versions of NDB Map/Reduce and Pipelines
- Created an update_libraries script to do this easily in the future
- Proprietary struct framework (probably about to be replaced with ProtoRPC...(LOL)
- NDB moved to application root & pipeline bugs fixed
- about to update all core libraries (pipelines, mapreduce, ndb) and install protorpc

**Sun, April 10 2011**

- Tons of changes...
- committing for developer's meeting and will document soon

**Thu, March 24 2011**

- Added var/downloads folder for compatibility with new development environments.
- Added bin/ and var/ folders for compatibility with new development environments.
- Moved lovely JSONRPC to lib (patched modifications), removed incompatible packages from the buildout.cfg
- Moved NDB to app root (fixed NDB reload bug during pipeline execution), cleaned up queues, added Dev menus

**Wed, March 23 2011 major release version tag 2-dev**

- Version increment
- Working pipelines and grapher.

**Sat, March 12 2011**

- New momentum and fcm graphics (improved dummy UI)
- Framework for FCM pipelines
- new graph write pipelines (framework)
- new jquery plugins

**Tue, March 08 2011**

- Fixed PolyModel inheritance issues
- created initial default data package (based on previous versions)
- Filled out simple properties for graph-related data models.

**Mon, March 07 2011**

- Initial commit.