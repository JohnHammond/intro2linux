# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1479426012.493729
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/linux/syscall.asm'
_template_uri = 'i386/linux/syscall.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u"\nArgs: [syscall_number, \\*args]\n    Does a syscall\n\nAny of the arguments can be expressions to be evaluated by :func:`pwnlib.constants.eval`.\n\nExample:\n\n        >>> print pwnlib.shellcraft.i386.linux.syscall('SYS_execve', 1, 'esp', 2, 0).rstrip()\n            /* call execve(1, 'esp', 2, 0) */\n            push (SYS_execve) /* 0xb */\n            pop eax\n            push 1\n            pop ebx\n            mov ecx, esp\n            push 2\n            pop edx\n            xor esi, esi\n            int 0x80\n        >>> print pwnlib.shellcraft.i386.linux.syscall('SYS_execve', 2, 1, 0, 20).rstrip()\n            /* call execve(2, 1, 0, 0x14) */\n            push (SYS_execve) /* 0xb */\n            pop eax\n            push 2\n            pop ebx\n            push 1\n            pop ecx\n            push 0x14\n            pop esi\n            cdq /* edx=0 */\n            int 0x80\n        >>> print pwnlib.shellcraft.i386.linux.syscall().rstrip()\n            /* call syscall() */\n            int 0x80\n        >>> print pwnlib.shellcraft.i386.linux.syscall('eax', 'ebx', 'ecx').rstrip()\n            /* call syscall('eax', 'ebx', 'ecx') */\n            /* setregs noop */\n            int 0x80\n        >>> print pwnlib.shellcraft.i386.linux.syscall('ebp', None, None, 1).rstrip()\n            /* call syscall('ebp', ?, ?, 1) */\n            mov eax, ebp\n            push 1\n            pop edx\n            int 0x80\n        >>> print pwnlib.shellcraft.i386.linux.syscall(\n        ...               'SYS_mmap2', 0, 0x1000,\n        ...               'PROT_READ | PROT_WRITE | PROT_EXEC',\n        ...               'MAP_PRIVATE | MAP_ANONYMOUS',\n        ...               -1, 0).rstrip()\n            /* call mmap2(0, 0x1000, 'PROT_READ | PROT_WRITE | PROT_EXEC', 'MAP_PRIVATE | MAP_ANONYMOUS', -1, 0) */\n            xor eax, eax\n            mov al, 0xc0\n            xor ebp, ebp\n            xor ebx, ebx\n            xor ecx, ecx\n            mov ch, 0x1000 >> 8\n            push -1\n            pop edi\n            push (PROT_READ | PROT_WRITE | PROT_EXEC) /* 7 */\n            pop edx\n            push (MAP_PRIVATE | MAP_ANONYMOUS) /* 0x22 */\n            pop esi\n            int 0x80\n"
def render_body(context,syscall=None,arg0=None,arg1=None,arg2=None,arg3=None,arg4=None,arg5=None,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(syscall=syscall,arg1=arg1,arg2=arg2,arg3=arg3,arg4=arg4,arg5=arg5,arg0=arg0,pageargs=pageargs)
        str = context.get('str', UNDEFINED)
        zip = context.get('zip', UNDEFINED)
        repr = context.get('repr', UNDEFINED)
        dict = context.get('dict', UNDEFINED)
        unicode = context.get('unicode', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        any = context.get('any', UNDEFINED)
        __M_writer = context.writer()

        from pwnlib.shellcraft import i386, pretty
        from pwnlib.constants import Constant
        from pwnlib.abi import linux_i386_syscall as abi
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['abi','i386','Constant','pretty'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')

        append_cdq = False
        if isinstance(syscall, (str, unicode, Constant)) and str(syscall).startswith('SYS_'):
            syscall_repr = str(syscall)[4:] + "(%s)"
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
                args.append(pretty(arg, False))
        while args and args[-1] == '?':
            args.pop()
        syscall_repr = syscall_repr % ', '.join(args)
        
        registers = abi.register_arguments
        arguments = [syscall, arg0, arg1, arg2, arg3, arg4, arg5]
        regctx    = dict(zip(registers, arguments))
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['regctx','args','registers','arguments','arg','append_cdq','syscall_repr'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'    /* call ')
        __M_writer(unicode(syscall_repr))
        __M_writer(u' */\n')
        if any(a is not None for a in arguments):
            __M_writer(u'    ')
            __M_writer(unicode(i386.setregs(regctx)))
            __M_writer(u'\n')
        __M_writer(u'    int 0x80\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"75": 100, "68": 96, "37": 5, "38": 6, "39": 70, "40": 71, "73": 98, "74": 98, "71": 97, "81": 75, "16": 7, "17": 6, "72": 98, "70": 96, "29": 1, "69": 96}, "uri": "i386/linux/syscall.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/linux/syscall.asm"}
__M_END_METADATA
"""
