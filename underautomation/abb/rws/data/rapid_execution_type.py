from enum import IntEnum

class RapidExecutionType(IntEnum):
	'''What kind of code a task is currently running'''
	Unknown = 0 # The controller reported a type this library does not know
	None_ = 1 # Nothing is running
	Normal = 2 # The normal program is running
	Interrupt = 3 # An interrupt is running
	ExternalInterrupt = 4 # An external interrupt is running
	UserRoutine = 5 # A user routine is running
	EventRoutine = 6 # An event routine is running
