from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import RapidServiceRoutineItem as rapid_service_routine_item

class RapidServiceRoutineItem:
	'''A routine of a task the program pointer can be moved to. Returned by RapidService.GetServiceRoutines().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidServiceRoutineItem class'''
		if(_internal == 0):
			self._instance = rapid_service_routine_item()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Name of the routine, for example "LoadIdentify"'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def url(self) -> str:
		'''Path of the routine, which RapidService.SetProgramPointerToRoutineUrl() takes'''
		return self._instance.Url

	@url.setter
	def url(self, value: str):
		self._instance.Url = value

	@property
	def is_service_routine(self) -> bool | None:
		'''Whether this is a service routine rather than an ordinary one, null when the controller did not report it'''
		return self._instance.IsServiceRoutine

	@is_service_routine.setter
	def is_service_routine(self, value: bool | None):
		self._instance.IsServiceRoutine = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidServiceRoutineItem):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
