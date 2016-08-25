# FatCatMap Labs - Code Documentation

##Change Log


**Wed, September 21 2011 software version tag 1.6.1-BETA**

- First BETA! :)
- Moved from Tipfy to Webapp2
- Full, finished service layer
- Switched to compiled templates for Jinja2, with Rodrigo Moraes' expert speed hax
- Application now running in threadsafe (and, therefore, multithreaded!)
- Data API v1.0
- Frame API v1.0
- Query API v1.0
- Core Caching API v1.0
- Graph API v1.0
- Version bump


**Tue, September 20 2011**

- Pre-BETA commit
- Massive refactoring and optimization for the Python 2.7 runtime
- Application now operating via WSGI
- New logo
- Many speed and reliability improvements to the CoffeeScript base
- Huge speed improvements in the Python base


**Wed, August 31 2011**

- Refactored core Momentum classes to live in better places
- Fixed crappy path issues with Core Assets API
- Beginnings of the Analyzer Engine


**Mon, August 22 2011**

- New, cleaner redesign
- Removed stupid iconset
- Streamlined asset import
- CDN-based asset packs
- Upgraded Core Assets API
- New boto config for uploading to Google Storage for Developers


**Tue, July 21-26 2011**

- Backbone integration
- Async JS lib loading via Yep/Nope
- Minification bugfixes
- Updated coffee build script
- Officially using the new D3-based Graphing Engine
- AmplifyJS AJAX adapter finished
- New setting to enable/disable browser-local caching
- Improvements and bugfixes to the JSAPI
- Quick change of import order
- Working service layer decorators
- Bugfix for after_request hook in service layer middleware
- Merge with servicelayer branch changes & improvements
- Merge with JS platform branch changes & improvements
- Updated Masonry, fixed bugs in SASS base
- Working service layer middleware system


**Fri, July 08 2011**

- Minor bugfixes
- Improvements to Cakefile tasks
- Service layer improvements
- Prep work for AmplifyJS Adapter


**Thu, July 07 2011**

- Numerous bug fixes in the CoreAssetsAPI, along with path/bundle config support
- More compatible support for fonts in browsers like iOS/Safari and IE
- Cleaned up lots of filename-based versioning
- Added bundle-wide config option for presence of minified assets and automatic version mode handling
- Installed CanVG polyfill, along with JS-level RGB color support
- Better coffee build script
- Added CoreLiveAPI module to the js codebase, for mediating communication over the Channel API on the client side
- Added CoreModelAPI module to manage schema and instantiated models (both remote and local)
- Installed Zepto for jQuery support on mobile
- Backbone sync method overridden (but not yet tested) to work through the JS Data API
- Created 'base' compiled JS file to contain _root, _underscore and milk (mustache templates for CoffeeScript)

**Tue, July 05 2011**

- Rewritten CoreAssetsAPI, supporting auto-switching to minified external assets
- Better, more modular approach to compiled JS files (storage JS and site JS split up)
- D3 js files installed (but not yet in use)
- Backbone JS and Underscore JS files installed (but not yet in use)
- New version of Modernizr installed
- Amplify JS installed (but not yet in use)
- Asset versioning convention switched to all dots (file.1.0.js instead of file-1.0.js)
- Better coffee build scripts on the way (halfway done in bin/coffee2)

**Thu, June 30 2011**

- New 'require'-based structure for CoffeeScript, with a better build script
- Proper compartmentalization of [Coffee/Java]Scripts, allowing more nimble page loads
- New coffee files for 'plugins' folder - geo + workers to start
- Version-by-getvar now a simple configuration switch for the Assets subsystem
- Split up config files into smaller chunks for easier versioning + development
- Cleaned up SCSS files from manual versioning
- Added nifty FPS counter for JS rendering speed benchmarking

**Wed, June 29 2011**

- Structure in place for service layer middleware (authentication, authorization & audit)
- Revamped AJAX and RPCAPI mechanism for the JS API layer
- Asset versioning by GETVARS now supported
- Config-based control of service layer caching, audit, and security
- Config-based control of exposed service layer to JS clients
- Dynamic generation of RPC APIs exposed to JS clients
- People can now see FCM without being logged in as an admin (or at all)

**Tue, June 21 2011**

- Merge commit with Alex
- New design for AJAX transport for JS API
- New design for asset management & versioning via GETVARS

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
