from __future__ import annotations
import typing
from datetime import datetime, timedelta
from UnderAutomation.ABB.Rws.Data import FileSystemItem as file_system_item

class FileSystemItem:
	'''Abstract base class for all file system items returned by the File Service. Derived classes: , ,'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = file_system_item()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Name of the item (file name, directory name, or device name such as "C:")'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def creation_date(self) -> datetime | None:
		'''Creation date of the resource, if available'''
		return None if self._instance.CreationDate is None else datetime(1, 1, 1) + timedelta(microseconds=self._instance.CreationDate.Ticks // 10)

	@creation_date.setter
	def creation_date(self, value: datetime | None):
		self._instance.CreationDate = value

	@property
	def modification_date(self) -> datetime | None:
		'''Last modification date of the resource, if available'''
		return None if self._instance.ModificationDate is None else datetime(1, 1, 1) + timedelta(microseconds=self._instance.ModificationDate.Ticks // 10)

	@modification_date.setter
	def modification_date(self, value: datetime | None):
		self._instance.ModificationDate = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, FileSystemItem):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
