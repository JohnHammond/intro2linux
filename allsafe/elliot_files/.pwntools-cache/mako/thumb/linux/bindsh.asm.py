# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.76906
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/thumb/linux/bindsh.asm'
_template_uri = 'thumb/linux/bindsh.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u"\n    bindsh(port,network)\n\n    Listens on a TCP port and spawns a shell for the first to connect.\n    Port is the TCP port to listen on, network is either 'ipv4' or 'ipv6'.\n"
def render_body(context,port,network='ipv4',**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,port=port,network=network)
        __M_writer = context.writer()
        from pwnlib.shellcraft.thumb.linux import listen, dupsh
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['dupsh','listen'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        from pwnlib import constants 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['constants'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        from socket import htons 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['htons'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(unicode(listen(port, network)))
        __M_writer(u'\n')
        __M_writer(unicode(dupsh()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"32": 3, "48": 42, "36": 3, "37": 4, "38": 10, "39": 11, "40": 11, "41": 12, "42": 12, "16": 5, "17": 4, "22": 1, "26": 1, "27": 2, "31": 2}, "uri": "thumb/linux/bindsh.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/thumb/linux/bindsh.asm"}
__M_END_METADATA
"""
