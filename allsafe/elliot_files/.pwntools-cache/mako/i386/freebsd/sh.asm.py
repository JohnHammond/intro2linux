# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.694609
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/freebsd/sh.asm'
_template_uri = 'i386/freebsd/sh.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u'Execute /bin/sh'
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        from pwnlib.shellcraft import i386 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['i386'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u"\n\n\n    /*  Clear eax, ecx, edx */\n    xor eax, eax\n    push eax\n\n    /*  Push '/bin//sh' */\n")
        __M_writer(unicode(i386.pushstr("/bin//sh")))
        __M_writer(u'\n    mov ecx, esp\n\n    /*  execve("/bin//sh", {junk, 0}, {0}); */\n    push eax\n    push esp\n    push esp\n    push ecx\n    push eax\n    mov al, SYS_execve\n    int 0x80\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"35": 29, "16": 2, "17": 0, "22": 1, "26": 1, "27": 2, "28": 10, "29": 10}, "uri": "i386/freebsd/sh.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/freebsd/sh.asm"}
__M_END_METADATA
"""
