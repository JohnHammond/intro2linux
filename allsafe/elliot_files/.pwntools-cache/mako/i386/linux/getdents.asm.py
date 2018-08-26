# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.717375
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/linux/getdents.asm'
_template_uri = 'i386/linux/getdents.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u" Reads to the stack from a directory.\n\nArgs:\n    in_fd (int/str): File descriptor to be read from.\n    size (int): Buffer size.\n    allocate_stack (bool): allocate 'size' bytes on the stack.\n\nYou can optioanlly shave a few bytes not allocating the stack space.\n\nThe size read is left in eax.\n"
def render_body(context,in_fd='ebp',size=255,allocate_stack=True,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,in_fd=in_fd,allocate_stack=allocate_stack,size=size)
        __M_writer = context.writer()
        from pwnlib.shellcraft import i386 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['i386'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n  ')
        __M_writer(unicode(i386.mov('ebx', in_fd)))
        __M_writer(u'\n  xor eax, eax\n  mov al, SYS_getdents\n  cdq\n  ')
        __M_writer(unicode(i386.mov('dl', size)))
        __M_writer(u'\n')
        if allocate_stack:
            __M_writer(u'  sub esp, edx\n')
        __M_writer(u'  mov ecx, esp\n  int 0x80\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"32": 18, "33": 19, "34": 20, "35": 22, "41": 35, "16": 3, "17": 2, "22": 1, "26": 1, "27": 2, "28": 13, "29": 14, "30": 14, "31": 18}, "uri": "i386/linux/getdents.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/linux/getdents.asm"}
__M_END_METADATA
"""
