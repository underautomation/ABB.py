from enum import IntEnum

class JogMode(IntEnum):
	'''How the jogging commands sent to a mechanical unit are interpreted'''
	Unknown = 0 # The controller reported a mode this library does not know
	AxisGroup1 = 1 # Each command moves one axis of the first axis group
	AxisGroup2 = 2 # Each command moves one axis of the second axis group
	Cartesian = 3 # The tool is moved along the axes of the active coordinate system
	Align = 4 # The tool is aligned with the closest axis of the active coordinate system
	GoToPosition = 5 # The robot moves to a given position
	ConfigurationJog = 6 # The robot changes axis configuration without moving the tool center point
