from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/dev/cache.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/dev.html', 'source/dev/cache.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_panel_content(context, environment=environment):
        l_link = context.resolve('link')
        l_message = context.resolve('message')
        l_stats = context.resolve('stats')
        if 0: yield None
        yield u'\n\n'
        if l_message:
            if 0: yield None
            yield u"\n\t<div class='notice'><p>%s</p></div>\n" % (
                l_message, 
            )
        yield u'\n\n<h2>Memcache Stats:</h2><br />\n\n<ul>\n\t<li>Hits: %s</li>\n\t<li>Misses: %s</li>\n\t<li>Byte Hits: %s</li>\n\t<li>Item Count: %s</li>\n\t<li>Byte Count: %s</li>\n\t<li>Oldest Item: %s</li>\n</ul>\n\n<br />\n<br />\n\n<h2>Flush Memcache:</h2><br />\n\n<form action="%s" method=\'post\'>\n\t<input type=\'hidden\' name=\'action\' value=\'clear\' />\n\t<input type=\'submit\' value=\'Clear Memcache of All Values\'>\n</form>\n\n<br />\n<br />\n\n' % (
            environment.getattr(l_stats, 'hits'), 
            environment.getattr(l_stats, 'misses'), 
            environment.getattr(l_stats, 'byte_hits'), 
            context.call(environment.getattr(l_stats, '__getitem__'), 'items'), 
            environment.getattr(l_stats, 'bytes'), 
            environment.getattr(l_stats, 'oldest_item_age'), 
            context.call(l_link, 'dev-cache'), 
        )

    def block_panel_header(context, environment=environment):
        if 0: yield None
        yield u'Cache Management'

    def block_page_title(context, environment=environment):
        if 0: yield None
        yield u'Cache Management'

    def block_panel_backnav(context, environment=environment):
        l_link = context.resolve('link')
        if 0: yield None
        yield u'<a href="%s">Development Console</a>' % (
            context.call(l_link, 'dev-index'), 
        )

    blocks = {'panel_content': block_panel_content, 'panel_header': block_panel_header, 'page_title': block_page_title, 'panel_backnav': block_panel_backnav}
    debug_info = '1=9&7=15&9=21&10=24&16=27&17=28&18=29&19=30&20=31&21=32&29=33&4=36&3=40&5=44'
    return locals()