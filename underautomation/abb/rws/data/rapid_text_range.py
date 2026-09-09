from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import RapidTextRange as rapid_text_range

class RapidTextRange:
	'''A span of source between two positions, counted from 1. Used wherever the controller reports where something is declared or where a statement sits.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidTextRange class'''
		if(_internal == 0):
			self._instance = rapid_text_range()
		else:
			self._instance = _internal

	@property
	def begin_row(self) -> int | None:
		'''Line the range begins at, null when the controller did not report it'''
		return self._instance.BeginRow

	@begin_row.setter
	def begin_row(self, value: int | None):
		self._instance.BeginRow = value

	@property
	def begin_column(self) -> int | None:
		'''Column the range begins at, null when the controller did not report it'''
		return self._instance.BeginColumn

	@begin_column.setter
	def begin_column(self, value: int | None):
		self._instance.BeginColumn = value

	@property
	def end_row(self) -> int | None:
		'''Line the range ends at, null when the controller did not report it'''
		return self._instance.EndRow

	@end_row.setter
	def end_row(self, value: int | None):
		self._instance.EndRow = value

	@property
	def end_column(self) -> int | None:
		'''Column the range ends at, null when the controller did not report it'''
		return self._instance.EndColumn

	@end_column.setter
	def end_column(self, value: int | None):
		self._instance.EndColumn = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidTextRange):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
