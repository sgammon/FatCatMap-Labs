from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/core/__base.html'

    def root(context, environment=environment):
        if 0: yield None
        included_template = environment.get_template('macros/rpc.html', 'source/core/__base.html').module
        l_jsapi_rpc = getattr(included_template, 'jsapi_rpc', missing)
        if l_jsapi_rpc is missing:
            l_jsapi_rpc = environment.undefined("the template %r (imported on line 1 in 'source/core/__base.html') does not export the requested name 'jsapi_rpc'" % included_template.__name__, name='jsapi_rpc')
        context.vars['jsapi_rpc'] = l_jsapi_rpc
        context.exported_vars.discard('jsapi_rpc')
        included_template = environment.get_template('macros/graph.html', 'source/core/__base.html').module
        l_d3grapher = getattr(included_template, 'd3grapher', missing)
        if l_d3grapher is missing:
            l_d3grapher = environment.undefined("the template %r (imported on line 2 in 'source/core/__base.html') does not export the requested name 'd3grapher'" % included_template.__name__, name='d3grapher')
        context.vars['d3grapher'] = l_d3grapher
        context.exported_vars.discard('d3grapher')
        included_template = environment.get_template('macros/form.html', 'source/core/__base.html').module
        l_renderForm = getattr(included_template, 'renderForm', missing)
        if l_renderForm is missing:
            l_renderForm = environment.undefined("the template %r (imported on line 3 in 'source/core/__base.html') does not export the requested name 'renderForm'" % included_template.__name__, name='renderForm')
        context.vars['renderForm'] = l_renderForm
        context.exported_vars.discard('renderForm')
        included_template = environment.get_template('macros/chart.html', 'source/core/__base.html').module
        l_renderChart = getattr(included_template, 'renderChart', missing)
        if l_renderChart is missing:
            l_renderChart = environment.undefined("the template %r (imported on line 4 in 'source/core/__base.html') does not export the requested name 'renderChart'" % included_template.__name__, name='renderChart')
        context.vars['renderChart'] = l_renderChart
        context.exported_vars.discard('renderChart')
        included_template = environment.get_template('macros/datagrid.html', 'source/core/__base.html').module
        l_renderDatagrid = getattr(included_template, 'renderDatagrid', missing)
        if l_renderDatagrid is missing:
            l_renderDatagrid = environment.undefined("the template %r (imported on line 5 in 'source/core/__base.html') does not export the requested name 'renderDatagrid'" % included_template.__name__, name='renderDatagrid')
        context.vars['renderDatagrid'] = l_renderDatagrid
        context.exported_vars.discard('renderDatagrid')
        for event in context.blocks['html'][0](context):
            yield event

    def block_prenorth(context, environment=environment):
        if 0: yield None

    def block_body(context, environment=environment):
        if 0: yield None
        yield u'\n\t'

    def block_presouth(context, environment=environment):
        if 0: yield None

    def block_north(context, environment=environment):
        if 0: yield None
        yield u'<!-- North Element -->\n\t\t'
        for event in context.blocks['prenorth'][0](context):
            yield event
        yield u'\n\t\t'
        template = environment.get_template('elements/__north.html', 'source/core/__base.html')
        for event in template.root_render_func(template.new_context(context.parent, True, locals())):
            yield event
        yield u'\n\t\t'
        for event in context.blocks['postnorth'][0](context):
            yield event
        yield u'\n\t<!-- End North -->'

    def block_title(context, environment=environment):
        l_sys = context.resolve('sys')
        l_title = context.resolve('title')
        if 0: yield None
        if l_title:
            if 0: yield None
            yield to_string(l_title)
            yield u' - '
        yield u'FatCatMap Labs (%s)' % (
            environment.getattr(l_sys, 'version'), 
        )

    def block_body_class(context, environment=environment):
        if 0: yield None
        yield u'fcm-dark'

    def block_postsouth(context, environment=environment):
        if 0: yield None

    def block_html(context, environment=environment):
        l_page = context.resolve('page')
        if 0: yield None
        yield u'<!doctype html>\n<!--[if lt IE 7 ]> <html lang="en" class="no-js ie6"> <![endif]-->\n<!--[if IE 7 ]>    <html lang="en" class="no-js ie7"> <![endif]-->\n<!--[if IE 8 ]>    <html lang="en" class="no-js ie8"> <![endif]-->\n<!--[if IE 9 ]>    <html lang="en" class="no-js ie9"> <![endif]-->\n\n<!--[if (gt IE 9)|!(IE)]><!-->\n\t<html lang="en" class="no-js"'
        if environment.getattr(l_page, 'manifest'):
            if 0: yield None
            yield u' manifest="/%s"' % (
                environment.getattr(l_page, 'manifest'), 
            )
        yield u'>\n<!--<![endif]-->\n\n<head>\n\n\t<!-- Set charset before title to plug potential XSS vectors -->\n\t<meta charset="UTF-8">\n\t<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\t\n\t\t\n\t<title>'
        for event in context.blocks['title'][0](context):
            yield event
        yield u'</title>'
        for event in context.blocks['north'][0](context):
            yield event
        yield u"</head>\n\n<body class='"
        for event in context.blocks['body_class'][0](context):
            yield event
        yield u" fcm-beta'>\n\n\t"
        for event in context.blocks['body'][0](context):
            yield event
        yield u'\n\n\n\t'
        for event in context.blocks['south'][0](context):
            yield event
        yield u'\n\t\n</body>\n</html>'

    def block_south(context, environment=environment):
        if 0: yield None
        yield u'\n\t<!-- South Element -->\n\t\t'
        for event in context.blocks['presouth'][0](context):
            yield event
        yield u'\n\t\t'
        template = environment.get_template('elements/__south.html', 'source/core/__base.html')
        for event in template.root_render_func(template.new_context(context.parent, True, locals())):
            yield event
        yield u'\n\t\t'
        for event in context.blocks['postsouth'][0](context):
            yield event
        yield u'\n\t<!-- End South -->\n\t'

    def block_postnorth(context, environment=environment):
        if 0: yield None

    blocks = {'prenorth': block_prenorth, 'body': block_body, 'presouth': block_presouth, 'north': block_north, 'title': block_title, 'body_class': block_body_class, 'postsouth': block_postsouth, 'html': block_html, 'south': block_south, 'postnorth': block_postnorth}
    debug_info = '1=8&2=14&3=20&4=26&5=32&7=38&28=41&38=44&44=48&26=51&28=54&29=57&30=61&24=65&36=77&46=81&7=84&14=88&24=94&26=97&36=100&38=103&42=106&44=113&45=116&46=120&30=124'
    return locals()