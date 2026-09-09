from enum import IntEnum

class MechanicalUnitMode(IntEnum):
	'''Whether a mechanical unit is activated and can be moved'''
	Unknown = 0 # The controller reported a mode this library does not know
	Activated = 1 # The mechanical unit is activated and takes part in the motion
	Deactivated = 2 # The mechanical unit is deactivated and stays where it is
