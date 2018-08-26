# -*- coding: utf-8 -*-
# @Author: John Hammond
# @Date:   2016-08-25 00:29:22
# @Last Modified by:   John Hammond
# @Last Modified time: 2016-09-07 22:19:23

import json
import base64
import os
from colors.colors import *

class SaveEngineClass():

	def __init__( self, parent ):

		self.save_filename = '/tmp/training_wheels.log'
		self.loaded_data = None
		self.parent = parent
		

		if ( os.path.exists( self.save_filename ) ):
			self.save_handle = open( self.save_filename, 'r' )
		else:
			self.save_handle = open( self.save_filename, 'w' )


	def load( self ):
		if ( self.save_handle.closed ):
			self.save_handle = open( self.save_filename, 'r' )

		if ( self.save_handle.mode != 'r' ):
			self.save_handle.close()
			self.save_handle = open( self.save_filename, 'r' )


		try:
			self.loaded_data = json.loads( base64.b64decode( 
												 self.save_handle.read() ) )
		except ValueError:
			return False

			
		if self.loaded_data != {}:

			print M('''
It looks like you've used this tool before! I'll bring you right back to where 
you left off. If you'd like to revisit older lesson or concepts, enter `@help`!''')

			self.parent.LessonBook.load_lesson( self.loaded_data["current_lesson"] )
			self.parent.LessonBook.lesson_pointer = self.loaded_data["lesson_pointer"]
			self.parent.LessonBook.new_lesson_pointer = self.loaded_data["lesson_pointer"]


			return True


	def save( self, data ):
		if ( self.save_handle.closed ):
			self.save_handle = open( self.save_filename, 'w' )

		if ( self.save_handle.mode != 'w' ):
			self.save_handle.close()
			self.save_handle = open( self.save_filename, 'w' )

		self.save_handle.seek(0)
		self.save_handle.write( base64.b64encode( json.dumps( data ) ) )



	def __del__( self ):
		self.save_handle.close()