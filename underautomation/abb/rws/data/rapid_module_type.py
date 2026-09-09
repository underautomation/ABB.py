from enum import IntEnum

class RapidModuleType(IntEnum):
	'''Whether a module belongs to the program or to the system'''
	Unknown = 0 # The controller reported a type this library does not know
	ProgramModule = 1 # A module of the program, saved and loaded with it
	SystemModule = 2 # A module of the system, which survives loading another program
