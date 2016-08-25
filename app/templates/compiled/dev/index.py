from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/dev/index.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('layouts/dev.html', 'source/dev/index.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_panel_header_subtext(context, environment=environment):
        if 0: yield None
        yield u"<i>for momentum's eyes only</i>"

    def block_panel_content(context, environment=environment):
        l_util = context.resolve('util')
        l_config = context.resolve('config')
        l_link = context.resolve('link')
        if 0: yield None
        yield u'\n\n<div class=\'panelSection floatleft clearleft padding-10\'>\n\t<h2>General Tools</h2>\n\t<ul>\n\t\t<li><a href="%s">Add Default Data</a></li>\n\t\t<li><a href="%s">Add Graph Data</a></li>\n\t\t<li><a href="%s">RPC Playground<a></li>\n\t\t<li><a href="%s">Cache Management</a></li>\n\t\t<li><a href="%s">Security Management</a></li>\n\t\t<li><a href="%s">Serving Environment</a></li>\t\t\n\t\t<li><a href="%s">Logs & Audit Trails</a></li>\n\t\t<li><a href="%s">Command Shell</a></li>\n\t</ul>\n</div>\n\t\t\t\n<div class=\'panelSection floatleft padding-10\'>\n\t<h2>Library Tools</h2>\n\t<ul>\n\t\t<li><a href="/_ah/datastore_admin/" target="_blank">Datastore Console</a></li>\t\t\n\t\t<li><a href="/_ah/pipeline/status" target="_blank">Pipelines Console</a></li>\n\t\t<li><a href="/_ah/protorpc" target="_blank">ProtoRPC Console</a></li>\t\t\n\t\t<li><a href="/_ah/mapreduce/" target="_blank">MapReduce Console</a></li>\n\t\t<li>\n\t\t\t<a href="/_ah/appstats" target="_blank">AppStats Console</a> (RPC Profiling)\n\t\t\t' % (
            context.call(l_link, 'dev-default-data'), 
            context.call(l_link, 'dev-add-data'), 
            context.call(l_link, 'dev-rpc-console'), 
            context.call(l_link, 'dev-cache'), 
            context.call(l_link, 'dev-cache'), 
            context.call(l_link, 'dev-cache'), 
            context.call(l_link, 'dev-cache'), 
            context.call(l_link, 'dev-shell'), 
        )
        if context.call(environment.getattr(context.call(environment.getattr(context.call(environment.getattr(environment.getattr(l_util, 'config'), 'get'), 'momentum.system', {}), 'get'), 'hooks', {}), 'get'), 'appstats', False) != True:
            if 0: yield None
            yield u'\n\t\t\t\t<br /><i><b>(Currently disabled in application config)</b></i>\t\t\t\t\n\t\t\t'
        yield u'\n\t\t</li>\n\t\t<li>\n\t\t\t<a href="/_ah/apptrace" target="_blank">AppTrace Console</a> (Memory Profiling)\n\t\t\t'
        if environment.getattr(environment.getattr(environment.getattr(l_util, 'config'), 'hooks'), 'apptrace') != True:
            if 0: yield None
            yield u'\n\t\t\t\t<br /><i><b>(Currently disabled in application config)</b></i>\n\t\t\t'
        else:
            if 0: yield None
            yield u'\n\t\t\t\t'
            if (not environment.getattr(l_config, 'debug')):
                if 0: yield None
                yield u'\n\t\t\t\t<i><b>(Not available in production)</b></li>\n\t\t\t\t'
            yield u'\n\t\t\t'
        yield u'\n\t\t</li>\n</div>\n\n<div class=\'panelSection floatleft padding-10\'>\n\t\n\t<h2>Client-Side Tools: </h2>Javascript API, HTML5 tools\n\t<ul>\n\t\t<li><a href="#">Local Storage</a></li>\n\t\t<li><a href="#">Session Storage</a></li>\n\t\t<li><a href="#">Application Cache</a></li>\n\t\t<li><a href="#">IndexedDB Console</a></li>\n\t\t<li><a href="#">WebSQL Console</a></li>\n\t\t<li><a href="#">Offline Debug</a></li>\n\t\t<li><a href="#">Agent/Platform Info</a></li>\n\t</ul>\n\t\n</div>\n\n<div class=\'panelSection floatleft padding-10\'>\n\t\n\t<h2>Local Chrome Shortcuts</h2> (you must copy + paste the linked href manually)\n\t<ul>\n\t\t<li><a href="about:version">Version</a> / <a href="about:about">About</a></li>\n\t\t<li><a href="about:appcache-internals">Appcache Internals</a></li>\n\t\t<li><a href="about:blob-internals">Blob Internals</a></li>\n\t\t<li><a href="about:memory">Memory</a> / <a href="about:view-http-cache">HTTP Cache</a></li>\n\t\t<li><a href="about:gpu">GPU Internals</a></li>\t\n\t\t<li><a href="about:dns">DNS</a> / <a href="about:net-internals">Net Internals</a></li>\n\t\t<li><a href="about:plugins">Plugins</a> / <a href="about:flags">Flags</a></li>\n\t</ul>\n\t\n</div>\n\n'

    def block_panel_header(context, environment=environment):
        if 0: yield None
        yield u'Development Console'

    def block_page_title(context, environment=environment):
        if 0: yield None
        yield u'Home'

    blocks = {'panel_header_subtext': block_panel_header_subtext, 'panel_content': block_panel_content, 'panel_header': block_panel_header, 'page_title': block_page_title}
    debug_info = '1=9&5=15&7=19&12=25&13=26&14=27&15=28&16=29&17=30&18=31&19=32&32=34&38=38&41=44&4=50&3=54'
    return locals()