import simplejson as json
from ProvidenceClarity.struct.util import ConfigurableStruct
from momentum.fatcatmap.core.adapters.format import FCMFormatAdapter


class FCMJSONEncoderMiddleware(ConfigurableStruct):
	
	def _encodeToJSON(self, input_s, **kwargs):
		return json.dumps(input_s, **kwargs)

		
class FCMJSONDecoderMiddleware(ConfigurableStruct):
	
	def _decodeFromJSON(self, input_s, **kwargs):
		return json.loads(input_s, **kwargs)
		

class FCMJSONAdapter(FCMFormatAdapter):

	encoder = FCMJSONEncoderMiddleware
	decoder = FCMJSONDecoderMiddleware
		
	def encode(self, **kwargs):
		self.set_output(self.encoder._encodeToJSON(self.get_input(), **kwargs))
		return self

	def decode(self, **kwargs):
		self.set_output(self.decoder._decodeFromJSON(self.get_input(), **kwargs))
		return self