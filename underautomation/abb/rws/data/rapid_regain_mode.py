from enum import IntEnum

class RapidRegainMode(IntEnum):
	'''What the robot does about the distance between where it stands and where the path it is about to resume expects it to be'''
	Continue_ = 0 # Resume from the current position without moving back to the path
	Regain = 1 # Move back onto the path before resuming
	Clear = 2 # Drop the path and resume from the current position
	EnterConsume = 3 # Resume by entering the consumption of the already generated path
