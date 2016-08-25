from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/dev/test.html'

    def root(context, environment=environment):
        if 0: yield None
        yield u'<h1>Hello world!</h1>'

    blocks = {}
    debug_info = ''
    return locals()