from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import RapidModifiablePositionItem as rapid_modifiable_position_item

class RapidModifiablePositionItem:
	'''One motion instruction of the system whose position can be rewritten to where the robot currently stands, wherever in whichever task it sits. Returned by RapidService.GetAllModifiablePositions().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidModifiablePositionItem class'''
		if(_internal == 0):
			self._instance = rapid_modifiable_position_item()
		else:
			self._instance = _internal

	@property
	def module_name(self) -> str:
		'''Name of the module holding the instruction'''
		return self._instance.ModuleName

	@module_name.setter
	def module_name(self, value: str):
		self._instance.ModuleName = value

	@property
	def task_name(self) -> str:
		'''Name of the task holding the module'''
		return self._instance.TaskName

	@task_name.setter
	def task_name(self, value: str):
		self._instance.TaskName = value

	@property
	def start_row(self) -> int | None:
		'''Line the instruction starts at, null when the controller did not report it'''
		return self._instance.StartRow

	@start_row.setter
	def start_row(self, value: int | None):
		self._instance.StartRow = value

	@property
	def start_column(self) -> int | None:
		'''Column the instruction starts at, null when the controller did not report it'''
		return self._instance.StartColumn

	@start_column.setter
	def start_column(self, value: int | None):
		self._instance.StartColumn = value

	@property
	def end_row(self) -> int | None:
		'''Line the instruction ends at, null when the controller did not report it'''
		return self._instance.EndRow

	@end_row.setter
	def end_row(self, value: int | None):
		self._instance.EndRow = value

	@property
	def end_column(self) -> int | None:
		'''Column the instruction ends at, null when the controller did not report it'''
		return self._instance.EndColumn

	@end_column.setter
	def end_column(self, value: int | None):
		self._instance.EndColumn = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidModifiablePositionItem):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
