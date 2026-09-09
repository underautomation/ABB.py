from enum import IntEnum

class RapidStartCondition(IntEnum):
	'''Condition the controller checks before it starts executing'''
	None_ = 0 # Start without any additional check
	CallChain = 1 # Start only when the call chain of the program pointer is still valid
