from protorpc import messages


class DatastoreKey(messages.Message):
	
	encoded = messages.StringField(1)
	parent = messages.StringField(2)
	kind = messages.StringField(3)
	ancestry = messages.StringField(4, repeated=True)