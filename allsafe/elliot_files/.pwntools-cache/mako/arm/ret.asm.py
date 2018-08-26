# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.641544
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/arm/ret.asm'
_template_uri = 'arm/ret.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u"A single-byte RET instruction.\n\nArgs:\n    return_value: Value to return\n\nExamples:\n    >>> with context.local(arch='arm'):\n    ...     print enhex(asm(shellcraft.ret()))\n    ...     print enhex(asm(shellcraft.ret(0)))\n    ...     print enhex(asm(shellcraft.ret(0xdeadbeef)))\n    1eff2fe1\n    000020e01eff2fe1\n    ef0e0be3ad0e4de31eff2fe1\n"
def render_body(context,return_value=None,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,return_value=return_value)
        __M_writer = context.writer()
        from pwnlib.shellcraft import arm 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['arm'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if return_value != None:
            __M_writer(u'    ')
            __M_writer(unicode(arm.mov('r0', return_value)))
            __M_writer(u'\n')
        __M_writer(u'\n    bx lr\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"32": 19, "33": 21, "39": 33, "16": 2, "17": 16, "22": 1, "26": 1, "27": 15, "28": 16, "29": 18, "30": 19, "31": 19}, "uri": "arm/ret.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/arm/ret.asm"}
__M_END_METADATA
"""
