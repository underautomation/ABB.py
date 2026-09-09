from enum import IntEnum

class MotionErrorState(IntEnum):
	'''Last error the motion system ran into, most of them raised by a jogging request it could not honour'''
	Unknown = 0 # The controller reported an error this library does not know
	Ok = 1 # No error
	MechanicalUnitNotActive = 2 # A mechanical unit was jogged whose activation failed
	UncalibratedJogMotionType = 3 # An uncalibrated robot was jogged in a mode that needs its calibration
	UnnormalizedQuaternion = 4 # A quaternion that is not normalized reached the jogging task, from a tool, a load or a work object
	ErroneousToolMass = 5 # A load definition carries a negative mass
	RobotHoldMismatch = 6 # The tool and the work object disagree on which one the robot holds
	WorkObjectMechanicalUnitNotFound = 7 # A mechanical unit used in coordinated jogging was not found
	InvalidJogMotionType = 8 # The requested jogging mode is not valid
