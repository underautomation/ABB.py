from enum import IntEnum

class CyclicBrakeCheckState(IntEnum):
	'''Cyclic brake check state of a mechanical unit'''
	Unknown = 0 # The state could not be determined
	Ok = 1 # No brake check is needed (CBC_STATUS_OK)
	PreWarning = 2 # A brake check will soon be required (CBC_STATUS_PREWARNING)
	Required = 3 # A brake check is required (CBC_STATUS_REQUIRE_CBC)
