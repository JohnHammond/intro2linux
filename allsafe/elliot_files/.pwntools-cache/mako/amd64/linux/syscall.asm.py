# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.630097
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/amd64/linux/syscall.asm'
_template_uri = 'amd64/linux/syscall.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u"\nArgs: [syscall_number, *args]\n    Does a syscall\n\nExample:\n\n        >>> print pwnlib.shellcraft.amd64.linux.syscall('SYS_execve', 1, 'rsp', 2, 0).rstrip()\n            /* call execve(1, 'rsp', 2, 0) */\n            push 0x1\n            pop rdi\n            mov rsi, rsp\n            push 0x2\n            pop rdx\n            xor r10d, r10d\n            push 0x3b\n            pop rax\n            syscall\n        >>> print pwnlib.shellcraft.amd64.linux.syscall('SYS_execve', 2, 1, 0, -1).rstrip()\n            /* call execve(2, 1, 0, -1) */\n            push 0x2\n            pop rdi\n            push 0x1\n            pop rsi\n            push -1\n            pop r10\n            push 0x3b\n            pop rax\n            cdq /* Set rdx to 0, rax is known to be positive */\n            syscall\n        >>> print pwnlib.shellcraft.amd64.linux.syscall().rstrip()\n            /* call syscall() */\n            syscall\n        >>> print pwnlib.shellcraft.amd64.linux.syscall('rax', 'rdi', 'rsi').rstrip()\n            /* call syscall('rax', 'rdi', 'rsi') */\n            /* moving rdi into rdi, but this is a no-op */\n            /* moving rsi into rsi, but this is a no-op */\n            /* moving rax into rax, but this is a no-op */\n            syscall\n        >>> print pwnlib.shellcraft.amd64.linux.syscall('rbp', None, None, 1).rstrip()\n            /* call syscall('rbp', ?, ?, 1) */\n            push 0x1\n            pop rdx\n            mov rax, rbp\n            syscall\n"
def render_body(context,syscall=None,arg0=None,arg1=None,arg2=None,arg3=None,arg4=None,arg5=None,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(syscall=syscall,arg1=arg1,arg2=arg2,arg3=arg3,arg4=arg4,arg5=arg5,arg0=arg0,pageargs=pageargs)
        str = context.get('str', UNDEFINED)
        zip = context.get('zip', UNDEFINED)
        repr = context.get('repr', UNDEFINED)
        getattr = context.get('getattr', UNDEFINED)
        unicode = context.get('unicode', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        __M_writer = context.writer()
        from pwnlib.shellcraft import amd64 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['amd64'] if __M_key in __M_locals_builtin_stored]))
        from pwnlib.constants.linux import amd64 as constants 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['constants'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')

        append_cdq = False
        if isinstance(syscall, (str, unicode)) and syscall.startswith('SYS_'):
            syscall_repr = syscall[4:] + "(%s)"
            args = []
        else:
            syscall_repr = 'syscall(%s)'
            if syscall == None:
                args = ['?']
            else:
                args = [repr(syscall)]
        
        for arg in [arg0, arg1, arg2, arg3, arg4, arg5]:
            if arg == None:
                args.append('?')
            else:
                args.append(repr(arg))
        while args and args[-1] == '?':
            args.pop()
        syscall_repr = syscall_repr % ', '.join(args)
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['append_cdq','args','arg','syscall_repr'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'    /* call ')
        __M_writer(unicode(syscall_repr))
        __M_writer(u' */\n')
        for dst, src in zip(['rdi', 'rsi', 'rdx', 'r10', 'r8', 'r9', 'rax'], [arg0, arg1, arg2, arg3, arg4, arg5, syscall]):
            if dst == 'rdx' and src == 0:
                __M_writer(u'    ')
                append_cdq = True 
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['append_cdq'] if __M_key in __M_locals_builtin_stored]))
            elif src != None:
                __M_writer(u'    ')

                if isinstance(src, (str, unicode)):
                    src = getattr(constants, src, src)
                    
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['src'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'    ')
                __M_writer(unicode(amd64.mov(dst, src)))
                __M_writer(u'\n')
        if append_cdq:
            __M_writer(u'    cdq /* Set rdx to 0, rax is known to be positive */\n')
        __M_writer(u'    syscall\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 4, "17": 3, "28": 1, "32": 2, "36": 3, "37": 48, "38": 49, "62": 70, "63": 70, "64": 70, "65": 71, "66": 72, "67": 73, "68": 73, "72": 74, "73": 75, "74": 75, "81": 79, "82": 79, "83": 79, "84": 82, "85": 83, "86": 85, "92": 86}, "uri": "amd64/linux/syscall.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/amd64/linux/syscall.asm"}
__M_END_METADATA
"""
