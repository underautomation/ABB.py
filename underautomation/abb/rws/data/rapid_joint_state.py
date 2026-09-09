from enum import IntEnum

class RapidJointState(IntEnum):
	'''What an external joint of a task is doing'''
	Unknown = 0 # The controller reported a state this library does not know
	Linear = 1 # The joint moves along a line
	Rotating = 2 # The joint turns
	NotActive = 3 # The joint is not active
	NoPosition = 4 # The joint is active but has no position
