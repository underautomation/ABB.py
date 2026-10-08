from enum import IntEnum

class RwsVersion(IntEnum):
	'''Version of the ABB Robot Web Services (RWS) protocol exposed by the robot controller. The two versions differ in URL shapes, parameter placement and media types, so the client has to know which one it talks to. Pick the value that matches the controller generation.'''
	Irc5_V1_0 = 10 # RWS 1.0, exposed by IRC5 controllers running RobotWare 6 and earlier.
	OmniCore_V2_0 = 20 # RWS 2.0, exposed by OmniCore controllers running RobotWare 7 and later. This is the default when no version is specified.
