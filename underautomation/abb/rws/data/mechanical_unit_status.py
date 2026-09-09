from enum import IntEnum

class MechanicalUnitStatus(IntEnum):
	'''Calibration and synchronization state of a mechanical unit or of one of its axes'''
	Unknown = 0 # The controller reported a state this library does not know
	Initiated = 1 # The unit is starting up
	NotCommutated = 2 # One or several motors have not been commutated
	NotCalibrated = 3 # The unit has never been calibrated
	NotAbsoluteSynchronized = 4 # One or several absolute measurement axes are not synchronized
	NotRelativeSynchronized = 5 # One or several relative measurement axes are not synchronized
	Synchronized = 6 # The unit is calibrated and synchronized, and can be moved
	Locked = 7 # The unit is locked and refuses to move
	LockedShow = 8 # The unit is locked, and the controller shows it as such
	Undefined = 9 # The controller knows the unit but does not report its state
