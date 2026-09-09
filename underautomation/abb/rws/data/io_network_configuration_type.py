from enum import IntEnum

class IoNetworkConfigurationType(IntEnum):
	'''Configuration type applied to an I/O network by IoService.SetNetworkConfigurationType()'''
	Bits = 0 # Configure the signals of the network
	Groups = 1 # Configure the signal groups of the network
	Both = 2 # Configure both the signals and the signal groups
	Scan = 3 # Scan the network for connected devices
	Units = 4 # Configure the devices of the network
