from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import RapidModuleText as rapid_module_text

class RapidModuleText:
	'''The source of a module and the counters that go with it. Returned by RapidService.GetModuleText().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidModuleText class'''
		if(_internal == 0):
			self._instance = rapid_module_text()
		else:
			self._instance = _internal

	@property
	def text(self) -> str:
		'''Source of the module'''
		return self._instance.Text

	@text.setter
	def text(self, value: str):
		self._instance.Text = value

	@property
	def change_count(self) -> int | None:
		'''Counter the controller increments whenever the module changes, null when it did not report it'''
		return self._instance.ChangeCount

	@change_count.setter
	def change_count(self, value: int | None):
		self._instance.ChangeCount = value

	@property
	def declared_length(self) -> int | None:
		'''Length the controller declares for the module, null when it did not report it. This is the size the controller reserves for the module and not the length of , so the two normally differ.'''
		return self._instance.DeclaredLength

	@declared_length.setter
	def declared_length(self, value: int | None):
		self._instance.DeclaredLength = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidModuleText):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
