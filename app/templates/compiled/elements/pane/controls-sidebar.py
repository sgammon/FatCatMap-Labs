from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/elements/pane/controls-sidebar.html'

    def root(context, environment=environment):
        l_assets = context.resolve('assets')
        if 0: yield None
        yield u'<div id=\'controlsPane\' class=\'sidebar sb-right folded\' data-element=\'controls_sidebar\' data-element-type=\'LayoutElement\'>\n\t\n\t<script type="text/javascript">\n\t$(document).ready(function initControlsPane() {\n\t\t$.fatcatmap.state.events.registerHook(\'PLATFORM_READY\', function (context) {\t\t\n\t\t\tcontrolspane = new Layout.Sidebar(\'#controlsPane\');\n\t\t\t$.fatcatmap.api.layout.register(\'controlspane\', controlspane);\n\t\t});\n\t});\n\t</script>\n\t\n\t<div class=\'paneButtonBox\'>\n\t\t<a class=\'paneButton multiButton expandButton cp-left enabled\'>\n\t\t\t<img class=\'expandMultiButton\' src="%s" width="18" height="18" />\n\t\t\t<img class=\'closeMultiButton hidden\' src="%s" width="18" height="18" />\n\t\t</a>\n\t</div>\n\t\n\t<div class=\'panelWrapper hidden\'>\n\t\t<div class=\'title\'>Controls Pane</div>\t\n\t\t<div class=\'content\'>\n\n\t\t\t<div class=\'panelBox\'>\n\t\t\t\t<div class=\'subtitle\'>View Options</div>\n\t\t\t\t<div class=\'content\'>\n\t\t\t\t\tSup123\n\t\t\t\t</div>\n\t\t\t</div>\n\n\t\t\t\n\t\t\t<div class=\'panelBox\'>\n\t\t\t\t<div class=\'subtitle\'>Graph Options</div>\n\t\t\t\t<div class=\'content\'>\n\t\t\t\t\t\n\t\t\t\t\t<table class=\'graphSettings\'>\n\t\t\t\t\t\t<tbody>\n\t\t\t\t\t\t\t<tr><td>Charge Constant</td><td><input type=\'text\' value=\'-110\' class=\'graphPhysicsInput\' name=\'chargeConstant\' /></td></tr>\n\t\t\t\t\t\t\t<tr><td>Charge Max Distance</td><td><input type=\'text\' value=\'500\' class=\'graphPhysicsInput\' name=\'chargeMaxDistance\' /></td></tr>\n\t\t\t\t\t\t\t<tr><td>Charge Min Distance</td><td><input type=\'text\' value=\'2\' class=\'graphPhysicsInput\' name=\'chargeMinDistance\' /></td></tr>\n\t\t\t\t\t\t\t<tr><td>Charge Theta</td><td><input type=\'text\' value=\'0.9\' class=\'graphPhysicsInput\' name=\'chargeTheta\' /></td></tr>\n\t\t\t\t\t\t\t<tr><td>Drag Constant</td><td><input type=\'text\' value=\'0.1\' class=\'graphPhysicsInput\' name=\'dragConstant\' /></td></tr>\n\t\t\t\t\t\t\t<tr><td>Spring Constant</td><td><input type=\'text\' value=\'0.1\' class=\'graphPhysicsInput\' name=\'springConstant\' /></td></tr>\n\t\t\t\t\t\t\t<tr><td>Spring Damping</td><td><input type=\'text\' value=\'0.3\' class=\'graphPhysicsInput\' name=\'springDamping\' /></td></tr>\n\t\t\t\t\t\t\t<tr><td>Spring Length</td><td><input type=\'text\' value=\'140\' class=\'graphPhysicsInput\' name=\'springLength\' /></td></tr>\n\t\t\t\t\t\t</tbody>\n\t\t\t\t\t</table>\n\t\t\t\t\t<br />\n\t\t\t\t\t<div class=\'graphButtons\'>\n\t\t\t\t\t\t<button>Reset</button> <button>Default</button> <button>Render</button>\n\t\t\t\t\t</div>\n\t\t\t\t</div>\n\t\t\t</div>\n\n\t\t\t<div class=\'panelBox\'>\n\t\t\t\t<div class=\'subtitle\'>Node Options</div>\n\t\t\t\t<div class=\'content\'>\n\t\t\t\t\tSup\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t\t\n\t\t\t<div class=\'panelBox\'>\n\t\t\t\t<div class=\'subtitle\'>Edge Options</div>\n\t\t\t\t<div class=\'content\'>\n\t\t\t\t\tSup\n\t\t\t\t</div>\n\t\t\t</div>\n\t\t\t\n\n\t\t</div>\n\t</div>\n\t\n</div>' % (
            context.call(environment.getattr(l_assets, 'image'), 'layout/sprites', 'arrow-left.png'), 
            context.call(environment.getattr(l_assets, 'image'), 'layout/sprites', 'close-x.png'), 
        )

    blocks = {}
    debug_info = '14=10&15=11'
    return locals()