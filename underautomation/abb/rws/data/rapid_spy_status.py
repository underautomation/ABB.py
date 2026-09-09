from enum import IntEnum

class RapidSpyStatus(IntEnum):
	'''Whether the controller is recording the RAPID execution trace to a file'''
	Unknown = 0 # The controller reported a status this library does not know
	Logging = 1 # The execution trace is being written
	NotLogging = 2 # No execution trace is being written
