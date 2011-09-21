from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/admin/index.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/main.html', 'source/admin/index.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_content_body(context, environment=environment):
        if 0: yield None
        yield u"\n\n<div class='padding-20 halfwidth fullheight'>\n\n\t<div class='contentPanel'>\n\n\t\t<div class='panelHeader'>\n\t\t\t<h1>Management Console</h1>\n\t\t</div>\n\t\t<div class='panelContent'>\n\t\t\t<ul>\n\t\t\t\t<li>There are no items here yet.</li>\n\t\t\t</ul>\n\t\t</div>\n\n\t</div>\n\t\n</div>\n\n"

    blocks = {'content_body': block_content_body}
    debug_info = '1=9&3=15'
    return locals()