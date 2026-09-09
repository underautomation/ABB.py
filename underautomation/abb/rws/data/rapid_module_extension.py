from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import RapidModuleExtension as rapid_module_extension

class RapidModuleExtension:
	'''How big the source of a module is, which is what it takes to ask for the whole of it as a range. Returned by RapidService.GetModuleExtension().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidModuleExtension class'''
		if(_internal == 0):
			self._instance = rapid_module_extension()
		else:
			self._instance = _internal

	@property
	def line_count(self) -> int | None:
		'''Number of lines the module holds, null when the controller did not report it'''
		return self._instance.LineCount

	@line_count.setter
	def line_count(self, value: int | None):
		self._instance.LineCount = value

	@property
	def max_column_count(self) -> int | None:
		'''Length of the longest line of the module, null when the controller did not report it'''
		return self._instance.MaxColumnCount

	@max_column_count.setter
	def max_column_count(self, value: int | None):
		self._instance.MaxColumnCount = value

	@property
	def change_count(self) -> int | None:
		'''Counter the controller increments whenever the module changes, null when it did not report it'''
		return self._instance.ChangeCount

	@change_count.setter
	def change_count(self, value: int | None):
		self._instance.ChangeCount = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidModuleExtension):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
