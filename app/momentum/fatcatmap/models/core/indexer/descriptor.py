from momentum.fatcatmap.models.core.descriptor import Descriptor


class ReverseIndexPresence(Descriptor):
	
	entries = m.ldb.StringListProperty()
	
	
class IndexingStatus(Descriptor):
	
	last_indexed = m.ldb.DateTimeProperty()
	next_indexing = m.ldb.DateTimeProperty()
	flag_for_indexing = m.ldb.BooleanProperty(default=False)