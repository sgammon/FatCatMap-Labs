import sys

## Google Imports
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

## Service Imports
from momentum.fatcatmap.api.data import DataAPIService
from momentum.fatcatmap.api.graph import GraphAPIService
from momentum.fatcatmap.api.frame import FrameAPIService
from momentum.fatcatmap.api.query import QueryAPIService
from momentum.fatcatmap.api.charts import ChartsAPIService
from momentum.fatcatmap.api.session import SessionAPIService


def main():
	
	## Add to sys.path
	if 'lib' not in sys.path:
		# Add lib as primary libraries directory, with fallback to lib/dist
		# and optionally to lib/dist.zip, loaded using zipimport.
		sys.path[0:0] = ['lib', 'lib/dist', 'lib/dist.zip']
	
	from protorpc import service_handlers
	
	## Map URL's to services
	service_mappings = service_handlers.service_mapping([

		('/_api/rpc/data', DataAPIService), ## For creating/updating/retrieving userspace data
		('/_api/rpc/graph', GraphAPIService), ## Recursively generates structures suitable for graphing
		('/_api/rpc/frame', FrameAPIService), ## Assembles full HTML or JSON template views for natives/other data
		('/_api/rpc/query', QueryAPIService), ## Exposes methods to query and search userland data
		('/_api/rpc/chart', ChartsAPIService), ## Assembles data structures suitable for visualizations.	
		('/_api/rpc/session', SessionAPIService) ## Allows a user to establish and manage a persistent session

	])
	
	application = webapp.WSGIApplication(service_mappings)
	util.run_wsgi_app(application)

if __name__ == '__main__':
	main()