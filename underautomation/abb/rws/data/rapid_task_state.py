from enum import IntEnum

class RapidTaskState(IntEnum):
	'''How far the controller has got in preparing the program of a task'''
	Unknown = 0 # The controller reported a state this library does not know
	Empty = 1 # The task holds no program
	Initiated = 2 # The task has been created but its program is not linked yet
	Linked = 3 # The program of the task is linked and ready to run
	Loaded = 4 # A program is loaded into the task but not linked yet
	Uninitialized = 5 # The task is not initialized
