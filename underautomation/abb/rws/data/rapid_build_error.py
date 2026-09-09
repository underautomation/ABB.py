from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import RapidBuildError as rapid_build_error

class RapidBuildError:
	'''An error the controller found while linking the program of a task. Returned by RapidService.GetBuildErrors().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidBuildError class'''
		if(_internal == 0):
			self._instance = rapid_build_error()
		else:
			self._instance = _internal

	@property
	def module_name(self) -> str:
		'''Name of the module the error was found in'''
		return self._instance.ModuleName

	@module_name.setter
	def module_name(self, value: str):
		self._instance.ModuleName = value

	@property
	def row(self) -> int | None:
		'''Line the error was found at, null when the controller did not report it'''
		return self._instance.Row

	@row.setter
	def row(self, value: int | None):
		self._instance.Row = value

	@property
	def column(self) -> int | None:
		'''Column the error was found at, null when the controller did not report it'''
		return self._instance.Column

	@column.setter
	def column(self, value: int | None):
		self._instance.Column = value

	@property
	def error_number(self) -> int | None:
		'''Numeric identifier of the error, null when the controller did not report it'''
		return self._instance.ErrorNumber

	@error_number.setter
	def error_number(self, value: int | None):
		self._instance.ErrorNumber = value

	@property
	def error(self) -> str:
		'''Description of the error as the controller worded it'''
		return self._instance.Error

	@error.setter
	def error(self, value: str):
		self._instance.Error = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidBuildError):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
