# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.730404
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/linux/sh.asm'
_template_uri = 'i386/linux/sh.asm'
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
        from pwnlib.constants.linux.i386 import SYS_execve 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['SYS_execve'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(unicode(i386.pushstr('/bin///sh')))
        __M_writer(u'\n\n')
        __M_writer(unicode(i386.linux.syscall('SYS_execve', 'esp', 0, 0)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"32": 3, "33": 5, "34": 5, "35": 7, "36": 7, "42": 36, "16": 3, "17": 0, "22": 1, "26": 1, "27": 2, "31": 2}, "uri": "i386/linux/sh.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/linux/sh.asm"}
__M_END_METADATA
"""
