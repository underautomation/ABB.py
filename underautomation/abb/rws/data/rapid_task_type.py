from enum import IntEnum

class RapidTaskType(IntEnum):
	'''Kind of RAPID task, which decides when the controller runs it'''
	Unknown = 0 # The controller reported a type this library does not know
	Normal = 1 # A task started and stopped together with the program
	Static = 2 # A task that keeps its program pointer where it was when the controller was switched off
	SemiStatic = 3 # A task restarted from its beginning every time the controller starts
