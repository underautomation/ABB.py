from enum import IntEnum

class SystemEnergyState(IntEnum):
	'''State of the energy measurement of the controller'''
	Unknown = 0 # The energy state could not be determined
	Blocked = 1 # Energy measurement is blocked and no new value is produced
	Paused = 2 # Energy measurement is paused
	NotPaused = 3 # Energy measurement is running
	Resuming = 4 # Energy measurement is being resumed
	Pausing = 5 # Energy measurement is being paused
	GoingToSleep = 6 # The controller is entering its low energy consumption mode
	Sleep = 7 # The controller is in its low energy consumption mode
