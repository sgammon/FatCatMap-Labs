import protorpc
from protorpc import remote

from momentum.services.flags import audit
from momentum.services.flags import caching
from momentum.services.flags import security

from ProvidenceClarity.struct.util import DictProxy

from momentum.services.core.service import MomentumService


## Expose service flags (middleware decorators)
flags = DictProxy({

	'audit': DictProxy({
		'monitor': audit.Monitor,
		'debug': audit.Debug,
		'loglevel': audit.LogLevel,
	}),
	
	'caching': DictProxy({
		'local': caching.LocalCacheable,
		'memcache': caching.MemCacheable,
		'cacheable': caching.Cacheable,
	}),
	
	'security': DictProxy({
		'authorize': security.Authorize,
		'authenticate': security.Authenticate,
		'admin': security.AdminOnly
	})

})