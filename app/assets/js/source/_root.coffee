# **Underscore.coffee
# (c) 2011 Jeremy Ashkenas, DocumentCloud Inc.**
# Underscore is freely distributable under the terms of the
# [MIT license](http://en.wikipedia.org/wiki/MIT_License).
# Portions of Underscore are inspired by or borrowed from
# [Prototype.js](http://prototypejs.org/api), Oliver Steele's
# [Functional](http://osteele.com), and John Resig's
# [Micro-Templating](http://ejohn.org).
# For all details and documentation:
# http://documentcloud.github.com/underscore/


# Baseline setup
# --------------

# Establish the root object, `window` in the browser, or `global` on the server.
root = this


# Save the previous value of the `_` variable.
previousUnderscore = root._


# Establish the object that gets thrown to break out of a loop iteration.
# `StopIteration` is SOP on Mozilla.
breaker = if typeof(StopIteration) is 'undefined' then '__break__' else StopIteration


# Helper function to escape **RegExp** contents, because JS doesn't have one.
escapeRegExp = (string) -> string.replace(/([.*+?^${}()|[\]\/\\])/g, '\\$1')


# Save bytes in the minified (but not gzipped) version:
ArrayProto           = Array.prototype
ObjProto             = Object.prototype


# Create quick reference variables for speed access to core prototypes.
slice                = ArrayProto.slice
unshift              = ArrayProto.unshift
toString             = ObjProto.toString
hasOwnProperty       = ObjProto.hasOwnProperty
propertyIsEnumerable = ObjProto.propertyIsEnumerable


# All **ECMA5** native implementations we hope to use are declared here.
nativeForEach        = ArrayProto.forEach
nativeMap            = ArrayProto.map
nativeReduce         = ArrayProto.reduce
nativeReduceRight    = ArrayProto.reduceRight
nativeFilter         = ArrayProto.filter
nativeEvery          = ArrayProto.every
nativeSome           = ArrayProto.some
nativeIndexOf        = ArrayProto.indexOf
nativeLastIndexOf    = ArrayProto.lastIndexOf
nativeIsArray        = Array.isArray
nativeKeys           = Object.keys


# Create a safe reference to the Underscore object for use below.
_ = (obj) -> new wrapper(obj)


# Export the Underscore object for **CommonJS**.
if typeof(exports) != 'undefined' then exports._ = _


# Export Underscore to global scope.
root._ = _


# Current version.
_.VERSION = '1.1.0'


# Collection Functions
# --------------------

# The cornerstone, an **each** implementation.
# Handles objects implementing **forEach**, arrays, and raw objects.
_.each = (obj, iterator, context) ->
  try
    if nativeForEach and obj.forEach is nativeForEach
      obj.forEach iterator, context
    else if _.isNumber obj.length
      iterator.call context, obj[i], i, obj for i in [0...obj.length]
    else
      iterator.call context, val, key, obj  for own key, val of obj
  catch e
    throw e if e isnt breaker
  obj


# Return the results of applying the iterator to each element. Use JavaScript
# 1.6's version of **map**, if possible.
_.map = (obj, iterator, context) ->
  return obj.map(iterator, context) if nativeMap and obj.map is nativeMap
  results = []
  _.each obj, (value, index, list) ->
    results.push iterator.call context, value, index, list
  results


# **Reduce** builds up a single result from a list of values. Also known as
# **inject**, or **foldl**. Uses JavaScript 1.8's version of **reduce**, if possible.
_.reduce = (obj, iterator, memo, context) ->
  if nativeReduce and obj.reduce is nativeReduce
    iterator = _.bind iterator, context if context
    return obj.reduce iterator, memo
  _.each obj, (value, index, list) ->
    memo = iterator.call context, memo, value, index, list
  memo


# The right-associative version of **reduce**, also known as **foldr**. Uses
# JavaScript 1.8's version of **reduceRight**, if available.
_.reduceRight = (obj, iterator, memo, context) ->
  if nativeReduceRight and obj.reduceRight is nativeReduceRight
    iterator = _.bind iterator, context if context
    return obj.reduceRight iterator, memo
  reversed = _.clone(_.toArray(obj)).reverse()
  _.reduce reversed, iterator, memo, context


