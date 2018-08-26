# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.612633
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/amd64/linux/dup.asm'
_template_uri = 'amd64/linux/dup.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u'\nArgs: [sock (imm/reg) = rbp]\n    Duplicates sock to stdin, stdout and stderr\n'
def render_body(context,sock='rbp',**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,sock=sock)
        __M_writer = context.writer()
        from pwnlib.shellcraft import common, amd64 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['common','amd64'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')

        dup       = common.label("dup")
        looplabel = common.label("loop")
        after     = common.label("after")
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['dup','after','looplabel'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n\n')
        __M_writer(unicode(dup))
        __M_writer(u':\n    ')
        __M_writer(unicode(amd64.mov('rbp', sock)))
        __M_writer(u'\n\n    push 3\n')
        __M_writer(unicode(looplabel))
        __M_writer(u':\n    pop rsi\n    dec rsi\n    js ')
        __M_writer(unicode(after))
        __M_writer(u'\n    push rsi\n\n    ')
        __M_writer(unicode(amd64.linux.syscall('SYS_dup2', 'rbp', 'rsi')))
        __M_writer(u'\n\n    jmp ')
        __M_writer(unicode(looplabel))
        __M_writer(u'\n')
        __M_writer(unicode(after))
        __M_writer(u':\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 3, "17": 2, "22": 1, "26": 1, "27": 2, "28": 6, "29": 7, "37": 11, "38": 14, "39": 14, "40": 15, "41": 15, "42": 18, "43": 18, "44": 21, "45": 21, "46": 24, "47": 24, "48": 26, "49": 26, "50": 27, "51": 27, "57": 51}, "uri": "amd64/linux/dup.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/amd64/linux/dup.asm"}
__M_END_METADATA
"""
