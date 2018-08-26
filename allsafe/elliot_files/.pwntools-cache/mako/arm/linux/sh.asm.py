# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.653394
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/arm/linux/sh.asm'
_template_uri = 'arm/linux/sh.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u'Execute /bin/sh'
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'\n\n    adr r0, bin_sh\n    mov r2, #0\n    push {r0, r2}\n    mov r1, sp\n    svc SYS_execve\n    bin_sh: .asciz "/bin/sh"\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 1, "17": 0, "28": 22, "22": 1}, "uri": "arm/linux/sh.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/arm/linux/sh.asm"}
__M_END_METADATA
"""
