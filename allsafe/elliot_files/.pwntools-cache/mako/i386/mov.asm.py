# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1479426012.515302
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/mov.asm'
_template_uri = 'i386/mov.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u"\nMove src into dest without newlines and null bytes.\n\nIf the src is a register smaller than the dest, then it will be\nzero-extended to fit inside the larger register.\n\nIf the src is a register larger than the dest, then only some of the bits will\nbe used.\n\nIf src is a string that is not a register, then it will locally set\n`context.arch` to `'i386'` and use :func:`pwnlib.constants.eval` to evaluate the\nstring. Note that this means that this shellcode can change behavior depending\non the value of `context.os`.\n\nArgs:\n  dest (str): The destination register.\n  src (str): Either the input register, or an immediate value.\n  stack_allowed (bool): Can the stack be used?\n\nExample:\n\n    >>> print shellcraft.i386.mov('eax','ebx').rstrip()\n        mov eax, ebx\n    >>> print shellcraft.i386.mov('eax', 0).rstrip()\n        xor eax, eax\n    >>> print shellcraft.i386.mov('ax', 0).rstrip()\n        xor ax, ax\n    >>> print shellcraft.i386.mov('ax', 17).rstrip()\n        xor ax, ax\n        mov al, 0x11\n    >>> print shellcraft.i386.mov('edi', ord('\\n')).rstrip()\n        push 9 /* mov edi, '\\n' */\n        pop edi\n        inc edi\n    >>> print shellcraft.i386.mov('al', 'ax').rstrip()\n        /* moving ax into al, but this is a no-op */\n    >>> print shellcraft.i386.mov('al','ax').rstrip()\n        /* moving ax into al, but this is a no-op */\n    >>> print shellcraft.i386.mov('esp', 'esp').rstrip()\n        /* moving esp into esp, but this is a no-op */\n    >>> print shellcraft.i386.mov('ax', 'bl').rstrip()\n        movzx ax, bl\n    >>> print shellcraft.i386.mov('eax', 1).rstrip()\n        push 1\n        pop eax\n    >>> print shellcraft.i386.mov('eax', 1, stack_allowed=False).rstrip()\n        xor eax, eax\n        mov al, 1\n    >>> print shellcraft.i386.mov('eax', 0xdead00ff).rstrip()\n        mov eax, -0xdead00ff\n        neg eax\n    >>> print shellcraft.i386.mov('eax', 0xc0).rstrip()\n        xor eax, eax\n        mov al, 0xc0\n    >>> print shellcraft.i386.mov('edi', 0xc0).rstrip()\n        mov edi, -0xc0\n        neg edi\n    >>> print shellcraft.i386.mov('eax', 0xc000).rstrip()\n        xor eax, eax\n        mov ah, 0xc000 >> 8\n    >>> print shellcraft.i386.mov('eax', 0xffc000).rstrip()\n        mov eax, 0x1010101\n        xor eax, 0x1010101 ^ 0xffc000\n    >>> print shellcraft.i386.mov('edi', 0xc000).rstrip()\n        mov edi, (-1) ^ 0xc000\n        not edi\n    >>> print shellcraft.i386.mov('edi', 0xf500).rstrip()\n        mov edi, 0x1010101\n        xor edi, 0x1010101 ^ 0xf500\n    >>> print shellcraft.i386.mov('eax', 0xc0c0).rstrip()\n        xor eax, eax\n        mov ax, 0xc0c0\n    >>> print shellcraft.i386.mov('eax', 'SYS_execve').rstrip()\n        push (SYS_execve) /* 0xb */\n        pop eax\n    >>> with context.local(os='freebsd'):\n    ...     print shellcraft.i386.mov('eax', 'SYS_execve').rstrip()\n        push (SYS_execve) /* 0x3b */\n        pop eax\n    >>> print shellcraft.i386.mov('eax', 'PROT_READ | PROT_WRITE | PROT_EXEC').rstrip()\n        push (PROT_READ | PROT_WRITE | PROT_EXEC) /* 7 */\n        pop eax\n"
def render_body(context,dest,src,stack_allowed=True,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(dest=dest,src=src,pageargs=pageargs,stack_allowed=stack_allowed)
        tuple = context.get('tuple', UNDEFINED)
        int = context.get('int', UNDEFINED)
        hex = context.get('hex', UNDEFINED)
        long = context.get('long', UNDEFINED)
        str = context.get('str', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        __M_writer = context.writer()

        from pwnlib.shellcraft import eval, pretty, okay
        from pwnlib.util import lists, packing, fiddling, misc
        from pwnlib.log import getLogger
        from pwnlib.shellcraft.registers import get_register, is_register, bits_required
        log = getLogger('pwnlib.shellcraft.i386.mov')
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['okay','eval','misc','bits_required','lists','get_register','getLogger','packing','fiddling','pretty','is_register','log'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')

        src_name = src
        if not isinstance(src, (str, tuple)):
            src_name = pretty(src)
        
        if not get_register(dest):
            log.error('%r is not a register' % dest)
        
        dest = get_register(dest)
        
        if dest.size > 32 or dest.is64bit:
            log.error("cannot use %s on i386" % dest)
        
        if get_register(src):
            src = get_register(src)
        
            if src.is64bit:
                log.error("cannot use %s on i386" % src)
        
            if dest.size < src.size and src.name not in dest.bigger:
                log.error("cannot mov %s, %s: dddest is smaller than src" % (dest, src))
        else:
            src = eval(src)
        
            if not dest.fits(src):
                log.error("cannot mov %s, %r: dest is smaller than src" % (dest, src))
        
            src_size = bits_required(src)
        
            # Calculate the packed version
            mask = ((1<<32)-1)
            masked = src & mask
            srcp = packing.pack(masked, dest.size)
        
            # Calculate the unsigned and signed versions
            srcu = packing.unpack(srcp, dest.size, sign=False)
            srcs = packing.unpack(srcp, dest.size, sign=True)
        
            srcp_not = packing.pack(fiddling.bnot(masked))
            srcp_neg = packing.pack(fiddling.negate(masked))
            srcu_not = packing.unpack(srcp_not)
            srcu_neg = packing.unpack(srcp_neg)
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['src','srcp_neg','src_size','dest','mask','srcu_not','srcp_not','srcs','srcp','masked','srcu','src_name','srcu_neg'] if __M_key in __M_locals_builtin_stored]))
        if is_register(src):
            if src == dest:
                __M_writer(u'    /* moving ')
                __M_writer(unicode(src))
                __M_writer(u' into ')
                __M_writer(unicode(dest))
                __M_writer(u', but this is a no-op */\n')
            elif src.name in dest.bigger:
                __M_writer(u'    /* moving ')
                __M_writer(unicode(src))
                __M_writer(u' into ')
                __M_writer(unicode(dest))
                __M_writer(u', but this is a no-op */\n')
            elif dest.size > src.size:
                __M_writer(u'    movzx ')
                __M_writer(unicode(dest))
                __M_writer(u', ')
                __M_writer(unicode(src))
                __M_writer(u'\n')
            else:
                __M_writer(u'    mov ')
                __M_writer(unicode(dest))
                __M_writer(u', ')
                __M_writer(unicode(src))
                __M_writer(u'\n')
        elif isinstance(src, (int, long)):
            if src == 0:
                __M_writer(u'        xor ')
                __M_writer(unicode(dest))
                __M_writer(u', ')
                __M_writer(unicode(dest))
                __M_writer(u'\n')
            elif stack_allowed and dest.size == 32 and src == 10:
                __M_writer(u'        push 9 /* mov ')
                __M_writer(unicode(dest))
                __M_writer(u", '\\n' */\n        pop ")
                __M_writer(unicode(dest))
                __M_writer(u'\n        inc ')
                __M_writer(unicode(dest))
                __M_writer(u'\n')
            elif stack_allowed and dest.size == 32 and okay(srcp):
                __M_writer(u'        push ')
                __M_writer(unicode(pretty(src)))
                __M_writer(u'\n        pop ')
                __M_writer(unicode(dest))
                __M_writer(u'\n')
            elif stack_allowed and dest.size == 32 and  -127 <= srcs < 128 and okay(srcp[0]):
                __M_writer(u'        push ')
                __M_writer(unicode(pretty(src)))
                __M_writer(u'\n        pop ')
                __M_writer(unicode(dest))
                __M_writer(u'\n')
            elif okay(srcp):
                __M_writer(u'        mov ')
                __M_writer(unicode(dest))
                __M_writer(u', ')
                __M_writer(unicode(pretty(src)))
                __M_writer(u'\n')
            elif 0 <= srcu < 2**8 and okay(srcp[0]) and dest.sizes.get(8, 0):
                __M_writer(u'        xor ')
                __M_writer(unicode(dest))
                __M_writer(u', ')
                __M_writer(unicode(dest))
                __M_writer(u'\n        mov ')
                __M_writer(unicode(dest.sizes[8]))
                __M_writer(u', ')
                __M_writer(unicode(pretty(srcu)))
                __M_writer(u'\n')
            elif srcu == (srcu & 0xff00) and okay(srcp[1]) and dest.ff00:
                __M_writer(u'        xor ')
                __M_writer(unicode(dest))
                __M_writer(u', ')
                __M_writer(unicode(dest))
                __M_writer(u'\n        mov ')
                __M_writer(unicode(dest.ff00))
                __M_writer(u', ')
                __M_writer(unicode(pretty(src)))
                __M_writer(u' >> 8\n')
            elif 0 <= srcu < 2**16 and okay(srcp[:2]) and dest.sizes[16]:
                __M_writer(u'        xor ')
                __M_writer(unicode(dest))
                __M_writer(u', ')
                __M_writer(unicode(dest))
                __M_writer(u'\n        mov ')
                __M_writer(unicode(dest.sizes[16]))
                __M_writer(u', ')
                __M_writer(unicode(pretty(src)))
                __M_writer(u'\n')
            elif okay(srcp_neg):
                __M_writer(u'        mov ')
                __M_writer(unicode(dest))
                __M_writer(u', -')
                __M_writer(unicode(pretty(src)))
                __M_writer(u'\n        neg ')
                __M_writer(unicode(dest))
                __M_writer(u'\n')
            elif okay(srcp_not):
                __M_writer(u'        mov ')
                __M_writer(unicode(dest))
                __M_writer(u', (-1) ^ ')
                __M_writer(unicode(pretty(src)))
                __M_writer(u'\n        not ')
                __M_writer(unicode(dest))
                __M_writer(u'\n')
            else:
                __M_writer(u'        ')

                a,b = fiddling.xor_pair(srcp, avoid = '\x00\n')
                a = hex(packing.unpack(a, dest.size))
                b = hex(packing.unpack(b, dest.size))
                
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['a','b'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'        mov ')
                __M_writer(unicode(dest))
                __M_writer(u', ')
                __M_writer(unicode(a))
                __M_writer(u'\n        xor ')
                __M_writer(unicode(dest))
                __M_writer(u', ')
                __M_writer(unicode(a))
                __M_writer(u' ^ ')
                __M_writer(unicode(pretty(src)))
                __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 9, "17": 8, "28": 1, "38": 7, "39": 8, "40": 91, "41": 92, "87": 135, "88": 136, "89": 137, "90": 137, "91": 137, "92": 137, "93": 137, "94": 138, "95": 139, "96": 139, "97": 139, "98": 139, "99": 139, "100": 140, "101": 141, "102": 141, "103": 141, "104": 141, "105": 141, "106": 142, "107": 143, "108": 143, "109": 143, "110": 143, "111": 143, "112": 145, "113": 147, "114": 148, "115": 148, "116": 148, "117": 148, "118": 148, "119": 150, "120": 151, "121": 151, "122": 151, "123": 152, "124": 152, "125": 153, "126": 153, "127": 157, "128": 158, "129": 158, "130": 158, "131": 159, "132": 159, "133": 160, "134": 161, "135": 161, "136": 161, "137": 162, "138": 162, "139": 164, "140": 165, "141": 165, "142": 165, "143": 165, "144": 165, "145": 167, "146": 168, "147": 168, "148": 168, "149": 168, "150": 168, "151": 169, "152": 169, "153": 169, "154": 169, "155": 173, "156": 174, "157": 174, "158": 174, "159": 174, "160": 174, "161": 175, "162": 175, "163": 175, "164": 175, "165": 177, "166": 178, "167": 178, "168": 178, "169": 178, "170": 178, "171": 179, "172": 179, "173": 179, "174": 179, "175": 181, "176": 182, "177": 182, "178": 182, "179": 182, "180": 182, "181": 183, "182": 183, "183": 184, "184": 185, "185": 185, "186": 185, "187": 185, "188": 185, "189": 186, "190": 186, "191": 189, "192": 190, "193": 190, "201": 195, "202": 195, "203": 195, "204": 195, "205": 195, "206": 196, "207": 196, "208": 196, "209": 196, "210": 196, "211": 196, "217": 211}, "uri": "i386/mov.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/mov.asm"}
__M_END_METADATA
"""
