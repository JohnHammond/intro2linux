# -*- coding: utf-8 -*-
# @Author: John Hammond
# @Date:   2016-08-24 23:44:30
# @Last Modified by:   John Hammond
# @Last Modified time: 2016-08-25 08:56:38

import os
from colors.colors import *
from shell import TrainingWheelsShellClass

class TrainingWheelsWrapperClass():

	def __init__( self ):
		
		os.system("clear")
		print 	B("_" * 79 + "\n\n" ) + c(\
" ... this tool was developed by John Hammond. If you're curious about it, ask!\n"+
			  	B("_" * 79 + "\n\n"))


	def run( self ):

		TraingWheelsShell = TrainingWheelsShellClass()
		TraingWheelsShell.run()