from enum import IntEnum

class ElogMessageType(IntEnum):
	'''Severity of an event log message'''
	Unknown = 0 # The message type could not be determined
	Information = 1 # State change, or informational event
	Warning = 2 # Warning event
	Error = 3 # Error event
