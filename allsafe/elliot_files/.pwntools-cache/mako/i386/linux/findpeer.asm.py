# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.710193
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/linux/findpeer.asm'
_template_uri = 'i386/linux/findpeer.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u'\nArgs: port (defaults to any port)\n    Finds a socket, which is connected to the specified port.\n    Leaves socket in ESI.\n'
def render_body(context,port=None,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,port=port)
        int = context.get('int', UNDEFINED)
        __M_writer = context.writer()
        from pwnlib.shellcraft import common 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['common'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        from socket import htons 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['htons'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')

        findpeer = common.label("findpeer")
        looplabel = common.label("loop")
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['findpeer','looplabel'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(unicode(findpeer))
        __M_writer(u':\n    push -1\n    push SYS_socketcall_getpeername\n    mov ebp, esp\n    pop ebx\n    pop esi\n\n')
        __M_writer(unicode(looplabel))
        __M_writer(u':\n    push SYS_socketcall\n    pop eax\n\n    inc esi\n    lea ecx, [esp-32]\n\n    push 4\n    pushad\n\n    int 0x80\n')
        if port == None:
            __M_writer(u'    test eax, eax\n    popad\n    pop edx\n    jnz ')
            __M_writer(unicode(looplabel))
            __M_writer(u'\n')
        else:
            __M_writer(u'    popad\n    pop edx\n    shr eax, 16\n    cmp ax, ')
            __M_writer(unicode(htons(int(port))))
            __M_writer(u'\n    jne ')
            __M_writer(unicode(looplabel))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 4, "17": 3, "23": 1, "27": 1, "28": 2, "32": 2, "33": 3, "34": 8, "35": 9, "42": 12, "43": 13, "44": 13, "45": 20, "46": 20, "47": 31, "48": 32, "49": 35, "50": 35, "51": 36, "52": 37, "53": 40, "54": 40, "55": 41, "56": 41, "62": 56}, "uri": "i386/linux/findpeer.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/linux/findpeer.asm"}
__M_END_METADATA
"""