# Return the first value which passes a truth test.
_.detect = (obj, iterator, context) ->
  result = null
  _.each obj, (value, index, list) ->
    if iterator.call context, value, index, list
      result = value
      _.breakLoop()
  result


# Return all the elements that pass a truth test. Use JavaScript 1.6's
# **filter**, if it exists.
_.filter = (obj, iterator, context) ->
  return obj.filter iterator, context if nativeFilter and obj.filter is nativeFilter
  results = []
  _.each obj, (value, index, list) ->
    results.push value if iterator.call context, value, index, list
  results


# Return all the elements for which a truth test fails.
_.reject = (obj, iterator, context) ->
  results = []
  _.each obj, (value, index, list) ->
    results.push value if not iterator.call context, value, index, list
  results


# Determine whether all of the elements match a truth test. Delegate to
# JavaScript 1.6's **every**, if it is present.
_.every = (obj, iterator, context) ->
  iterator ||= _.identity
  return obj.every iterator, context if nativeEvery and obj.every is nativeEvery
  result = true
  _.each obj, (value, index, list) ->
    _.breakLoop() unless (result = result and iterator.call(context, value, index, list))
  result


# Determine if at least one element in the object matches a truth test. Use
# JavaScript 1.6's **some**, if it exists.
_.some = (obj, iterator, context) ->
  iterator ||= _.identity
  return obj.some iterator, context if nativeSome and obj.some is nativeSome
  result = false
  _.each obj, (value, index, list) ->
    _.breakLoop() if (result = iterator.call(context, value, index, list))
  result


# Determine if a given value is included in the array or object,
# based on `===`.
_.include = (obj, target) ->
  return _.indexOf(obj, target) isnt -1 if nativeIndexOf and obj.indexOf is nativeIndexOf
  return true for own key, val of obj when val is target
  false


# Invoke a method with arguments on every item in a collection.
_.invoke = (obj, method) ->
  args = _.rest arguments, 2
  (if method then val[method] else val).apply(val, args) for val in obj


# Convenience version of a common use case of **map**: fetching a property.
_.pluck = (obj, key) ->
  _.map(obj, (val) -> val[key])


# Return the maximum item or (item-based computation).
_.max = (obj, iterator, context) ->
  return Math.max.apply(Math, obj) if not iterator and _.isArray(obj)
  result = computed: -Infinity
  _.each obj, (value, index, list) ->
    computed = if iterator then iterator.call(context, value, index, list) else value
    computed >= result.computed and (result = {value: value, computed: computed})
  result.value


# Return the minimum element (or element-based computation).
_.min = (obj, iterator, context) ->
  return Math.min.apply(Math, obj) if not iterator and _.isArray(obj)
  result = computed: Infinity
  _.each obj, (value, index, list) ->
    computed = if iterator then iterator.call(context, value, index, list) else value
    computed < result.computed and (result = {value: value, computed: computed})
  result.value


# Sort the object's values by a criterion produced by an iterator.
_.sortBy = (obj, iterator, context) ->
  _.pluck(((_.map obj, (value, index, list) ->
    {value: value, criteria: iterator.call(context, value, index, list)}
  ).sort((left, right) ->
    a = left.criteria; b = right.criteria
    if a < b then -1 else if a > b then 1 else 0
  )), 'value')


# Use a comparator function to figure out at what index an object should
# be inserted so as to maintain order. Uses binary search.
_.sortedIndex = (array, obj, iterator) ->
  iterator ||= _.identity
  low =  0
  high = array.length
  while low < high
    mid = (low + high) >> 1
    if iterator(array[mid]) < iterator(obj) then low = mid + 1 else high = mid
  low


