from enum import IntEnum

class BackupState(IntEnum):
	'''State of the backup operation of the controller'''
	Unknown = 0 # The backup state could not be determined
	None_ = 1 # No backup operation
	InitState = 2 # A backup operation has been initialized
	BackupInProgress = 3 # A backup operation is running
	BackupReady = 4 # The backup operation finished successfully
	ErrorDuringBackup = 5 # The backup operation failed
	Invalid = 6 # The backup state is invalid
