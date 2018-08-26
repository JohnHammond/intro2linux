# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473791889.606094
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwntools-3.2.0.dev0-py2.7.egg/pwnlib/shellcraft/templates/i386/linux/execve.asm'
_template_uri = 'i386/linux/execve.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u"\nExecute a different process.\n\nAttempts to perform some automatic detection of types.\nOtherwise, the arguments behave as normal.\n\n- If ``path`` is a string that is not a known register,\n  it is pushed onto the stack.\n- If ``argv`` is an array of strings, it is pushed onto\n  the stack, and NULL-terminated.\n- If ``envp`` is an dictionary of {string:string},\n  it is pushed onto the stack, and NULL-terminated.\n\nExample:\n\n    >>> path = '/bin/sh'\n    >>> argv = ['sh', '-c', 'echo Hello, $NAME; exit $STATUS']\n    >>> envp = {'NAME': 'zerocool', 'STATUS': 3}\n    >>> sc = shellcraft.i386.linux.execve(path, argv, envp)\n    >>> io = run_assembly(sc)\n    >>> io.recvall()\n    'Hello, zerocool\\n'\n    >>> io.poll(True)\n    3\n"
def render_body(context,path='/bin///sh',argv=0,envp=0,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(path=path,pageargs=pageargs,envp=envp,argv=argv)
        dict = context.get('dict', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        list = context.get('list', UNDEFINED)
        str = context.get('str', UNDEFINED)
        tuple = context.get('tuple', UNDEFINED)
        __M_writer = context.writer()

        from pwnlib.shellcraft import i386, registers
        from pwnlib.abi import linux_i386_syscall as abi
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['abi','i386','registers'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')

        if isinstance(envp, dict):
            envp = ['%s=%s' % (k,v) for (k,v) in envp.items()]
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['k','envp','v'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        if isinstance(argv, (list, tuple)):
            __M_writer(u'    ')
            __M_writer(unicode(i386.pushstr_array(abi.register_arguments[3], argv)))
            __M_writer(u'\n    ')
            argv = abi.register_arguments[3] 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['argv'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
        if isinstance(envp, (list, tuple)):
            __M_writer(u'    ')
            __M_writer(unicode(i386.pushstr_array(abi.register_arguments[2], envp)))
            __M_writer(u'\n    ')
            envp = abi.register_arguments[2] 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['envp'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
        if isinstance(path, str) and not registers.is_register(path):
            __M_writer(u'    ')
            __M_writer(unicode(i386.pushstr(path)))
            __M_writer(u'\n    ')
            path = 'esp' 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['path'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
        __M_writer(u'    ')
        __M_writer(unicode(i386.syscall('SYS_execve', path, argv, envp)))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 5, "17": 30, "27": 1, "34": 4, "35": 29, "36": 30, "37": 31, "44": 34, "45": 35, "46": 36, "47": 36, "48": 36, "49": 37, "53": 37, "54": 39, "55": 40, "56": 40, "57": 40, "58": 41, "62": 41, "63": 43, "64": 44, "65": 44, "66": 44, "67": 45, "71": 45, "72": 47, "73": 47, "74": 47, "80": 74}, "uri": "i386/linux/execve.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwntools-3.2.0.dev0-py2.7.egg/pwnlib/shellcraft/templates/i386/linux/execve.asm"}
__M_END_METADATA
"""