# Convert anything iterable into a real, live array.
_.toArray = (iterable) ->
  return []                   if (!iterable)
  return iterable.toArray()   if (iterable.toArray)
  return iterable             if (_.isArray(iterable))
  return slice.call(iterable) if (_.isArguments(iterable))
  _.values(iterable)


# Return the number of elements in an object.
_.size = (obj) -> _.toArray(obj).length


# Array Functions
# ---------------

# Get the first element of an array. Passing `n` will return the first N
# values in the array. Aliased as **head**. The `guard` check allows it to work
# with **map**.
_.first = (array, n, guard) ->
  if n and not guard then slice.call(array, 0, n) else array[0]


# Returns everything but the first entry of the array. Aliased as **tail**.
# Especially useful on the arguments object. Passing an `index` will return
# the rest of the values in the array from that index onward. The `guard`
# check allows it to work with **map**.
_.rest = (array, index, guard) ->
  slice.call(array, if _.isUndefined(index) or guard then 1 else index)


# Get the last element of an array.
_.last = (array) -> array[array.length - 1]


# Trim out all falsy values from an array.
_.compact = (array) -> item for item in array when item


# Return a completely flattened version of an array.
_.flatten = (array) ->
  _.reduce array, (memo, value) ->
    return memo.concat(_.flatten(value)) if _.isArray value
    memo.push value
    memo
  , []


# Return a version of the array that does not contain the specified value(s).
_.without = (array) ->
  values = _.rest arguments
  val for val in _.toArray(array) when not _.include values, val


# Produce a duplicate-free version of the array. If the array has already
# been sorted, you have the option of using a faster algorithm.
_.uniq = (array, isSorted) ->
  memo = []
  for el, i in _.toArray array
    memo.push el if i is 0 || (if isSorted is true then _.last(memo) isnt el else not _.include(memo, el))
  memo


# Produce an array that contains every item shared between all the
# passed-in arrays.
_.intersect = (array) ->
  rest = _.rest arguments
  _.select _.uniq(array), (item) ->
    _.all rest, (other) ->
      _.indexOf(other, item) >= 0


# Zip together multiple lists into a single array -- elements that share
# an index go together.
_.zip = ->
  length =  _.max _.pluck arguments, 'length'
  results = new Array length
  for i in [0...length]
    results[i] = _.pluck arguments, String i
  results


# If the browser doesn't supply us with **indexOf** (I'm looking at you, MSIE),
# we need this function. Return the position of the first occurrence of an
# item in an array, or -1 if the item is not included in the array.
_.indexOf = (array, item) ->
  return array.indexOf item if nativeIndexOf and array.indexOf is nativeIndexOf
  i = 0; l = array.length
  while l - i
    if array[i] is item then return i else i++
  -1


# Provide JavaScript 1.6's **lastIndexOf**, delegating to the native function,
# if possible.
_.lastIndexOf = (array, item) ->
  return array.lastIndexOf(item) if nativeLastIndexOf and array.lastIndexOf is nativeLastIndexOf
  i = array.length
  while i
    if array[i] is item then return i else i--
  -1


# Generate an integer Array containing an arithmetic progression. A port of
# [the native Python **range** function](http://docs.python.org/library/functions.html#range).
_.range = (start, stop, step) ->
  a         = arguments
  solo      = a.length <= 1
  i = start = if solo then 0 else a[0]
  stop      = if solo then a[0] else a[1]
  step      = a[2] or 1
  len       = Math.ceil((stop - start) / step)
  return []   if len <= 0
  range     = new Array len
  idx       = 0
  loop
    return range if (if step > 0 then i - stop else stop - i) >= 0
    range[idx] = i
    idx++
    i+= step


# Function Functions
# ------------------

# Create a function bound to a given object (assigning `this`, and arguments,
# optionally). Binding with arguments is also known as **curry**.
_.bind = (func, obj) ->
  args = _.rest arguments, 2
  -> func.apply obj or root, args.concat arguments


# Bind all of an object's methods to that object. Useful for ensuring that
# all callbacks defined on an object belong to it.
_.bindAll = (obj) ->
  funcs = if arguments.length > 1 then _.rest(arguments) else _.functions(obj)
  _.each funcs, (f) -> obj[f] = _.bind obj[f], obj
  obj


