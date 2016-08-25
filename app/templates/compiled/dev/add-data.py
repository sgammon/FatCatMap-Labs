from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/dev/add-data.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/dev.html', 'source/dev/add-data.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        included_template = environment.get_template('macros/form.html', 'source/dev/add-data.html').module
        l_renderForm = getattr(included_template, 'renderForm', missing)
        if l_renderForm is missing:
            l_renderForm = environment.undefined("the template %r (imported on line 2 in 'source/dev/add-data.html') does not export the requested name 'renderForm'" % included_template.__name__, name='renderForm')
        context.vars['renderForm'] = l_renderForm
        context.exported_vars.discard('renderForm')
        for event in parent_template.root_render_func(context):
            yield event

    def block_panel_content(context, environment=environment):
        l_msg = context.resolve('msg')
        l_renderForm = context.resolve('renderForm')
        l_create_relation = context.resolve('create_relation')
        l_create_collection = context.resolve('create_collection')
        t_1 = environment.tests['none']
        if 0: yield None
        yield u'\n\n'
        if (not t_1(l_msg)):
            if 0: yield None
            yield u"\n\t<div class='notice'><p>%s</p></div>\n" % (
                l_msg, 
            )
        yield u"\n\n<div class='floatleft'>\n\t<h2>Create Object Collection:</h2><br />\n\n\t%s\n</div>\n\n<div class='floatleft' style='margin-left: 25px'>\n\t<h2>Create Object Relation:</h2><br />\n\n\t%s\n</div>\n\n<div class='clearboth'></div>\n\n<br />\n<br />\n" % (
            context.call(l_renderForm, l_create_collection), 
            context.call(l_renderForm, l_create_relation), 
        )

    def block_panel_header(context, environment=environment):
        if 0: yield None
        yield u'Add Graph Data'

    def block_page_title(context, environment=environment):
        if 0: yield None
        yield u'Add Graph Data'

    def block_panel_backnav(context, environment=environment):
        l_link = context.resolve('link')
        if 0: yield None
        yield u'<a href="%s">Development Console</a>' % (
            context.call(l_link, 'dev-index'), 
        )

    blocks = {'panel_content': block_panel_content, 'panel_header': block_panel_header, 'page_title': block_page_title, 'panel_backnav': block_panel_backnav}
    debug_info = '1=9&2=12&8=21&10=29&11=32&17=35&23=36&5=39&4=43&6=47'
    return locals()