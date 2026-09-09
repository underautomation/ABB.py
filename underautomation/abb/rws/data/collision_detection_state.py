from enum import IntEnum

class CollisionDetectionState(IntEnum):
	'''State of the collision detection of the robot controller'''
	Unknown = 0 # The collision detection state could not be determined
	Init = 1 # No collision has been detected since the controller started
	Triggered = 2 # A collision has been detected and is waiting to be confirmed
	Confirmed = 3 # A detected collision has been confirmed
	TriggeredAcknowledged = 4 # A detected collision has been acknowledged by an operator
