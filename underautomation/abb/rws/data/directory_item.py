from __future__ import annotations
import typing
from underautomation.abb.rws.data.file_system_item import FileSystemItem
from UnderAutomation.ABB.Rws.Data import DirectoryItem as directory_item

class DirectoryItem(FileSystemItem):
	'''Represents a directory entry in the robot controller file system.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the DirectoryItem class'''
		if(_internal == 0):
			self._instance = directory_item()
		else:
			self._instance = _internal

	@property
	def is_read_only(self) -> bool:
		'''Indicates if the directory is read-only'''
		return self._instance.IsReadOnly

	@is_read_only.setter
	def is_read_only(self, value: bool):
		self._instance.IsReadOnly = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DirectoryItem):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
