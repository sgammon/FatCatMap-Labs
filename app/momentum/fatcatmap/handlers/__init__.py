# -*- coding: utf-8 -*-
from tipfy import RequestHandler, Response
from tipfyext.jinja2 import Jinja2Mixin

from google.appengine.api import users


class WebHandler(RequestHandler, Jinja2Mixin):

    def render(self, path, **kwargs):
		return self.render_response(path, link=self.url_for, user=users.get_current_user(), **kwargs)