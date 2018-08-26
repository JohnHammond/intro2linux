# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.728143
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/linux/setreuid.asm'
_template_uri = 'i386/linux/setreuid.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u'\nArgs: [uid (imm/reg) = euid]\n    Sets the real and effective user id.\n'
def render_body(context,uid='euid',**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,uid=uid)
        __M_writer = context.writer()
        from pwnlib.shellcraft import i386 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['i386'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        if uid == 'euid':
            __M_writer(u'    /*  geteuid */\n    ')
            __M_writer(unicode(i386.linux.syscall('SYS_geteuid')))
            __M_writer(u'\n    ')
            __M_writer(unicode(i386.mov('ebx', 'eax')))
            __M_writer(u'\n')
        else:
            __M_writer(u'    ')
            __M_writer(unicode(i386.mov('ebx', uid)))
            __M_writer(u'\n')
        __M_writer(u'\n    /*  setreuid(eax, eax) */\n    ')
        __M_writer(unicode(i386.syscall('SYS_setreuid', 'ebx', 'ebx')))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"32": 10, "33": 11, "34": 11, "35": 12, "36": 13, "37": 13, "38": 13, "39": 15, "40": 17, "41": 17, "47": 41, "16": 3, "17": 2, "22": 1, "26": 1, "27": 2, "28": 6, "29": 8, "30": 9, "31": 10}, "uri": "i386/linux/setreuid.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/linux/setreuid.asm"}
__M_END_METADATA
"""
