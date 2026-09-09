from enum import IntEnum

class RapidSymbolSearchView(IntEnum):
	'''Which part of the system a symbol search walks'''
	Undefined = 0 # Let the controller decide
	Block = 1 # Search the block the search path names, and optionally what it contains
	Scope = 2 # Search what is visible from a position of the source, which the search path and the position both have to be given for
	Stack = 3 # Search what is visible from a frame of the call stack, which needs the program pointer to be set
