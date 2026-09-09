from enum import IntEnum

class RapidExecutionCycle(IntEnum):
	'''How many times the controller runs the program before stopping'''
	Unknown = 0 # The controller reported a cycle this library does not know
	Forever = 1 # The program runs again every time it reaches its end
	AsIs = 2 # The cycle currently configured is left untouched
	Once = 3 # The program runs once and stops at its end
	OnceDone = 4 # The program was asked to run once and has finished doing so
