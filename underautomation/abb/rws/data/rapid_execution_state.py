from enum import IntEnum

class RapidExecutionState(IntEnum):
	'''Whether the controller is currently executing RAPID code'''
	Unknown = 0 # The controller reported a state this library does not know
	Running = 1 # RAPID execution is running
	Stopped = 2 # RAPID execution is stopped
