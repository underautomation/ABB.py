from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import RapidSetTextRangeResult as rapid_set_text_range_result

class RapidSetTextRangeResult:
	'''What the controller did with a change written into the source of a module. Returned by RapidService.SetModuleTextRange(). Rewriting the MODULE line renames the module, which is why the controller reports the name it ended up with.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidSetTextRangeResult class'''
		if(_internal == 0):
			self._instance = rapid_set_text_range_result()
		else:
			self._instance = _internal

	@property
	def module_renamed(self) -> bool:
		'''Whether the change renamed the module'''
		return self._instance.ModuleRenamed

	@module_renamed.setter
	def module_renamed(self, value: bool):
		self._instance.ModuleRenamed = value

	@property
	def new_module_name(self) -> str:
		'''Name the module now has, empty when the change did not rename it'''
		return self._instance.NewModuleName

	@new_module_name.setter
	def new_module_name(self, value: str):
		self._instance.NewModuleName = value

	@property
	def change_count(self) -> int | None:
		'''Counter the controller incremented for the change, null when it did not report it'''
		return self._instance.ChangeCount

	@change_count.setter
	def change_count(self, value: int | None):
		self._instance.ChangeCount = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidSetTextRangeResult):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