# Delays a function for the given number of milliseconds, and then calls
# it with the arguments supplied.
_.delay = (func, wait) ->
  args = _.rest arguments, 2
  setTimeout((-> func.apply(func, args)), wait)


# Memoize an expensive function by storing its results.
_.memoize = (func, hasher) ->
  memo = {}
  hasher or= _.identity
  ->
    key = hasher.apply this, arguments
    return memo[key] if key of memo
    memo[key] = func.apply this, arguments


# Defers a function, scheduling it to run after the current call stack has
# cleared.
_.defer = (func) ->
  _.delay.apply _, [func, 1].concat _.rest arguments


# Returns the first function passed as an argument to the second,
# allowing you to adjust arguments, run code before and after, and
# conditionally execute the original function.
_.wrap = (func, wrapper) ->
  -> wrapper.apply wrapper, [func].concat arguments


# Returns a function that is the composition of a list of functions, each
# consuming the return value of the function that follows.
_.compose = ->
  funcs = arguments
  ->
    args = arguments
    for i in [funcs.length - 1..0] by -1
      args = [funcs[i].apply(this, args)]
    args[0]


# Object Functions
# ----------------

# Retrieve the names of an object's properties.
_.keys = nativeKeys or (obj) ->
  return _.range 0, obj.length if _.isArray(obj)
  key for key, val of obj


# Retrieve the values of an object's properties.
_.values = (obj) ->
  _.map obj, _.identity


# Return a sorted list of the function names available in Underscore.
_.functions = (obj) ->
  _.filter(_.keys(obj), (key) -> _.isFunction(obj[key])).sort()


# Extend a given object with all of the properties in a source object.
_.extend = (obj) ->
  for source in _.rest(arguments)
    obj[key] = val for key, val of source
  obj


# Create a (shallow-cloned) duplicate of an object.
_.clone = (obj) ->
  return obj.slice 0 if _.isArray obj
  _.extend {}, obj


# Invokes interceptor with the obj, and then returns obj.
# The primary purpose of this method is to "tap into" a method chain, in order to perform operations on intermediate results within the chain.
_.tap = (obj, interceptor) ->
  interceptor obj
  obj


# Perform a deep comparison to check if two objects are equal.
_.isEqual = (a, b) ->
  # Check object identity.
  return true if a is b
  # Different types?
  atype = typeof(a); btype = typeof(b)
  return false if atype isnt btype
  # Basic equality test (watch out for coercions).
  return true if `a == b`
  # One is falsy and the other truthy.
  return false if (!a and b) or (a and !b)
  # One of them implements an `isEqual()`?
  return a.isEqual(b) if a.isEqual
  # Check dates' integer values.
  return a.getTime() is b.getTime() if _.isDate(a) and _.isDate(b)
  # Both are NaN?
  return false if _.isNaN(a) and _.isNaN(b)
  # Compare regular expressions.
  if _.isRegExp(a) and _.isRegExp(b)
    return a.source     is b.source and
           a.global     is b.global and
           a.ignoreCase is b.ignoreCase and
           a.multiline  is b.multiline
  # If a is not an object by this point, we can't handle it.
  return false if atype isnt 'object'
  # Check for different array lengths before comparing contents.
  return false if a.length and (a.length isnt b.length)
  # Nothing else worked, deep compare the contents.
  aKeys = _.keys(a); bKeys = _.keys(b)
  # Different object sizes?
  return false if aKeys.length isnt bKeys.length
  # Recursive comparison of contents.
  return false for key, val of a when !(key of b) or !_.isEqual(val, b[key])
  true


# Is a given array or object empty?
_.isEmpty = (obj) ->
  return obj.length is 0 if _.isArray(obj) or _.isString(obj)
  return false for own key of obj
  true


# Is a given value a DOM element?
_.isElement   = (obj) -> obj and obj.nodeType is 1


