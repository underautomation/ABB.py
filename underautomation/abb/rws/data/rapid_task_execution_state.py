from enum import IntEnum

class RapidTaskExecutionState(IntEnum):
	'''Whether a single task is running, and whether it could be'''
	Unknown = 0 # The controller reported a state this library does not know
	Ready = 1 # The task is ready to be started
	Stopped = 2 # The task was running and has been stopped
	Started = 3 # The task is running
	Uninitialized = 4 # The task is not initialized
