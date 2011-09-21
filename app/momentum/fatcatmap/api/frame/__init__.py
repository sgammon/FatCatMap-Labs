import logging
from momentum.services import remote

from jinja2 import Environment as JEnvironment

from momentum.fatcatmap.api import FatCatMapAPIService
from momentum.fatcatmap.messages import frame as messages

from momentum.fatcatmap.core.output import fcmOutputEnvironmentFactory


class FrameAPIService(FatCatMapAPIService):

	config_path = 'services.frame.config'

	@remote.method(messages.FrameRequest, messages.RawFrameResponse)
	def raw(self, request):
		pass

	@remote.method(messages.FrameRequest, messages.RenderedFrameResponse)
	def render(self, request):
		
		if request.path is None:
			raise remote.ApplicationError('Must provide a template path to render.')
		else:		
			try:
				## Load template
				loader = JEnvironment()
				fcmOutputEnvironmentFactory(loader)

				## Build context
				if len(request.context) > 0:
					template_context = {}
					for contextitem in request.context:
						template_context[contextitem.name]

				template = loader.get_template(request.path).render()
				return messages.RenderedFrameResponse(src=template, path=request.path)
			except Exception, e:
				raise remote.ApplicationError(str(e))