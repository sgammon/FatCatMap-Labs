from __future__ import division
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = 'source/macros/form.html'

    def root(context, environment=environment):
        t_1 = environment.filters['e']
        t_2 = environment.tests['string']
        if 0: yield None
        def macro(l_name, l_value, l_type, l_size, l_class):
            t_3 = []
            pass
            t_3.extend((
                u'<input type="', 
                to_string(l_type), 
                u'" name="', 
                to_string(l_name), 
                u'" value="', 
                to_string(t_1(l_value)), 
                u'" size="', 
                to_string(l_size), 
                u'" class="', 
                to_string(l_class), 
                u'" />', 
            ))
            return concat(t_3)
        context.exported_vars.add('input')
        context.vars['input'] = l_input = Macro(environment, macro, 'input', ('name', 'value', 'type', 'size', 'class'), ('', 'text', 20, '', ), False, False, False)
        def macro(l_field):
            t_4 = []
            pass
            t_4.extend((
                u'<label for="', 
                to_string(environment.getattr(l_field, 'id')), 
                u'" class=\'fieldlabel\'>', 
                to_string(environment.getattr(environment.getattr(l_field, 'label'), 'text')), 
            ))
            if environment.getattr(environment.getattr(l_field, 'flags'), 'required'):
                pass
                t_4.append(
                    u'<abbr title="This field is required.">*</abbr>', 
                )
            t_4.append(
                u'</label>\n', 
            )
            return concat(t_4)
        context.exported_vars.add('form_field_label')
        context.vars['form_field_label'] = l_form_field_label = Macro(environment, macro, 'form_field_label', ('field',), (), False, False, False)
        def macro(l_field):
            t_5 = []
            pass
            if environment.getattr(l_field, 'description'):
                pass
                t_5.extend((
                    u'\n        <span class="descr">', 
                    to_string(environment.getattr(l_field, 'description')), 
                    u'</span>\n    ', 
                ))
            return concat(t_5)
        context.exported_vars.add('form_field_description')
        context.vars['form_field_description'] = l_form_field_description = Macro(environment, macro, 'form_field_description', ('field',), (), False, False, False)
        def macro(l_field):
            t_6 = []
            pass
            if environment.getattr(l_field, 'errors'):
                pass
                t_6.append(
                    u'\n    <ul class="errors">', 
                )
                l_error = missing
                for l_error in environment.getattr(l_field, 'errors'):
                    pass
                    t_6.extend((
                        u'<li>', 
                        to_string(l_error), 
                        u'</li>', 
                    ))
                l_error = missing
                t_6.append(
                    u'</ul>\n    ', 
                )
            return concat(t_6)
        context.exported_vars.add('form_field_errors')
        context.vars['form_field_errors'] = l_form_field_errors = Macro(environment, macro, 'form_field_errors', ('field',), (), False, False, False)
        def macro(l_field, l_kwargs):
            t_7 = []
            pass
            t_7.extend((
                to_string(context.call(l_field, **l_kwargs)), 
                u'\n    ', 
                to_string(context.call(l_form_field_label, l_field)), 
                u'\n    ', 
                to_string(context.call(l_form_field_description, l_field)), 
                u'\n    ', 
                to_string(context.call(l_form_field_errors, l_field)), 
            ))
            return concat(t_7)
        context.exported_vars.add('form_field_boolean')
        context.vars['form_field_boolean'] = l_form_field_boolean = Macro(environment, macro, 'form_field_boolean', ('field',), (), True, False, False)
        def macro(l_field, l_kwargs):
            t_8 = []
            pass
            if environment.getattr(l_field, 'type') == 'SubmitField':
                pass
                t_8.extend((
                    u'\n\t\t', 
                    to_string(context.call(l_field)), 
                    u'\n\t', 
                ))
            else:
                pass
                t_8.append(
                    u'\n\t\t', 
                )
                if environment.getattr(l_field, 'type') == 'MultiCheckboxField':
                    pass
                    t_8.extend((
                        u'\n\t\t\t', 
                        to_string(context.call(l_field)), 
                        u'\n\t\t', 
                    ))
                else:
                    pass
                    t_8.append(
                        u'\n\t\t    ', 
                    )
                    if environment.getattr(l_field, 'type') == 'BooleanField':
                        pass
                        t_8.extend((
                            u'\n\t\t        ', 
                            to_string(context.call(l_form_field_boolean, l_field, **l_kwargs)), 
                            u'\n\t\t    ', 
                        ))
                    else:
                        pass
                        t_8.extend((
                            u'\n\t\t        ', 
                            to_string(context.call(l_form_field_label, l_field)), 
                            u'\n\t\t        ', 
                        ))
                        if environment.getattr(l_field, 'type') == 'RadioField':
                            pass
                            t_8.extend((
                                u'\n\t\t            ', 
                                to_string(context.call(l_field, **dict({'class': 'radio-group', }, **l_kwargs))), 
                                u'\n\t\t        ', 
                            ))
                        else:
                            pass
                            t_8.extend((
                                u'\n\t\t            ', 
                                to_string(context.call(l_field, **l_kwargs)), 
                                u'\n\t\t        ', 
                            ))
                        t_8.extend((
                            u'\n\t\t        ', 
                            to_string(context.call(l_form_field_description, l_field)), 
                            u'\n\t\t        ', 
                            to_string(context.call(l_form_field_errors, l_field)), 
                            u'\n\t\t    ', 
                        ))
                    t_8.append(
                        u'\n\t\t', 
                    )
                t_8.append(
                    u'\n\t', 
                )
            return concat(t_8)
        context.exported_vars.add('form_field')
        context.vars['form_field'] = l_form_field = Macro(environment, macro, 'form_field', ('field',), (), True, False, False)
        def macro(l_form_object, l_omitFormTag, l_omitSubmitButton, l_kwargs):
            t_9 = []
            pass
            if t_2(context.call(environment.getattr(l_form_object, 'get_script_snippet'), 'north')):
                pass
                t_9.append(
                    u"\n<script type='text/javascript'>\n\t", 
                )
                if 0: dummy(l_form_field_boolean, l_form_field_description, l_kwargs, l_input, l_form_field_errors, l_form_field_label, l_form_field)
                template = environment.get_or_select_template(context.call(environment.getattr(l_form_object, 'get_script_snippet'), 'north'), 'source/macros/form.html')
                for event in template.root_render_func(template.new_context(context.parent, True, locals())):
                    t_9.append(event)
                t_9.append(
                    u'\n</script>\n', 
                )
            t_9.append(
                u'\n\n', 
            )
            if l_omitFormTag != True:
                pass
                t_9.extend((
                    u"\n\t<form action='", 
                    to_string(context.call(environment.getattr(l_form_object, 'get_action'))), 
                    u"' method='", 
                    to_string(context.call(environment.getattr(l_form_object, 'get_method'))), 
                    u"'", 
                ))
                if environment.getattr(l_kwargs, 'id'):
                    pass
                    t_9.extend((
                        u" id='", 
                        to_string(environment.getattr(l_kwargs, 'id')), 
                        u"'", 
                    ))
                if environment.getattr(l_kwargs, 'class'):
                    pass
                    t_9.extend((
                        u" class='", 
                        to_string(environment.getattr(l_kwargs, 'class')), 
                        u"'", 
                    ))
                else:
                    pass
                    t_9.append(
                        u" class='spi-form'", 
                    )
                if environment.getattr(l_kwargs, 'name'):
                    pass
                    t_9.extend((
                        u" name='", 
                        to_string(environment.getattr(l_kwargs, 'name')), 
                        u"'", 
                    ))
                t_9.append(
                    u'>\n', 
                )
            t_9.append(
                u'\n\n\t    ', 
            )
            l_field = missing
            l_renderForm = context.resolve('renderForm')
            for l_field in l_form_object:
                pass
                t_9.append(
                    u'\n\t        \n\t\t\t', 
                )
                if environment.getattr(l_field, 'type') == 'HiddenField':
                    pass
                    t_9.extend((
                        u'\n\t            ', 
                        to_string(context.call(l_field)), 
                        u'\n\t        ', 
                    ))
                t_9.append(
                    u'\n\n\t\t\t', 
                )
                if environment.getattr(l_field, 'type') == 'FormField':
                    pass
                    t_9.extend((
                        u'\n\t\t\t\t', 
                        to_string(context.call(l_renderForm, l_field)), 
                        u'\n\t\t\t', 
                    ))
                t_9.append(
                    u'\n\t\t\t\n\t    ', 
                )
            l_field = missing
            t_9.append(
                u'\n\n\t    <ul>\n\t    ', 
            )
            l_field = missing
            for l_field in l_form_object:
                pass
                t_9.append(
                    u'\n\t        ', 
                )
                if environment.getattr(l_field, 'type') != 'HiddenField':
                    pass
                    t_9.extend((
                        u"\n\t            <li><div id='", 
                        to_string(environment.getattr(l_field, 'id')), 
                        u"-box' class='fieldbox'>", 
                        to_string(context.call(l_form_field, l_field)), 
                        u'</div></li>\n\t        ', 
                    ))
                t_9.append(
                    u'\n\t    ', 
                )
            l_field = missing
            t_9.append(
                u'\n\t    </ul>\n\n', 
            )
            if l_omitSubmitButton != True:
                pass
                t_9.append(
                    u"\n\t\t<input type='submit'", 
                )
                if environment.getattr(l_kwargs, 'submit_value'):
                    pass
                    t_9.extend((
                        u" value='", 
                        to_string(environment.getattr(l_kwargs, 'submit_value')), 
                        u"'", 
                    ))
                if environment.getattr(l_kwargs, 'submit_class'):
                    pass
                    t_9.extend((
                        u" class='", 
                        to_string(environment.getattr(l_kwargs, 'submit_class')), 
                        u"'", 
                    ))
                else:
                    pass
                    t_9.append(
                        u" class='spi-submit'", 
                    )
                t_9.append(
                    u'>\n', 
                )
            t_9.append(
                u'\n\n', 
            )
            if l_omitFormTag != True:
                pass
                t_9.append(
                    u'\n</form>\n', 
                )
            t_9.append(
                u'\n\n', 
            )
            if t_2(context.call(environment.getattr(l_form_object, 'get_script_snippet'), 'south')):
                pass
                t_9.append(
                    u"\n<script type='text/javascript'>\n\t", 
                )
                if 0: dummy(l_form_field_boolean, l_form_field_description, l_kwargs, l_input, l_form_field_errors, l_form_field_label, l_form_field)
                template = environment.get_or_select_template(context.call(environment.getattr(l_form_object, 'get_script_snippet'), 'south'), 'source/macros/form.html')
                for event in template.root_render_func(template.new_context(context.parent, True, locals())):
                    t_9.append(event)
                t_9.append(
                    u'\t\n</script>\n', 
                )
            return concat(t_9)
        context.exported_vars.add('renderForm')
        context.vars['renderForm'] = l_renderForm = Macro(environment, macro, 'renderForm', ('form_object', 'omitFormTag', 'omitSubmitButton'), (False, False, ), True, False, False)

    blocks = {}
    debug_info = '1=10&2=15&5=29&6=34&7=38&12=49&13=52&14=56&18=62&19=65&21=71&22=75&28=85&29=89&30=91&31=93&32=95&35=100&37=103&38=107&40=115&41=119&43=127&44=131&46=138&47=141&48=145&50=152&52=157&53=159&61=171&63=174&65=180&69=189&70=193&73=232&75=237&76=241&79=247&80=251&86=262&87=267&88=271&93=283&94=288&97=313&101=321&103=327'
    return locals()