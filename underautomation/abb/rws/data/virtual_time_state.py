from enum import IntEnum

class VirtualTimeState(IntEnum):
	'''State of the virtual time server of a virtual controller'''
	Unknown = 0 # The state could not be determined
	Stop = 1 # Virtual time is stopped (VTSTOP)
	FreeRun = 2 # Virtual time runs freely (VTFREERUN)
	RunSlice = 3 # Virtual time runs one time slice at a time (VTRUNSLICE)
	NextEvent = 4 # Virtual time runs until the next event (VTNEXTEVENT)
