# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.590156
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/amd64/mov.asm'
_template_uri = 'amd64/mov.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u"\nMove src into dest without newlines and null bytes.\n\nIf the src is a register smaller than the dest, then it will be\nzero-extended to fit inside the larger register.\n\nIf the src is a register larger than the dest, then only some of the bits will\nbe used.\n\nExample:\n\n    >>> print shellcraft.amd64.mov('eax','ebx').rstrip()\n        mov eax, ebx\n    >>> print shellcraft.amd64.mov('eax', 0).rstrip()\n        xor eax, eax\n    >>> print shellcraft.amd64.mov('ax', 0).rstrip()\n        xor ax, ax\n    >>> print shellcraft.amd64.mov('rax', 0).rstrip()\n        xor eax, eax\n    >>> print shellcraft.amd64.mov('al', 'ax').rstrip()\n        /* moving ax into al, but this is a no-op */\n    >>> print shellcraft.amd64.mov('bl', 'ax').rstrip()\n        mov bl, al\n    >>> print shellcraft.amd64.mov('ax', 'bl').rstrip()\n        movzx ax, bl\n    >>> print shellcraft.amd64.mov('eax', 1).rstrip()\n        push 0x1\n        pop rax\n    >>> print shellcraft.amd64.mov('rax', 0xdead00ff).rstrip()\n        mov eax, 0x1010101\n        xor eax, 0xdfac01fe\n    >>> print shellcraft.amd64.mov('rax', 0x11dead00ff).rstrip()\n        mov rax, 0x101010101010101\n        push rax\n        mov rax, 0x1010110dfac01fe\n        xor [rsp], rax\n        pop rax\n\nArgs:\n  dest (str): The destination register.\n  src (str): Either the input register, or an immediate value.\n  stack_allowed (bool): Can the stack be used?\n"
def render_body(context,dest,src,stack_allowed=True,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(dest=dest,src=src,pageargs=pageargs,stack_allowed=stack_allowed)
        int = context.get('int', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        hex = context.get('hex', UNDEFINED)
        long = context.get('long', UNDEFINED)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        from pwnlib.util import lists, packing, fiddling, misc 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['packing','fiddling','misc','lists'] if __M_key in __M_locals_builtin_stored]))

        import logging
        log = logging.getLogger('pwnlib.shellcraft')
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['logging','log'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')

        regs = [['rax', 'eax', 'ax', 'al'],
                ['rbx', 'ebx', 'bx', 'bl'],
                ['rcx', 'ecx', 'cx', 'cl'],
                ['rdx', 'edx', 'dx', 'dl'],
                ['rdi', 'edi', 'di', 'dil'],
                ['rsi', 'esi', 'si', 'sil'],
                ['rbp', 'ebp', 'bp', 'bpl'],
                ['rsp', 'esp', 'sp', 'spl'],
                ['r8', 'r8d', 'r8w', 'r8b'],
                ['r9', 'r9d', 'r9w', 'r9b'],
                ['r10', 'r10d', 'r10w', 'r10b'],
                ['r11', 'r11d', 'r11w', 'r11b'],
                ['r12', 'r12d', 'r12w', 'r12b'],
                ['r13', 'r13d', 'r13w', 'r13b'],
                ['r14', 'r14d', 'r14w', 'r14b'],
                ['r15', 'r15d', 'r15w', 'r15b']
                ]
        def okay(s):
            return '\0' not in s and '\n' not in s
        
        def pretty(n):
            if n < 0:
              return str(n)
            else:
              return hex(n)
        
        all_regs, sizes, bigger, smaller = misc.register_sizes(regs, [64, 32, 16, 8])
        dest_orig = dest
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['smaller','okay','sizes','regs','dest_orig','pretty','all_regs','bigger'] if __M_key in __M_locals_builtin_stored]))
        if dest not in all_regs:
            __M_writer(u'    ')
            log.error('%s is not a register' % str(dest_orig)) 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
        elif isinstance(src, (int, long)):
            __M_writer(u'    ')

            if not (-2 ** (sizes[dest]-1) <= src < 2**sizes[dest]):
                log.error('Number %s does not fit into %s' % (pretty(src), dest_orig))
            
            # Calculate the unsigned and signed versions
            srcu = src & (2 ** sizes[dest] - 1)
            srcs = srcu - 2 * (srcu & (2 ** (sizes[dest] - 1)))
            
            # micro-optimization: if you ever touch e.g. eax, then all the upper bits
            # of rax will be set to 0. We exploit this fact here
            if 0 <= src < 2 ** 32 and sizes[dest] == 64:
                dest = smaller[dest][0]
            
            # Calculate the packed version
            srcp = packing.pack(srcu, sizes[dest], 'little', False)
                
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['dest','srcs','srcp','srcu'] if __M_key in __M_locals_builtin_stored]))
            if src == 0:
                __M_writer(u'        xor ')
                __M_writer(unicode(dest))
                __M_writer(u', ')
                __M_writer(unicode(dest))
                __M_writer(u'\n')
            elif src == 10 and stack_allowed and sizes[dest] == 32: # sizes[dest] == 64 not possible here
                __M_writer(u'        push 9\n        pop ')
                __M_writer(unicode(bigger[dest][0]))
                __M_writer(u'\n        inc ')
                __M_writer(unicode(dest))
                __M_writer(u'\n')
            elif stack_allowed and sizes[dest] in [32, 64] and -2**7 <= srcs < 2**7 and okay(srcp[0]):
                __M_writer(u'        push ')
                __M_writer(unicode(pretty(srcs)))
                __M_writer(u'\n        pop ')
                __M_writer(unicode(dest if sizes[dest] == 64 else bigger[dest][0]))
                __M_writer(u'\n')
            elif okay(srcp):
                __M_writer(u'        mov ')
                __M_writer(unicode(dest))
                __M_writer(u', ')
                __M_writer(unicode(pretty(src)))
                __M_writer(u'\n')
            elif stack_allowed and sizes[dest] in [32, 64] and -2**31 <= srcs < 2**31 and okay(srcp[:4]):
                __M_writer(u'        push ')
                __M_writer(unicode(pretty(srcs)))
                __M_writer(u'\n        pop ')
                __M_writer(unicode(dest if sizes[dest] == 64 else bigger[dest][0]))
                __M_writer(u'\n')
            else:
                __M_writer(u'        ')

                a,b = fiddling.xor_pair(srcp, avoid = '\x00\n')
                a = pretty(packing.unpack(a, sizes[dest], 'little', False))
                b = pretty(packing.unpack(b, sizes[dest], 'little', False))
                
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['a','b'] if __M_key in __M_locals_builtin_stored]))
                if sizes[dest] != 64:
                    __M_writer(u'          mov ')
                    __M_writer(unicode(dest))
                    __M_writer(u', ')
                    __M_writer(unicode(a))
                    __M_writer(u'\n          xor ')
                    __M_writer(unicode(dest))
                    __M_writer(u', ')
                    __M_writer(unicode(b))
                    __M_writer(u'\n')
                elif stack_allowed:
                    __M_writer(u'          mov ')
                    __M_writer(unicode(dest))
                    __M_writer(u', ')
                    __M_writer(unicode(a))
                    __M_writer(u'\n          push ')
                    __M_writer(unicode(dest))
                    __M_writer(u'\n          mov ')
                    __M_writer(unicode(dest))
                    __M_writer(u', ')
                    __M_writer(unicode(b))
                    __M_writer(u'\n          xor [rsp], ')
                    __M_writer(unicode(dest))
                    __M_writer(u'\n          pop ')
                    __M_writer(unicode(dest))
                    __M_writer(u'\n')
                else:
                    __M_writer(u'          ')
                    log.error("Cannot put %s into '%s' without using stack." % (pretty(src), dest_orig)) 
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
        elif src in all_regs:
            __M_writer(u'    ')

      # micro-optimization: if you ever touch e.g. eax, then all the upper bits
      # of rax will be set to 0. We exploit this fact here
            if sizes[dest] == 64 and sizes[src] != 64:
                dest = smaller[dest][0]
                
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['dest'] if __M_key in __M_locals_builtin_stored]))
            if src == dest or src in bigger[dest] or src in smaller[dest]:
                __M_writer(u'        /* moving ')
                __M_writer(unicode(src))
                __M_writer(u' into ')
                __M_writer(unicode(dest_orig))
                __M_writer(u', but this is a no-op */\n')
            elif sizes[dest] == sizes[src]:
                __M_writer(u'        mov ')
                __M_writer(unicode(dest))
                __M_writer(u', ')
                __M_writer(unicode(src))
                __M_writer(u'\n')
            elif sizes[dest] > sizes[src]:
                __M_writer(u'        movzx ')
                __M_writer(unicode(dest))
                __M_writer(u', ')
                __M_writer(unicode(src))
                __M_writer(u'\n')
            else:
                for r in smaller[src]:
                    if sizes[r] == sizes[dest]:
                        __M_writer(u'                mov ')
                        __M_writer(unicode(dest))
                        __M_writer(u', ')
                        __M_writer(unicode(r))
                        __M_writer(u'\n                ')
                        break 
                        
                        __M_locals_builtin_stored = __M_locals_builtin()
                        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
        else:
            __M_writer(u'    ')
            log.error('%s is neither a register nor an immediate' % src) 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin_stored]))
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 7, "17": 6, "27": 1, "31": 2, "38": 6, "39": 49, "40": 50, "73": 80, "74": 81, "75": 81, "79": 82, "80": 83, "81": 83, "100": 99, "101": 100, "102": 100, "103": 100, "104": 100, "105": 100, "106": 101, "107": 102, "108": 103, "109": 103, "110": 104, "111": 104, "112": 105, "113": 106, "114": 106, "115": 106, "116": 107, "117": 107, "118": 108, "119": 109, "120": 109, "121": 109, "122": 109, "123": 109, "124": 110, "125": 111, "126": 111, "127": 111, "128": 112, "129": 112, "130": 113, "131": 114, "132": 114, "140": 119, "141": 120, "142": 120, "143": 120, "144": 120, "145": 120, "146": 121, "147": 121, "148": 121, "149": 121, "150": 122, "151": 123, "152": 123, "153": 123, "154": 123, "155": 123, "156": 124, "157": 124, "158": 125, "159": 125, "160": 125, "161": 125, "162": 126, "163": 126, "164": 127, "165": 127, "166": 128, "167": 129, "168": 129, "172": 132, "173": 133, "174": 133, "183": 139, "184": 140, "185": 140, "186": 140, "187": 140, "188": 140, "189": 141, "190": 142, "191": 142, "192": 142, "193": 142, "194": 142, "195": 143, "196": 144, "197": 144, "198": 144, "199": 144, "200": 144, "201": 145, "202": 146, "203": 147, "204": 148, "205": 148, "206": 148, "207": 148, "208": 148, "209": 149, "213": 153, "214": 154, "215": 154, "224": 215}, "uri": "amd64/mov.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/amd64/mov.asm"}
__M_END_METADATA
"""
