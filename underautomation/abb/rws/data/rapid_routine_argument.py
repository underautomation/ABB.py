from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import RapidRoutineArgument as rapid_routine_argument

class RapidRoutineArgument:
	'''One argument of the routine call found at a given position of a module, and where it sits in the source. Returned by RapidService.GetRoutineArguments().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidRoutineArgument class'''
		if(_internal == 0):
			self._instance = rapid_routine_argument()
		else:
			self._instance = _internal

	@property
	def parameter_number(self) -> int | None:
		'''Position of the argument in the call, counted from 0'''
		return self._instance.ParameterNumber

	@parameter_number.setter
	def parameter_number(self, value: int | None):
		self._instance.ParameterNumber = value

	@property
	def alternate_argument(self) -> int | None:
		'''Which alternative of the parameter this argument fills, null when the controller did not report it'''
		return self._instance.AlternateArgument

	@alternate_argument.setter
	def alternate_argument(self, value: int | None):
		self._instance.AlternateArgument = value

	@property
	def start_row(self) -> int | None:
		'''Line the argument starts at, null when the controller did not report it'''
		return self._instance.StartRow

	@start_row.setter
	def start_row(self, value: int | None):
		self._instance.StartRow = value

	@property
	def start_column(self) -> int | None:
		'''Column the argument starts at, null when the controller did not report it'''
		return self._instance.StartColumn

	@start_column.setter
	def start_column(self, value: int | None):
		self._instance.StartColumn = value

	@property
	def end_row(self) -> int | None:
		'''Line the argument ends at, null when the controller did not report it'''
		return self._instance.EndRow

	@end_row.setter
	def end_row(self, value: int | None):
		self._instance.EndRow = value

	@property
	def end_column(self) -> int | None:
		'''Column the argument ends at, null when the controller did not report it'''
		return self._instance.EndColumn

	@end_column.setter
	def end_column(self, value: int | None):
		self._instance.EndColumn = value

	@property
	def object_type(self) -> str:
		'''What the argument is, for example a required argument or a name reference'''
		return self._instance.ObjectType

	@object_type.setter
	def object_type(self, value: str):
		self._instance.ObjectType = value

	@property
	def data_type(self) -> str:
		'''Type of the argument, for example "num"'''
		return self._instance.DataType

	@data_type.setter
	def data_type(self, value: str):
		self._instance.DataType = value

	@property
	def list_number(self) -> int | None:
		'''Position of the argument in the argument list, null when the controller did not report it'''
		return self._instance.ListNumber

	@list_number.setter
	def list_number(self, value: int | None):
		self._instance.ListNumber = value

	@property
	def list_length(self) -> int | None:
		'''Length of the argument list, null when the controller did not report it'''
		return self._instance.ListLength

	@list_length.setter
	def list_length(self, value: int | None):
		self._instance.ListLength = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidRoutineArgument):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
