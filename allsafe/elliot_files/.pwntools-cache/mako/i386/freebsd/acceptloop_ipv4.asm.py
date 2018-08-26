# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.689904
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/freebsd/acceptloop_ipv4.asm'
_template_uri = 'i386/freebsd/acceptloop_ipv4.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u'\n    Args: port\n    Waits for a connection.  Leaves socket in EBP.\n    ipv4 only\n'
def render_body(context,port,**pageargs):
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
        acceptloop = common.label("acceptloop")
        accept = common.label("accept")
        parent = common.label("parent")
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['acceptloop','parent','accept'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        __M_writer(unicode(acceptloop))
        __M_writer(u':\n        /*  Listens for and accepts a connection on ')
        __M_writer(unicode(int(port)))
        __M_writer(u'd forever */\n        /*  Socket file descriptor is placed in EBP */\n\n        /*  servfd = socket(AF_INET, SOCK_STREAM, 0) */\n        push SYS_socket\n        pop eax\n        cdq\n        push edx\n        push SOCK_STREAM\n        push AF_INET\n        push edx\n        int 0x80\n\n        /*  bind(servfd, &addr, sizeof addr); // sizeof addr == 0x10 */\n        pushw ')
        __M_writer(unicode(htons(int(port))))
        __M_writer(u'\n        pushw AF_INET\n        mov ebx, esp\n        push 0x10\n        push ebx\n        push eax\n        push eax\n        mov al, SYS_bind\n        int 0x80\n\n        /*  listen(servfd, whatever) */\n        mov al, SYS_listen\n        int 0x80\n\n        /*  sockfd = accept(servfd, NULL, whatever) */\n        pop ebx\n')
        __M_writer(unicode(accept))
        __M_writer(u':\n        push edx\n        push ebx\n        push ebx\n        mov al, SYS_accept\n        int 0x80\n\n        /*  fork() */\n        push eax\n        mov al, SYS_fork\n        int 0x80\n\n        /*  close(is_parent ? sockfd : servfd) */\n        test eax, eax\n        jnz ')
        __M_writer(unicode(parent))
        __M_writer(u'\n        pop ebp\n\n')
        __M_writer(unicode(parent))
        __M_writer(u':\n        push eax\n        push SYS_close\n        pop eax\n        int 0x80\n\n        /*  if(is_parent) goto .accept */\n        pop ecx\n        test ecx, ecx\n        jnz ')
        __M_writer(unicode(accept))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 4, "17": 3, "23": 1, "27": 1, "28": 2, "32": 2, "33": 3, "34": 8, "35": 9, "42": 12, "43": 14, "44": 14, "45": 15, "46": 15, "47": 29, "48": 29, "49": 45, "50": 45, "51": 59, "52": 59, "53": 62, "54": 62, "55": 71, "56": 71, "62": 56}, "uri": "i386/freebsd/acceptloop_ipv4.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/freebsd/acceptloop_ipv4.asm"}
__M_END_METADATA
"""
