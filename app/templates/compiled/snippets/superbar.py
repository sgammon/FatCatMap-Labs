from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/snippets/superbar.html'

    def root(context, environment=environment):
        l_api = context.resolve('api')
        l_link = context.resolve('link')
        l_user = context.resolve('user')
        if 0: yield None
        yield u'<!-- Top-right FCM branding -->\n<div id=\'fcmTopBranding\'>\n\t<a href="%s"><img src=\'/assets/img/static/branding/fatcatmap-alpha-v3-10.png\' height=\'19\' width=\'170\' alt=\'fatcatmap alpha\' /></a>\n</div>\n\n<nav id=\'topnav\' class=\'navbar\'>\n\n\t<!-- Superbar Navigation -->\n\t<ul class=\'topNavigation floatleft\'>\n\n\t\t<li class=\'dotSpacer\'>&#183;</li>\n\n\t\t<li><a href="%s">Home</a></li>\n\t\n\t\t<li><a href="#" data-navref=\'browse\' class=\'SupernavLink\'>Browse</a></li>\n\n\t\t<li><a href=\'#\' data-navref=\'search\' class=\'SupernavLink\'>Search</a></li>\n\n\t\t<li><a href=\'#\' data-navref=\'map\' class=\'SupernavLink\'>Map</a></li>\n\n\t\t<li><a href=\'#\' data-navref=\'visualize\' class=\'SupernavLink\'>Visualize</a></li>\n\n\t\t<li><a href=\'#\' data-navref=\'interact\' class=\'SupernavLink\'>Interact</a></li>\t\n\n\t</ul>\n\n\t<!-- Utility bar -->\n\n\t<ul id=\'util_navigation\' class=\'floatright\'>\n\t\n\t\t' % (
            context.call(l_link, 'landing'), 
            context.call(l_link, 'landing'), 
        )
        if l_user != None:
            if 0: yield None
            yield u'\n\t\t<li class=\'navButton\'><a href=\'#\'>%s</a>\n\t\t\t<ul class=\'subnav rightsub\'>\n\t\t\t\t<li><a href="#settings">Settings</a></li>\n\t\t\t\t<li class=\'last\'><a href="%s">Log Out</a></li>\n\t\t\t</ul>\n\t\t</li>\n\t\t\n\t\t<li id=\'utilDotSpacer\'>&#183;</li>\n\t\t<li class=\'navButton\'><a href=\'#\'><span id=\'inboxCount\'>0</span> Inbox</a></li>\n\t\t\n\t\t' % (
                context.call(environment.getattr(l_user, 'nickname')), 
                context.call(environment.getattr(environment.getattr(l_api, 'users'), 'create_logout_url'), '/'), 
            )
        else:
            if 0: yield None
            yield u'\n\t\t<li class=\'navButton\'><a href="%s">Log In</a></li>\n\t\t' % (
                context.call(environment.getattr(environment.getattr(l_api, 'users'), 'create_login_url'), '/'), 
            )
        yield u"\n\t\t\t\t\n\t\t<li id='utilDotSpacer'>&#183;</li>\t\t\n\t\t\n\t\t<li class='navButton'><a href='#'>momentum</a>\n\t\t\t<ul class='subnav rightsub'>\n\t\t\t\t"
        if context.call(environment.getattr(environment.getattr(l_api, 'users'), 'is_current_user_admin')):
            if 0: yield None
            yield u'\n\t\t\t\t\t<li><a href="%s">Developer Console</a></li>\n\t\t\t\t\t<li><a href="%s">Management Console</a></li>\n\t\t\t\t\t<li><a href="/_pc/console/">Infrastructure Console</a></li>\n\t\t\t\t\t<li class=\'last\'><a href="/_pc/ifx/platform/console">Platform Console</a></li>\n\t\t\t\t' % (
                context.call(l_link, 'dev-index'), 
                context.call(l_link, 'admin-index'), 
            )
        yield u"\n\t\t\t</ul>\n\t\t</li>\n\t</ul>\n</nav>\n<div class='clearboth'></div>"

    blocks = {}
    debug_info = '3=12&13=13&31=15&32=18&35=19&43=24&50=27&51=30&52=31'
    return locals()