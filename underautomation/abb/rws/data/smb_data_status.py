from enum import IntEnum

class SmbDataStatus(IntEnum):
	'''State of one block of serial measurement board data, on the controller side or on the robot side'''
	Unknown = 0 # The controller reported a state this library does not know
	Valid = 1 # The data is present and the two copies agree
	ValidNotEqual = 2 # The data is present on both sides, but the two copies differ
	NotValid = 3 # The data is missing or unusable
	NotUsed = 4 # The robot system does not use this block of data
