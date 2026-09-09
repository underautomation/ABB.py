from enum import IntEnum

class BackupRestoreIgnore(IntEnum):
	'''Mismatches between a backup and the current system that are ignored when restoring'''
	None_ = 0 # No mismatch is ignored
	All = 1 # All mismatches are ignored
	SystemId = 2 # A mismatch between the system id of the backup and the system id of the current system is ignored
	TemplateId = 3 # A mismatch between the template id of the backup and the template id of the current system is ignored
