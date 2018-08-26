# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.763837
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/thumb/pushstr.asm'
_template_uri = 'thumb/pushstr.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u"\nPushes a string onto the stack without using\nnull bytes or newline characters.\n\nArgs:\n  string (str): The string to push.\n  append_null (bool): Whether to append a single NULL-byte before pushing.\n\nExamples:\n    >>>> with context.local():\n    ...    context.arch = 'thumb'\n    ...    print enhex(asm(shellcraft.pushstr('Hello\\nWorld!', True)))\n    81ea010102b4dff8041001e0726c642102b4dff8041001e06f0a576f02b4dff8041001e048656c6c02b4\n    >>>> with context.local():\n    ...    context.arch = 'thumb'\n    ...    print enhex(asm(shellcraft.pushstr('', True)))\n    81ea010102b4\n    >>>> with context.local():\n    ...    context.arch = 'thumb'\n    ...    print enhex(asm(shellcraft.pushstr('\\x00', False)))\n    81ea010102b4\n\n"
def render_body(context,string,append_null=True,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,string=string,append_null=append_null)
        repr = context.get('repr', UNDEFINED)
        __M_writer = context.writer()
        from pwnlib.shellcraft.thumb import mov 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['mov'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        from pwnlib.util import lists, packing 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['packing','lists'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')

        if append_null:
            string += '\x00'
        if not string:
            return
        
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['string'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'    /* push ')
        __M_writer(unicode(repr(string)))
        __M_writer(u' */\n\n')
        for word in lists.group(4, string, 'fill', '\x00')[::-1]:
            __M_writer(u'    ')
            __M_writer(unicode(mov('r1', packing.unpack(word))))
            __M_writer(u'\n    push {r1}\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"32": 3, "33": 26, "34": 27, "49": 37, "48": 37, "44": 34, "45": 34, "46": 34, "47": 36, "16": 4, "17": 3, "50": 37, "23": 1, "56": 50, "27": 1, "28": 2}, "uri": "thumb/pushstr.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/thumb/pushstr.asm"}
__M_END_METADATA
"""
