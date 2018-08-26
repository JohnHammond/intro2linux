# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.685125
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/stackhunter.asm'
_template_uri = 'i386/stackhunter.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u"\n    stackhunter(cookie = 0x7afceb58)\n\n    Returns an an egghunter, which searches from esp and upwards\n    for a cookie. However to save bytes, it only looks at a single\n    4-byte alignment. Use the function stackhunter_helper to\n    generate a suitable cookie prefix for you.\n\n    The default cookie has been chosen, because it makes it possible\n    to shave a single byte, but other cookies can be used too.\n\nExample:\n\n    >>> with context.local():\n    ...    context.arch = 'i386'\n    ...    print enhex(asm(shellcraft.stackhunter()))\n    3d58ebfc7a75faffe4\n    >>> with context.local():\n    ...    context.arch = 'i386'\n    ...    print enhex(asm(shellcraft.stackhunter(0xdeadbeef)))\n    583defbeadde75f8ffe4\n"
def render_body(context,cookie=2063395672,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,cookie=cookie)
        hex = context.get('hex', UNDEFINED)
        __M_writer = context.writer()
        from pwnlib.shellcraft import common 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['common'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')
        stackhunter = common.label("stackhunter") 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['stackhunter'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        if (cookie & 0xffffff) == 0xfceb58:
            __M_writer(unicode(stackhunter))
            __M_writer(u':\n    cmp eax, ')
            __M_writer(unicode(hex(cookie)))
            __M_writer(u'\n    jne ')
            __M_writer(unicode(stackhunter))
            __M_writer(u'+1\n    jmp esp\n')
        else:
            __M_writer(unicode(stackhunter))
            __M_writer(u':\n    pop eax\n    cmp eax, ')
            __M_writer(unicode(hex(cookie)))
            __M_writer(u'\n    jne ')
            __M_writer(unicode(stackhunter))
            __M_writer(u'\n    jmp esp\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 3, "17": 2, "23": 1, "27": 1, "28": 2, "29": 24, "30": 25, "34": 25, "35": 26, "36": 27, "37": 27, "38": 28, "39": 28, "40": 29, "41": 29, "42": 31, "43": 32, "44": 32, "45": 34, "46": 34, "47": 35, "48": 35, "54": 48}, "uri": "i386/stackhunter.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/stackhunter.asm"}
__M_END_METADATA
"""
