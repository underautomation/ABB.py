from enum import IntEnum

class OperationMode(IntEnum):
	'''Operating mode selected on the robot controller'''
	Unknown = 0 # The operating mode could not be determined
	Init = 1 # The controller is initializing
	AutomaticChangeRequest = 2 # A change to the automatic mode has been requested and is waiting to be acknowledged
	ManualFullSpeedChangeRequest = 3 # A change to the manual full speed mode has been requested and is waiting to be acknowledged
	ManualReducedSpeed = 4 # Manual mode at reduced speed
	ManualFullSpeed = 5 # Manual mode at full speed
	Automatic = 6 # Automatic mode
	Undefined = 7 # The controller reports an undefined operating mode
