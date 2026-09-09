from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import RapidStructuralChangeCount as rapid_structural_change_count

class RapidStructuralChangeCount:
	'''The two counters a task keeps of what has changed in it, so that a client can tell whether it needs to read the task again instead of fetching everything periodically. Returned by RapidService.GetStructuralChangeCount().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidStructuralChangeCount class'''
		if(_internal == 0):
			self._instance = rapid_structural_change_count()
		else:
			self._instance = _internal

	@property
	def change_count(self) -> int | None:
		'''Counter the controller increments whenever anything relevant changes in the task'''
		return self._instance.ChangeCount

	@change_count.setter
	def change_count(self, value: int | None):
		self._instance.ChangeCount = value

	@property
	def structural_change_count(self) -> int | None:
		'''Counter the controller increments when a module is loaded, unloaded or renamed. A rename counts as an unload followed by a load.'''
		return self._instance.StructuralChangeCount

	@structural_change_count.setter
	def structural_change_count(self, value: int | None):
		self._instance.StructuralChangeCount = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidStructuralChangeCount):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
