from enum import IntEnum

class IoSignalType(IntEnum):
	'''Type of an I/O signal'''
	Unknown = 0 # The signal type could not be determined
	DigitalOutput = 1 # Digital output
	DigitalInput = 2 # Digital input
	AnalogOutput = 3 # Analog output
	AnalogInput = 4 # Analog input
	GroupInput = 5 # Group input
	GroupOutput = 6 # Group output
