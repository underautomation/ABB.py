from enum import IntEnum

class MastershipHolder(IntEnum):
	'''Who holds the mastership of a domain'''
	Unknown = 0 # The controller reported a holder this library does not know
	None_ = 1 # Nobody holds the mastership, it is free to be taken
	Remote = 2 # A client connected over the network holds it, possibly this one
	Local = 3 # A device attached to the controller holds it, the teach pendant for instance
	Internal = 4 # The controller itself holds it, while it runs an operation that must not be interrupted
