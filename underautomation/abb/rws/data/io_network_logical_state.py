from enum import IntEnum

class IoNetworkLogicalState(IntEnum):
	'''Logical state of an I/O network'''
	Unknown = 0 # The logical state could not be determined
	Started = 1 # The network is started
	Stopped = 2 # The network is stopped
