from enum import IntEnum

class ControllerState(IntEnum):
	'''State of the robot controller, as reported by the control panel'''
	Unknown = 0 # The state could not be determined
	Init = 1 # The robot is starting up. It will shift to MotorsOff once it has started.
	MotorsOff = 2 # The robot is in a standby state where there is no power to its motors. The state has to be shifted to MotorsOn before the robot can move.
	MotorsOn = 3 # The robot is ready to move, either by jogging or by running programs
	GuardStop = 4 # The robot is stopped because the safety runchain is opened, for instance because a door of its cell is open
	EmergencyStop = 5 # The robot is stopped because the emergency stop was activated
	EmergencyStopReset = 6 # The robot is ready to leave the emergency stop state: the emergency stop is no longer activated, but the state transition is not confirmed yet.
	SystemFailure = 7 # The robot is in a system failure state and requires a restart
