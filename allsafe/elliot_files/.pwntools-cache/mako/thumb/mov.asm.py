# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1473634653.756647
_enable_loop = True
_template_filename = '/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/thumb/mov.asm'
_template_uri = 'thumb/mov.asm'
_source_encoding = 'ascii'
_exports = []


__doc__ = u'\n    mov(dst, src)\n\n    Returns THUMB code for moving the specified source value\n    into the specified destination register.\n'
def render_body(context,dst,src,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(src=src,dst=dst,pageargs=pageargs)
        int = context.get('int', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        long = context.get('long', UNDEFINED)
        __M_writer = context.writer()
        from pwnlib.shellcraft import common 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['common'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n')
        __M_writer(u'\n')
        __M_writer(u'\n/* Set ')
        __M_writer(unicode(dst))
        __M_writer(u' = ')
        __M_writer(unicode(src))
        __M_writer(u' */\n')
        if not isinstance(src, (int, long)):
            __M_writer(u'    mov ')
            __M_writer(unicode(dst))
            __M_writer(u', ')
            __M_writer(unicode(src))
            __M_writer(u'\n')
        else:
            __M_writer(u'  ')

            srcu = src & 0xffffffff
            srcs = srcu - 2 * (srcu & 0x80000000)
              
            
            __M_locals_builtin_stored = __M_locals_builtin()
            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['srcs','srcu'] if __M_key in __M_locals_builtin_stored]))
            __M_writer(u'\n')
            if srcu == 0:
                __M_writer(u'    eor ')
                __M_writer(unicode(dst))
                __M_writer(u', ')
                __M_writer(unicode(dst))
                __M_writer(u'\n')
            elif srcu < 256:
                __M_writer(u'    mov ')
                __M_writer(unicode(dst))
                __M_writer(u', #')
                __M_writer(unicode(src))
                __M_writer(u'\n')
            elif -256 < srcs < 0:
                __M_writer(u'    eor ')
                __M_writer(unicode(dst))
                __M_writer(u', ')
                __M_writer(unicode(dst))
                __M_writer(u'\n    sub ')
                __M_writer(unicode(dst))
                __M_writer(u', #')
                __M_writer(unicode(-srcs))
                __M_writer(u'\n')
            else:
                __M_writer(u'    ')

                shift1 = 0
                while (1 << shift1) & src == 0:
                    shift1 += 1
                    
                
                __M_locals_builtin_stored = __M_locals_builtin()
                __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['shift1'] if __M_key in __M_locals_builtin_stored]))
                __M_writer(u'\n')
                if (0xff << shift1) & src == src:
                    if shift1 < 4:
                        __M_writer(u'        mov ')
                        __M_writer(unicode(dst))
                        __M_writer(u', #')
                        __M_writer(unicode(src >> shift1))
                        __M_writer(u'\n        lsl ')
                        __M_writer(unicode(dst))
                        __M_writer(u', #4\n        lsr ')
                        __M_writer(unicode(dst))
                        __M_writer(u', #{4 - shift1}\n')
                    else:
                        __M_writer(u'        mov ')
                        __M_writer(unicode(dst))
                        __M_writer(u', #')
                        __M_writer(unicode(src >> shift1))
                        __M_writer(u'\n        lsl ')
                        __M_writer(unicode(dst))
                        __M_writer(u', #')
                        __M_writer(unicode(shift1))
                        __M_writer(u'\n')
                else:
                    __M_writer(u'      ')

                    shift2 = 8
                    while (1 << shift2) & src == 0:
                        shift2 += 1
                          
                    
                    __M_locals_builtin_stored = __M_locals_builtin()
                    __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['shift2'] if __M_key in __M_locals_builtin_stored]))
                    __M_writer(u'\n')
                    if ((0xff << shift2) | 0xff) & src == src:
                        __M_writer(u'        mov ')
                        __M_writer(unicode(dst))
                        __M_writer(u', #')
                        __M_writer(unicode(src >> shift2))
                        __M_writer(u'\n        lsl ')
                        __M_writer(unicode(dst))
                        __M_writer(u', #')
                        __M_writer(unicode(shift2))
                        __M_writer(u'\n        add ')
                        __M_writer(unicode(dst))
                        __M_writer(u', #')
                        __M_writer(unicode(src & 0xff))
                        __M_writer(u'\n')
                    else:
                        __M_writer(u'        ')

                        shift3 = shift1 + 8
                        while (1 << shift3) & src == 0:
                            shift3 += 1
                                
                        
                        __M_locals_builtin_stored = __M_locals_builtin()
                        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['shift3'] if __M_key in __M_locals_builtin_stored]))
                        __M_writer(u'\n')
                        if ((0xff << shift1) | (0xff << shift3)) & src == src:
                            __M_writer(u'          mov ')
                            __M_writer(unicode(dst))
                            __M_writer(u', #')
                            __M_writer(unicode(src >> shift3))
                            __M_writer(u'\n          lsl ')
                            __M_writer(unicode(dst))
                            __M_writer(u', #')
                            __M_writer(unicode(shift3 - shift1))
                            __M_writer(u'\n          add ')
                            __M_writer(unicode(dst))
                            __M_writer(u', #')
                            __M_writer(unicode((src >> shift1) & 0xff))
                            __M_writer(u'\n          lsl ')
                            __M_writer(unicode(dst))
                            __M_writer(u', #')
                            __M_writer(unicode(shift1))
                            __M_writer(u'\n')
                        else:
                            __M_writer(u'            ')

                            id = common.label("value")
                            extra = ''
                            if (src & 0xff000000 == 0):
                                src = src | 0xff000000
                                extra = '\n '.join([
                                  "lsl %s, #8" % dst,
                                  "lsr %s, #8" % dst
                                ])
                                        
                            
                            __M_locals_builtin_stored = __M_locals_builtin()
                            __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['src','id','extra'] if __M_key in __M_locals_builtin_stored]))
                            __M_writer(u'\n            ldr ')
                            __M_writer(unicode(dst))
                            __M_writer(u', ')
                            __M_writer(unicode(id))
                            __M_writer(u'\n            b ')
                            __M_writer(unicode(id))
                            __M_writer(u'_after\n            ')
                            __M_writer(unicode(id))
                            __M_writer(u': .word ')
                            __M_writer(unicode(src))
                            __M_writer(u'\n            ')
                            __M_writer(unicode(id))
                            __M_writer(u'_after:\n            ')
                            __M_writer(unicode(extra))
                            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"16": 3, "17": 2, "25": 1, "29": 1, "30": 2, "31": 8, "32": 9, "33": 9, "34": 9, "35": 9, "36": 10, "37": 11, "38": 11, "39": 11, "40": 11, "41": 11, "42": 12, "43": 13, "44": 13, "51": 16, "52": 17, "53": 18, "54": 18, "55": 18, "56": 18, "57": 18, "58": 19, "59": 20, "60": 20, "61": 20, "62": 20, "63": 20, "64": 21, "65": 22, "66": 22, "67": 22, "68": 22, "69": 22, "70": 23, "71": 23, "72": 23, "73": 23, "74": 24, "75": 25, "76": 25, "84": 29, "85": 30, "86": 31, "87": 32, "88": 32, "89": 32, "90": 32, "91": 32, "92": 33, "93": 33, "94": 34, "95": 34, "96": 35, "97": 36, "98": 36, "99": 36, "100": 36, "101": 36, "102": 37, "103": 37, "104": 37, "105": 37, "106": 39, "107": 40, "108": 40, "116": 44, "117": 45, "118": 46, "119": 46, "120": 46, "121": 46, "122": 46, "123": 47, "124": 47, "125": 47, "126": 47, "127": 48, "128": 48, "129": 48, "130": 48, "131": 49, "132": 50, "133": 50, "141": 54, "142": 55, "143": 56, "144": 56, "145": 56, "146": 56, "147": 56, "148": 57, "149": 57, "150": 57, "151": 57, "152": 58, "153": 58, "154": 58, "155": 58, "156": 59, "157": 59, "158": 59, "159": 59, "160": 60, "161": 61, "162": 61, "175": 70, "176": 71, "177": 71, "178": 71, "179": 71, "180": 72, "181": 72, "182": 73, "183": 73, "184": 73, "185": 73, "186": 74, "187": 74, "188": 75, "189": 75, "195": 189}, "uri": "thumb/mov.asm", "filename": "/usr/local/lib/python2.7/dist-packages/pwnlib/shellcraft/templates/thumb/mov.asm"}
__M_END_METADATA
"""
