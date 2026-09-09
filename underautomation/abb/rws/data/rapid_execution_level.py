from enum import IntEnum

class RapidExecutionLevel(IntEnum):
	'''Level at which the code of a task is currently executing'''
	Unknown = 0 # The controller reported a level this library does not know
	None_ = 1 # Nothing is executing
	Normal = 2 # The normal user code is executing
	Trap = 3 # A trap routine is executing
	User = 4 # A user routine is executing
