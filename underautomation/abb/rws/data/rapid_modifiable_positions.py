from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import RapidModifiablePositions as rapid_modifiable_positions

class RapidModifiablePositions:
	'''How many motion instructions of a range can have their position rewritten to where the robot currently stands, and which range they cover. Returned by RapidService.GetModifiablePositions(). The controller leaves the range empty when it found nothing modifiable.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidModifiablePositions class'''
		if(_internal == 0):
			self._instance = rapid_modifiable_positions()
		else:
			self._instance = _internal

	@property
	def modifiable_line_count(self) -> int:
		'''Number of motion instructions of the range whose position can be rewritten'''
		return self._instance.ModifiableLineCount

	@modifiable_line_count.setter
	def modifiable_line_count(self, value: int):
		self._instance.ModifiableLineCount = value

	@property
	def start_row(self) -> int | None:
		'''Line the modifiable range starts at, null when the controller did not report it'''
		return self._instance.StartRow

	@start_row.setter
	def start_row(self, value: int | None):
		self._instance.StartRow = value

	@property
	def start_column(self) -> int | None:
		'''Column the modifiable range starts at, null when the controller did not report it'''
		return self._instance.StartColumn

	@start_column.setter
	def start_column(self, value: int | None):
		self._instance.StartColumn = value

	@property
	def end_row(self) -> int | None:
		'''Line the modifiable range ends at, null when the controller did not report it'''
		return self._instance.EndRow

	@end_row.setter
	def end_row(self, value: int | None):
		self._instance.EndRow = value

	@property
	def end_column(self) -> int | None:
		'''Column the modifiable range ends at, null when the controller did not report it'''
		return self._instance.EndColumn

	@end_column.setter
	def end_column(self, value: int | None):
		self._instance.EndColumn = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidModifiablePositions):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
