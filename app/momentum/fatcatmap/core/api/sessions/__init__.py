import os
import hashlib
from momentum.fatcatmap.core.api import MomentumCoreAPI


class CoreSessionsAPI(MomentumCoreAPI):


	def keyFactory(self, client_id=None):

		return ('CLIENT', 'SESSION')

		''' Provision a new session ID and (optionally) client ID. '''

		if not client_id:
			client_id = hashlib.md5(reduce(lambda x, y: x+'::'+y, [os.environ['REMOTE_ADDR'], self.request.headers.get('User-Agent', '--UNKNOWNUA--') , os.urandom(8).encode('hex')])).hexdigest()

		session_id = hashlib.sha256(reduce(lambda x, y: x+'::'+y, [client_id, os.urandom(8).encode('hex')])).hexdigest()

		return (client_id, session_id)