from enum import IntEnum

class RapidTaskExecutionMode(IntEnum):
	'''Stepping mode a task was last started with'''
	Unknown = 0 # The controller reported a mode this library does not know
	Continuous = 1 # The task runs without stepping
	StepOver = 2 # The task steps over the routine calls
	StepIn = 3 # The task steps into the routine calls
	StepOutOf = 4 # The task steps out of the current routine
	StepBack = 5 # The task steps backwards
	StepLast = 6 # The task steps to the last instruction
	StepWise = 7 # The task advances one instruction at a time
