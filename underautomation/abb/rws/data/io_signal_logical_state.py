from enum import IntEnum

class IoSignalLogicalState(IntEnum):
	'''Logical state of an I/O signal'''
	Unknown = 0 # The logical state could not be determined
	Simulated = 1 # The signal is simulated: its logical value is forced and no longer follows the physical value
	NotSimulated = 2 # The signal is not simulated
