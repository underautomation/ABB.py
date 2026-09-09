from enum import IntEnum

class ControllerType(IntEnum):
	'''Type of the robot controller (real or virtual)'''
	Unknown = 0 # The controller type could not be determined
	RealController = 1 # Physical robot controller (RC)
	VirtualController = 2 # Virtual controller (VC), for example running in RobotStudio
