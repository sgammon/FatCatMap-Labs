from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/elements/__south.html'

    def root(context, environment=environment):
        l_util = context.resolve('util')
        l_api = context.resolve('api')
        l_assets = context.resolve('assets')
        if 0: yield None
        yield u'<!--[if lt IE 7 ]>\n<script src="%s"></script>\n<script> DD_belatedPNG.fix(\'img, .png_bg\');</script>\n<![endif]-->\n\n' % (
            context.call(environment.getattr(l_assets, 'script'), 'belated_png'), 
        )
        if (not context.call(environment.getattr(environment.getattr(l_api, 'users'), 'is_current_user_admin'))):
            if 0: yield None
            yield u"\n\n<!-- Google Analytics: Track pageview -->\n<script>\n\tvar _gaq=[['_setAccount','UA-2908422-24'],['_setDomainName','%s'],['_setAllowLinker', true], ['_trackPageview']];\n\t(function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];g.async=1;\n\tg.src=('https:'==location.protocol?'//ssl':'//www')+'.google-analytics.com/ga.js';\n\ts.parentNode.insertBefore(g,s)}(document,'script'));\n</script>\n\n" % (
                context.call(environment.getattr(environment.getattr(l_util, 'env'), 'get'), 'SERVER_NAME'), 
            )
        else:
            if 0: yield None
            yield u'\n\n<!-- On-screen FPS/MB widget -->\n<script src="%s"></script>\n\n' % (
                context.call(environment.getattr(l_assets, 'script'), 'fps_stats', 'dev'), 
            )

    blocks = {}
    debug_info = '2=12&6=14&10=17&19=22'
    return locals()