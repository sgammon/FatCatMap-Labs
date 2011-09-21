from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/snippets/superfooter.html'

    def root(context, environment=environment):
        l_link = context.resolve('link')
        if 0: yield None
        yield u'<div class=\'floatleft\' id=\'utilityLinks\'>\n\t&copy;2011 political momentum (<a href="%s">about</a> - <a href="%s"> legal</a> - <a href="%s">help</a>)\n</div>\n\n\n<div id=\'bottomFcmBranding\' class=\'floatright\'>\n\t<a href=\'http://momentum.io\' target=\'_blank\' class=\'noicon\'><div id=\'momentumBrand\'></div></a>\n</div>\n\n<div id=\'globalActivityIndicator\' class=\'floatright\'>\n</div>' % (
            context.call(l_link, 'about:landing'), 
            context.call(l_link, 'legal:landing'), 
            context.call(l_link, 'help:landing'), 
        )

    blocks = {}
    debug_info = '2=10'
    return locals()