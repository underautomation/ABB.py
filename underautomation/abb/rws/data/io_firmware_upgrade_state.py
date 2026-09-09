from enum import IntEnum

class IoFirmwareUpgradeState(IntEnum):
	'''Progress of a firmware upgrade of an I/O device'''
	Unknown = 0 # The state is unknown, or could not be parsed
	Automatic = 1 # The upgrade is performed automatically
	Manual = 2 # The upgrade has to be started manually
	Info = 3 # The firmware information is being collected
	Allocate = 4 # The upgrade resources are being allocated
	Start = 5 # The upgrade is starting
	Running = 6 # The upgrade is running
	RunningStartReceived = 7 # The device acknowledged the start of the upgrade
	RunningCheckInProgress = 8 # The firmware is being checked
	RunningEraseInProgress = 9 # The device memory is being erased
	RunningBurnInProgress = 10 # The firmware is being written to the device
	RunningEndReceived = 11 # The device acknowledged the end of the upgrade
	Check = 12 # The upgraded firmware is being verified
	Deallocate = 13 # The upgrade resources are being released
	Finished = 14 # The upgrade is finished
