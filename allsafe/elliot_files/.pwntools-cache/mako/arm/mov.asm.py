# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.637552
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/arm/mov.asm'
_template_uri = 'arm/mov.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u'\n    mov(dst, src)\n\n    Returns THUMB code for moving the specified source value\n    into the specified destination register.\n'
def render_body(context,dst,src,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(src=src,dst=dst,pageargs=pageargs)
        int = context.get('int', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        long = context.get('long', UNDEFINED)
        __M_writer = context.writer()
        from pwnlib.shellcraft import common 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['common'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n/* Set ')
        __M_writer(unicode(dst))
        __M_writer(u' = ')
        __M_writer(unicode(src))
        __M_writer(u' = 0x')
        __M_writer(unicode('%x' % src))
        __M_writer(u' */\n')
        if not isinstance(src, (int, long)):
            __M_writer(u'    mov ')
            __M_writer(unicode(dst))
            __M_writer(u', ')
            __M_writer(unicode(src))
            __M_writer(u'\n')
        else:
            if src == 0:
                __M_writer(u'    eor ')
                __M_writer(unicode(dst))
                __M_writer(u', ')
                __M_writer(unicode(dst))
                __M_writer(u'\n')
            elif src & 0xffff0000 == 0:
                __M_writer(u'    mov ')
                __M_writer(unicode(dst))
                __M_writer(u', #')
                __M_writer(unicode(src))
                __M_writer(u'\n')
            else:
                __M_writer(u'    movw ')
                __M_writer(unicode(dst))
                __M_writer(u', #')
                __M_writer(unicode(src & 0xffff))
                __M_writer(u'\n    movt ')
                __M_writer(unicode(dst))
                __M_writer(u', #')
                __M_writer(unicode(src >> 16))
                __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 3, "17": 2, "25": 1, "29": 1, "30": 2, "31": 8, "32": 9, "33": 9, "34": 9, "35": 9, "36": 9, "37": 9, "38": 10, "39": 11, "40": 11, "41": 11, "42": 11, "43": 11, "44": 12, "45": 13, "46": 14, "47": 14, "48": 14, "49": 14, "50": 14, "51": 15, "52": 16, "53": 16, "54": 16, "55": 16, "56": 16, "57": 17, "58": 18, "59": 18, "60": 18, "61": 18, "62": 18, "63": 19, "64": 19, "65": 19, "66": 19, "72": 66}, "uri": "arm/mov.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/arm/mov.asm"}
__M_END_METADATA
"""