# Is a given value an array?
_.isArray     = nativeIsArray or (obj) -> !!(obj and obj.concat and obj.unshift and not obj.callee)


# Is a given variable an arguments object?
_.isArguments = (obj) -> obj and obj.callee


# Is the given value a function?
_.isFunction  = (obj) -> !!(obj and obj.constructor and obj.call and obj.apply)


# Is the given value a string?
_.isString    = (obj) -> !!(obj is '' or (obj and obj.charCodeAt and obj.substr))


# Is a given value a number?
_.isNumber    = (obj) -> (obj is +obj) or toString.call(obj) is '[object Number]'


# Is a given value a boolean?
_.isBoolean   = (obj) -> obj is true or obj is false


# Is a given value a Date?
_.isDate      = (obj) -> !!(obj and obj.getTimezoneOffset and obj.setUTCFullYear)


# Is the given value a regular expression?
_.isRegExp    = (obj) -> !!(obj and obj.exec and (obj.ignoreCase or obj.ignoreCase is false))


# Is the given value NaN -- this one is interesting. `NaN != NaN`, and
# `isNaN(undefined) == true`, so we make sure it's a number first.
_.isNaN       = (obj) -> _.isNumber(obj) and window.isNaN(obj)


# Is a given value equal to null?
_.isNull      = (obj) -> obj is null


# Is a given variable undefined?
_.isUndefined = (obj) -> typeof obj is 'undefined'


# Utility Functions
# -----------------

# Run Underscore.js in noConflict mode, returning the `_` variable to its
# previous owner. Returns a reference to the Underscore object.
_.noConflict = ->
  root._ = previousUnderscore
  this


# Keep the identity function around for default iterators.
_.identity = (value) -> value


# Run a function `n` times.
_.times = (n, iterator, context) ->
  iterator.call context, i for i in [0...n]


# Break out of the middle of an iteration.
_.breakLoop = -> throw breaker


# Add your own custom functions to the Underscore object, ensuring that
# they're correctly added to the OOP wrapper as well.
_.mixin = (obj) ->
  for name in _.functions(obj)
    addToWrapper name, _[name] = obj[name]


# Generate a unique integer id (unique within the entire client session).
# Useful for temporary DOM ids.
idCounter = 0
_.uniqueId = (prefix) ->
  (prefix or '') + idCounter++


# By default, Underscore uses **ERB**-style template delimiters, change the
# following template settings to use alternative delimiters.
_.templateSettings = {
  start:        '<%'
  end:          '%>'
  interpolate:  /<%=(.+?)%>/g
}


# JavaScript templating a-la **ERB**, pilfered from John Resig's
# *Secrets of the JavaScript Ninja*, page 83.
# Single-quote fix from Rick Strahl.
# With alterations for arbitrary delimiters, and to preserve whitespace.
_.template = (str, data) ->
  c = _.templateSettings
  endMatch = new RegExp("'(?=[^"+c.end.substr(0, 1)+"]*"+escapeRegExp(c.end)+")","g")
  fn = new Function 'obj',
    'var p=[],print=function(){p.push.apply(p,arguments);};' +
    'with(obj||{}){p.push(\'' +
    str.replace(/\r/g, '\\r')
       .replace(/\n/g, '\\n')
       .replace(/\t/g, '\\t')
       .replace(endMatch,"✄")
       .split("'").join("\\'")
       .split("✄").join("'")
       .replace(c.interpolate, "',$1,'")
       .split(c.start).join("');")
       .split(c.end).join("p.push('") +
       "');}return p.join('');"
  if data then fn(data) else fn


# Aliases
# -------

_.forEach  = _.each
_.foldl    = _.inject = _.reduce
_.foldr    = _.reduceRight
_.select   = _.filter
_.all      = _.every
_.any      = _.some
_.contains = _.include
_.head     = _.first
_.tail     = _.rest
_.methods  = _.functions


# Setup the OOP Wrapper
# ---------------------

