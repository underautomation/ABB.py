from enum import IntEnum

class RapidTaskScope(IntEnum):
	'''Whether an execution command applies to the normal tasks only or to every task'''
	Normal = 0 # Apply to the tasks the task selection panel has enabled
	AllTasks = 1 # Apply to every task of the system
