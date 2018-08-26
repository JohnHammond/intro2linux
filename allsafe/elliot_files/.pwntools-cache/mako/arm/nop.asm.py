# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.639849
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/arm/nop.asm'
_template_uri = 'arm/nop.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u'A nop instruction.'
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n    orr r1, r1, r1\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 1, "17": 0, "28": 22, "22": 1}, "uri": "arm/nop.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/arm/nop.asm"}
__M_END_METADATA
"""
