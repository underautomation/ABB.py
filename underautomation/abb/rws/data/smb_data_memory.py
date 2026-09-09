from enum import IntEnum

class SmbDataMemory(IntEnum):
	'''Which of the two copies of the serial measurement board data is erased'''
	Robot = 0 # The copy held by the robot itself
	Controller = 1 # The copy held by the controller cabinet
