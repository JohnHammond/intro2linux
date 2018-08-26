# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1479426012.488035
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/pushstr.asm'
_template_uri = 'i386/pushstr.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u'\nPushes a string onto the stack without using\nnull bytes or newline characters.\n\nExample:\n\n    >>> print shellcraft.i386.pushstr(\'\').rstrip()\n        /* push \'\\x00\' */\n        push 1\n        dec byte ptr [esp]\n    >>> print shellcraft.i386.pushstr(\'a\').rstrip()\n        /* push \'a\\x00\' */\n        push 0x61\n    >>> print shellcraft.i386.pushstr(\'aa\').rstrip()\n        /* push \'aa\\x00\' */\n        push 0x1010101\n        xor dword ptr [esp], 0x1016060\n    >>> print shellcraft.i386.pushstr(\'aaa\').rstrip()\n        /* push \'aaa\\x00\' */\n        push 0x1010101\n        xor dword ptr [esp], 0x1606060\n    >>> print shellcraft.i386.pushstr(\'aaaa\').rstrip()\n        /* push \'aaaa\\x00\' */\n        push 1\n        dec byte ptr [esp]\n        push 0x61616161\n    >>> print shellcraft.i386.pushstr(\'aaaaa\').rstrip()\n        /* push \'aaaaa\\x00\' */\n        push 0x61\n        push 0x61616161\n    >>> print shellcraft.i386.pushstr(\'aaaa\', append_null = False).rstrip()\n        /* push \'aaaa\' */\n        push 0x61616161\n    >>> print shellcraft.i386.pushstr(\'\\xc3\').rstrip()\n        /* push \'\\xc3\\x00\' */\n        push 0x1010101\n        xor dword ptr [esp], 0x10101c2\n    >>> print shellcraft.i386.pushstr(\'\\xc3\', append_null = False).rstrip()\n        /* push \'\\xc3\' */\n        push -0x3d\n    >>> with context.local():\n    ...    context.arch = \'i386\'\n    ...    print enhex(asm(shellcraft.pushstr("/bin/sh")))\n    68010101018134242e726901682f62696e\n    >>> with context.local():\n    ...    context.arch = \'i386\'\n    ...    print enhex(asm(shellcraft.pushstr("")))\n    6a01fe0c24\n    >>> with context.local():\n    ...    context.arch = \'i386\'\n    ...    print enhex(asm(shellcraft.pushstr("\\x00", False)))\n    6a01fe0c24\n\nArgs:\n  string (str): The string to push.\n  append_null (bool): Whether to append a single NULL-byte before pushing.\n'
def render_body(context,string,append_null=True,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,string=string,append_null=append_null)
        ord = context.get('ord', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()

        from pwnlib.util import lists, packing, fiddling
        from pwnlib.shellcraft import pretty, okay
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['packing','fiddling','okay','pretty','lists'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')

        original = string
        string   = packing.flat(string)
        
        if append_null:
            string += '\x00'
            if isinstance(original, str):
                original += '\x00'
        
        if not string:
            return
        
        if ord(string[-1]) >= 128:
            extend = '\xff'
        else:
            extend = '\x00'
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['original','extend','string'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'    /* push ')
        __M_writer(unicode(pretty(original, False)))
        __M_writer(u' */\n')
        for word in lists.group(4, string, 'fill', extend)[::-1]:

            sign = packing.u32(word, endian='little', sign='signed')
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['sign'] if __M_key in __M_locals_builtin_stored]))
            if sign in [0, 0xa]:
                __M_writer(u'    push ')
                __M_writer(unicode(pretty(sign + 1)))
                __M_writer(u'\n    dec byte ptr [esp]\n')
            elif -0x80 <= sign <= 0x7f and okay(word[0]):
                __M_writer(u'    push ')
                __M_writer(unicode(pretty(sign)))
                __M_writer(u'\n')
            elif okay(word):
                __M_writer(u'    push ')
                __M_writer(unicode(pretty(sign)))
                __M_writer(u'\n')
            else:

                a,b = fiddling.xor_pair(word, avoid = '\x00\n')
                a   = packing.u32(a, endian='little', sign='unsigned')
                b   = packing.u32(b, endian='little', sign='unsigned')
                
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['a','b'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'    push ')
                __M_writer(unicode(pretty(a)))
                __M_writer(u'\n    xor dword ptr [esp], ')
                __M_writer(unicode(pretty(b)))
                __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 6, "17": 5, "25": 1, "32": 4, "33": 5, "34": 62, "35": 63, "55": 80, "56": 80, "57": 80, "58": 81, "59": 82, "65": 85, "66": 86, "67": 86, "68": 86, "69": 88, "70": 89, "71": 89, "72": 89, "73": 90, "74": 91, "75": 91, "76": 91, "77": 92, "78": 93, "86": 98, "87": 98, "88": 98, "89": 99, "90": 99, "96": 90}, "uri": "i386/pushstr.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/pushstr.asm"}
__M_END_METADATA
"""
