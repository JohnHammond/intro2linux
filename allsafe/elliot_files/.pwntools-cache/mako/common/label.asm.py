# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1479426012.480522
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/common/label.asm'
_template_uri = 'common/label.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u'\nReturns a new unique label with a given prefix.\n\nArgs:\n  prefix (str): The string to prefix the label with\n'

label_num = 0


def render_body(context,prefix='label',**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(prefix=prefix,pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')

        global label_num
        label_num += 1
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['label_num'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(unicode(prefix))
        __M_writer(u'_')
        __M_writer(unicode(label_num))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"36": 14, "37": 15, "38": 15, "39": 15, "40": 15, "46": 40, "16": 2, "17": 8, "21": 1, "26": 1, "27": 7, "28": 10, "29": 11}, "uri": "common/label.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/common/label.asm"}
__M_END_METADATA
"""
