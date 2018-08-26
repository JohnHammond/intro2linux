# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.715066
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/linux/findpeerstager.asm'
_template_uri = 'i386/linux/findpeerstager.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u'\nFindpeer + stager\nArgs:\n    size, the size of the payload\n    port, the port given to findpeer (defaults to any)\n'
def render_body(context,size,port=None,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,port=port,size=size)
        __M_writer = context.writer()
        from pwnlib.shellcraft import common 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['common'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        from pwnlib.shellcraft.i386 import linux 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['linux'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')
        __M_writer(unicode(linux.findpeer(port)))
        __M_writer(u'\n')
        __M_writer(unicode(linux.stager("esi", size)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"32": 8, "33": 9, "34": 11, "35": 11, "36": 12, "37": 12, "43": 37, "16": 3, "17": 9, "22": 1, "26": 1, "27": 2, "31": 2}, "uri": "i386/linux/findpeerstager.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/linux/findpeerstager.asm"}
__M_END_METADATA
"""
