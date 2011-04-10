from ProvidenceClarity.struct.util import DictProxy

from momentum.fatcatmap.models.core.indexer import map as m
from momentum.fatcatmap.models.core.indexer import entry as e
from momentum.fatcatmap.models.core.indexer import config as c
from momentum.fatcatmap.models.core.indexer import descriptor as d

from momentum.fatcatmap.pipelines.indexer import FCMIndexerPipeline


class CoreIndexerPipeline(FCMIndexerPipeline):

	models = DictProxy({
	
		'kind': c.IndexedKind,
		'entry': m.IndexEntry,
		'mapping': m.IndexMapping,
		'property': c.IndexedProperty,
		'descriptor': DictProxy({		
			'status': d.IndexingStatus,
			'reverse': d.ReverseIndexPresence
		})
	
	})