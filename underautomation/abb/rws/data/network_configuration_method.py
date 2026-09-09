from enum import IntEnum

class NetworkConfigurationMethod(IntEnum):
	'''IP configuration method of a controller LAN adapter'''
	FixIp = 0 # Fixed IP address, the address, mask and gateway have to be provided
	Dhcp = 1 # IP address obtained from a DHCP server
	NoIp = 2 # No IP address configured on the adapter
