from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/macros/datagrid.html'

    def root(context, environment=environment):
        if 0: yield None
        def macro():
            t_1 = []
            pass
            t_1.append(
                u'\n', 
            )
            return concat(t_1)
        context.exported_vars.add('renderDatagrid')
        context.vars['renderDatagrid'] = l_renderDatagrid = Macro(environment, macro, 'renderDatagrid', (), (), False, False, False)

    blocks = {}
    debug_info = '1=8'
    return locals()