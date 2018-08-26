# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.646727
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/arm/linux/egghunter.asm'
_template_uri = 'arm/linux/egghunter.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u'\n    egghunter(egg, start_address = 0, double_check = True)\n\n    Searches for an egg, which is either a four byte integer\n    or a four byte string. The egg must appear twice in a row\n    if double_check is True.\n    When the egg has been found the egghunter branches to the\n    address following it.\n    If start_address has been specified search will start on the\n    first address of the page that contains that address.\n'
def render_body(context,egg,start_address=0,double_check=True,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(start_address=start_address,pageargs=pageargs,egg=egg,double_check=double_check)
        int = context.get('int', UNDEFINED)
        Exception = context.get('Exception', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        long = context.get('long', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        from pwnlib.shellcraft.arm import mov 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['mov'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        from pwnlib.util.packing import unpack 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['unpack'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        from pwnlib import constants 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['constants'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n')

        if not isinstance(egg, (int, long)):
            if not len(egg) == 4:
                raise Exception('Egg should be either an integer or a four byte string')
            egg = unpack(egg)
        
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['egg'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\negghunter:\n    eor r1, r1, r1\n')
        if start_address < 1024:
            __M_writer(u'    mvn r2, r1\n')
        else:
            __M_writer(u'    ')
            __M_writer(unicode(mov('r2', (start_address & ~(4096-1)) - 1)))
            __M_writer(u'\n')
        __M_writer(u'\n    /* Put egg in r3 */\n    ')
        __M_writer(unicode(mov('r3', egg)))
        __M_writer(u'\n\nnext_page:\n    mvn r2, r2, lsr #0x0c\n    mvn r2, r2, lsl #0x0c\n\nnext_byte:\n    add r2, r2, #0x01\n\n')
        if double_check:
            __M_writer(u'    add r0, r2, #0x07\n')
        else:
            __M_writer(u'    add r0, r2, #0x03\n')
        __M_writer(u'    mov r7, #0x21\n    swi #0\n\n    /* EFAULT = ')
        __M_writer(unicode(constants.linux.arm.EFAULT))
        __M_writer(u' means unmapped memory */\n    cmn r0, #')
        __M_writer(unicode(constants.linux.arm.EFAULT))
        __M_writer(u'\n    beq next_page\n\n')
        if double_check:
            __M_writer(u'    ldm r2, {r4, r5}\n')
        else:
            __M_writer(u'    ldm r2, {r4}\n')
        __M_writer(u'\n    cmp r4, r3\n    bne next_byte\n')
        if double_check:
            __M_writer(u'    cmp r5, r3\n    bne next_byte\n')
        __M_writer(u'\negg_found:\n')
        if double_check:
            __M_writer(u'    add pc, r2, #0x08\n')
        else:
            __M_writer(u'    add pc, r2, #0x04\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 5, "17": 4, "27": 1, "31": 1, "32": 2, "36": 2, "37": 3, "41": 3, "42": 4, "43": 15, "44": 16, "53": 21, "54": 24, "55": 25, "56": 26, "57": 27, "58": 27, "59": 27, "60": 29, "61": 31, "62": 31, "63": 40, "64": 41, "65": 42, "66": 43, "67": 45, "68": 48, "69": 48, "70": 49, "71": 49, "72": 52, "73": 53, "74": 54, "75": 55, "76": 57, "77": 60, "78": 61, "79": 64, "80": 66, "81": 67, "82": 68, "83": 69, "89": 83}, "uri": "arm/linux/egghunter.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/arm/linux/egghunter.asm"}
__M_END_METADATA
"""
