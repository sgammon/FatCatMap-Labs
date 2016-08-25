"""
Warmup request handler - imports and caches a bunch of data to prepare for requests. Always responds with a 200 OK.

"""

## Get ready
import os
import sys
import bootstrap

bootstrap.MomentumBootstrapper.prepareImports()

## Libraries
import ndb
import webob
import jinja2
import config
import logging
import webapp2
import slimmer
import protorpc
import pipeline
import mapreduce
import webapp2_extras
import wsgiref.handlers
import ProvidenceClarity

## GAE APIs
import google
from google import appengine
from google.appengine import api
from google.appengine import ext
from google.appengine.api import mail
from google.appengine.api import users
from google.appengine.api import images
from google.appengine.api import runtime
from google.appengine.api import urlfetch
from google.appengine.api import memcache
from google.appengine.api import datastore
from google.appengine.api import taskqueue

## GAE Ext
from google.appengine.ext import db
from google.appengine.ext import gql
from google.appengine.ext import search

## Momentum
import momentum
from momentum import platform
from momentum import fatcatmap

## Platform
from momentum.platform import api
from momentum.platform import gateway
from momentum.platform import mappers
from momentum.platform import handlers
from momentum.platform import pipelines

## FatCatMap
from momentum.fatcatmap import api
from momentum.fatcatmap import core
from momentum.fatcatmap import forms
from momentum.fatcatmap import models
from momentum.fatcatmap import routing
from momentum.fatcatmap import messages
from momentum.fatcatmap import handlers
from momentum.fatcatmap import pipelines
from momentum.fatcatmap import decorators

## Compiled templates
try:
	import templates
	import templates.compiled
except ImportError, e:
	logging.warning('Failed to import compiled templates path... skipping.')

else:
	try:
		import templates.compiled.admin
		import templates.compiled.content
		import templates.compiled.core
		import templates.compiled.dev
		import templates.compiled.elements
		import templates.compiled.layouts
		import templates.compiled.macros
		import templates.compiled.main
		import templates.compiled.platform
		import templates.compiled.snippets
	
		from templates.compiled.admin import *
		from templates.compiled.content import *
		from templates.compiled.core import *
		from templates.compiled.dev import *
		from templates.compiled.elements import *
		from templates.compiled.layouts import *
		from templates.compiled.macros import *
		from templates.compiled.main import *
		from templates.compiled.platform import *
		from templates.compiled.snippets import *
		
	except ImportError, e:
		logging.warning('Failed to import compiled template module: '+str(e))


def respond200():

	logging.debug('Warming up interpreter caches [CGI]...')
	
	print "HTTP/1.1 200 OK"
	print "Content-Type: text/plain"
	print ""
	print "WARMUP_SUCCESS"


class WarmupHandler(webapp2.RequestHandler):

	def get(self):
	
		logging.debug('Warming up interpreter caches [WSGI]...')
		self.response.out.write("Warmup succeeded.")
		
		
Warmup = webapp2.WSGIApplication([webapp2.Route('/_ah/warmup', WarmupHandler, name='warmup')])

if __name__ == '__main__':
	respond200()