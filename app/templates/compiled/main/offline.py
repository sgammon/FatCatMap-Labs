from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/main/offline.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/main.html', 'source/main/offline.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_content_body(context, environment=environment):
        if 0: yield None
        yield u"\n\n\t<div class='alignmiddle textcenter halfwidth halfheight padding-20' style='margin-top: 9%; background: #222;border-radius: 15px; border: 20px solid rgba(17, 17, 17, .7); background-clip:padding-box;'>\n\t\t<br /><br />\n\t\t<h1 class='bigtext'>You are currently in offline mode.</h1><br /><br /><br />\n\t\t<p>Unfortunately, the page you requested is not available in your local cache.<br />\n\t\t\tPlease find a network connection and try again, or press the 'back' button.</p>\n\n\t\t<br />\n\t\t<br />\n\t\t<br />\n\t\t\n\t\t<img src='/assets/img/static/layout/fail/offline.png' title='offline fail :(' />\n\t\t\n\t</div>\n\n"

    def block_title(context, environment=environment):
        if 0: yield None
        yield u'offline - welcome to fatcatmap! &lt;^..^&gt;'

    blocks = {'content_body': block_content_body, 'title': block_title}
    debug_info = '1=9&5=15&3=19'
    return locals()