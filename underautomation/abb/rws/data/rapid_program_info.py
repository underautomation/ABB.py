from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import RapidProgramInfo as rapid_program_info

class RapidProgramInfo:
	'''The program loaded into a task. Returned by RapidService.GetProgram(), which returns null when the task holds no program at all.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidProgramInfo class'''
		if(_internal == 0):
			self._instance = rapid_program_info()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Name of the program, null when the controller did not report it'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def entry_point(self) -> str:
		'''Routine the program pointer moves to when it is reset, null when the controller did not report it'''
		return self._instance.EntryPoint

	@entry_point.setter
	def entry_point(self, value: str):
		self._instance.EntryPoint = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidProgramInfo):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
