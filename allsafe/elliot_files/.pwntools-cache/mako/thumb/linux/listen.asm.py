# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.783254
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/thumb/linux/listen.asm'
_template_uri = 'thumb/linux/listen.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u"\n    listen(port,network)\n\n    Listens on a TCP port, accept a client and leave his socket in r6.\n    Port is the TCP port to listen on, network is either 'ipv4' or 'ipv6'.\n"
def render_body(context,port,network='ipv4',**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,port=port,network=network)
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
        __M_writer(u'\n    /* First create listening socket */\n    ')
        __M_writer(unicode(mov('r7', constants.linux.thumb.SYS_socket)))
        __M_writer(u'\n')
        if network == 'ipv4':
            __M_writer(u'    ')
            __M_writer(unicode(mov('r0', constants.linux.thumb.AF_INET)))
            __M_writer(u'\n')
        else:
            __M_writer(u'    ')
            __M_writer(unicode(mov('r0', constants.linux.thumb.AF_INET6)))
            __M_writer(u'\n')
        __M_writer(u'    ')
        __M_writer(unicode(mov('r1', constants.linux.thumb.SOCK_STREAM)))
        __M_writer(u'\n    eor r2, r2\n    svc 1\n\n    /* Save socket in r6 */\n    mov r6, r0\n\n')
        if network == 'ipv4':
            __M_writer(u'    /* Build sockaddr_in structure */\n    /* r2 is zero == INADDR_ANY */\n    /* Put port and address family into r1 */\n    ')
            __M_writer(unicode(mov('r1', ((htons(port) << 16) + constants.linux.thumb.AF_INET))))
            __M_writer(u'\n    push {r1, r2}\n\n    /* Address of sockaddr_in into r1 */\n    mov r1, sp\n\n    /* sizeof(sockaddr_in) into r2 */\n    mov r2, #16\n\n    /* Socket already in r0 */\n    /* r7 is 281 = SYS_socket, add one and it is 282 = SYS_bind */\n    add r7, #1\n    svc 1\n')
        else:
            __M_writer(u'    /* Build sockaddr_in6 structure */\n    /* r2 is already zero */\n    eor r1, r1\n    eor r3, r3\n    push {r1, r2, r3}\n    push {r1, r2, r3}\n    \n    /* Then port = %d */\n    ')
            __M_writer(unicode(mov('r1', (htons(port) << 16) + constants.linux.thumb.AF_INET6)))
            __M_writer(u'\n    push {r1, r2, r3}\n\n    /* Address of sockaddr_in6 into r1 */\n    mov r1, sp\n\n    /* sizeof(sockaddr_in6) into r2 */\n    mov r2, #28\n\n    /* Socket already in r0 */\n    /* r7 is 281 = SYS_socket, add one and it is 282 = SYS_bind */\n    add r7, #1\n    svc 1\n')
        __M_writer(u'\n    /* Server socket from r6 into r0 */\n    mov r0, r6\n\n    /* Backlog */\n    mov r1, #1\n\n    /* r7 = SYS_listen = 284 */\n    /* r7 is already = 282 so just add two */\n    add r7, #2\n    svc 1\n\n    /* Server socket from r6 into r0 */\n    mov r0, r6\n\n    /* Other args are null */\n    eor r1, r1\n    eor r2, r2\n\n    /* r7 = SYS_accept = 285 */\n    /* r7 is already = 284 so just add one */\n    add r7, #1\n    svc 1\n\n    /* Move accepted socket to r6 */\n    mov r6, r0\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 5, "17": 4, "22": 1, "26": 1, "27": 2, "31": 2, "32": 3, "36": 3, "37": 4, "38": 10, "39": 12, "40": 12, "41": 13, "42": 14, "43": 14, "44": 14, "45": 15, "46": 16, "47": 16, "48": 16, "49": 18, "50": 18, "51": 18, "52": 25, "53": 26, "54": 29, "55": 29, "56": 42, "57": 43, "58": 51, "59": 51, "60": 65, "66": 60}, "uri": "thumb/linux/listen.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/thumb/linux/listen.asm"}
__M_END_METADATA
"""
