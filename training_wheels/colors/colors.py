#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: john
# @Date:   2016-08-13 23:48:50
# @Last Modified by:   John Hammond
# @Last Modified time: 2016-09-30 22:14:21


from colorama import *

# These are meant to be shorthand function calls to quickly turn a string
# into something with color. 

def G(string): return Fore.GREEN + Style.BRIGHT + string + Fore.RESET + Style.NORMAL 
def g(string): return Fore.GREEN + string + Fore.RESET
def B(string): return Fore.BLUE + Style.BRIGHT + string + Fore.RESET + Style.NORMAL
def b(string): return Fore.BLUE + string + Fore.RESET
def R(string): return Fore.RED + Style.BRIGHT + string + Fore.RESET + Style.NORMAL
def r(string): return Fore.RED + string + Fore.RESET
def Y(string): return Fore.YELLOW + Style.BRIGHT + string + Fore.RESET + Style.NORMAL
def y(string): return Fore.YELLOW + string + Fore.RESET
def M(string): return Fore.MAGENTA + Style.BRIGHT + string + Fore.RESET + Style.NORMAL
def m(string): return Fore.MAGENTA + string + Fore.RESET
def C(string): return Fore.CYAN + Style.BRIGHT + string + Fore.RESET + Style.NORMAL
def c(string): return Fore.CYAN + string + Fore.RESET
def W(string): return Fore.WHITE + Style.BRIGHT + string + Fore.RESET + Style.NORMAL
def w(string): return Fore.WHITE + string + Fore.RESET 

def _G(string): return Back.GREEN + Style.BRIGHT + string + Back.RESET + Style.NORMAL
def _g(string): return Back.GREEN + string + Back.RESET
def _B(string): return Back.BLUE + Style.BRIGHT + string + Back.RESET + Style.NORMAL
def _b(string): return Back.BLUE + string + Back.RESET
def _R(string): return Back.RED + Style.BRIGHT + string + Back.RESET + Style.NORMAL
def _r(string): return Back.RED + string + Back.RESET
def _Y(string): return Back.YELLOW + Style.BRIGHT + string + Back.RESET + Style.NORMAL
def _y(string): return Back.YELLOW + string + Back.RESET
def _M(string): return Back.MAGENTA + Style.BRIGHT + string + Back.RESET + Style.NORMAL
def _m(string): return Back.MAGENTA + string + Back.RESET
def _C(string): return Back.CYAN + Style.BRIGHT + string + Back.RESET + Style.NORMAL
def _c(string): return Back.CYAN + string + Back.RESET
def _W(string): return Back.WHITE + Style.BRIGHT + string + Back.RESET + Style.NORMAL
def _w(string): return Back.WHITE + string + Back.RESET 