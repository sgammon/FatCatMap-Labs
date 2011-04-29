import webapp2 as webapp
from google.appengine.ext.webapp import util

## ProtoRPC Imports
from protorpc import remote
from protorpc import messages
from protorpc import service_handlers

## Service Imports
from momentum.fatcatmap.api.data import DataAPIService
from momentum.fatcatmap.api.graph import GraphAPIService
from momentum.fatcatmap.api.query import QueryAPIService
from momentum.fatcatmap.api.charts import ChartsAPIService

## Map URL's to services
service_mappings = service_handlers.service_mapping([

	('/_api/rpc/data', DataAPIService), ## For creating/updating/retrieving userspace data
	('/_api/rpc/graph', GraphAPIService), ## Recursively generates structures suitable for graphing
	('/_api/rpc/query', QueryAPIService), ## Exposes methods to query and search userland data
	('/_api/rpc/chart', ChartsAPIService), ## Assembles data structures suitable for visualizations.	

])

application = webapp.WSGIApplication(service_mappings)

def main():
	util.run_wsgi_app(application)

if __name__ == '__main__':
	main()