from enum import IntEnum

class RapidSymbolVariableType(IntEnum):
	'''Which variables a symbol search keeps, by what may be done with them'''
	Undefined = 0 # Let the controller decide
	ReadWrite = 1 # Only the variables that can be read and written
	ReadOnly = 2 # Only the variables that can be read but not written
	Loop = 3 # Only the loop variables
	Any = 4 # Any of them
