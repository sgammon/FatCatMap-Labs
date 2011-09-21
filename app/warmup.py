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