from enum import IntEnum

class IoDeviceLogicalState(IntEnum):
	'''Logical state of an I/O device'''
	Unknown = 0 # The logical state could not be determined
	Enabled = 1 # The device is enabled
	Disabled = 2 # The device is disabled