# If Underscore is called as a function, it returns a wrapped object that
# can be used OO-style. This wrapper holds altered versions of all the
# underscore functions. Wrapped objects may be chained.
wrapper = (obj) ->
  this._wrapped = obj
  this


# Helper function to continue chaining intermediate results.
result = (obj, chain) ->
  if chain then _(obj).chain() else obj


# A method to easily add functions to the OOP wrapper.
addToWrapper = (name, func) ->
  wrapper.prototype[name] = ->
    args = _.toArray arguments
    unshift.call args, this._wrapped
    result func.apply(_, args), this._chain


# Add all ofthe Underscore functions to the wrapper object.
_.mixin _


# Add all mutator Array functions to the wrapper.
_.each ['pop', 'push', 'reverse', 'shift', 'sort', 'splice', 'unshift'], (name) ->
  method = Array.prototype[name]
  wrapper.prototype[name] = ->
    method.apply(this._wrapped, arguments)
    result(this._wrapped, this._chain)


# Add all accessor Array functions to the wrapper.
_.each ['concat', 'join', 'slice'], (name) ->
  method = Array.prototype[name]
  wrapper.prototype[name] = ->
    result(method.apply(this._wrapped, arguments), this._chain)


# Start chaining a wrapped Underscore object.
wrapper::chain = ->
  this._chain = true
  this


# Extracts the result from a wrapped and chained object.
wrapper::value = -> this._wrapped



# Milk is a simple, fast way to get more Mustache into your CoffeeScript and
# Javascript.
#
# Mustache templates are reasonably simple -- plain text templates are
# sprinkled with "tags", which are (by default) a pair of curly braces
# surrounding some bit of content. A good resource for Mustache can be found
# [here](mustache.github.com).
TemplateCache = {}

# Tags used for working with data get their data by looking up a name in a
# context stack. This name corresponds to a key in a hash, and the stack is
# searched top to bottom for an object with given key. Dots in names are
# special: a single dot ('.') is "top of stack", and dotted names like 'a.b.c'
# do a chained lookups.
Find = (name, stack, value = null) ->
  return stack[stack.length - 1] if name == '.'
  [name, parts...] = name.split(/\./)
  for i in [stack.length - 1...-1]
    continue unless stack[i]?
    continue unless typeof stack[i] == 'object' and name of (ctx = stack[i])
    value = ctx[name]
    break

  value = Find(part, [value]) for part in parts

  # If we find a function in the stack, we'll treat it as a method, and call it
  # with `this` bound to the element it came from. If a method returns a
  # function, we treat it as a lambda, which doesn't have a bound `this`.
  if value instanceof Function
    value = do (value) -> ->
      val = value.apply(ctx, arguments)
      return (val instanceof Function) and val.apply(null, arguments) or val

  # Null values will be coerced to the empty string.
  return value

# Parsed templates are expanded by simply calling each function in turn.
Expand = (obj, tmpl, args...) -> (f.call(obj, args...) for f in tmpl).join('')

