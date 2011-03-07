# -*- coding: utf-8 -*-
from tipfy import RequestHandler, Response
from tipfyext.jinja2 import Jinja2Mixin


class WebHandler(RequestHandler, Jinja2Mixin):

    def render(self, path, **kwargs):
        return self.render_response(path, **kwargs)