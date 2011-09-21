from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/layouts/lite.html'

    def root(context, environment=environment):
        parent_template = None
        l_page = context.resolve('page')
        if 0: yield None
        if (not environment.getattr(l_page, 'standalone')):
            if 0: yield None
            if parent_template is None:
                yield u' \n\t'
            parent_template = environment.get_template('core/__base_web.html', 'source/layouts/lite.html')
            for name, parent_block in parent_template.blocks.iteritems():
                context.blocks.setdefault(name, []).append(parent_block)
            if parent_template is None:
                yield u'\n'
        if parent_template is None:
            yield u'\n\n'
        if parent_template is None:
            for event in context.blocks['body_class'][0](context):
                yield event
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
            yield u'\n\n\n'
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
        yield u'\n\t\t\t\t'
        if environment.getattr(environment.getattr(l_page, 'elements'), 'infoNotice'):
            if 0: yield None
            yield u'\n\t\t\t\t\t%s\n\t\t\t\t' % (
                environment.getattr(environment.getattr(l_page, 'elements'), 'infoNotice'), 
            )
        yield u'\n\t\t\t'

    def block_superfooter(context, environment=environment):
        l_link = context.resolve('link')
        if 0: yield None
        yield u'\n<footer id=\'momentumSuperfooter\' class=\'superfooter litefooter\' data-element=\'superfooter\' data-element-type=\'SuperPanel\'>\n\t<div class=\'floatleft\' id=\'utilityLinks\'>\n\t\t&copy;2011 political momentum (<a href="%s">about</a> - <a href="%s"> legal</a> - <a href="%s">help</a>)\n\t</div>\n\n\n\t<div id=\'bottomFcmBranding\' class=\'floatright\'>\n\t\t<a href=\'http://momentum.io\' target=\'_blank\' class=\'noicon\'><div id=\'momentumBrand\'></div></a>\n\t</div>\n\n\t<div id=\'globalActivityIndicator\' class=\'floatright\'>\n\t</div>\n</footer>\n' % (
            context.call(l_link, 'about:landing'), 
            context.call(l_link, 'legal:landing'), 
            context.call(l_link, 'help:landing'), 
        )

    def block_successNotice(context, environment=environment):
        l_page = context.resolve('page')
        if 0: yield None
        yield u'\n\t\t\t\t'
        if environment.getattr(environment.getattr(l_page, 'elements'), 'successNotice'):
            if 0: yield None
            yield u'\n\t\t\t\t\t%s\n\t\t\t\t' % (
                environment.getattr(environment.getattr(l_page, 'elements'), 'successNotice'), 
            )
        yield u'\n\t\t\t'

    def block_content_footer_class(context, environment=environment):
        if 0: yield None
        yield u'content_footer'

    def block_body_class(context, environment=environment):
        if 0: yield None
        yield u'fcm-lite fcm-dark'

    def block_notice(context, environment=environment):
        l_page = context.resolve('page')
        if 0: yield None
        yield u'\n\t\t\t\t'
        if environment.getattr(environment.getattr(l_page, 'elements'), 'generalNotice'):
            if 0: yield None
            yield u'\n\t\t\t\t\t%s\n\t\t\t\t' % (
                environment.getattr(environment.getattr(l_page, 'elements'), 'generalNotice'), 
            )
        yield u'\n\t\t\t'

    def block_sidebars(context, environment=environment):
        if 0: yield None
        yield u'\n'

    def block_content(context, environment=environment):
        l_page = context.resolve('page')
        if 0: yield None
        yield u'\n<div id="main" role="main" class=\'rootContent fcmlite\'>\n\n'
        if (not environment.getattr(l_page, 'standalone')):
            if 0: yield None
            yield u"\n\t<div id='contentBody' class='"
            for event in context.blocks['content_body_class'][0](context):
                yield event
            yield u"'>\n\n\t<div id='globalAlerts'>\n\t\t<div id='globalErrorNotice' class='"
            if (not environment.getattr(environment.getattr(l_page, 'elements'), 'errorNotice')):
                if 0: yield None
                yield u'hidden '
            yield u"error globalAlert'>\n\t\t\t"
            for event in context.blocks['errorNotice'][0](context):
                yield event
            yield u"\n\t\t</div>\n\n\t\t<div id='globalInfoNotice' class='"
            if (not environment.getattr(environment.getattr(l_page, 'elements'), 'infoNotice')):
                if 0: yield None
                yield u'hidden '
            yield u"info globalAlert'>\n\t\t\t"
            for event in context.blocks['infoNotice'][0](context):
                yield event
            yield u"\n\t\t</div>\n\n\t\t<div id='globalNotice' class='"
            if (not environment.getattr(environment.getattr(l_page, 'elements'), 'generalNotice')):
                if 0: yield None
                yield u'hidden '
            yield u"notice globalAlert'>\n\t\t\t"
            for event in context.blocks['notice'][0](context):
                yield event
            yield u"\n\t\t</div>\n\t\t\n\t\t<div id='globalSuccess' class='"
            if (not environment.getattr(environment.getattr(l_page, 'elements'), 'successNotice')):
                if 0: yield None
                yield u'hidden '
            yield u"success globalAlert'>\n\t\t\t"
            for event in context.blocks['successNotice'][0](context):
                yield event
            yield u'\n\t\t</div>\n\t</div>\n\n'
        else:
            if 0: yield None
            yield u"\n\t<div id='frameContent'>\n"
        yield u'\n\n\t'
        for event in context.blocks['content_body'][0](context):
            yield event
        yield u'\n\n\t'
        if (not environment.getattr(l_page, 'standalone')):
            if 0: yield None
            yield u'\n\t\t'
            if environment.getattr(l_page, 'watermark'):
                if 0: yield None
                yield u'\n\t\t\t'
                template = environment.get_template('snippets/dev_widget.html', 'source/layouts/lite.html')
                for event in template.root_render_func(template.new_context(context.parent, True, locals())):
                    yield event
                yield u'\n\t\t'
            yield u'\n\t'
        yield u'\n\n</div>\n\n'
        for event in context.blocks['sidebars'][0](context):
            yield event
        yield u'\n\n'
        if (not environment.getattr(l_page, 'standalone')):
            if 0: yield None
            yield u"\n\t<div id='contentFooter' class='"
            for event in context.blocks['content_footer_class'][0](context):
                yield event
            yield u" hidden'>\n\t\t"
            for event in context.blocks['content_footer'][0](context):
                yield event
            yield u'\n\t</div>\n'
        yield u'\n\n</div>\n'

    def block_superbar(context, environment=environment):
        if 0: yield None
        yield u'\n'
        template = environment.get_template('snippets/litebar.html', 'source/layouts/lite.html')
        for event in template.root_render_func(template.new_context(context.parent, True, locals())):
            yield event
        yield u'\n'

    def block_errorNotice(context, environment=environment):
        l_page = context.resolve('page')
        if 0: yield None
        yield u'\n\t\t\t\t'
        if environment.getattr(environment.getattr(l_page, 'elements'), 'errorNotice'):
            if 0: yield None
            yield u'\n\t\t\t\t\t%s\n\t\t\t\t' % (
                environment.getattr(environment.getattr(l_page, 'elements'), 'errorNotice'), 
            )
        yield u'\n\t\t\t'

    def block_content_body(context, environment=environment):
        if 0: yield None
        yield u'\n\t'

    def block_content_footer(context, environment=environment):
        if 0: yield None
        yield u'\n\t\t'

    blocks = {'content_body_class': block_content_body_class, 'infoNotice': block_infoNotice, 'superfooter': block_superfooter, 'successNotice': block_successNotice, 'content_footer_class': block_content_footer_class, 'body_class': block_body_class, 'notice': block_notice, 'sidebars': block_sidebars, 'content': block_content, 'superbar': block_superbar, 'errorNotice': block_errorNotice, 'content_body': block_content_body, 'content_footer': block_content_footer}
    debug_info = '1=10&2=14&5=22&7=27&11=32&80=37&15=43&27=47&28=51&29=54&80=58&83=62&43=67&44=71&45=74&70=78&5=82&35=86&36=90&37=93&66=97&11=101&14=105&15=108&18=111&19=115&26=118&27=122&34=125&35=129&42=132&43=136&55=143&58=146&59=149&60=152&66=158&69=161&70=164&71=167&7=172&8=175&19=180&20=184&21=187&55=191&71=195'
    return locals()