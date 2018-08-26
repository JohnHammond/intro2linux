# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.60465
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/amd64/pushstr.asm'
_template_uri = 'amd64/pushstr.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u'\nPushes a string onto the stack without using\nnull bytes or newline characters.\n\nExample:\n\n    >>> print shellcraft.amd64.pushstr(\'\').rstrip()\n        /* push \'\\x00\' */\n        push 1\n        dec byte ptr [rsp]\n    >>> print shellcraft.amd64.pushstr(\'a\').rstrip()\n        /* push \'a\\x00\' */\n        push 0x61\n    >>> print shellcraft.amd64.pushstr(\'aa\').rstrip()\n        /* push \'aa\\x00\' */\n        push 0x...\n        xor dword ptr [rsp], 0x...\n    >>> print shellcraft.amd64.pushstr(\'aaa\').rstrip()\n        /* push \'aaa\\x00\' */\n        push 0x...\n        xor dword ptr [rsp], 0x...\n    >>> print shellcraft.amd64.pushstr(\'aaaa\').rstrip()\n        /* push \'aaaa\\x00\' */\n        push 0x61616161\n    >>> print shellcraft.amd64.pushstr(\'aaa\\xc3\').rstrip()\n        /* push \'aaa\\xc3\\x00\' */\n        push 0x...\n        xor dword ptr [rsp], 0x...\n    >>> print shellcraft.amd64.pushstr(\'aaa\\xc3\', append_null = False).rstrip()\n        /* push \'aaa\\xc3\' */\n        push 0x...\n    >>> print shellcraft.amd64.pushstr(\'\\xc3\').rstrip()\n        /* push \'\\xc3\\x00\' */\n        push 0x...\n        xor dword ptr [rsp], 0x...\n    >>> print shellcraft.amd64.pushstr(\'\\xc3\', append_null = False).rstrip()\n        /* push \'\\xc3\' */\n        push 0x...c3\n    >>> with context.local():\n    ...    context.arch = \'amd64\'\n    ...    print enhex(asm(shellcraft.pushstr("/bin/sh")))\n    48b801010101010101015048b82e63686f2e72690148310424\n    >>> with context.local():\n    ...    context.arch = \'amd64\'\n    ...    print enhex(asm(shellcraft.pushstr("")))\n    6a01fe0c24\n    >>> with context.local():\n    ...    context.arch = \'amd64\'\n    ...    print enhex(asm(shellcraft.pushstr("\\x00", False)))\n    6a01fe0c24\n\nArgs:\n  string (str): The string to push.\n  append_null (bool): Whether to append a single NULL-byte before pushing.\n'
def render_body(context,string,append_null=True,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,string=string,append_null=append_null)
        ord = context.get('ord', UNDEFINED)
        hex = context.get('hex', UNDEFINED)
        repr = context.get('repr', UNDEFINED)
        __M_writer = context.writer()
        from pwnlib.util import lists, packing, fiddling 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['packing','fiddling','lists'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')

        if append_null:
            string += '\x00'
        if not string:
            return
        
        def okay(s):
            return '\n' not in s and '\0' not in s
        
        if ord(string[-1]) >= 128:
            extend = '\xff'
        else:
            extend = '\x00'
        
        def pretty(n):
            return hex(n & (2 ** 64 - 1))
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['pretty','okay','string','extend'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'    /* push ')
        __M_writer(unicode(repr(string)))
        __M_writer(u' */\n')
        for word in lists.group(8, string, 'fill', extend)[::-1]:

            sign = packing.u64(word, 'little', 'signed')
            
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['sign'] if __M_key in __M_locals_builtin_stored]))
            if sign in [0, 0xa]:
                __M_writer(u'    push ')
                __M_writer(unicode(sign + 1))
                __M_writer(u'\n    dec byte ptr [rsp]\n')
            elif -0x80 <= sign <= 0x7f and okay(word[0]):
                __M_writer(u'    push ')
                __M_writer(unicode(pretty(sign)))
                __M_writer(u'\n')
            elif -0x80000000 <= sign <= 0x7fffffff and okay(word[:4]):
                __M_writer(u'    push ')
                __M_writer(unicode(pretty(sign)))
                __M_writer(u'\n')
            elif okay(word):
                __M_writer(u'    mov rax, ')
                __M_writer(unicode(hex(sign)))
                __M_writer(u'\n    push rax\n')
            elif word[4:] == '\x00\x00\x00\x00':

                a,b = fiddling.xor_pair(word[:4], avoid = '\x00\n')
                a   = packing.u32(a, 'little', 'unsigned')
                b   = packing.u32(b, 'little', 'unsigned')
                
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['a','b'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'    push ')
                __M_writer(unicode(pretty(a)))
                __M_writer(u'\n    xor dword ptr [rsp], ')
                __M_writer(unicode(pretty(b)))
                __M_writer(u'\n')
            else:

                a,b = fiddling.xor_pair(word, avoid = '\x00\n')
                a   = packing.u64(a, 'little', 'unsigned')
                b   = packing.u64(b, 'little', 'unsigned')
                
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['a','b'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'    mov rax, ')
                __M_writer(unicode(pretty(a)))
                __M_writer(u'\n    push rax\n    mov rax, ')
                __M_writer(unicode(pretty(b)))
                __M_writer(u'\n    xor [rsp], rax\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 3, "17": 2, "25": 1, "29": 2, "30": 57, "31": 58, "51": 75, "52": 75, "53": 75, "54": 76, "55": 77, "61": 80, "62": 81, "63": 81, "64": 81, "65": 83, "66": 84, "67": 84, "68": 84, "69": 85, "70": 86, "71": 86, "72": 86, "73": 87, "74": 88, "75": 88, "76": 88, "77": 90, "78": 91, "86": 96, "87": 96, "88": 96, "89": 97, "90": 97, "91": 98, "92": 99, "100": 104, "101": 104, "102": 104, "103": 106, "104": 106, "110": 104}, "uri": "amd64/pushstr.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/amd64/pushstr.asm"}
__M_END_METADATA
"""
