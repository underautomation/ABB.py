from enum import IntEnum

class IoClientAction(IntEnum):
	'''Action the client is expected to take after an I/O network auto configuration, returned by IoService.SetNetworkConfigurationType(). Only available when connected with version 2.'''
	Unknown = 0 # The controller did not report any client action. Always returned when connected with version 1, which does not report this information.
	None_ = 1 # Nothing to do
	Info = 2 # The user should be informed of the configuration result
	Restart = 3 # The controller has to be restarted for the configuration to take effect
