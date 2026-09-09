from enum import IntEnum

class RapidSymbolType(IntEnum):
	'''What a RAPID symbol is: a value, a routine, a type or one of the structural elements of the language'''
	Unknown = 0 # The controller reported a type this library does not know
	Undefined = 1 # The type is not defined
	Atomic = 2 # A built-in type such as num or string
	Record = 3 # A record type
	Alias = 4 # An alias of another type
	RecordComponent = 5 # One component of a record
	Constant = 6 # A constant
	Variable = 7 # A variable
	Persistent = 8 # A persistent variable, whose value survives a restart
	Parameter = 9 # A parameter of a routine
	Label = 10 # A label
	ForVariable = 11 # The loop variable of a FOR statement
	Function = 12 # A function
	Procedure = 13 # A procedure
	Trap = 14 # A trap routine
	Module = 15 # A module
	Task = 16 # A task
	Any = 17 # Any of the other types, which a search uses to mean that it does not filter on the type
