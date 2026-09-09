from enum import IntEnum

class DeviceType(IntEnum):
	'''Represents the type of storage device'''
	Fixed = 0 # Fixed storage device (hard drive)
	Removable = 1 # Removable storage device (USB, SD card, etc.)
	RamDisk = 2 # RAM disk
	Remote = 3 # Remote or network storage
	Unknown = 4 # Unknown device type
