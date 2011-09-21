fs = require 'fs'
path = require 'path'
util = require 'util'
{exec} = require 'child_process'

out =
	say: (module, message) ->
		util.log '['+module+']: '+message

	shout: (module, message) ->
		util.log ''
		util.log '['+module+']: [########## ===== '+message+' ===== ##########]'
		util.log ''
		
	spawn: (command, flags) ->
		op = exec command, (err, stdout, stderr) ->
			throw err if err
			console.log stdout + stderr
			
		op.stdout.on 'data', (data) ->	
			console.log('operation: '+data)
	
	
## Script Options
option 'd', '--deploy [APP]', 'app id to deploy to'
option 'p', '--port [PORT]', 'port to run development instance on'
option 'b', '--backends', 'run backends on local instance'
option 'c', '--wipe', 'clear local datastore data'



######### =======  Platform Tools  ========== #########
## App ID's
app_options =
	
	development: 'fatcatmap'
	staging: 'momentum-labs'
	production: 'fat-cat-map'	

task 'install', 'run me on first install!', (options) ->

	out.shout 'install', 'Starting Installation'
	
	out.say 'install', 'Running bootstrap...'
	out.spawn 'python bootstrap.py --distribute'

	out.say 'install', 'From now on, you can use `cake make` to update dependencies. Happy coding!'
	out.shout 'install', 'Installation complete.'

	invoke 'make'
	
		
task 'make', 'download dependencies and prepare dev environment', (options) ->

	out.shout 'make', 'Starting Envrionment Setup'

	out.say 'make', 'Running buildout...'
	out.spawn 'bin/buildout'
	
	out.say 'make', 'Updating core libraries...'
	out.spawn 'bin/update_libraries'
	
	out.shout 'make', 'Environment setup complete.'

	
task 'bake', 'compile and minify all js, templates, and coffeescript', (options) ->
	
	out.shout 'bake', 'Starting Compilation'
	
	## 1) Compile everything first
	out.say 'bake', 'Compiling JS codebase (CoffeeScript)...'
	invoke 'compile:codebase'
	
	out.say 'bake', 'Compiling JS templates (mustasche)...'
	invoke 'compile:jstemplates'
	
	out.say 'bake', 'Compiling Jinja2 templates...'
	invoke 'compile:templates'
	
	out.say 'bake', 'Compiling SASS...'
	invoke 'compile:sass'
	
	
	## 2) Bundle things
	out.say 'bake', 'Bundling JS dependencies...'
	invoke 'bundle:dependencies'
	
	out.say 'bake', 'Bundling JS templates...'
	invoke 'bundle:jstemplates'
	
	## 3) Minify things
	out.say 'bake', 'Minifying JS codebase...'
	invoke 'minify:codebase'
	
	out.say 'bake', 'Minifying JS dependencies...'
	invoke 'minify:dependencies'
	
	out.say 'bake', 'Minifying JS templates...'
	invoke 'minify:jstemplates'
	
	out.say 'bake', 'Minifying CSS...'
	invoke 'minify:sass'
	

task 'slice', 'run fatcatmap\'s local dev server', (options) ->
	out.spawn 'bin/dev_appserver'

task 'serve', 'deploy fatcatmap to appengine', (options) ->
	out.spawn 'bin/appcfg upload app'



######## =======  Stylesheets/SASS  ========== ########
task 'compile:sass', 'compile SASS to CSS', (options) ->
	out.spawn 'compass compile'
	
task 'minify:sass', 'minify SASS into production-ready CSS', (options) ->
	out.spawn 'compass compile --output-style compressed'



########## =======  CoffeeScript  ========== ##########
task 'compile:codebase', 'compile js codebase', (options) ->
	out.spawn 'bin/coffee2'

task 'minify:codebase', 'minify js codebase', (options) ->
	out.spawn 'bin/uglify'



########## =======  JS Libraries  ========== ##########
task 'minify:dependencies', 'minify js dependencies', (options) ->

	
task 'bundle:dependencies', 'bundle js dependencies for production', (options) ->	



############ =======  Templates  ========== ############
task 'compile:templates', 'compile jinja2 templates', (options) ->
	

task 'compile:jstemplates', 'compile mustasche templates', (options) ->
	
	
task 'minify: jstemplates', 'minify mustasche templates', (options) ->