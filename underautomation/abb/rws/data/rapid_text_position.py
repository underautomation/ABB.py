from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import RapidTextPosition as rapid_text_position

class RapidTextPosition:
	'''A position in the source of a module, counted from 1. Returned by RapidService.SearchModuleText(), which reports row and column 0 when the text was not found rather than failing.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidTextPosition class'''
		if(_internal == 0):
			self._instance = rapid_text_position()
		else:
			self._instance = _internal

	@property
	def row(self) -> int:
		'''Line of the position, 0 when the search found nothing'''
		return self._instance.Row

	@row.setter
	def row(self, value: int):
		self._instance.Row = value

	@property
	def column(self) -> int:
		'''Column of the position, 0 when the search found nothing'''
		return self._instance.Column

	@column.setter
	def column(self, value: int):
		self._instance.Column = value

	@property
	def found(self) -> bool:
		'''Whether the position points at something, which it does not when a search found nothing'''
		return self._instance.Found

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidTextPosition):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
