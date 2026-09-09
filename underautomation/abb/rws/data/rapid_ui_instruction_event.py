from enum import IntEnum

class RapidUiInstructionEvent(IntEnum):
	'''What a UI instruction is asking of the client'''
	Unknown = 0 # The controller reported an event this library does not know
	Send = 1 # The instruction is waiting for an answer
	Post = 2 # The instruction only displays something and expects no answer
	Abort = 3 # The instruction has been abandoned and no answer is expected any more
