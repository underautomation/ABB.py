from enum import IntEnum

class RapidModuleAttribute(IntEnum):
	'''A property declared on a module, which restricts what may be done with it'''
	Unknown = 0 # The controller reported an attribute this library does not know
	SystemModule = 1 # The module belongs to the system rather than to the program
	Encoded = 2 # The source of the module is encoded and cannot be read back
	NoView = 3 # The source of the module may not be displayed
	NoStepIn = 4 # Execution may not step into the routines of the module
	ViewOnly = 5 # The source may be displayed but not changed
	ReadOnly = 6 # The module may not be changed
