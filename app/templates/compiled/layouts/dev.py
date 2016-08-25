from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/layouts/dev.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/main.html', 'source/layouts/dev.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_panel_content(context, environment=environment):
        if 0: yield None

    def block_page_title(context, environment=environment):
        if 0: yield None

    def block_title(context, environment=environment):
        if 0: yield None
        for event in context.blocks['page_title'][0](context):
            yield event
        yield u' - Development Console - FatCatMap'

    def block_panel_header(context, environment=environment):
        if 0: yield None

    def block_panel_header_subtext(context, environment=environment):
        if 0: yield None
        yield u" <span class='small'>return to --> "
        for event in context.blocks['panel_backnav'][0](context):
            yield event
        yield u'</span>'

    def block_content_body(context, environment=environment):
        if 0: yield None
        yield u"\n\n<div class='padding-20'>\n\n\t<div class='contentPanel'>\n\n\t\t<div class='panelHeader'>\n\t\t\t<h1>"
        for event in context.blocks['panel_header'][0](context):
            yield event
        yield u'</h1>'
        for event in context.blocks['panel_header_subtext'][0](context):
            yield event
        yield u"\n\t\t</div>\n\t\t<div class='panelContent'>\n\t\t\t"
        for event in context.blocks['panel_content'][0](context):
            yield event
        yield u'\n\t\t</div>\n\t\t\n\t</div>\n\n</div>\t\n'

    def block_panel_backnav(context, environment=environment):
        if 0: yield None

    blocks = {'panel_content': block_panel_content, 'page_title': block_page_title, 'title': block_title, 'panel_header': block_panel_header, 'panel_header_subtext': block_panel_header_subtext, 'content_body': block_content_body, 'panel_backnav': block_panel_backnav}
    debug_info = '1=9&15=15&3=18&12=27&5=37&12=40&15=46&12=50'
    return locals()