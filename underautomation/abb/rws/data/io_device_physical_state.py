from enum import IntEnum

class IoDevicePhysicalState(IntEnum):
	'''Physical state of an I/O device'''
	Unknown = 0 # The physical state could not be determined
	Deactivated = 1 # The device is deactivated
	Running = 2 # The device is running
	Error = 3 # The device reports an error
	Unconnected = 4 # The device is not connected
	Unconfigured = 5 # The device is not configured
	Startup = 6 # The device is starting up
	Init = 7 # The device is initializing
	Halted = 8 # The device is halted
