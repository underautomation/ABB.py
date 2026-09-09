from enum import IntEnum

class MechanicalUnitType(IntEnum):
	'''Kind of mechanical unit the controller drives'''
	Unknown = 0 # The controller reported a type this library does not know
	None_ = 1 # No mechanical unit
	TcpRobot = 2 # A robot arm holding a tool center point, which can be moved in cartesian coordinates
	Robot = 3 # A robot arm without a tool center point, which can only be moved axis by axis
	Single = 4 # A single external axis, such as a track or a positioner
	Undefined = 5 # The controller knows the unit but does not report what it is
