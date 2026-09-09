from __future__ import annotations
import typing
from underautomation.abb.rws.data.device_type import DeviceType
from underautomation.abb.rws.data.file_system_item import FileSystemItem
from UnderAutomation.ABB.Rws.Data import DeviceItem as device_item
from UnderAutomation.ABB.Rws.Data import DeviceType as device_type

class DeviceItem(FileSystemItem):
	'''Represents a device entry in the robot controller file system (e.g. C:, hd0a). Devices are returned alongside files and directories when listing the root path ("/") or any directory that contains mounted devices.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the DeviceItem class'''
		if(_internal == 0):
			self._instance = device_item()
		else:
			self._instance = _internal

	@property
	def device_type(self) -> DeviceType:
		'''Type of device (Fixed, Removable, RamDisk, Remote)'''
		return DeviceType(int(self._instance.DeviceType))

	@device_type.setter
	def device_type(self, value: DeviceType):
		self._instance.DeviceType = device_type(int(value))

	@property
	def total_space(self) -> int:
		'''Total storage space in bytes'''
		return self._instance.TotalSpace

	@total_space.setter
	def total_space(self, value: int):
		self._instance.TotalSpace = value

	@property
	def free_space(self) -> int:
		'''Free storage space in bytes'''
		return self._instance.FreeSpace

	@free_space.setter
	def free_space(self, value: int):
		self._instance.FreeSpace = value

	@property
	def is_enabled(self) -> bool:
		'''Indicates if the device is enabled'''
		return self._instance.IsEnabled

	@is_enabled.setter
	def is_enabled(self, value: bool):
		self._instance.IsEnabled = value

	@property
	def is_read_only(self) -> bool:
		'''Indicates if the device is read-only'''
		return self._instance.IsReadOnly

	@is_read_only.setter
	def is_read_only(self, value: bool):
		self._instance.IsReadOnly = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DeviceItem):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
