from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/elements/pane/details-sidebar.html'

    def root(context, environment=environment):
        l_assets = context.resolve('assets')
        if 0: yield None
        yield u'<div id=\'detailsPane\' class=\'sidebar sb-left folded\' data-element=\'details_sidebar\' data-element-type=\'LayoutElement\'>\n\n\t<script type="text/javascript">\n\t$(document).ready(function initDetailsPane() {\t\n\t\t$.fatcatmap.state.events.registerHook(\'PLATFORM_READY\', function (context) {\n\t\t\tdetailspane = new Layout.Sidebar(\'#detailsPane\', {maximizable: true, unfolded_width: 360});\n\t\t\t$.fatcatmap.api.layout.register(\'detailspane\', detailspane);\t\t\n\t\t});\n\t});\n\t</script>\n\t\t\n\t<div class=\'paneButtonBox\'>\n\t\t<a class=\'paneButton enabled closeButton cp-left hidden\'><img src="%s" width="18" height="18" /></a>\n\n\t\t<a class=\'paneButton enabled expandButton cp-right\'><img src="%s" width="18" height="18" /></a>\n\t\t<a class=\'paneButton hidden minimizeButton cp-right\'><img src="%s" width="18" height="18" /></a>\t\t\n\t</div>\n\t\n\t<div class=\'panelWrapper hidden textleft\'>\n\t\t<div class=\'title\'>Details</div>\n\t\t<div class=\'content\'>\n\n\t\t\t<div class=\'nodeDetailsPane\'>\n\t\t\t\t<b>Current Node:</b>\n\t\t\t\t<ul>\n\t\t\t\t\t<li>Key: <span id=\'nodekey\'></span></li>\n\t\t\t\t\t<li>Label: <span id=\'nodelabel\'></span></li>\n\t\t\t\t</ul>\n\t\t\t</div>\n\n\t\t</div>\n\t</div>\n\t\n</div>' % (
            context.call(environment.getattr(l_assets, 'image'), 'layout/sprites', 'close-x.png'), 
            context.call(environment.getattr(l_assets, 'image'), 'layout/sprites', 'arrow-right.png'), 
            context.call(environment.getattr(l_assets, 'image'), 'layout/sprites', 'arrow-left.png'), 
        )

    blocks = {}
    debug_info = '13=10&15=11&16=12'
    return locals()