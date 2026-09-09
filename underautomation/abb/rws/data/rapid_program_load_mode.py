from enum import IntEnum

class RapidProgramLoadMode(IntEnum):
	'''What happens to the modules already in a task when a program is loaded into it'''
	Add = 0 # Keep the modules already loaded and add the ones of the program
	Replace = 1 # Replace everything the task holds with the program
