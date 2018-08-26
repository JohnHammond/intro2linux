# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.779465
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/thumb/linux/findpeersh.asm'
_template_uri = 'thumb/linux/findpeersh.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u'\n    findpeersh(port)\n\n    Finds a connected socket. If port is specified it is checked\n    against the peer port. A dup2 shell is spawned on it.\n'
def render_body(context,port=None,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,port=port)
        __M_writer = context.writer()
        from pwnlib.shellcraft.thumb.linux import findpeer, dupsh 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['findpeer','dupsh'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(unicode(findpeer(port)))
        __M_writer(u'\n')
        __M_writer(unicode(dupsh()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"32": 10, "38": 32, "16": 3, "17": 2, "22": 1, "26": 1, "27": 2, "28": 8, "29": 9, "30": 9, "31": 10}, "uri": "thumb/linux/findpeersh.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/thumb/linux/findpeersh.asm"}
__M_END_METADATA
"""
