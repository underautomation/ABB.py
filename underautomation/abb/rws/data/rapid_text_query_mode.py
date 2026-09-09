from enum import IntEnum

class RapidTextQueryMode(IntEnum):
	'''How hard the controller tries to apply a change to the source of a running task'''
	Force = 0 # Apply the change even when it invalidates the program pointer
	Try_ = 1 # Apply the change only when the program pointer survives it
