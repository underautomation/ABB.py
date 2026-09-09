from __future__ import annotations
import typing
from underautomation.abb.rws.data.rapid_execution_level import RapidExecutionLevel
from UnderAutomation.ABB.Rws.Data import RapidActivationRecord as rapid_activation_record
from UnderAutomation.ABB.Rws.Data import RapidExecutionLevel as rapid_execution_level

class RapidActivationRecord:
	'''One frame of the call stack of a task: which routine is running and where the execution stands in it. Returned by RapidService.GetActivationRecord(). Frame 1 is the routine holding the program pointer, and the number grows towards the entry point of the program.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidActivationRecord class'''
		if(_internal == 0):
			self._instance = rapid_activation_record()
		else:
			self._instance = _internal

	@property
	def execution_level(self) -> RapidExecutionLevel:
		'''Level at which this frame is executing'''
		return RapidExecutionLevel(int(self._instance.ExecutionLevel))

	@execution_level.setter
	def execution_level(self, value: RapidExecutionLevel):
		self._instance.ExecutionLevel = rapid_execution_level(int(value))

	@property
	def begin_row(self) -> int | None:
		'''Line the executing statement starts at, null when the controller did not report it'''
		return self._instance.BeginRow

	@begin_row.setter
	def begin_row(self, value: int | None):
		self._instance.BeginRow = value

	@property
	def begin_column(self) -> int | None:
		'''Column the executing statement starts at, null when the controller did not report it'''
		return self._instance.BeginColumn

	@begin_column.setter
	def begin_column(self, value: int | None):
		self._instance.BeginColumn = value

	@property
	def end_row(self) -> int | None:
		'''Line the executing statement ends at, null when the controller did not report it'''
		return self._instance.EndRow

	@end_row.setter
	def end_row(self, value: int | None):
		self._instance.EndRow = value

	@property
	def end_column(self) -> int | None:
		'''Column the executing statement ends at, null when the controller did not report it'''
		return self._instance.EndColumn

	@end_column.setter
	def end_column(self, value: int | None):
		self._instance.EndColumn = value

	@property
	def stack_url(self) -> str:
		'''Path identifying this stack frame, which the UI instruction resources also take'''
		return self._instance.StackUrl

	@stack_url.setter
	def stack_url(self, value: str):
		self._instance.StackUrl = value

	@property
	def routine_url(self) -> str:
		'''Path of the routine this frame is executing'''
		return self._instance.RoutineUrl

	@routine_url.setter
	def routine_url(self, value: str):
		self._instance.RoutineUrl = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidActivationRecord):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
