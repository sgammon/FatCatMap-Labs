from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/macros/rpc.html'

    def root(context, environment=environment):
        if 0: yield None
        def macro(l_module, l_method, l_success, l_failure, l_params, l_async, l_tags):
            t_1 = []
            pass
            t_1.append(
                u'\n\t', 
            )
            if l_tags == True:
                pass
                t_1.append(
                    u"\n\t\t<script type='text/javascript'>\n\t", 
                )
            t_1.extend((
                u'\n\n\tfatcatmap.rpc.api.', 
                to_string(l_module), 
                u'.', 
                to_string(l_method), 
                u'(', 
            ))
            l_util = context.resolve('util')
            pass
            t_2 = context.eval_ctx.save()
            context.eval_ctx.autoescape = False
            t_1.append(
                to_string(context.call(environment.getattr(environment.getattr(environment.getattr(l_util, 'converters'), 'json'), 'dumps'), l_params)), 
            )
            context.eval_ctx.revert(t_2)
            t_1.extend((
                u').fulfill({\n\t\t\n\t\tsuccess: function (response) {\n\t\t\t', 
                to_string(l_success), 
                u'(response);\n\t\t},\n\t\t\n\t\tfailure: function (response)\n\t\t{\n\t\t\t', 
                to_string(l_failure), 
                u'(response);\n\t\t}\n\t\t\n\t}, {async: ', 
            ))
            if l_async == True:
                pass
                t_1.append(
                    u'true', 
                )
            else:
                pass
                t_1.append(
                    u'false', 
                )
            t_1.append(
                u'});\n\n\t', 
            )
            if l_tags == True:
                pass
                t_1.append(
                    u'\n\t\t</script>\n\t', 
                )
            t_1.append(
                u'\n', 
            )
            return concat(t_1)
        context.exported_vars.add('jsapi_rpc')
        context.vars['jsapi_rpc'] = l_jsapi_rpc = Macro(environment, macro, 'jsapi_rpc', ('module', 'method', 'success', 'failure', 'params', 'async', 'tags'), ({}, False, False, ), False, False, False)

    blocks = {}
    debug_info = '1=8&2=14&6=21&9=36&14=38&17=41&19=54'
    return locals()