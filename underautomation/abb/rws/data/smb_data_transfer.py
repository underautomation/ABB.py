from enum import IntEnum

class SmbDataTransfer(IntEnum):
	'''Which of the two copies of the serial measurement board data overwrites the other'''
	RobotToController = 0 # The copy held by the robot is written into the controller cabinet
	ControllerToRobot = 1 # The copy held by the controller cabinet is written into the robot
