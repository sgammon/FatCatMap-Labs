from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/layouts/main.html'

    def root(context, environment=environment):
        parent_template = None
        l_page = context.resolve('page')
        if 0: yield None
        if (not environment.getattr(l_page, 'standalone')):
            if 0: yield None
            if parent_template is None:
                yield u' \n\t'
            parent_template = environment.get_template('core/__base_web.html', 'source/layouts/main.html')
            for name, parent_block in parent_template.blocks.iteritems():
                context.blocks.setdefault(name, []).append(parent_block)
            if parent_template is None:
                yield u'\n'
        if parent_template is None:
            yield u'\n\n'
        if parent_template is None:
            for event in context.blocks['superbar'][0](context):
                yield event
        if parent_template is None:
            yield u'\n\n'
        if parent_template is None:
            for event in context.blocks['content'][0](context):
                yield event
        if parent_template is None:
            yield u'\n\n'
        if parent_template is None:
            for event in context.blocks['superfooter'][0](context):
                yield event
        if parent_template is not None:
            for event in parent_template.root_render_func(context):
                yield event

    def block_content_body_class(context, environment=environment):
        if 0: yield None
        yield u'content_body'

    def block_infoNotice(context, environment=environment):
        l_page = context.resolve('page')
        if 0: yield None
        yield u'\n\t\t\t\t\t'
        if environment.getattr(environment.getattr(l_page, 'elements'), 'infoNotice'):
            if 0: yield None
            yield u'\n\t\t\t\t\t\t%s\n\t\t\t\t\t' % (
                environment.getattr(environment.getattr(l_page, 'elements'), 'infoNotice'), 
            )
        yield u'\n\t\t\t\t'

    def block_superfooter(context, environment=environment):
        if 0: yield None
        yield u"\n<footer id='momentumSuperfooter' class='superfooter fullfooter' data-element='superfooter' data-element-type='SuperPanel'>\n\t"
        template = environment.get_template('snippets/superfooter.html', 'source/layouts/main.html')
        for event in template.root_render_func(template.new_context(context.parent, True, locals())):
            yield event
        yield u'\n</footer>\n'

    def block_successNotice(context, environment=environment):
        l_page = context.resolve('page')
        if 0: yield None
        yield u'\n\t\t\t\t\t'
        if environment.getattr(environment.getattr(l_page, 'elements'), 'successNotice'):
            if 0: yield None
            yield u'\n\t\t\t\t\t\t%s\n\t\t\t\t\t' % (
                environment.getattr(environment.getattr(l_page, 'elements'), 'successNotice'), 
            )
        yield u'\n\t\t\t\t'

    def block_content_footer_class(context, environment=environment):
        if 0: yield None
        yield u'content_footer'

    def block_content_header(context, environment=environment):
        l_link = context.resolve('link')
        if 0: yield None
        yield u'\n\t\t\t<div class=\'extendedNav\'>\n\n\t\t\t\t<div id=\'browsePane\' class=\'navpane hidden\' data-navref=\'browse\'>\n\n\t\t\t\t\t<div class=\'floatleft fullheight tenthwidth\'>\n\t\t\t\t\t\t<a href="%s" title=\'browse raw data, in context and with easy connections to related information\'><img src=\'/assets/img/static/layout/headers/browse.png\' alt=\'fatcatmap: browse\' width=\'124\' height=\'90\' /></a>\n\t\t\t\t\t</div>\n\t\t\t\t\n\t\t\t\t\t<div class=\'floatleft fullheight halfwidth\'>\n\t\t\t\t\t\tsup\n\t\t\t\t\t</div>\n\n\t\t\t\t</div>\n\n\t\t\t\t<div id=\'searchPane\' class=\'navpane hidden\' data-navref=\'search\'>\n\n\t\t\t\t\t<div class=\'floatleft fullheight tenthwidth\'>\n\t\t\t\t\t\t<a href="%s" title=\'search our enourmous database of american political transparency data\'><img src=\'/assets/img/static/layout/headers/search.png\' alt=\'fatcatmap: search\' width=\'124\' height=\'90\' /></a>\n\t\t\t\t\t</div>\n\t\t\t\t\n\t\t\t\t\t<div class=\'floatleft fullheight halfwidth\'>\n\t\t\t\t\t\tsup\n\t\t\t\t\t</div>\n\n\t\t\t\t</div>\n\n\t\t\t\t<div id=\'mapPane\' class=\'navpane hidden\' data-navref=\'map\'>\n\t\t\t\t\n\t\t\t\t\t<div class=\'floatleft fullheight tenthwidth\'>\n\t\t\t\t\t\n\t\t\t\t\t\t<a href="%s" title=\'interactively explore data as a map of connected nodes and edges\'><img src=\'/assets/img/static/layout/headers/map.png\' alt=\'fatcatmap: graph\' width=\'124\' height=\'90\' /></a>\n\t\t\t\t\t\n\t\t\t\t\t</div>\n\t\t\t\t\n\t\t\t\t\t<div class=\'floatleft fullheight halfwidth\'>\n\t\t\t\t\t\n\t\t\t\t\t\tsup\n\t\t\t\t\t\n\t\t\t\t\t</div>\n\t\t\t\t\n\t\t\t\t</div>\n\n\t\t\t\t<div id=\'visualizePane\' class=\'navpane hidden\' data-navref=\'visualize\'>\n\n\t\t\t\t\t<div class=\'floatleft fullheight tenthwidth\'>\n\t\t\t\t\t\n\t\t\t\t\t\t<a href="%s" title=\'mash up, compare, and analyze data in real time with our dynamic charting tools\'><img src=\'/assets/img/static/layout/headers/visualize.png\' alt=\'fatcatmap: visualize\' width=\'124\' height=\'90\' /></a>\n\t\t\t\t\t\n\t\t\t\t\t</div>\n\t\t\t\t\n\t\t\t\t\t<div class=\'floatleft fullheight halfwidth\'>\n\t\t\t\t\t\n\t\t\t\t\t\tsup\n\t\t\t\t\t\n\t\t\t\t\t</div>\n\n\n\t\t\t\t</div>\n\t\t\t\n\t\t\t\t<div id=\'interactPane\' class=\'navpane hidden\' data-navref=\'interact\'>\n\n\t\t\t\t\t<div class=\'floatleft fullheight tenthwidth\'>\n\t\t\t\t\t\n\t\t\t\t\t\t<a href="%s" title="share interesting data you\'ve found or visualizations you\'ve made with friends and the world"><img src=\'/assets/img/static/layout/headers/interact.png\' alt=\'fatcatmap: interact\' width=\'124\' height=\'90\' />\n\t\t\t\t\t\n\t\t\t\t\t</div>\n\t\t\t\t\n\t\t\t\t\t<div class=\'floatleft fullheight halfwidth\'>\n\t\t\t\t\t\n\t\t\t\t\t\tsup\n\t\t\t\t\t\n\t\t\t\t\t</div>\n\n\t\t\t\t</div>\t\t\t\t\n\n\t\t\t</div>\t\t\n\t\t' % (
            context.call(l_link, 'browse:landing'), 
            context.call(l_link, 'search:landing'), 
            context.call(l_link, 'map:landing'), 
            context.call(l_link, 'visualize:landing'), 
            context.call(l_link, 'interact:landing'), 
        )

    def block_notice(context, environment=environment):
        l_page = context.resolve('page')
        if 0: yield None
        yield u'\n\t\t\t\t\t'
        if environment.getattr(environment.getattr(l_page, 'elements'), 'generalNotice'):
            if 0: yield None
            yield u'\n\t\t\t\t\t\t%s\n\t\t\t\t\t' % (
                environment.getattr(environment.getattr(l_page, 'elements'), 'generalNotice'), 
            )
        yield u'\n\t\t\t\t'

    def block_sidebars(context, environment=environment):
        if 0: yield None
        yield u'\n\t'

    def block_content(context, environment=environment):
        l_page = context.resolve('page')
        if 0: yield None
        yield u'\n<div id="main" role="main" class=\'rootContent fcmfull\'>\n\n'
        if (not environment.getattr(l_page, 'standalone')):
            if 0: yield None
            yield u"\n\t<div id='contentHeader' class='"
            for event in context.blocks['content_headerheader_class'][0](context):
                yield event
            yield u" hidden'>\n\t\t"
            for event in context.blocks['content_header'][0](context):
                yield event
            yield u"\n\t\t<div class='foldNavigation'>\n\t\t\t<a href='#'>close menu</a>\n\t\t</div>\n\t</div>\n"
        yield u'\n\n\t'
        if (not environment.getattr(l_page, 'standalone')):
            if 0: yield None
            yield u"\n\t\t<div id='contentBody' class='"
            for event in context.blocks['content_body_class'][0](context):
                yield event
            yield u"'>\n\n\t\t<div id='globalAlerts'>\n\t\t\t<div id='globalErrorNotice' class='"
            if (not environment.getattr(environment.getattr(l_page, 'elements'), 'errorNotice')):
                if 0: yield None
                yield u'hidden '
            yield u"error globalAlert'>\n\t\t\t\t"
            for event in context.blocks['errorNotice'][0](context):
                yield event
            yield u"\n\t\t\t</div>\n\n\t\t\t<div id='globalInfoNotice' class='"
            if (not environment.getattr(environment.getattr(l_page, 'elements'), 'infoNotice')):
                if 0: yield None
                yield u'hidden '
            yield u"info globalAlert'>\n\t\t\t\t"
            for event in context.blocks['infoNotice'][0](context):
                yield event
            yield u"\n\t\t\t</div>\n\n\t\t\t<div id='globalNotice' class='"
            if (not environment.getattr(environment.getattr(l_page, 'elements'), 'generalNotice')):
                if 0: yield None
                yield u'hidden '
            yield u"notice globalAlert'>\n\t\t\t\t"
            for event in context.blocks['notice'][0](context):
                yield event
            yield u"\n\t\t\t</div>\n\t\t\t\n\t\t\t<div id='globalSuccess' class='"
            if (not environment.getattr(environment.getattr(l_page, 'elements'), 'successNotice')):
                if 0: yield None
                yield u'hidden '
            yield u"success globalAlert'>\n\t\t\t\t"
            for event in context.blocks['successNotice'][0](context):
                yield event
            yield u'\n\t\t\t</div>\n\t\t</div>\n\n\t'
        else:
            if 0: yield None
            yield u"\n\t\t<div id='frameContent'>\n\t"
        yield u'\n\n\t\t'
        for event in context.blocks['content_body'][0](context):
            yield event
        yield u'\n\n\t\t'
        if (not environment.getattr(l_page, 'standalone')):
            if 0: yield None
            yield u'\n\t\t\t'
            if environment.getattr(l_page, 'watermark'):
                if 0: yield None
                yield u'\n\t\t\t\t'
                template = environment.get_template('snippets/dev_widget.html', 'source/layouts/main.html')
                for event in template.root_render_func(template.new_context(context.parent, True, locals())):
                    yield event
                yield u'\n\t\t\t'
            yield u'\n\t\t'
        yield u'\n\t\n\t</div>\n\n\t'
        for event in context.blocks['sidebars'][0](context):
            yield event
        yield u'\n\n\t'
        if (not environment.getattr(l_page, 'standalone')):
            if 0: yield None
            yield u"\n\t\t<div id='contentFooter' class='"
            for event in context.blocks['content_footer_class'][0](context):
                yield event
            yield u" hidden'>\n\t\t\t"
            for event in context.blocks['content_footer'][0](context):
                yield event
            yield u'\n\t\t</div>\n\t'
        yield u'\n\n</div>\n'

    def block_superbar(context, environment=environment):
        if 0: yield None
        yield u"\n<header id='momentumSuperbar' class='superbar' data-element='superbar' data-element-type='SuperPanel'>\n\t"
        template = environment.get_template('snippets/superbar.html', 'source/layouts/main.html')
        for event in template.root_render_func(template.new_context(context.parent, True, locals())):
            yield event
        yield u'\n</header>\n'

    def block_content_headerheader_class(context, environment=environment):
        if 0: yield None
        yield u'content_header'

    def block_errorNotice(context, environment=environment):
        l_page = context.resolve('page')
        if 0: yield None
        yield u'\n\t\t\t\t\t'
        if environment.getattr(environment.getattr(l_page, 'elements'), 'errorNotice'):
            if 0: yield None
            yield u'\n\t\t\t\t\t\t%s\n\t\t\t\t\t' % (
                environment.getattr(environment.getattr(l_page, 'elements'), 'errorNotice'), 
            )
        yield u'\n\t\t\t\t'

    def block_content_body(context, environment=environment):
        if 0: yield None
        yield u'\n\t\t'

    def block_content_footer(context, environment=environment):
        if 0: yield None
        yield u'\n\t\t\t'

    blocks = {'content_body_class': block_content_body_class, 'infoNotice': block_infoNotice, 'superfooter': block_superfooter, 'successNotice': block_successNotice, 'content_footer_class': block_content_footer_class, 'content_header': block_content_header, 'notice': block_notice, 'sidebars': block_sidebars, 'content': block_content, 'superbar': block_superbar, 'content_headerheader_class': block_content_headerheader_class, 'errorNotice': block_errorNotice, 'content_body': block_content_body, 'content_footer': block_content_footer}
    debug_info = '1=10&2=14&5=22&11=27&165=32&101=38&113=42&114=46&115=49&165=53&167=56&129=61&130=65&131=68&156=72&16=76&22=80&34=81&47=82&63=83&80=84&121=87&122=91&123=94&152=98&11=102&14=106&15=109&16=112&100=116&101=119&104=122&105=126&112=129&113=133&120=136&121=140&128=143&129=147&141=154&144=157&145=160&146=163&152=169&155=172&156=175&157=178&5=183&7=186&15=191&105=195&106=199&107=202&141=206&157=210'
    return locals()