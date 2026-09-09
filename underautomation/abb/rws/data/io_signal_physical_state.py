from enum import IntEnum

class IoSignalPhysicalState(IntEnum):
	'''Physical state of an I/O signal'''
	Unknown = 0 # The physical state could not be determined
	Valid = 1 # The physical value of the signal is valid
	Invalid = 2 # The physical value of the signal is not valid
