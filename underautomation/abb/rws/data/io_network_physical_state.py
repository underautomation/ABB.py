from enum import IntEnum

class IoNetworkPhysicalState(IntEnum):
	'''Physical state of an I/O network'''
	Unknown = 0 # The physical state could not be determined
	Halted = 1 # The network is halted
	Running = 2 # The network is running
	Error = 3 # The network reports an error
	Startup = 4 # The network is starting up
	Init = 5 # The network is initializing
