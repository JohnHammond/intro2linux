# -*- coding: utf-8 -*-
# @Author: John Hammond
# @Date:   2016-08-25 00:02:23
# @Last Modified by:   John Hammond
# @Last Modified time: 2016-10-04 00:19:33

import os
import textwrap
import readline
import colorama
import sys
import socket
import subprocess

from colors.colors import *
from save_engine.save_engine import SaveEngineClass
from lessons.lesson_book import LessonBookClass

class TrainingWheelsShellClass():

	def __init__( self ):


		self.SaveEngine = SaveEngineClass( parent = self )
		self.LessonBook = LessonBookClass( parent = self )

		self.using_time = True
		self.time_on = True

		self.entered_input = ""

		self.commands = {
			"@help" 		: 		self.do_help,		
			"@lessons" 		:	 	self.LessonBook.select_lesson,
			"@concepts" 	:	 	self.LessonBook.select_concept,
		}

		self.special_cases = {
			"quit": self.say_goodbye,
			"cd": self.change_directory,
			"nano": self.protect_from_nano,
			"sudo passwd guest": self.change_guest_password,
		}

	def change_guest_password(self):
		# Have to run it this way so the line handling happens correctly...
		os.system("sudo passwd guest")

	def protect_from_nano(self):
		print R("Training Wheels cannot handle running nano!")
		print R("The line buffering causes it to choke... sorry!")

	def change_directory( self ):

		to_directory = " ".join( self.entered_input.split(" ")[1:] )
		
		to_directory = to_directory.replace("~", os.environ['HOME'] )

		if ( to_directory == '' ):
			os.chdir(os.environ['HOME'])
			
		else:
			try:
				os.chdir(to_directory)
			except OSError:
				print "bash: cd: " + to_directory + ": No such file or directory"

	def do_help( self ):

		print \
		textwrap.dedent('''

	@help:		View this help message.
	@lessons:	Select from a menu of lessons what to study from.
	@concepts:	Choose a concept from the lesson that you are on.

	TO ADD: @setspeed

		''' )


	def error( self, e ):
		print colorama.Back.BLACK + R("Oh no! I hit an error!")
		print r("\n" + str(e.__repr__())), colorama.Back.RESET
		print r("\n" + e.child_traceback), colorama.Back.RESET



	def prompt( self ):

		if ( self.using_time and self.time_on ):
			self.time_on = False

		ps1 = "".join([	

						colorama.Fore.MAGENTA, colorama.Style.BRIGHT, 
						"TRAINING WHEELS SHELL: ",
						colorama.Fore.GREEN, colorama.Style.BRIGHT, 
						os.environ['USER'], '@', socket.gethostname(), 
						colorama.Fore.BLUE,
						" ", os.getcwd(), " $ ", 
						colorama.Fore.MAGENTA, colorama.Style.BRIGHT, 
						". . .",
						colorama.Style.NORMAL, colorama.Fore.RESET,
						"\n"
					  ]).replace( os.environ["HOME"], "~" )
		
		sys.stdout.write(ps1)
		self.entered_input = raw_input(   ).strip()
		sys.stdin.flush()
		readline.add_history( self.entered_input )

	def say_goodbye( self ):

		print C("\n\nGoodbye!") 
		print B("_" * 78 + "\n")
		exit()


	def process( self ):

		if self.entered_input == "": return

		command = self.entered_input.split(" ")[0]
		if command in self.special_cases.iterkeys():
			# Run the corresponding function that follows the 
			self.special_cases[command]()
			return True
		if self.entered_input in self.commands.iterkeys():
			# Run the corresponding function that follows the 
			self.commands[self.entered_input]()
			raise KeyboardInterrupt
			# return 
		


		''' If they actually entered something, treat it as a command '''
		try:
			p = subprocess.Popen(	#self.entered_input.split(), 
									self.entered_input, 
									shell = True,
									stdout = subprocess.PIPE, 
									stdin=subprocess.PIPE,
								)

			while ( p ):
				try:
					sys.stdout.write( self.LessonBook.something_to_say_inbetween )
					sys.stdout.write( p.stdout.next() )
				except StopIteration:
					break

		except OSError as e:
			print self.entered_input + ": command not found"



	def run( self ):
		''' The main loop of the program is here, creating the shell...'''

		if (not self.SaveEngine.load() ):

			self.LessonBook.select_lesson()
			self.LessonBook.select_concept()

		while ( True ):

			try:
				
				self.LessonBook.go()

			except KeyboardInterrupt:
				self.time_on = False
				sys.stdout.write("^C\n")
				continue

			except Exception as e:
				self.error(e)