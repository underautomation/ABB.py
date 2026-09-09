from enum import IntEnum

class RapidObjectListType(IntEnum):
	'''Which of the lists a RAPID object holds is being asked about'''
	Statements = 0 # The statements of the object
	BackwardStatements = 1 # The statements of its BACKWARD handler
	ErrorStatements = 2 # The statements of its ERROR handler
	UndoStatements = 3 # The statements of its UNDO handler
	TypeDeclarations = 4 # The type declarations it holds
	DataDeclarations = 5 # The data declarations it holds
	ParameterDeclarations = 6 # The parameter declarations it holds
	RoutineDeclarations = 7 # The routine declarations it holds
	Attributes = 8 # The attributes it declares
