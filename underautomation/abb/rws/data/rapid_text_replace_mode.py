from enum import IntEnum

class RapidTextReplaceMode(IntEnum):
	'''Where new text is put relative to the range it is written against'''
	After = 0 # Insert the new text after the range, leaving it in place
	Before = 1 # Insert the new text before the range, leaving it in place
	Replace = 2 # Replace the range with the new text
