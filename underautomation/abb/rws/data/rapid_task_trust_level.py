from enum import IntEnum

class RapidTaskTrustLevel(IntEnum):
	'''What the controller does to the system when a task that is not a normal one stops unexpectedly'''
	Unknown = 0 # The controller reported a level this library does not know
	None_ = 1 # The system carries on
	SystemFailure = 2 # The whole system fails
	SystemHalt = 3 # The system halts
	SystemStop = 4 # The system stops
