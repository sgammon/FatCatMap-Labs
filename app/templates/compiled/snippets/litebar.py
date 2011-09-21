from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/snippets/litebar.html'

    def root(context, environment=environment):
        l_assets = context.resolve('assets')
        if 0: yield None
        yield u'<header id=\'momentumSuperbar\' class=\'litebar\' data-element=\'superbar\' data-element-type=\'SuperPanel\'>\t\n\n\t<div id=\'liteNavigation\'>\n\t\t<div id=\'liteNavContent\' class=\'hidden\'>\n\t\t\tHere is all the crazy content up top\n\t\t\t<br />\n\t\t\tCool navigation stuff will go here\n\t\t\t<br />\n\t\t\tHopefully it will start working\n\t\t</div>\n\t</div>\n\n\t<div id=\'toploader\'>\n\t\t<div id=\'globalProgress\'></div>\n\t</div>\n\n\t<div id=\'fcmTopBranding\' class=\'pulldown\'>\n\t\t<img src="%s" height=\'30\' width=\'228\'  alt=\'fatcatmap alpha\' />\n\t</div>\n\t\t\n</header>\n\n<script type="text/javascript">\n\n$(\'#fcmTopBranding\').click(function () {\n\t\n\tlitenav = $(\'#liteNavigation\');\n\tlitenav_content = $(\'#liteNavContent\');\n\t\n\tif (litenav.hasClass(\'expanded\'))\n\t{\n\t\tlitecss = {height: 0};\n\t\tlitecss[\'min-height\'] = 0;\n\t\t\n\t\tlitenav_content.animate({opacity: 0}, function () {\n\t\t\n\t\t\tlitenav_content.addClass(\'hidden\');\n\t\t\t\n\t\t}).parent().animate(litecss, function () {\n\t\t\tlitenav.removeClass(\'expanded\').addClass(\'hidden\');\n\t\t});\n\t}\n\telse\n\t{\n\t\tlitecss = {height: $(document).height() * .2};\n\t\tlitecss[\'min-height\'] = 115;\n\t\t\n\t\tlitenav.animate(litecss, function () {\n\t\t\t\n\t\t\tlitenav_content.animate({opacity: 1}).removeClass(\'hidden\');\n\t\t\t\t\n\t\t}).addClass(\'expanded\').removeClass(\'hidden\');\n\t}\n\t\n});\n\n</script>' % (
            context.call(environment.getattr(l_assets, 'image'), 'branding', 'fatcatmap-alpha-v3-alt-15.png'), 
        )

    blocks = {}
    debug_info = '18=10'
    return locals()