from enum import IntEnum

class OperationModeLockState(IntEnum):
	'''Lock state of the operating mode selector'''
	Unknown = 0 # The lock state could not be determined
	Error = 1 # The controller reports an error on the mode selector lock
	Unlocked = 2 # The operating mode can be changed freely
	Locked = 3 # The operating mode is locked and can be unlocked again with the pin code it was locked with
	PermanentlyLocked = 4 # The operating mode is permanently locked
	PendingPermanentLock = 5 # A permanent lock has been requested and is not effective yet
