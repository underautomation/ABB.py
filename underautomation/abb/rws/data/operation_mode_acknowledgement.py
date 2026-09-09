from enum import IntEnum

class OperationModeAcknowledgement(IntEnum):
	'''Pending change that an operating mode acknowledgement confirms'''
	Automatic = 0 # Confirms the switch to the automatic mode
	ManualFullSpeed = 1 # Confirms the switch to the manual full speed mode
	CollisionDetection = 2 # Confirms a collision detection
