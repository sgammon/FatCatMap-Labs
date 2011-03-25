from ndb import context
from ndb import tasklets
from wtforms import fields as f
from momentum.fatcatmap.core.forms import FCMForm
from momentum.fatcatmap.models.core.object import Node

def doNodeQuery():
	n = Node.query()
	return n.fetch(50)

def getNodeOptions():
	
	n = doNodeQuery()
	nodes = [('__NULL__', '---Select a Node---')]
	for node in n:
		nodes.append((node.key.urlsafe(), node.label))
	return nodes


class NewObjectCollectionForm(FCMForm):

	mode = f.HiddenField(default='new_graph_object')
	object_type = f.TextField(default='natural.Person')
	node_type = f.TextField(default='politics.legislative.Legislator')
	label = f.TextField()
	
	
class NewObjectRelationForm(FCMForm):

	mode = f.HiddenField(default='new_graph_relation')
	edge_type = f.TextField(default='social.Friendship')
	node1 = f.SelectField(choices=getNodeOptions())
	node2 = f.SelectField(choices=getNodeOptions())