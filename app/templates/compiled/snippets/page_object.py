from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/snippets/page_object.js'

    def root(context, environment=environment):
        l_sys = context.resolve('sys')
        l_api = context.resolve('api')
        l_services = context.resolve('services')
        l_script_tag = context.resolve('script_tag')
        if 0: yield None
        if l_script_tag:
            if 0: yield None
            yield u'\n<script type="text/javascript">\n'
        yield u'\n\nfatcatmap = window.fatcatmap;\n\n'
        if l_services:
            if 0: yield None
            yield u'\n\t'
            l_action = l_opts = l_service = l_config = missing
            for (l_service, l_action, l_config, l_opts) in l_services:
                if 0: yield None
                yield u"\t\n\t\tfatcatmap.rpc.api.factory('%s', '%s', [" % (
                    l_service, 
                    l_action, 
                )
                l_method = missing
                for l_method in environment.getattr(l_config, 'methods'):
                    if 0: yield None
                    yield u"'%s'," % (
                        l_method, 
                    )
                l_method = missing
                yield u'], '
                l_util = context.resolve('util')
                if 0: yield None
                t_1 = context.eval_ctx.save()
                context.eval_ctx.autoescape = False
                yield to_string(context.call(environment.getattr(environment.getattr(environment.getattr(l_util, 'converters'), 'json'), 'dumps'), l_opts))
                context.eval_ctx.revert(t_1)
                yield u');\n\t'
            l_action = l_opts = l_service = l_config = missing
            yield u"\n\n\t\tfatcatmap.state.events.triggerEvent('API_READY');\n"
        yield u'\n\n// Initliaze user object\nfatcatmap.user.setUserInfo({\n\n\t'
        if context.call(environment.getattr(environment.getattr(l_api, 'users'), 'current_user')) != None:
            if 0: yield None
            yield u'\n\t\tcurrent_user: "%s",\n\t\tis_user_admin: "%s",\n\t' % (
                context.call(environment.getattr(environment.getattr(l_api, 'users'), 'current_user')), 
                context.call(environment.getattr(environment.getattr(l_api, 'users'), 'is_current_user_admin')), 
            )
        else:
            if 0: yield None
            yield u'\n\t\tcurrent_user: null,\n\t\tis_user_admin: false,\n\t'
        yield u'\n\tlogin_url: "%s",\n\tlogout_url: "%s"\n\n});\n\n// Initialize Sys Object\n_PLATFORM_VERSION = "%s";\n\n' % (
            context.call(environment.getattr(environment.getattr(l_api, 'users'), 'create_login_url'), '/'), 
            context.call(environment.getattr(environment.getattr(l_api, 'users'), 'create_logout_url'), '/'), 
            environment.getattr(l_sys, 'version'), 
        )
        if environment.getattr(l_sys, 'dev'):
            if 0: yield None
            yield u'\n// Drop in server environment (DEV ONLY)\nfatcatmap.dev.environment = {\n\t'
            l_value = l_key = missing
            for (l_key, l_value) in context.call(environment.getattr(environment.getattr(l_sys, 'environ'), 'items')):
                if 0: yield None
                yield u'\n\t%s: "%s",\n\t' % (
                    l_key, 
                    l_value, 
                )
            l_value = l_key = missing
            yield u'\n};\n\nfatcatmap.dev.setDebug({logging: true, eventlog: true, verbose: true});\n'
        yield u'\n\n'
        if l_script_tag:
            if 0: yield None
            yield u'\n</script>\n'

    blocks = {}
    debug_info = '1=12&7=16&8=20&9=23&18=44&19=47&20=48&25=54&26=55&31=56&33=58&36=62&37=65&44=71'
    return locals()