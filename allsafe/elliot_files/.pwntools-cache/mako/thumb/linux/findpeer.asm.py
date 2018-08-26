# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.777119
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/thumb/linux/findpeer.asm'
_template_uri = 'thumb/linux/findpeer.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u'\n    findpeer(port)\n\n    Finds a connected socket. If port is specified it is checked\n    against the peer port. Resulting socket is left in r6.\n'
def render_body(context,port=None,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,port=port)
        int = context.get('int', UNDEFINED)
        __M_writer = context.writer()
        from pwnlib.shellcraft.thumb import mov 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['mov'] if __M_key in __M_locals_builtin_stored]))
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
        __M_writer(u'\nfindpeer:\n    /* File descriptor in r6 */\n    /* Inside the loop we begin by incrementing it */\n    /* so initially we want it to be -1 */\n    ')
        __M_writer(unicode(mov('r6', -1)))
        __M_writer(u'\n    /* Let us restore stack easily */\n    mov lr, sp\n\nnext_socket:\n    /* Next file descriptor */\n    add r6, #1\n\n    ')
        __M_writer(unicode(mov('r7', constants.linux.thumb.SYS_getpeername)))
        __M_writer(u'\n\n    /* Reset stack */\n    mov sp, lr\n\n    /* First argument is file descriptor */\n    mov r0, r6\n\n    /* Make room on stack - inet addr structure is 16 bytes and size of addr is four bytes */\n    /* First four bytes will be the size of the address, the remaining 16 bytes will be */\n    /* the address structure */\n    push {r0, r1, r2, r3, r4}\n\n    /* Second argument is pointer to where to store inet addr */\n    add r1, sp, #4\n\n    /* Third argument is pointer to size */\n    mov r2, sp\n\n    /* Now issue system call */\n    svc 1\n\n    /* If the syscall returned -1 this was a bad socket */\n    /* so move on to the next one */\n    /* Testing on r0 has nul bytes but moving to r1 achieves the same */\n    cmp r0, #0\n    bne next_socket\n')
        if not port is None:
            __M_writer(u'\ncompare_port:\n    /* Read the port into r0 */\n    ldr r1, [sp, #4]\n    lsr r1, #16\n\n    /* Put the port (')
            __M_writer(unicode(port))
            __M_writer(u') to search for into r1 */\n    ')
            __M_writer(unicode(mov('r2', htons(int(port)))))
            __M_writer(u'\n\n    /* Is it the one we have been searching for? */\n    cmp r1, r2\n    \n    /* If not try the next one */\n    bne next_socket\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"32": 2, "33": 3, "48": 58, "37": 3, "38": 4, "39": 10, "40": 15, "41": 15, "42": 23, "43": 23, "44": 50, "45": 51, "46": 57, "47": 57, "16": 5, "17": 4, "23": 1, "55": 49, "49": 58, "27": 1, "28": 2}, "uri": "thumb/linux/findpeer.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/thumb/linux/findpeer.asm"}
__M_END_METADATA
"""
