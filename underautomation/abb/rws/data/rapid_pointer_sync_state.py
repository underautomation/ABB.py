from enum import IntEnum

class RapidPointerSyncState(IntEnum):
	'''Whether the pointers of every task are synchronized with each other'''
	Unknown = 0 # The controller reported a state this library does not know
	On = 1 # The pointers are synchronized
	Off = 2 # The pointers are not synchronized
