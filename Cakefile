fs = require 'fs'

## App ID's
app_options =
	
	development: 'fatcatmap'
	staging: 'momentum-labs'
	production: 'fat-cat-map'


## Script Options
option '-d', '--deploy [APP]', 'upload and stage application'
option '-m', '--minify', 'generate minified versions of compiled source'
option '-v', '--verbose', 'talk a lot about what\'s going on'
option '-t', '--tests', 'run fcm testsuite'


## Compile CoffeeScript codebase
task 'compile:coffeescript', 'compile js codebase', (options) ->


## Minify JS codebase
task 'minify:coffeescript', 'minify js codebase', (options) ->
	

## Minify dependencies (backbone, underscore)
task 'minify:dependencies', 'minify js dependencies', (options) ->
	
	
task 'bundle:dependencies', 'bundle js dependencies for production', (options) ->	

	
task 'compile:jstemplates', 'compile mustasche templates', (options) ->
	

task 'compile:templates', 'compile jinja2 templates', (options) ->
	
	
task 'compile:sass', 'compile SASS to CSS', (options) ->
	
	
task 'build:parser', 'rebuild the Jison parser', (options) ->
	require 'jison'
	code = require('./lib/grammar').parser.generate()
	dir  = options.output or 'lib'
	fs.writeFile "#{dir}/parser.js", code