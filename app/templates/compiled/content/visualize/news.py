from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/content/visualize/news.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('content/visualize/layout.html', 'source/content/visualize/news.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_postsouth(context, environment=environment):
        if 0: yield None
        yield u"\n\n<script type='text/javascript'>\n\n\t$(document).ready(function () {\n\t\n\t\t$.fatcatmap.state.events.registerHook('PLATFORM_READY', function buildMasonry() {\n\t\t\t\n\t\t\t$('#newsmap').masonry({\n\n\t\t\t\titemSelector: '.newsbox',\n\t\t\t\tisFitWidth: true,\n\t\t\t\tisResizable: true,\n\t\t\t\tisAnimated: true,\n\t\t\t\tanimationOptions: { queue: false, duration: 500 }\n\n\t\t\t});\n\n\t\t\t$('.newsmap_dialog').fancybox({\n\n\t\t\t\topacity: true,\n\t\t\t\twidth: 480,\n\t\t\t\theight: 400,\n\t\t\t\toverlayColor: '#333',\n\t\t\t\tpadding:20,\n\t\t\t\tshowCloseButton: true,\n\t\t\t\tenableEscapeButton: true,\n\t\t\t\tcenterOnScroll: true,\n\t\t\t\toverlayShow: true,\n\t\t\t\ttype: 'inline'\n\n\t\t\t});\t\t\t\n\t\t\t\n\t\t});\n\t\n\t});\n\n</script>\n\n"

    def block_subtitle(context, environment=environment):
        if 0: yield None
        yield u'News Explorer - '

    def block_visualizer(context, environment=environment):
        l_util = context.resolve('util')
        l_lipsum = context.resolve('lipsum')
        if 0: yield None
        yield u"\n\t\n\t<!-- Newsmap navigation bar -->\n\t<div id='newsmapHeader'>\n\t\t<h1>News Explorer</h1>\n\t\t\n\t\t<span id='topbarLoading' class='contentNavbar'>loading...</span>\n\t\t\n\t\t<span class='contentNavbar hidden'>View as <b>newspaper</b>, <a href='#treemap' class='newsmap_view'>tree map</a>, <a href='#heatmap' class='newsmap_view'>heatmap</a> | <a href='#newsmap.alerts'>alerts</a>, <a href='#newsmap.filters'>filters</a> | <a href='#options' class='newsmap_dialog'>view options</a>, <a href='#settings' class='newsmap_dialog'>settings</a></span>\n\t\t\n\t\t<span class='contentStatus hidden'>\n\t\t\tupdated <a href='#status'>6 minutes ago</a> | <a href='#update'>update</a> | <a href='#offline'>go offline</a></span>\n\t\t</span>\n\t</div>\n\t\n\t<!-- Newsmap navigation entry content -->\n\t<div id='newsmapOptions' class='displaynone'>\n\t\t\n\t\t<div id='options'>\n\t\t\t<p>%s</p>\n\t\t</div>\n\t\t\n\t</div>\t\n\n\t<div id='newsmapSettings' class='displaynone'>\n\t\t\n\t\t<div id='settings'>\n\t\t\t<p>%s</p>\n\t\t</div>\n\t\t\n\t</div>\n\t\n\t<div id='mainLoading' class='alignmiddle textcenter'>\n\t\t<div class='fullwidth textcenter fullheight'>\n\t\t\tloading...\n\t\t</div>\n\t</div>\n\t\n\t<!-- The newsmap! :) -->\n\t<div id='newsmap' class='alignmiddle textcenter hidden'>\n\t\n\t\t<div class='newsbox worldNews nbHalf'>\n\t\t\t<h3>News headline 1 here</h3>\n\t\t\t<p>%s <a href='#'>Read more...</a></p>\n\t\t</div>\n\n\t\t<div class='newsbox nationalNews nbFull'>\n\t\t\t<h3>News headline 2 here</h3>\n\t\t\t<p>%s <a href='#'>Read more...</a></p>\n\t\t</div>\n\n\t\t<div class='newsbox worldNews nbFull'>\n\t\t\t<h3>News headline 3 here</h3>\n\t\t\t<p>%s <a href='#'>Read more...</a></p>\n\t\t</div>\n\n\t\t<div class='newsbox businessNews nbHalf'>\n\t\t\t<h3>News headline 4 here</h3>\n\t\t\t<p>%s <a href='#'>Read more...</a></p>\n\t\t</div>\n\n\t\t<div class='newsbox sportsNews nbHalf'>\n\t\t\t<h3>News headline 5 here</h3>\n\t\t\t<p>%s <a href='#'>Read more...</a></p>\n\t\t</div>\n\n\t\t<div class='newsbox techNews nbFull'>\n\t\t\t<h3>News headline 6 here</h3>\n\t\t\t<p>%s <a href='#'>Read more...</a></p>\n\t\t</div>\n\n\t\t<div class='newsbox techNews nbHalf'>\n\t\t\t<h3>News headline 7 here</h3>\n\t\t\t<p>%s <a href='#'>Read more...</a></p>\n\t\t</div>\n\t\n\t\t<div class='newsbox worldNews nbHalf'>\n\t\t\t<h3>News headline 8 here</h3>\n\t\t\t<p>%s <a href='#'>Read more...</a></p>\n\t\t</div>\n\t\n\t\t<div class='newsbox sportsNews nbHalf'>\n\t\t\t<h3>News headline 9 here</h3>\n\t\t\t<p>%s <a href='#'>Read more...</a></p>\n\t\t</div>\n\t\n\t\t<div class='newsbox nationalNews nbFull'>\n\t\t\t<h3>News headline 10 here</h3>\n\t\t\t<p>%s <a href='#'>Read more...</a></p>\n\t\t</div>\n\t\n\t\t<div class='newsbox nationalNews nbHalf'>\n\t\t\t<h3>News headline 11 here</h3>\n\t\t\t<p>%s <a href='#'>Read more...</a></p>\n\t\t</div>\n\t\n\t\t<div class='newsbox nationalNews nbHalf'>\n\t\t\t<h3>News headline 12 here</h3>\n\t\t\t<p>%s <a href='#'>Read more...</a></p>\n\t\t</div>\n\t\n\t\t<div class='newsbox worldNews nbHalf'>\n\t\t\t<h3>News headline 13 here</h3>\n\t\t\t<p>%s <a href='#'>Read more...</a></p>\n\t\t</div>\n\t\n\t\t<div class='newsbox sportsNews nbFull'>\n\t\t\t<h3>News headline 14 here</h3>\n\t\t\t<p>%s <a href='#'>Read more...</a></p>\n\t\t</div>\n\t\n\t</div>\n\t\n\t<!-- Treemap -->\n\t<div id='treemap' class='hidden'>\t\t\n\t\t<h1 class='alignmiddle padding-20'>No treemap yet!</h1>\n\t</div>\n\t\n\t<!-- Heatmap -->\n\t<div id='heatmap' class='hidden'>\n\t\t<h1 class='alignmiddle padding-20'>No heatmap yet!</h1>\n\t</div>\n" % (
            context.call(l_lipsum, 1), 
            context.call(l_lipsum, 1), 
            context.call(l_lipsum, context.call(environment.getattr(environment.getattr(l_util, 'random'), 'randrange'), 1, 2)), 
            context.call(l_lipsum, context.call(environment.getattr(environment.getattr(l_util, 'random'), 'randrange'), 1, 2)), 
            context.call(l_lipsum, context.call(environment.getattr(environment.getattr(l_util, 'random'), 'randrange'), 1, 2)), 
            context.call(l_lipsum, context.call(environment.getattr(environment.getattr(l_util, 'random'), 'randrange'), 1, 2)), 
            context.call(l_lipsum, context.call(environment.getattr(environment.getattr(l_util, 'random'), 'randrange'), 1, 2)), 
            context.call(l_lipsum, context.call(environment.getattr(environment.getattr(l_util, 'random'), 'randrange'), 1, 2)), 
            context.call(l_lipsum, context.call(environment.getattr(environment.getattr(l_util, 'random'), 'randrange'), 1, 2)), 
            context.call(l_lipsum, context.call(environment.getattr(environment.getattr(l_util, 'random'), 'randrange'), 1, 2)), 
            context.call(l_lipsum, context.call(environment.getattr(environment.getattr(l_util, 'random'), 'randrange'), 1, 2)), 
            context.call(l_lipsum, context.call(environment.getattr(environment.getattr(l_util, 'random'), 'randrange'), 1, 2)), 
            context.call(l_lipsum, context.call(environment.getattr(environment.getattr(l_util, 'random'), 'randrange'), 1, 2)), 
            context.call(l_lipsum, context.call(environment.getattr(environment.getattr(l_util, 'random'), 'randrange'), 1, 2)), 
            context.call(l_lipsum, context.call(environment.getattr(environment.getattr(l_util, 'random'), 'randrange'), 1, 2)), 
            context.call(l_lipsum, context.call(environment.getattr(environment.getattr(l_util, 'random'), 'randrange'), 1, 2)), 
        )

    blocks = {'postsouth': block_postsouth, 'subtitle': block_subtitle, 'visualizer': block_visualizer}
    debug_info = '1=9&130=15&3=19&5=23&24=28&32=29&48=30&53=31&58=32&63=33&68=34&73=35&78=36&83=37&88=38&93=39&98=40&103=41&108=42&113=43'
    return locals()