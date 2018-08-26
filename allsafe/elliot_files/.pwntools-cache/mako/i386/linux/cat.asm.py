# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1479426009.704954
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/linux/cat.asm'
_template_uri = 'i386/linux/cat.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u"\nOpens a file and writes its contents to the specified file descriptor.\n\nExample:\n\n    >>> f = tempfile.mktemp()\n    >>> write(f, 'FLAG')\n    >>> run_assembly(shellcraft.i386.linux.cat(f)).recvall()\n    'FLAG'\n\n"
def render_body(context,filename,fd=1,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,fd=fd,filename=filename)
        __M_writer = context.writer()

        from pwnlib.shellcraft import i386
        from pwnlib.shellcraft import common
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['i386','common'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')

        label = common.label("sendfile_loop")
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['label'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n    ')
        __M_writer(unicode(i386.pushstr(filename)))
        __M_writer(u'\n    ')
        __M_writer(unicode(i386.syscall('SYS_open', 'esp', 0, 'O_RDONLY')))
        __M_writer(u'\n    ')
        __M_writer(unicode(i386.syscall('SYS_sendfile', fd, 'eax', 0, 0x7fffffff)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"32": 17, "38": 19, "39": 21, "40": 21, "41": 22, "42": 22, "43": 23, "44": 23, "16": 6, "17": 5, "50": 44, "22": 1, "29": 4, "30": 5, "31": 16}, "uri": "i386/linux/cat.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/linux/cat.asm"}
__M_END_METADATA
"""
