from enum import IntEnum

class CheckRestoreStatus(IntEnum):
	'''Result status of a backup restore check'''
	Unknown = 0 # The status could not be determined
	Accepted = 1 # The backup is accepted and can be restored
	RestoreMismatchSystemId = 2 # The backup was not created from the current system, there might be differences in active options and selected languages
	RestoreMismatchTemplateId = 3 # The current system and the backed up system may be generated from different key ids, possibly with different robot types
	DirectoryNotComplete = 4 # The backup directory is not complete
	ConfigurationDataIncorrect = 5 # Error in the configuration data of the backup
