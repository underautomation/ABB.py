from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import RapidProgramCounterPosition as rapid_program_counter_position

class RapidProgramCounterPosition:
	'''Where the program pointer of a task stands, expressed as the piece of source it points at. Returned by RapidService.GetProgramCounterPosition(). The controller refuses the request when the task has no program pointer set, so reset it or start the program first.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidProgramCounterPosition class'''
		if(_internal == 0):
			self._instance = rapid_program_counter_position()
		else:
			self._instance = _internal

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
	def start_line(self) -> int | None:
		'''Line the pointed instruction starts at, null when the controller did not report it'''
		return self._instance.StartLine

	@start_line.setter
	def start_line(self, value: int | None):
		self._instance.StartLine = value

	@property
	def start_column(self) -> int | None:
		'''Column the pointed instruction starts at, null when the controller did not report it'''
		return self._instance.StartColumn

	@start_column.setter
	def start_column(self, value: int | None):
		self._instance.StartColumn = value

	@property
	def end_line(self) -> int | None:
		'''Line the pointed instruction ends at, null when the controller did not report it'''
		return self._instance.EndLine

	@end_line.setter
	def end_line(self, value: int | None):
		self._instance.EndLine = value

	@property
	def end_column(self) -> int | None:
		'''Column the pointed instruction ends at, null when the controller did not report it'''
		return self._instance.EndColumn

	@end_column.setter
	def end_column(self, value: int | None):
		self._instance.EndColumn = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidProgramCounterPosition):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
