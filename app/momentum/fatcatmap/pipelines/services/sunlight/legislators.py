from momentum.fatcatmap.models.government.boundaries import USState

from momentum.fatcatmap.models.government.legislative import Legislator
from momentum.fatcatmap.models.government.legislative import Legislature
from momentum.fatcatmap.models.government.legislative import LegislativeChamber

from momentum.fatcatmap.pipelines.services.sunlight import SunlightPipeline


class GetLegislator(SunlightPipeline):

	def run(self, legislator=False, **kwargs):
		pass
	
	
class GetLegislators(SunlightPipeline):

	def run(self, **kwargs):
		pass
		

class GetCommittee(SunlightPipeline):
	
	def run(self, **kwargs):
		pass
		
		
class GetCommittees(SunlightPipeline):
	
	def run(self, **kwargs):
		pass