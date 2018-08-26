# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.698612
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/linux/acceptloop_ipv4.asm'
_template_uri = 'i386/linux/acceptloop_ipv4.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u'\n    Args: port\n    Waits for a connection.  Leaves socket in EBP.\n    ipv4 only\n'
def render_body(context,port,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,port=port)
        int = context.get('int', UNDEFINED)
        i386 = context.get('i386', UNDEFINED)
        __M_writer = context.writer()
        from pwnlib.shellcraft import common 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['common'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        from pwnlib.constants.linux import i386 as constants 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['constants'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        from pwnlib.util.packing import make_packer 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['make_packer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        from socket import htons 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['htons'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')

        acceptloop = common.label("acceptloop")
        looplabel = common.label("loop")
        p16  = make_packer(16, 'little', 'unsigned')
        p16b = make_packer(16, 'big', 'unsigned')
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['acceptloop','p16b','looplabel','p16'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        __M_writer(unicode(acceptloop))
        __M_writer(u':\n        /*  Listens for and accepts a connection on ')
        __M_writer(unicode(int(port)))
        __M_writer(u'd forever */\n        /*  Socket file descriptor is placed in EBP */\n\n        /*  sock = socket(AF_INET, SOCK_STREAM, 0) */\n        ')
        __M_writer(unicode(i386.mov('eax', constants.SYS_socketcall)))
        __M_writer(u'\n        ')
        __M_writer(unicode(i386.mov('ebx', constants.SYS_socketcall_socket)))
        __M_writer(u'\n        cdq                     /*  clear EDX */\n        push edx                /*  IPPROTO_IP (= 0) */\n        push ebx                /*  SOCK_STREAM */\n        push AF_INET\n        ')
        __M_writer(unicode(i386.linux.syscall('eax', 'ebx', 'esp')))
        __M_writer(u'\n\n        /*  bind(sock, &addr, sizeof addr); // sizeof addr == 0x10 */\n        push edx\n        ')
        __M_writer(unicode(i386.pushstr(p16(constants.AF_INET) + p16b(int(port)))))
        __M_writer(u'\n        mov ecx, esp\n        push 0x10\n        push ecx\n        push eax\n        mov ecx, esp\n        mov esi, eax\n        inc ebx                 /*  EBX = bind (= 2) */\n        mov al, byte SYS_socketcall\n        int 0x80\n\n        /*  listen(sock, whatever) */\n        mov al, byte SYS_socketcall\n        mov bl, byte SYS_socketcall_listen\n        int 0x80\n\n\n')
        __M_writer(unicode(looplabel))
        __M_writer(u':\n        /*  accept(sock, NULL, NULL) */\n        push edx\n        push esi                /*  sock */\n        mov ecx, esp\n        mov al, byte SYS_socketcall\n        mov bl, byte SYS_socketcall_accept\n        int 0x80\n\n        mov ebp, eax\n\n        mov al, SYS_fork\n        int 0x80\n        xchg eax, edi\n\n        test edi, edi\n        mov ebx, ebp\n        cmovz ebx, esi /*  on child we close the server sock instead */\n\n        /*  close(sock) */\n        ')
        __M_writer(unicode(i386.linux.syscall('SYS_close', 'ebx')))
        __M_writer(u'\n\n        test edi, edi\n        jnz ')
        __M_writer(unicode(looplabel))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 6, "17": 5, "24": 1, "28": 1, "29": 2, "33": 2, "34": 3, "38": 3, "39": 4, "43": 4, "44": 5, "45": 10, "46": 11, "55": 16, "56": 18, "57": 18, "58": 19, "59": 19, "60": 23, "61": 23, "62": 24, "63": 24, "64": 29, "65": 29, "66": 33, "67": 33, "68": 50, "69": 50, "70": 70, "71": 70, "72": 73, "73": 73, "79": 73}, "uri": "i386/linux/acceptloop_ipv4.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/linux/acceptloop_ipv4.asm"}
__M_END_METADATA
"""
