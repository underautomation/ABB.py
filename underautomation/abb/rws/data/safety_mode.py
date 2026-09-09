from enum import IntEnum

class SafetyMode(IntEnum):
	'''Safety mode of the safety controller'''
	Unknown = 0 # The safety mode could not be determined
	Active = 1 # The safety configuration is active and supervised
	Commissioning = 2 # Commissioning mode, used while configuring the safety controller
	Service = 3 # Service mode
	ModeError = 4 # The safety controller reports a mode error
