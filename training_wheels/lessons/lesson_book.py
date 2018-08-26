# -*- coding: utf-8 -*-
# @Author: John Hammond
# @Date:   2016-08-25 00:50:06
# @Last Modified by:   John Hammond
# @Last Modified time: 2016-10-04 00:59:00

import json
from colors.colors import *
import glob
import sys
import textwrap
import time
import curses
import os

class LessonBookClass(object):

	def __init__( self, parent, filename = "" ):

		self.parent = parent

		self.punction_stops = "\n.,!?-"

		path = os.path.dirname(os.path.realpath(__file__))
		# print path

		self.lesson_pointer = 0
		self.new_lesson_pointer = 0
		self.lesson_is_loaded = False
		self.selected_lesson_number = 0

		self.current_lesson = {}

		self.available_lessons = [file for file in 
					sorted(glob.glob(os.path.join(path, '.*.json')))]

		self.cleaned_available_lessons = [ 	

			l.split('/')[-1][1:].replace('.json','').\
							replace('lesson_','').\
							replace('_',' ')

			for l in self.available_lessons  ]

		self.seen_entries = {}
		self.something_to_say_inbetween = ""

	def say( self, message ):

		if ( not message.endswith('\n\n') ): message += '\n\n'

		for character in message:
			sys.stdout.write(character)
			sys.stdout.flush()
			if self.parent.using_time:
				if self.parent.time_on:
					if character in self.punction_stops:
						time.sleep(0.12)
					else:
						time.sleep(0.04)

	def is_in_directory( self, directory = None ):
		if directory == None: return True
		else: return os.getcwd() == directory.replace("~", os.environ["HOME"])

	def select_lesson( self ):

		if ( not self.lesson_is_loaded ):
			print M("\nIt looks like a lesson has not yet been loaded.")
		else:
			print M("\nYou already have ") + C(self.current_lesson["name"]) + M(" loaded.")
			print M("Load something else?")

			entered = False
			while ( not entered ):
				answer = raw_input("(y/n): ").lower()
				if answer == "yes" or answer == "y":
					self.lesson_is_loaded = False
					self.lesson_pointer = 0
					self.new_lesson_pointer = 0
					entered = True
					pass
				elif answer == "no" or answer == "n":
					return
				else:
					print R("\nPlease enter yes or no.")

		print M('''
Please select one of the available lessons by entering the corresponding number.
Enter the number '0' to go back to what you were doing.\n''')		

		for l in self.cleaned_available_lessons:
			print "\t", l
		print "\n\n"

		
		while ( not self.lesson_is_loaded ):
			print M("lesson #:"),
			self.selected_lesson_number = raw_input()

			if ( self.selected_lesson_number == "0" or self.selected_lesson_number == "quit" ):
				return

			try:
				self.selected_lesson_number = int( self.selected_lesson_number ) - 1
			except:
				print R("That does not look like a valid input. Please try again.")
				continue

			if ( self.selected_lesson_number >= 0 and 
				self.selected_lesson_number < len(self.available_lessons) ):

				print B("_"*79 + "\n")
				self.load_lesson( self.available_lessons[self.selected_lesson_number] )
				
				return
			else:
				print R("That does not look like a valid input. Please try again.")
				continue


	def go_to_next_lesson( self ):

		print M("It looks like you are all done with this lesson!")
		print M("I'm going to move you to the next one. You are now on lesson:\n")

		
		next_lesson_number = self.selected_lesson_number + 1

		if ( next_lesson_number >= len( self.available_lessons ) ):
			print( Y("Actually -- there are no more lessons!") )
			print( Y("You're all done for now... go practice Linux!") )
			self.parent.SaveEngine.save( "done" )
			exit()
		else:

			next_lesson_name = self.cleaned_available_lessons[next_lesson_number]
			print "\t" + next_lesson_name + "\n\n"

			self.lesson_pointer = 0
			self.new_lesson_pointer = 0
			self.selected_lesson_number += 1
			self.load_lesson( self.available_lessons[next_lesson_number] )

	def load_lesson( self, lesson_identifier ):

		try:
			self.file_handle = open(lesson_identifier, 'r')
		except IOError:
			# The file does not exist.
			raise Exception("This file does not exist!")
		
		self.current_lesson = json.loads( self.file_handle.read() )
		self.selected_lesson_number = int(self.current_lesson['name'].split(".")[0]) - 1
		
		self.lesson_is_loaded = True

	def select_concept( self ):
		if ( self.current_lesson == {} ):
			print R("There is currently no lesson loaded!")
			print R("Enter `@lessons` to select one to load.")
			return 

		print M('''
The current lesson that is loaded is: ''') + C(self.current_lesson["name"])+ M('''".

Please select one of the concepts you would like to jump to.
The lesson you are currently looking at is highlighted in '''+ y('yellow') + M('''.
Enter the number '0' to go back to what you were doing.\n'''))

		# Display all of the concepts that are available in that lesson.
		for i in range( len(self.current_lesson["concepts"]) ):
			number = str(i + 1)
			if i == self.lesson_pointer:
				print "\t" + Y( number + ". " +self.current_lesson["concepts"][i]["tag"])
			else:
				print "\t" + number + ". " + self.current_lesson["concepts"][i]["tag"]
		print "\n\n"
		

		selected = False
		
		while ( not selected ):
			print M("concept #:"),
			selected_concept_number = raw_input()

			if ( selected_concept_number == "0" or selected_concept_number == "quit" ):
				return

			try:
				selected_concept_number = int( selected_concept_number ) - 1
			except:
				print R("That does not look like a valid input. Please try again.")
				continue


			if ( selected_concept_number >= 0 and 
				selected_concept_number < len(self.current_lesson["concepts"]) ):

				
				self.lesson_pointer = selected_concept_number
				self.new_lesson_pointer = selected_concept_number
				print B("_"*79 + "\n")
				return
			else:
				print R("That does not look like a valid input. Please try again.")
				continue



	def go( self ):
		
		# Save all our progress so far.
		self.parent.SaveEngine.save( \
			{ 	"current_lesson" : self.available_lessons[self.selected_lesson_number],
				"lesson_pointer" : self.lesson_pointer } )

		current_lesson = self.current_lesson["concepts"][self.lesson_pointer]

		# Begin to load everything from the lesson and current concept...
		# if ( current_lesson.has_key("message") ): message = current_lesson["message"]

		if ( current_lesson.has_key("message") ): message = current_lesson["message"]

		if ( current_lesson.has_key("command_waiting") ): 
			command_waiting = current_lesson["command_waiting"]

			if ( current_lesson.has_key("proper_directory") ): 
				proper_directory = current_lesson["proper_directory"]
				if proper_directory.endswith('/'): proper_directory = proper_directory[:-1]
			else: proper_directory = None

			# print R(command_waiting) # This was for debugging...

			if ( current_lesson.has_key("incorrect") ): 
				incorrect = current_lesson["incorrect"]
			if self.current_lesson["concepts"][self.lesson_pointer].has_key("in_between_text"):
				self.something_to_say_inbetween = \
					R( self.current_lesson["concepts"][self.lesson_pointer]["in_between_text"] )
			else:
				self.something_to_say_inbetween = ""

		else:
			# This is the very end of the lesson. Say your last words and move on.
			self.say(C( message ))

			self.go_to_next_lesson()
			return


		while ( self.new_lesson_pointer == self.lesson_pointer ):
			
			# Prompt for this concept.
			time.sleep(1)
			self.say(C( message ))


			# Determine what we really want the user to type in.
			wanted_arguments = command_waiting.split()
			number_of_wanted_arguments = len(wanted_arguments)


			# While they have not entered their command, keep prompting.
			while (command_waiting not in self.seen_entries):

				self.parent.prompt()

				if ( self.is_in_directory( proper_directory ) ):

					# Analyze what they entered and determined if it is correct
					arguments = self.parent.entered_input.split()
					number_of_arguments = len(arguments)

					if ( number_of_arguments != number_of_wanted_arguments ):
						self.parent.process()
						print( Y("\n" + textwrap.dedent(incorrect) + "\n") )
						continue
						
					correct = True
					for arg in range(number_of_wanted_arguments):
						if wanted_arguments[arg] == "???":
							if number_of_wanted_arguments == number_of_arguments:
								continue
							else: correct = False
						if wanted_arguments[arg] != arguments[arg]:
							correct = False
					if correct:

						self.new_lesson_pointer += 1
						self.parent.time_on = True
				else:
					
					self.parent.process()

					if ( not self.is_in_directory( proper_directory ) ):
						print R( "\nYOU ARE IN THE WRONG DIRECTORY" )
						print R( "To continue, please change directory to '" + proper_directory + "'\n\n" )

					continue
				
				self.parent.process()

				if ( self.new_lesson_pointer == self.lesson_pointer ):
					print( Y("\n" + textwrap.dedent(incorrect) + "\n") )
				else:
					
					return # THIS NEEDS TO BE HERE FOR COMMANDS WITH ARGUMENTS

			self.something_to_say_inbetween = ""
			self.seen_entries = []

		else:
			self.lesson_pointer = self.new_lesson_pointer