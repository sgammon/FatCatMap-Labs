from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/dev/default-data.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/dev.html', 'source/dev/default-data.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_panel_content(context, environment=environment):
        l_msgs = context.resolve('msgs')
        if 0: yield None
        yield u'\n\n'
        l_msg = missing
        for l_msg in l_msgs:
            if 0: yield None
            yield u'\n\t<p>%s</p>\n' % (
                l_msg, 
            )
        l_msg = missing
        yield u'\n\n'

    def block_panel_header(context, environment=environment):
        if 0: yield None
        yield u'Add Default Data'

    def block_page_title(context, environment=environment):
        if 0: yield None
        yield u'Add Default Data'

    def block_panel_backnav(context, environment=environment):
        l_link = context.resolve('link')
        if 0: yield None
        yield u'<a href="%s">Development Console</a>' % (
            context.call(l_link, 'dev-index'), 
        )

    blocks = {'panel_content': block_panel_content, 'panel_header': block_panel_header, 'page_title': block_page_title, 'panel_backnav': block_panel_backnav}
    debug_info = '1=9&7=15&9=20&10=23&4=28&3=32&5=36'
    return locals()