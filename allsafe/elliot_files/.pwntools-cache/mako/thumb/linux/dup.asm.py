# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.772003
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/thumb/linux/dup.asm'
_template_uri = 'thumb/linux/dup.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u'\nArgs: [sock (imm/reg) = r6]\n    Duplicates sock to stdin, stdout and stderr\n'
def render_body(context,sock='r6',**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,sock=sock)
        __M_writer = context.writer()
        from pwnlib.shellcraft import common 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['common'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        from pwnlib.shellcraft.thumb import mov 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['mov'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')

        dup       = common.label("dup")
        looplabel = common.label("loop")
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['dup','looplabel'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(unicode(dup))
        __M_writer(u':\n        ')
        __M_writer(unicode(mov('r1', 2)))
        __M_writer(u'\n        ')
        __M_writer(unicode(mov('r7', 'SYS_dup2')))
        __M_writer(u'\n\n')
        __M_writer(unicode(looplabel))
        __M_writer(u':\n        ')
        __M_writer(unicode(mov('r0', sock)))
        __M_writer(u'\n        svc 1\n        subs r1, #1\n        bpl ')
        __M_writer(unicode(looplabel))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 4, "17": 3, "22": 1, "26": 1, "27": 2, "31": 2, "32": 3, "33": 7, "34": 8, "41": 11, "42": 12, "43": 12, "44": 13, "45": 13, "46": 14, "47": 14, "48": 16, "49": 16, "50": 17, "51": 17, "52": 20, "53": 20, "59": 53}, "uri": "thumb/linux/dup.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/thumb/linux/dup.asm"}
__M_END_METADATA
"""
