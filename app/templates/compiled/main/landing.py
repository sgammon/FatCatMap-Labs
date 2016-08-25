from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/main/landing.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/main.html', 'source/main/landing.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_content_body(context, environment=environment):
        l_name = context.resolve('name')
        if 0: yield None
        yield u'\n\n\t<h1>Hello, %s!</h1>\n\t\n' % (
            l_name, 
        )

    def block_title(context, environment=environment):
        if 0: yield None
        yield u'welcome to fatcatmap! &lt;^..^&gt;'

    blocks = {'content_body': block_content_body, 'title': block_title}
    debug_info = '1=9&5=15&7=19&3=22'
    return locals()