from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/content/visualize/layout.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/main.html', 'source/content/visualize/layout.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_content_body(context, environment=environment):
        if 0: yield None
        yield u"\n\n\t<div id='landingWrapper' class='fullwidth fullheight textcenter'>\n\t\t"
        for event in context.blocks['visualizer'][0](context):
            yield event
        yield u'\n\t</div>\n\n'

    def block_subtitle(context, environment=environment):
        if 0: yield None

    def block_visualizer(context, environment=environment):
        if 0: yield None
        yield u'\n\t\t'

    def block_postnorth(context, environment=environment):
        l_assets = context.resolve('assets')
        if 0: yield None
        yield u'<link rel="stylesheet" media="screen" href="%s">' % (
            context.call(environment.getattr(l_assets, 'style'), 'visualize', 'site'), 
        )

    def block_title(context, environment=environment):
        if 0: yield None
        for event in context.blocks['subtitle'][0](context):
            yield event
        yield u'Visualize - FatCatMap'

    blocks = {'content_body': block_content_body, 'subtitle': block_subtitle, 'visualizer': block_visualizer, 'postnorth': block_postnorth, 'title': block_title}
    debug_info = '1=9&7=15&10=18&3=22&10=25&5=29&3=36'
    return locals()