# For parsing, we'll basically need a template string to parse. We do need to
# remember to take the tag delimiters into account for the cache -- different
# parse trees can exist for the same template string!
Parse = (template, delimiters = ['{{','}}'], section = null) ->
  cache = (TemplateCache[delimiters.join(' ')] ||= {})
  return cache[template] if template of cache

  buffer = []

  # We'll use a regular expression to handle tag discovery. A proper parser
  # might be faster, but this is simpler, and certainly fast enough for now.
  # Since the tag delimiters may change over time, we'll want to rebuild the
  # regex when they change.
  BuildRegex = ->
    [tagOpen, tagClose] = delimiters
    return ///
      ([\s\S]*?)                # Capture the pre-tag content
      ([#{' '}\t]*)             # Capture the pre-tag whitespace
      (?: #{tagOpen} \s*        # Match the opening tag
      (?:
        (!)                  \s* ([\s\S]+?)       | # Comments
        (=)                  \s* ([\s\S]+?) \s* = | # Set Delimiters
        ({)                  \s* (\w[\S]*?) \s* } | # Triple Mustaches
        ([^0-9a-zA-Z._!={]?) \s* ([\w.][\S]*?)      # Everything else
      )
      \s* #{tagClose} )         # Match the closing tag
    ///gm

  tagPattern = BuildRegex()
  tagPattern.lastIndex = pos = (section || { start: 0 }).start

  # Useful errors should always be prefered - we should compile as much
  # relevant information as possible.
  parseError = (pos, msg) ->
    (endOfLine = /$/gm).lastIndex = pos
    endOfLine.exec(template)

    parsedLines = template.substr(0, pos).split('\n')
    lineNo      = parsedLines.length
    lastLine    = parsedLines[lineNo - 1]
    tagStart    = contentEnd + whitespace.length
    lastTag     = template.substr(tagStart + 1, pos - tagStart - 1)

    indent   = new Array(lastLine.length - lastTag.length + 1).join(' ')
    carets   = new Array(lastTag.length + 1).join('^')
    lastLine = lastLine + template.substr(pos, endOfLine.lastIndex - pos)

    error = new Error()
    error[key] = e[key] for key of e =
      "message": "#{msg}\n\nLine #{lineNo}:\n#{lastLine}\n#{indent}#{carets}"
      "error": msg, "line": lineNo, "char": indent.length, "tag": lastTag
    return error

  # As we start matching things, let's pull out our captures and build indices.
  while match = tagPattern.exec(template)
    [content, whitespace] = match[1..2]
    type = match[3] || match[5] || match[7] || match[9]
    tag  = match[4] || match[6] || match[8] || match[10]

    contentEnd = (pos + content.length) - 1
    pos        = tagPattern.lastIndex

    # Standalone tags are tags on lines without any non-whitespace characters.
    isStandalone = (contentEnd == -1 or template.charAt(contentEnd) == '\n') &&
                   template.charAt(pos) in [ undefined, '', '\r', '\n' ]

    # We should just add static content to the buffer.
    buffer.push(do (content) -> -> content) if content

    # If we're dealing with a standalone tag that's not interpolation, we
    # should consume the newline immediately following the tag. If we're not,
    # we need to buffer the whitespace we captured earlier.
    if isStandalone and type not in ['', '&', '{']
      pos += 1 if template.charAt(pos) == '\r'
      pos += 1 if template.charAt(pos) == '\n'
    else if whitespace
      buffer.push(do (whitespace) -> -> whitespace)
      contentEnd += whitespace.length
      whitespace = ''

    # Now we'll handle the tag itself:
    switch type

      # Comment tags should simply be ignored.
      when '!' then break

      # Interpolations are handled by finding the value in the context stack,
      # calling and rendering lambdas, and escaping the value if appropriate.
      when '', '&', '{'
        buildInterpolationTag = (name, is_unescaped) ->
          return (context) ->
            if (value = Find(name, context) ? '') instanceof Function
              value = Expand(this, Parse("#{value()}"), arguments...)
            value = @escape("#{value}") unless is_unescaped
            return "#{value}"
        buffer.push(buildInterpolationTag(tag, type))

      # Partial data is looked up lazily by the given function, indented as
      # appropriate, and then rendered.
      when '>'
        buildPartialTag = (name, indentation) ->
          return (context, partials) ->
            partial = partials(name).toString()
            partial = partial.replace(/^(?=.)/gm, indentation) if indentation
            return Expand(this, Parse(partial), arguments...)
        buffer.push(buildPartialTag(tag, whitespace))

      # Sections and Inverted Sections make a recursive parsing pass, allowing
      # us to use the call stack to handle section parsing. This will go until
      # it reaches the matching End Section tag, when it will return the
      # (cached!) template it parsed, along with the index it stopped at.
      when '#', '^'
        sectionInfo =
          name: tag, start: pos
          error: parseError(tagPattern.lastIndex, "Unclosed section '#{tag}'!")
        [tmpl, pos] = Parse(template, delimiters, sectionInfo)

        # Sections are rendered by finding the value in the context stack,
        # coercing it into an array (unless the value is falsey), and rendering
        # the template with each element of the array taking a turn atop the
        # context stack. If the value was a function, the template is filtered
        # through it before rendering.
        sectionInfo['#'] = buildSectionTag = (name, delims, raw) ->
          return (context) ->
            value = Find(name, context) || []
            tmpl  = if value instanceof Function then value(raw) else raw
            value = [value] unless value instanceof Array
            parsed = Parse(tmpl || '', delims)

            context.push(value)
            result = for v in value
              context[context.length - 1] = v
              Expand(this, parsed, arguments...)
            context.pop()

            return result.join('')

        # Inverted Sections render under almost opposite conditions: their
        # contents will only be rendered when the retrieved value is either
        # falsey or an empty array.
        sectionInfo['^'] = buildInvertedSectionTag = (name, delims, raw) ->
          return (context) ->
            value = Find(name, context) || []
            value = [1] unless value instanceof Array
            value = if value.length is 0 then Parse(raw, delims) else []
            return Expand(this, value, arguments...)

        buffer.push(sectionInfo[type](tag, delimiters, tmpl))

      # When the parser encounters an End Section tag, it runs a couple of
      # quick sanity checks, then returns control back to its caller.
      when '/'
        unless section?
          error = "End Section tag '#{tag}' found, but not in section!"
        else if tag != (name = section.name)
          error = "End Section tag closes '#{tag}'; expected '#{name}'!"
        throw parseError(tagPattern.lastIndex, error) if error

        template = template[section.start..contentEnd]
        cache[template] = buffer
        return [template, pos]

      # The Set Delimiters tag needs to update the delimiters after some error
      # checking, and rebuild the regular expression we're using to match tags.
      when '='
        unless (delimiters = tag.split(/\s+/)).length == 2
          error = "Set Delimiters tags should have two and only two values!"
        throw parseError(tagPattern.lastIndex, error) if error

        escape     = /[-[\]{}()*+?.,\\^$|#]/g
        delimiters = (d.replace(escape, "\\$&") for d in delimiters)
        tagPattern = BuildRegex()

      # Any other tag type is probably a typo.
      else
        throw parseError(tagPattern.lastIndex, "Unknown tag type -- #{type}")

    # Now that we've finished with this tag, we prepare to parse the next one!
    tagPattern.lastIndex = if pos? then pos else template.length

  # At this point, we've parsed all the tags.  If we've still got a `section`,
  # someone left a section tag open.
  throw section.error if section?

  # All the tags is not all the content; if there's anything left over, append
  # it to the buffer.  Then we'll cache the buffer and return it!
  buffer.push(-> template[pos..]) unless template.length == pos
  return cache[template] = buffer

# ### Public API

# The exported object (globally `Milk` in browsers) forms Milk's public API:
Milk =
  VERSION: '1.2.0'
  # Helpers are a form of context, implicitly on the bottom of the stack. This
  # is a global value, and may be either an object or an array.
  helpers:  []
  # Partials may also be provided globally.
  partials: null
  # The `escape` method performs basic content escaping, and may be either
  # called or overridden with an alternate escaping mechanism.
  escape: (value) ->
    entities = { '&': 'amp', '"': 'quot', '<': 'lt', '>': 'gt' }
    return value.replace(/[&"<>]/g, (ch) -> "&#{ entities[ch] };")
  # Rendering is simple: given a template and some data, it populates the
  # template. If your template uses Partial Tags, you may also supply a hash or
  # a function, or simply override `Milk.partials`. There is no Step Three.
  render: (template, data, partials = null) ->
    unless (partials ||= @partials || {}) instanceof Function
      partials = do (partials) -> (name) ->
        throw "Unknown partial '#{name}'!" unless name of partials
        return Find(name, [partials])

    context = if @helpers instanceof Array then @helpers else [@helpers]
    return Expand(this, Parse(template), context.concat([data]), partials)

# Happy hacking!
if exports?
  exports[key] = Milk[key] for key of Milk
else
  this.Milk = Milk