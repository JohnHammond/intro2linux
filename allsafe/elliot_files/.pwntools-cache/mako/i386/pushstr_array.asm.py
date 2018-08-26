# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473636254.113084
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/pushstr_array.asm'
_template_uri = 'i386/pushstr_array.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u'\nPushes an array/envp-style array of pointers onto the stack.\n\nArguments:\n    reg(str):\n        Destination register to hold the pointer.\n    array(str,list):\n        Single argument or list of arguments to push.\n        NULL termination is normalized so that each argument\n        ends with exactly one NULL byte.\n'
def render_body(context,reg,array,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(array=array,reg=reg,pageargs=pageargs)
        reversed = context.get('reversed', UNDEFINED)
        repr = context.get('repr', UNDEFINED)
        len = context.get('len', UNDEFINED)
        str = context.get('str', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        __M_writer = context.writer()
        from pwnlib.shellcraft import i386 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['i386'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')

        if isinstance(array, (str)):
            array = [array]
        
        array_str = ''
        
        # Normalize all of the arguments' endings
        array      = [arg.rstrip('\x00') + '\x00' for arg in array]
        array_str  = ''.join(array)
        
        word_size = 4
        offset = len(array_str) + word_size
        
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['word_size','array','offset','array_str','arg'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'    /* push argument array ')
        __M_writer(unicode(repr(array)))
        __M_writer(u' */\n    ')
        __M_writer(unicode(i386.pushstr(array_str)))
        __M_writer(u'\n    ')
        __M_writer(unicode(i386.mov(reg, 0)))
        __M_writer(u'\n    push ')
        __M_writer(unicode(reg))
        __M_writer(u' /* null terminate */\n')
        for i,arg in enumerate(reversed(array)):
            __M_writer(u'    ')
            __M_writer(unicode(i386.mov(reg, offset + word_size*i - len(arg))))
            __M_writer(u'\n    add ')
            __M_writer(unicode(reg))
            __M_writer(u', esp\n    push ')
            __M_writer(unicode(reg))
            __M_writer(u' /* ')
            __M_writer(unicode(repr(arg)))
            __M_writer(u' */\n    ')
            offset -= len(arg) 
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['offset'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'    ')
        __M_writer(unicode(i386.mov(reg,'esp')))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 2, "17": 13, "28": 1, "32": 1, "33": 12, "34": 13, "35": 14, "52": 28, "53": 28, "54": 28, "55": 29, "56": 29, "57": 30, "58": 30, "59": 31, "60": 31, "61": 32, "62": 33, "63": 33, "64": 33, "65": 34, "66": 34, "67": 35, "68": 35, "69": 35, "70": 35, "71": 36, "75": 38, "76": 38, "77": 38, "83": 77}, "uri": "i386/pushstr_array.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/i386/pushstr_array.asm"}
__M_END_METADATA
"""
