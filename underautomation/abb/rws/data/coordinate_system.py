from enum import IntEnum

class CoordinateSystem(IntEnum):
	'''Reference frame a cartesian position is expressed in'''
	Unknown = 0 # The controller reported a frame this library does not know
	World = 1 # The world frame, shared by every mechanical unit of the system
	Base = 2 # The base frame of the mechanical unit
	Tool = 3 # The frame of the active tool
	WorkObject = 4 # The frame of the active work object
