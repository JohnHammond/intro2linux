# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.692689
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/freebsd/i386_to_amd64.asm'
_template_uri = 'i386/freebsd/i386_to_amd64.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u'Returns code to switch from i386 to amd64 mode.'
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        from pwnlib.shellcraft import common 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['common'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        helper, end = common.label("helper"), common.label("end") 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['end','helper'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n.code32\n    push 0x43 /*  This is the segment we want to go to */\n    call $+4\n')
        __M_writer(unicode(helper))
        __M_writer(u':\n    .byte 0xc0\n    add dword ptr [esp], ')
        __M_writer(unicode(end))
        __M_writer(u' - ')
        __M_writer(unicode(helper))
        __M_writer(u'\n    jmp far [esp]\n')
        __M_writer(unicode(end))
        __M_writer(u':\n.code64\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"32": 3, "33": 7, "34": 7, "35": 9, "36": 9, "37": 9, "38": 9, "39": 11, "40": 11, "46": 40, "16": 2, "17": 0, "22": 1, "26": 1, "27": 2, "28": 3}, "uri": "i386/freebsd/i386_to_amd64.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/freebsd/i386_to_amd64.asm"}
__M_END_METADATA
"""
