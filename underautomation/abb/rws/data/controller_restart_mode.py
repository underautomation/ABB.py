from enum import IntEnum

class ControllerRestartMode(IntEnum):
	'''Restart mode of the robot controller'''
	Restart = 0 # The controller will be restarted. The state is saved and any changed system parameter settings will be activated after the restart.
	Shutdown = 1 # The main computer will be shut down. Should be used if the controller UPS is broken.
	XStart = 2 # The controller will be restarted and the Boot Application will be started. The current system is saved and deactivated (the controller is non-functional, for advanced maintenance only).
	IStart = 3 # The controller will be restarted. The current system parameter settings and RAPID programs will be discarded, and the original system installation settings will be used.
	PStart = 4 # The controller will be restarted. The current RAPID programs and data will be discarded, but not the system parameter settings.
	BStart = 5 # The controller will be restarted. The last automatically saved system state will be loaded. Should be used to recover from a system crash.
