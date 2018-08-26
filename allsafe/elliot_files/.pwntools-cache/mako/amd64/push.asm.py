# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.598552
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/amd64/push.asm'
_template_uri = 'amd64/push.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u'\nPushes a value onto the stack without using\nnull bytes or newline characters.\n\nArgs:\n  value (int,str): The value or register to push\n'
def render_body(context,value,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,value=value)
        int = context.get('int', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        repr = context.get('repr', UNDEFINED)
        long = context.get('long', UNDEFINED)
        __M_writer = context.writer()
        from pwnlib.util import packing 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['packing'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        from pwnlib.shellcraft import amd64 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['amd64'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        import re 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['re'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if isinstance(value, (int,long)):
            __M_writer(u'    /* push ')
            __M_writer(unicode(repr(value)))
            __M_writer(u' */\n    ')
            __M_writer(unicode(re.sub(r'^\s*/.*\n', '', amd64.pushstr(packing.pack(value, 64, 'little', True), False), 1)))
            __M_writer(u'\n')
        else:
            __M_writer(u'    push ')
            __M_writer(unicode(value))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"48": 15, "35": 2, "36": 3, "49": 16, "40": 3, "41": 4, "42": 11, "43": 13, "44": 14, "45": 14, "46": 14, "47": 15, "16": 5, "17": 4, "50": 17, "51": 17, "52": 17, "26": 1, "58": 52, "30": 1, "31": 2}, "uri": "amd64/push.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/amd64/push.asm"}
__M_END_METADATA
"""
