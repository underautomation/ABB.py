from enum import IntEnum

class CyclicBrakeCheckTestStatus(IntEnum):
	'''Result of the last cyclic brake check test'''
	Unknown = 0 # The test status could not be determined
	Ok = 1 # The last brake check succeeded (CBC_TEST_OK)
	Warning = 2 # The last brake check ended with a warning (CBC_TEST_WARNING)
	Error = 3 # The last brake check failed (CBC_TEST_ERROR)
	Undefined = 4 # No brake check has been performed yet (CBC_TEST_UNDEFINED)
