from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import BackupSystemInfo as backup_system_info

class BackupSystemInfo:
	'''Information about a backup stored on the controller file system. Returned by ControllerService.GetBackupInfo(backupPath).'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the BackupSystemInfo class'''
		if(_internal == 0):
			self._instance = backup_system_info()
		else:
			self._instance = _internal

	@property
	def system_name(self) -> str:
		'''Name of the backed up system'''
		return self._instance.SystemName

	@system_name.setter
	def system_name(self, value: str):
		self._instance.SystemName = value

	@property
	def robot_ware_version(self) -> str:
		'''RobotWare version of the backed up system. Only available when connected with version 1.'''
		return self._instance.RobotWareVersion

	@robot_ware_version.setter
	def robot_ware_version(self, value: str):
		self._instance.RobotWareVersion = value

	@property
	def robot_control_version(self) -> str:
		'''RobotControl version of the backed up system. Only available when connected with version 2.'''
		return self._instance.RobotControlVersion

	@robot_control_version.setter
	def robot_control_version(self, value: str):
		self._instance.RobotControlVersion = value

	@property
	def robot_os_version(self) -> str:
		'''RobotOS version of the backed up system. Only available when connected with version 2.'''
		return self._instance.RobotOsVersion

	@robot_os_version.setter
	def robot_os_version(self, value: str):
		self._instance.RobotOsVersion = value

	@property
	def options(self) -> typing.List[str]:
		'''Options installed on the backed up system'''
		return self._instance.Options

	@options.setter
	def options(self, value: typing.List[str]):
		self._instance.Options = value

	@property
	def option_count(self) -> int:
		'''Number of options installed on the backed up system'''
		return self._instance.OptionCount

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, BackupSystemInfo):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
