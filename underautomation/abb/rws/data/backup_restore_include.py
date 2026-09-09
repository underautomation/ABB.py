from enum import IntEnum

class BackupRestoreInclude(IntEnum):
	'''Content included when restoring a backup'''
	All = 0 # Restore configuration files and RAPID modules
	Cfg = 1 # Restore configuration files only
	Modules = 2 # Restore RAPID modules only
