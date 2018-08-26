# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.617571
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/amd64/linux/echo.asm'
_template_uri = 'amd64/linux/echo.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u'Writes a string to a file descriptor'
def render_body(context,string,sock='rbp',**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,sock=sock,string=string)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        from pwnlib.shellcraft import amd64 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['amd64'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        from pwnlib.constants.linux.amd64 import SYS_write 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['SYS_write'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(unicode(amd64.pushstr(string, append_null = False)))
        __M_writer(u'\n')
        __M_writer(unicode(amd64.linux.syscall('SYS_write', sock, 'rsp', len(string))))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"32": 2, "33": 3, "34": 4, "35": 6, "36": 6, "37": 7, "38": 7, "44": 38, "16": 4, "17": 3, "23": 1, "27": 1, "28": 2}, "uri": "amd64/linux/echo.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/amd64/linux/echo.asm"}
__M_END_METADATA
"""
