from enum import IntEnum

class IoFirmwareUpgradeStatus(IntEnum):
	'''Result of a firmware upgrade of an I/O device'''
	Unknown = 0 # The controller did not report a status, or it could not be parsed
	Error = 1 # The upgrade failed
	Ok = 2 # The upgrade finished, the firmware was already up to date
	Upgraded = 3 # The upgrade finished, the firmware was updated
	Pending = 4 # The upgrade is pending
