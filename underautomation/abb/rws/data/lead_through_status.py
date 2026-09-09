from enum import IntEnum

class LeadThroughStatus(IntEnum):
	'''Whether an operator can push the robot arm around by hand'''
	Unknown = 0 # The controller reported a state this library does not know
	Active = 1 # The arm gives way when pushed
	Inactive = 2 # The arm holds its position
