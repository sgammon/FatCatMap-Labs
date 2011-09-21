from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/content/map/landing.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('content/map/layout.html', 'source/content/map/landing.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_subtitle(context, environment=environment):
        l_origin = context.resolve('origin')
        if 0: yield None
        if l_origin:
            if 0: yield None
            yield to_string(environment.getattr(l_origin, 'label'))
        else:
            if 0: yield None
            yield u'Mapper'

    def block_content_footer(context, environment=environment):
        if 0: yield None

    def block_grapher(context, environment=environment):
        if 0: yield None
        yield u'\n\t<script type="text/javascript">\n\n\t\t// Define local context vars\n\t\t_g = null;\n\t\t_graph = null;\n\t\t_visualizer = null;\n\t\tmakeGrapher = null;\n\n\t\t$(document).ready(function registerGraphCallback()\n\t\t{\n\t\t\t$.fatcatmap.state.events.registerHook(\'PLATFORM_READY\', function drawGraph()\n\t\t\t{\n\t\t\t\t_g = new Interaction.Graph(\'#grapher\').build('
        l_util = context.resolve('util')
        l_rpc_params = context.resolve('rpc_params')
        l_off = context.resolve('off')
        if 0: yield None
        t_1 = context.eval_ctx.save()
        context.eval_ctx.autoescape = l_off
        yield (context.eval_ctx.autoescape and escape or to_string)(context.call(environment.getattr(environment.getattr(environment.getattr(l_util, 'converters'), 'json'), 'dumps'), l_rpc_params))
        context.eval_ctx.revert(t_1)
        yield u').render().draw();\n\t\t\t});\n\t\t});\n\t\n\t</script>\n'

    blocks = {'subtitle': block_subtitle, 'content_footer': block_content_footer, 'grapher': block_grapher}
    debug_info = '1=9&3=15&25=25&5=28&18=37'
    return locals()