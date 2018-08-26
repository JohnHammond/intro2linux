# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473984793.144923
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/linux/read.asm'
_template_uri = 'i386/linux/read.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u"\nInvokes the syscall read.  See 'man 2 read' for more information.\n\nArguments:\n    fd(int): fd\n    buf(void): buf\n    nbytes(size_t): nbytes\n"
def render_body(context,fd,buf,nbytes,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(buf=buf,pageargs=pageargs,fd=fd,nbytes=nbytes)
        __M_writer = context.writer()
        __M_writer(u'\n')

        from pwnlib.shellcraft.i386.linux import syscall
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['syscall'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n    ')
        __M_writer(unicode(syscall('SYS_read', fd, buf, nbytes)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"32": 15, "33": 15, "39": 33, "16": 6, "17": 5, "22": 1, "23": 2, "29": 4, "30": 5, "31": 13}, "uri": "i386/linux/read.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/linux/read.asm"}
__M_END_METADATA
"""
