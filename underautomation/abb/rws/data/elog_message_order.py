from enum import IntEnum

class ElogMessageOrder(IntEnum):
	'''Order in which the event log messages of a domain are returned'''
	NewestFirst = 0 # Most recent message first
	OldestFirst = 1 # Oldest message first
