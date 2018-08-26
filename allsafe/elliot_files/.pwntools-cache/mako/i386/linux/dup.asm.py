# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.702357
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/linux/dup.asm'
_template_uri = 'i386/linux/dup.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u'\nArgs: [sock (imm/reg) = ebp]\n    Duplicates sock to stdin, stdout and stderr\n'
def render_body(context,sock='ebp',**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,sock=sock)
        __M_writer = context.writer()
        from pwnlib.shellcraft import i386 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['i386'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        from pwnlib.shellcraft import common 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['common'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')

        dup       = common.label("dup")
        looplabel = common.label("loop")
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['dup','looplabel'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        __M_writer(unicode(dup))
        __M_writer(u':\n    ')
        __M_writer(unicode(i386.mov('ebx', sock)))
        __M_writer(u'\n    ')
        __M_writer(unicode(i386.mov('ecx', 3)))
        __M_writer(u'\n')
        __M_writer(unicode(looplabel))
        __M_writer(u':\n    dec ecx\n\n    ')
        __M_writer(unicode(i386.linux.syscall('SYS_dup2', 'ebx', 'ecx')))
        __M_writer(u'\n    jnz ')
        __M_writer(unicode(looplabel))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 4, "17": 3, "22": 1, "26": 1, "27": 2, "31": 2, "32": 3, "33": 7, "34": 8, "41": 11, "42": 13, "43": 13, "44": 14, "45": 14, "46": 15, "47": 15, "48": 16, "49": 16, "50": 19, "51": 19, "52": 20, "53": 20, "59": 53}, "uri": "i386/linux/dup.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/linux/dup.asm"}
__M_END_METADATA
"""
