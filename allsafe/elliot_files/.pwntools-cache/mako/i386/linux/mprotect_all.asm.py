# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.722395
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/linux/mprotect_all.asm'
_template_uri = 'i386/linux/mprotect_all.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u'Calls mprotect(page, 4096, PROT_READ | PROT_WRITE | PROT_EXEC) for every page.\n\nIt takes around 0.3 seconds on my box, but your milage may vary.\n\nArgs:\n  clear_ebx(bool): If this is set to False, then the shellcode will assume that ebx has already been zeroed.\n  fix_null(bool): If this is set to True, then the NULL-page will also be mprotected at the cost of slightly larger shellcode\n'
def render_body(context,clear_ebx=True,fix_null=False,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(clear_ebx=clear_ebx,pageargs=pageargs,fix_null=fix_null)
        __M_writer = context.writer()
        from pwnlib.shellcraft import common 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['common'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        label = common.label("mprotect_loop") 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['label'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        if clear_ebx:
            __M_writer(u'    xor ebx, ebx\n')
        if fix_null:
            __M_writer(u'    xor ecx, ecx\n')
        __M_writer(unicode(label))
        __M_writer(u':\n    push PROT_READ | PROT_WRITE | PROT_EXEC\n    pop edx\n    push SYS_mprotect\n    pop eax\n    int 0x80\n    xor ecx, ecx\n    mov ch, 0x10\n    add ebx, ecx\n    jnz ')
        __M_writer(unicode(label))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"33": 11, "34": 13, "35": 14, "36": 16, "37": 17, "38": 19, "39": 19, "40": 28, "41": 28, "47": 41, "16": 3, "17": 2, "22": 1, "26": 1, "27": 2, "28": 10, "29": 11}, "uri": "i386/linux/mprotect_all.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/linux/mprotect_all.asm"}
__M_END_METADATA
"""
