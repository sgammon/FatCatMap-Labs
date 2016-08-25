from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/content/map/layout.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/lite.html', 'source/content/map/layout.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_subtitle(context, environment=environment):
        if 0: yield None

    def block_northstyle(context, environment=environment):
        l_assets = context.resolve('assets')
        if 0: yield None
        yield u'\n<link rel=\'stylesheet\' href="%s" media=\'screen\'>\n' % (
            context.call(environment.getattr(l_assets, 'style'), 'map', 'site'), 
        )

    def block_title(context, environment=environment):
        if 0: yield None
        for event in context.blocks['subtitle'][0](context):
            yield event
        yield u' - Map influence data in real time - FatCatMap'

    def block_sidebars(context, environment=environment):
        if 0: yield None
        yield u'\n\t<!-- Sidebars -->\n\t'
        template = environment.get_template('elements/pane/details-sidebar.html', 'source/content/map/layout.html')
        for event in template.root_render_func(template.new_context(context.parent, True, locals())):
            yield event
        yield u'\n\t'
        template = environment.get_template('elements/pane/controls-sidebar.html', 'source/content/map/layout.html')
        for event in template.root_render_func(template.new_context(context.parent, True, locals())):
            yield event
        yield u'\n'

    def block_southloader(context, environment=environment):
        l_assets = context.resolve('assets')
        if 0: yield None
        yield u'\n\t{\n\t\tload: ["%s"]\n\t},\n\t{\n\t\tload: ["%s"]\n\t},\n' % (
            context.call(environment.getattr(l_assets, 'script'), 'core', 'd3'), 
            context.call(environment.getattr(l_assets, 'script'), 'map', 'site'), 
        )

    def block_grapher(context, environment=environment):
        if 0: yield None
        yield u'\n\t\t'

    def block_content_body(context, environment=environment):
        if 0: yield None
        yield u"\n\t\n\t<div id='nodeCompare'>\n\t\t<div id='compareleft' class='graphblock muted'>\n\t\t\t<span>drag for details</span>\n\t\t</div>\n\t\n\t\t<div id='compareright' class='graphblock muted hidden'>\n\t\t\t<span>drag to compare</span>\n\t\t</div>\n\t</div>\n\n\t<div id='grapher' class='fullheight fullwidth textcenter'>\n\t\t"
        for event in context.blocks['grapher'][0](context):
            yield event
        yield u'\n\t</div>\n'

    blocks = {'subtitle': block_subtitle, 'northstyle': block_northstyle, 'title': block_title, 'sidebars': block_sidebars, 'southloader': block_southloader, 'grapher': block_grapher, 'content_body': block_content_body}
    debug_info = '1=9&3=15&5=18&6=22&3=25&10=31&12=34&13=38&34=43&36=47&39=48&29=51&16=55&29=58'
    return locals()