from enum import IntEnum

class RapidStopMode(IntEnum):
	'''How abruptly RAPID execution is stopped'''
	Cycle = 0 # Stop when the current cycle ends
	Instruction = 1 # Stop when the current instruction ends
	Stop = 2 # Stop as soon as the robot can decelerate along its path
	QuickStop = 3 # Stop as fast as the robot can, leaving the path
