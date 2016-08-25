from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/elements/__north.html'

    def root(context, environment=environment):
        if 0: yield None
        yield u'<meta name="description" content="FatCatMap lets you browse the political universe!">\n<meta name="author" content="Political Momentum, Inc.">\n<link rel="shortcut icon" href="/favicon.ico">\n<link rel="apple-touch-icon" href="/apple-touch-icon.png">'

    blocks = {}
    debug_info = ''
    return locals()