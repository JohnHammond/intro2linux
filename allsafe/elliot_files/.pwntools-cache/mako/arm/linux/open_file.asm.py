# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.651038
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/arm/linux/open_file.asm'
_template_uri = 'arm/linux/open_file.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u'Opens a file. Leaves the file descriptor in r0.\n\nArgs:\n  filepath(str): The file to open.\n  flags(int/str): The flags to call open with.\n  mode(int/str): The attribute to create the flag. Only matters of ``flags & O_CREAT`` is set.\n'
def render_body(context,filepath,flags='O_RDONLY',mode=420,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,flags=flags,mode=mode,filepath=filepath)
        int = context.get('int', UNDEFINED)
        hex = context.get('hex', UNDEFINED)
        repr = context.get('repr', UNDEFINED)
        long = context.get('long', UNDEFINED)
        len = context.get('len', UNDEFINED)
        str = context.get('str', UNDEFINED)
        ord = context.get('ord', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\n')
        __M_writer(u'\n')

        from pwnlib.shellcraft.common import label
        from pwnlib.asm import cpp
        from pwnlib.util.safeeval import expr
        from pwnlib.constants.linux import arm as consts
        filepath_lab, after = label("filepath"), label("after")
        filepath_out = [hex(ord(c)) for c in filepath]
        while True:
            filepath_out.append("0")
            if len(filepath_out) % 4 == 0:
                break
        filepath_out = ', '.join(filepath_out)
        
        if isinstance(mode, (int, long)):
            mode = hex(mode)
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['c','filepath_lab','expr','after','filepath_out','label','mode','consts','cpp'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        if expr(cpp("%s & O_CREAT" % flags, arch = 'arm', os = 'linux')):
            __M_writer(u'    mov r2, #(')
            __M_writer(unicode(mode))
            __M_writer(u')\n')
        __M_writer(u'    mov r1, #(')
        __M_writer(unicode(flags))
        __M_writer(u')\n    adr r0, ')
        __M_writer(unicode(filepath_lab))
        __M_writer(u'\n    svc SYS_open\n    b ')
        __M_writer(unicode(after))
        __M_writer(u'\n\n    /* The string ')
        __M_writer(unicode(repr(str(filepath))))
        __M_writer(u' */\n')
        __M_writer(unicode(filepath_lab))
        __M_writer(u': .byte ')
        __M_writer(unicode(filepath_out))
        __M_writer(u'\n\n')
        __M_writer(unicode(after))
        __M_writer(u':\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 2, "17": 1, "30": 1, "31": 8, "32": 9, "51": 24, "52": 25, "53": 26, "54": 26, "55": 26, "56": 28, "57": 28, "58": 28, "59": 29, "60": 29, "61": 31, "62": 31, "63": 33, "64": 33, "65": 34, "66": 34, "67": 34, "68": 34, "69": 36, "70": 36, "76": 70}, "uri": "arm/linux/open_file.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/arm/linux/open_file.asm"}
__M_END_METADATA
"""
