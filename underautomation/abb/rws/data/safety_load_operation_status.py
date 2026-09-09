from enum import IntEnum

class SafetyLoadOperationStatus(IntEnum):
	'''Indicates whether a new safety configuration is allowed to be loaded'''
	Unknown = 0 # The status could not be determined
	Ok = 1 # Loading a new safety configuration is allowed
	OptionNotPresent = 2 # The safety option is not present on the controller (SCORCH_ERR_OPTION_NOT_PRESENT)
	NotInManualMode = 3 # The controller is not in manual mode (SCORCH_ERR_NOT_IN_MANUAL_MODE)
	NotInMotorsOff = 4 # The motors are not switched off (SCORCH_ERR_NOT_IN_MOTORS_OFF)
	CurrentConfigurationLocked = 5 # The current safety configuration is locked (SCORCH_ERR_CURRENT_CONFIG_LOCKED)
	UserGrantMissing = 6 # The user does not have the required grant (SCORCH_ERR_USER_GRANT_IS_MISSING)
