from enum import IntEnum

class ControllerLevel(IntEnum):
	'''Level the controller is currently running at'''
	Unknown = 0 # The controller level could not be determined
	SystemLevel = 1 # A system is loaded and running (system level)
	BootLevel = 2 # The controller runs the boot application (bootserver mode)
