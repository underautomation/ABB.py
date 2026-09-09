from __future__ import annotations
import typing
from underautomation.abb.rws.data.rapid_execution_type import RapidExecutionType
from UnderAutomation.ABB.Rws.Data import RapidPointerPosition as rapid_pointer_position
from UnderAutomation.ABB.Rws.Data import RapidExecutionType as rapid_execution_type

class RapidPointerPosition:
	'''Where one of the two pointers of a task stands. Carried by . tells apart a pointer that is really placed somewhere from one the controller could not report, which happens for the motion pointer whenever the task has not moved yet.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidPointerPosition class'''
		if(_internal == 0):
			self._instance = rapid_pointer_position()
		else:
			self._instance = _internal

	@property
	def available(self) -> bool:
		'''Whether the controller reported a position for this pointer at all'''
		return self._instance.Available

	@available.setter
	def available(self, value: bool):
		self._instance.Available = value

	@property
	def module(self) -> str:
		'''Name of the module the pointer stands in'''
		return self._instance.Module

	@module.setter
	def module(self, value: str):
		self._instance.Module = value

	@property
	def routine(self) -> str:
		'''Name of the routine the pointer stands in'''
		return self._instance.Routine

	@routine.setter
	def routine(self, value: str):
		self._instance.Routine = value

	@property
	def begin_row(self) -> int | None:
		'''Line the pointer begins at, null when the controller did not report it'''
		return self._instance.BeginRow

	@begin_row.setter
	def begin_row(self, value: int | None):
		self._instance.BeginRow = value

	@property
	def begin_column(self) -> int | None:
		'''Column the pointer begins at, null when the controller did not report it'''
		return self._instance.BeginColumn

	@begin_column.setter
	def begin_column(self, value: int | None):
		self._instance.BeginColumn = value

	@property
	def end_row(self) -> int | None:
		'''Line the pointer ends at, null when the controller did not report it'''
		return self._instance.EndRow

	@end_row.setter
	def end_row(self, value: int | None):
		self._instance.EndRow = value

	@property
	def end_column(self) -> int | None:
		'''Column the pointer ends at, null when the controller did not report it'''
		return self._instance.EndColumn

	@end_column.setter
	def end_column(self, value: int | None):
		self._instance.EndColumn = value

	@property
	def change_count(self) -> int | None:
		'''How many times the pointer has been moved, null when the controller did not report it'''
		return self._instance.ChangeCount

	@change_count.setter
	def change_count(self, value: int | None):
		self._instance.ChangeCount = value

	@property
	def execution_type(self) -> RapidExecutionType:
		'''What kind of code the pointer is standing in'''
		return RapidExecutionType(int(self._instance.ExecutionType))

	@execution_type.setter
	def execution_type(self, value: RapidExecutionType):
		self._instance.ExecutionType = rapid_execution_type(int(value))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidPointerPosition):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
