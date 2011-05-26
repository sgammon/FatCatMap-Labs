import logging

from google.appengine.api import memcache
from momentum.fatcatmap.handlers import WebHandler

from momentum.fatcatmap.forms.graph import NewObjectRelationForm
from momentum.fatcatmap.forms.graph import NewObjectCollectionForm

from momentum.fatcatmap.pipelines.graph.relation import NewObjectRelation
from momentum.fatcatmap.pipelines.graph.collection import NewObjectCollection


class Index(WebHandler):
	
	def get(self):
		return self.render('dev/index.html')
		
		
class CacheManagement(WebHandler):
	
	def get(self):
		if 'message' in self.request.args:
			return self.render('dev/cache.html', stats=memcache.get_stats(), message=self.request.args.get('message'))
		else:
			return self.render('dev/cache.html', stats=memcache.get_stats())

		
	def post(self):
		if 'action' in self.request.form and self.request.form.get('action') == 'clear':
			memcache.flush_all()
			return self.redirect(self.url_for('dev-cache', message='Memcache successfully reset.'))
		
		
class RPCConsole(WebHandler):
	
	def get(self):
		return self.render('dev/rpc-console.html')
		
		
class DefaultData(WebHandler):
	
	def get(self):
		from momentum.fatcatmap.dev.default_data import *
		messages = []
		for fxn in all_functions:
			res = fxn()
			messages.append('Created '+str(len(res))+' keys with function '+str(fxn)+'.')
		return self.render('dev/default-data.html', msgs=messages)
		
		
class AddData(WebHandler):

	def get(self):
		if self.request.args.get('msg', False) is not False:
			message = self.request.args.get('msg')
		else:
			message = None
			
		new_collection = NewObjectCollectionForm(self.request)
		new_collection.set_method('POST')
		new_collection.set_action(self.url_for('dev-add-data'))
		
		new_relation = NewObjectRelationForm(self.request)
		new_relation.set_method('POST')
		new_relation.set_action(self.url_for('dev-add-data'))
			
		return self.render('dev/add-data.html',
							msg=message,
							create_collection=new_collection,
							create_relation=new_relation)
							
	def post(self):
		if self.request.form.get('mode', False) == False:
			return self.redirect_to('dev-add-data', msg='You must post a mode and form data.')
		else:
			if self.request.form.get('mode') == 'new_graph_object':
				form = NewObjectCollectionForm(self.request)
				if form.validate():
					n = NewObjectCollection(form.object_type.data, form.node_type.data, form.label.data)
					logging.info('Starting NewObjectCollection:')
					logging.info('---Object Type: '+str(form.object_type.data))
					logging.info('---Node Type: '+str(form.node_type.data))
					logging.info('---Label: '+str(form.label.data))
					n.start(queue_name='graph')
					return self.redirect_to('dev-add-data', msg='NewObjectCollection pipeline started successfully.')
				else:
					return self.redirect_to('dev-add-data', msg='Form would not validate!')
			elif self.request.form.get('mode') == 'new_graph_relation':
				form = NewObjectRelationForm(self.request)
				if form.validate():
					r = NewObjectRelation(form.edge_type.data, [form.node1.data, form.node2.data])
					logging.info('Starting NewObjectRelation:')
					logging.info('---Edge Type: '+str(form.edge_type.data))
					logging.info('---Node A: '+str(form.node1.data))
					logging.info('---Node B: '+str(form.node2.data))
					r.start(queue_name='graph')
					return self.redirect_to('dev-add-data', msg='NewObjectRelation pipeline started successfully.')
				else:
					return self.redirect_to('dev-add-data', msg='Form would not validate!')
		
		
class WebShell(WebHandler):
	
	def get(self):
		pass