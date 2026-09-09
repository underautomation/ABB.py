from enum import IntEnum

class RapidExecutionMode(IntEnum):
	'''How far the program advances when execution is started'''
	Continue_ = 0 # Run until something stops it
	StepIn = 1 # Step into the routine called by the current instruction
	StepOver = 2 # Run the current instruction whole, without entering the routine it calls
	StepOut = 3 # Run until the current routine returns
	StepBack = 4 # Step one instruction backwards
	StepLast = 5 # Step to the last instruction
	StepMotion = 6 # Step to the next motion instruction
