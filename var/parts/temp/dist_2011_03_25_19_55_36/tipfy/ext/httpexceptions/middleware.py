# -*- coding: utf-8 -*-

from tipfy import Response, Tipfy
from tipfy.ext.jinja2 import render_template
import logging

class HTTPExceptionMiddleware(object):

  def handle_exception(self, handler):
    logging.exception(handler)
    code = handler.code if hasattr(handler, 'code') else 500
    return Response(render_template("common/templates/%s.html" % \
                                    str(code if code in (404, 500) else 500),
                                    ** {'request': Tipfy.request}),
                    status = code, mimetype = 'text/html')
