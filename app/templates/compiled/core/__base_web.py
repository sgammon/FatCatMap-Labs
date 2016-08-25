from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/core/__base_web.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('core/__base.html', 'source/core/__base_web.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_prenorth(context, environment=environment):
        l_page = context.resolve('page')
        l_assets = context.resolve('assets')
        if 0: yield None
        yield u'\n\n'
        if environment.getattr(l_page, 'optimize'):
            if 0: yield None
            yield u'\n\t<link rel="stylesheet" media="screen" href="%s">\n' % (
                context.call(environment.getattr(l_assets, 'style'), 'fcm', 'compiled'), 
            )
        else:
            if 0: yield None
            yield u'\n\t<link rel="stylesheet" media="screen" href="%s">\n\t<link rel="stylesheet" media="screen" href="%s">\n\t<link rel="stylesheet" media="screen" href="%s">\n' % (
                context.call(environment.getattr(l_assets, 'style'), 'fonts', 'core'), 
                context.call(environment.getattr(l_assets, 'style'), 'main', 'compiled'), 
                context.call(environment.getattr(l_assets, 'style'), 'interaction', 'compiled'), 
            )
        yield u'\n\n'
        if environment.getattr(l_page, 'mobile'):
            if 0: yield None
            yield u'\n<link rel="stylesheet" media="handheld" href="%s">\n' % (
                context.call(environment.getattr(l_assets, 'style'), 'mobile', 'core'), 
            )
        yield u'\n\n'
        if environment.getattr(l_page, 'print'):
            if 0: yield None
            yield u'\n<link rel="stylesheet" media="screen" href="%s">\n' % (
                context.call(environment.getattr(l_assets, 'style'), 'print', 'compiled'), 
            )
        yield u'\n\n'
        if environment.getattr(l_page, 'ie'):
            if 0: yield None
            yield u'\n<link rel="stylesheet" media="screen" href="%s">\n' % (
                context.call(environment.getattr(l_assets, 'style'), 'ie', 'compiled'), 
            )
        yield u'\n\n\n'
        for event in context.blocks['northstyle'][0](context):
            yield event
        yield u'\n\n<!-- jQuery via CDN -->\n<!-- script src="http://ajax.googleapis.com/ajax/libs/jquery/1.5.1/jquery.min.js"></script -->\n<script src="%s"></script>\n\n<!-- Core Dependencies -->\n<script src="%s"></script>\n<script src="%s"></script>\n\n\n' % (
            context.call(environment.getattr(l_assets, 'script'), 'core', 'jquery'), 
            context.call(environment.getattr(l_assets, 'script'), 'base', 'fatcatmap'), 
            context.call(environment.getattr(l_assets, 'script'), 'yepnope', 'core'), 
        )
        for event in context.blocks['northloader'][0](context):
            yield event
        yield u'\n\n'

    def block_body(context, environment=environment):
        if 0: yield None
        yield u'\n<div id="container">\n\n\t\n\t'
        for event in context.blocks['superbar'][0](context):
            yield event
        yield u'\n\n\t\n\t'
        for event in context.blocks['content'][0](context):
            yield event
        yield u'\n\n\t\n\t'
        for event in context.blocks['superfooter'][0](context):
            yield event
        yield u'\n\t\n</div>\n'

    def block_presouth(context, environment=environment):
        l_assets = context.resolve('assets')
        if 0: yield None
        yield u'\n<script src="%s"></script>\n<script src="%s"></script>\n<script src="%s"></script>\n<script src="%s"></script>\n\n<!-- FatCatMap Platform -->\n<script src="%s"></script>\n\n<script type="text/javascript">\n\t' % (
            context.call(environment.getattr(l_assets, 'script'), 'backbone', 'core'), 
            context.call(environment.getattr(l_assets, 'script'), 'data', 'core'), 
            context.call(environment.getattr(l_assets, 'script'), 'lawnchair', 'core'), 
            context.call(environment.getattr(l_assets, 'script'), 'modernizr', 'core'), 
            context.call(environment.getattr(l_assets, 'script'), 'fcm', 'fatcatmap'), 
        )
        l_link = context.resolve('link')
        if 0: yield None
        t_1 = context.eval_ctx.save()
        context.eval_ctx.autoescape = False
        yield u'\n\t\tyepnope([\n\n\t\t\t{\n\t\t\t\t// Polyfill JSON Support\n\t\t\t\ttest : window.JSON && window.JSON.parse,\n\t\t\t\tnope: "%s"\n\t\t\t},\n\n\t\t\t{\n\t\t\t\t// Load jQuery and jQuery Plugins\n\t\t\t\ttest: window.jQuery,\n\t\t\t\tnope: "%s",\n\t\t\t\tload: ["%s", "%s",\n\t\t\t\t\t\t"%s", "%s"]\n\t\t\t},\n\t\t\t\n\t\t\t{\n\t\t\t\t// Load Lawnchair and plugins\n\t\t\t\ttest: window.Lawnchair,\n\t\t\t\tnope: ["%s"]\n\t\t\t},\n\t\t\t\n\t\t\t{\n\t\t\t\t// CSS Animations Support\n\t\t\t\ttest: Modernizr.cssanimations,\n\t\t\t\tyep: ["%s"]\n\t\t\t},\n\n\t\t\t{\n\t\t\t\t// FCM Layout + Interaction packages\n\t\t\t\ttest: $.fatcatmap,\n\t\t\t\tnope: "%s",\n\t\t\t\tload: ["%s", "%s"]\n\t\t\t},\n\n\t\t\t{\n\t\t\t\t// Load FatCatMap JSAPI & Channel JSAPI\n\t\t\t\tload: ["%s", "/_ah/channel/jsapi"],\n\t\t\t},\n\n\t\t\t{\n\t\t\t\t// Combined Storage\n\t\t\t\ttest: Modernizr.localstorage && Modernizr.sessionstorage && Modernizr.indexeddb,\n\t\t\t\tyep: ["%s"],\n\t\t\t},\n\t\t\t\n\t\t\t{\n\t\t\t\t// Local Storage Only\n\t\t\t\ttest: (Modernizr.localstorage || Modernizr.sessionstorage) && !Modernizr.indexeddb,\n\t\t\t\tyep: ["%s"]\n\t\t\t},\n\t\t\t\n\t\t\t{\n\t\t\t\t// Object Storage Only\n\t\t\t\ttest: Modernizr.indexeddb && !(Modernizr.localstorage || Modernizr.sessionstorage),\n\t\t\t\tyep: ["%s"]\n\t\t\t},\n\t\t\t\n\t\t\t' % (
            context.call(environment.getattr(l_assets, 'script'), 'json2', 'polyfills'), 
            context.call(environment.getattr(l_assets, 'script'), 'core', 'jquery'), 
            context.call(environment.getattr(l_assets, 'script'), 'masonry', 'jquery-ui'), 
            context.call(environment.getattr(l_assets, 'script'), 'fancybox', 'jquery-ui'), 
            context.call(environment.getattr(l_assets, 'script'), 'easing', 'jquery'), 
            context.call(environment.getattr(l_assets, 'script'), 'mousewheel', 'jquery'), 
            context.call(environment.getattr(l_assets, 'script'), 'lawnchair', 'core'), 
            context.call(environment.getattr(l_assets, 'script'), 'animate-enhanced', 'jquery-ui'), 
            context.call(environment.getattr(l_assets, 'script'), 'fcm', 'fatcatmap'), 
            context.call(environment.getattr(l_assets, 'script'), 'layout', 'fatcatmap'), 
            context.call(environment.getattr(l_assets, 'script'), 'interaction', 'fatcatmap'), 
            context.call(l_link, 'js-api'), 
            context.call(environment.getattr(l_assets, 'script'), 'combined', 'storage'), 
            context.call(environment.getattr(l_assets, 'script'), 'local', 'storage'), 
            context.call(environment.getattr(l_assets, 'script'), 'object', 'storage'), 
        )
        for event in context.blocks['southloader'][0](context):
            yield event
        yield u"\n\n\t\t\t{\n\t\t\t\tcomplete: function (){\n\n\t\t\t\t\tsuperbar = new Layout.SuperBar({id: 'momentumSuperbar', el: document.getElementById('momentumSuperbar')});\n\t\t\t\t\t$.fatcatmap.api.layout.register('superbar', superbar);\n\n\t\t\t\t\tsupernav = new Layout.Navigation({id: 'topnav', el: document.getElementById('topnav')});\n\t\t\t\t\t$.fatcatmap.api.layout.register('supernav', supernav);\n\n\t\t\t\t\tsuperfooter = new Layout.SuperFooter({id: 'momentumSuperfooter', el: document.getElementById('momentumSuperfooter')});\n\t\t\t\t\t$.fatcatmap.api.layout.register('superfooter', superfooter);\t\t\t\t\t\n\t\t\t\t\t\n\t\t\t\t\t$.fatcatmap.state.events.triggerEvent('PLATFORM_READY', {fcm: $.fatcatmap});\n\t\t\t\t}\n\t\t\t}\n\t\t]);\n\t"
        context.eval_ctx.revert(t_1)
        yield u'\n</script>\n'

    def block_superfooter(context, environment=environment):
        if 0: yield None
        yield u'\n\t'

    def block_content(context, environment=environment):
        if 0: yield None
        yield u'\n\t'

    def block_southloader(context, environment=environment):
        if 0: yield None
        yield u'\n\t\t\t'

    def block_superbar(context, environment=environment):
        if 0: yield None
        yield u'\n\t'

    def block_northstyle(context, environment=environment):
        if 0: yield None

    def block_northloader(context, environment=environment):
        if 0: yield None

    blocks = {'prenorth': block_prenorth, 'body': block_body, 'presouth': block_presouth, 'superfooter': block_superfooter, 'content': block_content, 'southloader': block_southloader, 'superbar': block_superbar, 'northstyle': block_northstyle, 'northloader': block_northloader}
    debug_info = '1=9&3=15&5=20&6=23&8=28&9=29&10=30&13=33&14=36&17=39&18=42&21=45&22=48&26=51&30=54&33=55&34=56&37=58&41=62&45=65&49=68&53=71&59=75&60=79&61=80&62=81&63=82&66=83&75=90&81=91&82=92&83=94&89=96&95=97&101=98&102=99&107=101&113=102&119=103&125=104&128=106&53=112&49=116&128=120&45=124&26=128&37=131'
    return locals()