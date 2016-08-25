from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/snippets/dev_widget.html'

    def root(context, environment=environment):
        l_util = context.resolve('util')
        l_api = context.resolve('api')
        if 0: yield None
        yield u"<div id='devNotice'>\n\t<a href='http://labs.momentum.io/fatcatmap' class='noicon'>FATCATMAP LABS</a> - WORK IN PROGRESS<br />\n\t&copy; 2008-2011, POLITICAL <a href='http://momentum.io' class='noicon'>MOMENTUM</a><br />\n\n\t"
        if context.call(environment.getattr(environment.getattr(l_api, 'users'), 'is_current_user_admin')):
            if 0: yield None
            yield u'\n\t\n\t<hr />\n\t<div id=\'devMenu\'>\n\t\t<ul>\n\t\t\t<li><a href=\'#dEnv\' onclick="$(\'.devContentSection\').hide(); $(\'#devMenu\').hide(); $(\'#devTools\').show(); $(\'#devTools\').removeClass(\'hidden\');">Development Tools</a></li>\n\t\t\t<li><a href=\'#dEnv\' onclick="$(\'.devContentSection\').hide(); $(\'#devMenu\').hide(); $(\'#perfTools\').show(); $(\'#perfTools\').removeClass(\'hidden\');">Performance Tools</a></li>\n\t\t\t<li><a href=\'#dEnv\' onclick="$(\'.devContentSection\').hide(); $(\'#devMenu\').hide(); $(\'#devEnvironmentInfo\').show(); $(\'#devEnvironmentInfo\').removeClass(\'hidden\');">Request Environment</a></li>\n\t\t\t<li><a href="#dEnv" onclick="$(\'.devContentSection\').hide(); $(\'#devMenu\').hide(); $(\'#agentEnvironment\').show(); $(\'#agentEnvironment\').removeClass(\'hidden\');">Browser Environment</a></li>\t\t\t\t\t\t\n\t\t\t<li><a href="#dEnv" onclick="$(\'.devContentSection\').hide(); $(\'#devMenu\').hide(); $(\'#runtimeEnvironment\').show(); $(\'#runtimeEnvironment\').removeClass(\'hidden\');">Runtime Environment</a></li>\t\t\t\t\t\t\t\t\t\n\t\t</ul>\n\t</div>\n\t\n\t<div id=\'devContent\'>\n\n\t\t<div id=\'devEnvironmentInfo\' class=\'devContentSection hidden\'>\n\n\t\t\t<b>VERSION:</b> %s.%s.%s <b>//</b> <b>BUILD:</b> %s-%s\n\t\t\t<br />\n\t\t\t\n\t\t\t<b>RELEASE:</b> %s <b>//</b> <b>REVISION:</b> %s <br />\n\t\t\t\n\t\t\t<b>NAMESPACE:</b> ' % (
                environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_util, 'config'), 'fcm'), 'version'), 'major'), 
                environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_util, 'config'), 'fcm'), 'version'), 'minor'), 
                environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_util, 'config'), 'fcm'), 'version'), 'micro'), 
                environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_util, 'config'), 'fcm'), 'version'), 'build'), 
                environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_util, 'config'), 'fcm'), 'version'), 'release'), 
                environment.getitem(context.call(environment.getattr(context.call(environment.getattr(environment.getattr(l_util, 'env'), 'get'), 'CURRENT_VERSION_ID'), 'split'), '.'), 0), 
                environment.getitem(context.call(environment.getattr(context.call(environment.getattr(environment.getattr(l_util, 'env'), 'get'), 'CURRENT_VERSION_ID'), 'split'), '.'), 1), 
            )
            if context.call(environment.getattr(environment.getattr(l_api, 'multitenancy'), 'get_namespace')) == '':
                if 0: yield None
                yield u'None'
            else:
                if 0: yield None
                yield to_string(context.call(environment.getattr(environment.getattr(l_api, 'multitenancy'), 'get_namespace')))
            yield u' <b>//</b> <b>DATACENTER:</b> %s\n\t\t\t <br /><b>R(hash):</b> %s <b>//</b> <b>S(hash):</b> None<br />\n\t\t\t<b>LAYER:</b> ' % (
                context.call(environment.getattr(environment.getattr(l_util, 'env'), 'get'), 'DATACENTER'), 
                context.call(environment.getattr(environment.getattr(l_util, 'env'), 'get'), 'REQUEST_ID_HASH'), 
            )
            if context.call(environment.getattr(environment.getattr(l_api, 'backends'), 'get_backend')) == None:
                if 0: yield None
                yield u'Frontend'
            else:
                if 0: yield None
                yield u'Backend'
            yield u' <b>//</b> <b>BACKEND:</b> %s <b>//</b> <b>INSTANCE:</b> %s\n\t\t\t\n\t\t\t<br />\n\t\t\t<br />\n\t\t\t<a href=\'#\' onclick="$(\'#devEnvironmentInfo\').hide().addClass(\'hidden\'); $(\'#devMenu\').show();">Back to Dev Menu</a>\n\n\t\t</div>\n\n\t\t<div id=\'perfTools\' class=\'devContentSection hidden\'>\n\t\t\t<a href=\'#\' onclick="fatcatmap.dev.performance.tools.fpsstats.show();">FPS/Memory Counter</a>\n\n\t\t\t<br />\n\t\t\t<br />\n\t\t\t<a href=\'#\' onclick="$(\'#perfTools\').hide().addClass(\'hidden\'); $(\'#devMenu\').show();">Back to Dev Menu</a>\n\t\t</div>\n\t\t\n\t\t<div id=\'devTools\' class=\'devContentSection hidden\'>\n\t\t\t<a href=\'/_fcm/dev\'>Developer\'s Console</a><br />\n\t\t\t<a href=\'/_fcm/manage\'>Management Console</a><br />\n\t\t\t<a href=\'/_fcm/platform/manage\'>Platform Console</a><br />\n\n\t\t\t<br />\n\t\t\t<br />\n\t\t\t<a href=\'#\' onclick="$(\'#devTools\').hide().addClass(\'hidden\'); $(\'#devMenu\').show();">Back to Dev Menu</a>\n\t\t</div>\t\n\t\t\n\t\t<div id=\'agentEnvironment\' class=\'devContentSection hidden\'>\n\n\t\t\t<div class=\'floatleft textleft\'>\n\n\t\t\t\t<i>Platform</i>\n\t\t\t\t<ul>\n\t\t\t\t\t<li><b>Browser:</b> <span id=\'agent_browser\'></span></li>\n\t\t\t\t\t<li><b>OS:</b> <span id=\'agent_os\'></span></li>\n\t\t\t\t\t<li><b>Engine:</b> <span id=\'agent_engine\'></span></li>\n\t\t\t\t\t<li><b>Vendor:</b> <span id=\'agent_vendor\'></span></li>\n\t\t\t\t\t<li><b>Version:</b> <span id=\'agent_version\'></span></li>\n\t\t\t\t</ul>\n\n\t\t\t</div>\n\t\t\t\n\t\t\t<div class=\'floatleft textleft\'>\n\t\t\t\t\n\t\t\t\t<i>Capabilities</i>\n\t\t\t\t<ul>\n\t\t\t\t\t<li><b>SVG:</b> <span id=\'capabilities_svg\'></span></li>\n\t\t\t\t\t<li><b>Workers:</b> <span id=\'agent_browser\'></span></li>\n\t\t\t\t\t<li><b>AJAX:</b> <span id=\'capabilities_ajax\'></span></li>\n\t\t\t\t\t<li><b>- Storage:</b> <span id=\'capabilities_simple_storage\'></span></li>\n\t\t\t\t\t<li><b>+ Storage:</b> <span id=\'capabilities_advanced_storage\'></span></li>\t\t\t\t\t\n\t\t\t\t</ul>\n\t\t\t\t\n\t\t\t</div>\n\n\t\t\t<div class=\'clearboth\'></div>\n\t\t\t<br />\n\t\t\t<br />\n\t\t\t<a href=\'#\' onclick="$(\'#agentEnvironment\').hide().addClass(\'hidden\'); $(\'#devMenu\').show();">Back to Dev Menu</a>\n\t\t</div>\t\t\t\t\t\t\n\t\t\n\t\t<div id=\'runtimeEnvironment\' class=\'devContentSection hidden\'>\n\t\t\t\n\t\t\t<div class=\'floatleft textleft\'>\n\t\t\t\t<i>Libraries:</i>\n\t\t\t\t<ul>\n\t\t\t\t\t<li><b>jQuery:</b> <span id=\'capabilities_svg\'></span></li>\n\t\t\t\t\t<li><b>Amplify:</b> <span id=\'capabilities_svg\'></span></li>\n\t\t\t\t\t<li><b>Backbone:</b> <span id=\'capabilities_svg\'></span></li>\n\t\t\t\t\t<li><b>Lawnchair:</b> <span id=\'capabilities_svg\'></span></li>\n\t\t\t\t\t<li><b>DataJS:</b> <span id=\'capabilities_svg\'></span></li>\n\t\t\t\t</ul>\n\t\t\t</div>\n\t\t\t\n\t\t\t<div class=\'floatleft textleft\'>\n\t\t\t\t<i>Page State:</i>\n\t\t\t\t<ul>\n\t\t\t\t\t<li><b>Channel:</b> <span id=\'capabilities_svg\'></span></li>\n\t\t\t\t\t<li><b>Workers:</b> <span id=\'capabilities_svg\'></span></li>\n\t\t\t\t\t<li><b>RPC\'s:</b> <span id=\'capabilities_svg\'></span></li>\n\t\t\t\t\t<li><b>Session:</b> <span id=\'capabilities_svg\'></span></li>\n\t\t\t\t\t<li><b>User:</b> <span id=\'capabilities_svg\'></span></li>\n\t\t\t</div>\n\t\t\t\n\t\t\t<div class=\'clearboth\'></div>\n\t\t\t<br />\n\t\t\t<br />\n\t\t\t<a href=\'#\' onclick="$(\'#runtimeEnvironment\').hide().addClass(\'hidden\'); $(\'#devMenu\').show();">Back to Dev Menu</a>\t\t\t\n\t\t</div>\n\t\t\n\t</div>\n\t' % (
                context.call(environment.getattr(environment.getattr(l_api, 'backends'), 'get_backend')), 
                context.call(environment.getattr(environment.getattr(l_util, 'env'), 'get'), 'INSTANCE_ID', '0'), 
            )
        yield u'\n</div>'

    blocks = {}
    debug_info = '5=11&22=14&25=19&27=22&28=30&29=32'
    return locals()