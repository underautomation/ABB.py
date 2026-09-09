from __future__ import annotations
import typing
from underautomation.abb.rws.data.file_item import FileItem
from underautomation.abb.rws.data.directory_item import DirectoryItem
from underautomation.abb.rws.data.device_item import DeviceItem
from UnderAutomation.ABB.Rws.Data import DirectoryListing as directory_listing

class DirectoryListing:
	'''Represents a directory listing containing files, subdirectories, and devices. Returned by FileService.ListDirectory(path).When listing the root path ("/"), the array contains available storage devices (C:, hd0a, etc.).When listing a subdirectory, only and are typically populated.'''
	def __init__(self, path: str, _internal = 0):
		'''Initializes a new instance of the DirectoryListing class'''
		if(_internal == 0):
			self._instance = directory_listing(path)
		else:
			self._instance = _internal

	@property
	def files(self) -> typing.List[FileItem]:
		'''Files contained in this directory'''
		return [FileItem(x) for x in self._instance.Files]

	@files.setter
	def files(self, value: typing.List[FileItem]):
		self._instance.Files = [x._instance if x else None for x in value]

	@property
	def directories(self) -> typing.List[DirectoryItem]:
		'''Subdirectories contained in this directory'''
		return [DirectoryItem(x) for x in self._instance.Directories]

	@directories.setter
	def directories(self, value: typing.List[DirectoryItem]):
		self._instance.Directories = [x._instance if x else None for x in value]

	@property
	def devices(self) -> typing.List[DeviceItem]:
		'''Devices available in this listing (typically only present at root "/")'''
		return [DeviceItem(x) for x in self._instance.Devices]

	@devices.setter
	def devices(self, value: typing.List[DeviceItem]):
		self._instance.Devices = [x._instance if x else None for x in value]

	@property
	def path(self) -> str:
		'''Path that was listed'''
		return self._instance.Path

	@property
	def file_count(self) -> int:
		'''Number of files in this listing'''
		return self._instance.FileCount

	@property
	def directory_count(self) -> int:
		'''Number of subdirectories in this listing'''
		return self._instance.DirectoryCount

	@property
	def device_count(self) -> int:
		'''Number of devices in this listing'''
		return self._instance.DeviceCount

	@property
	def total_count(self) -> int:
		'''Total number of items (files + directories + devices)'''
		return self._instance.TotalCount

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DirectoryListing):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
