from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/macros/chart.html'

    def root(context, environment=environment):
        if 0: yield None
        def macro():
            t_1 = []
            pass
            t_1.append(
                u'\n', 
            )
            return concat(t_1)
        context.exported_vars.add('renderChart')
        context.vars['renderChart'] = l_renderChart = Macro(environment, macro, 'renderChart', (), (), False, False, False)

    blocks = {}
    debug_info = '1=8'
    return locals()