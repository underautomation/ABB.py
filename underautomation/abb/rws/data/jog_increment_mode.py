from enum import IntEnum

class JogIncrementMode(IntEnum):
	'''Size of the step a jogging command moves the robot by'''
	None_ = 0 # The robot moves for as long as the command is repeated, with no fixed step
	User = 1 # One step of the size configured in the system parameters
	Small = 2 # One small step
	Medium = 3 # One medium step
	Large = 4 # One large step
