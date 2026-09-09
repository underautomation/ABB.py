from enum import IntEnum

class RapidHoldToRunState(IntEnum):
	'''State of the hold-to-run control that gates RAPID execution in manual mode'''
	Press = 0 # Ask for execution to be allowed to start
	Held = 1 # Confirm that execution may keep running, which has to be repeated about every two seconds
	Release = 2 # Stop execution immediately
