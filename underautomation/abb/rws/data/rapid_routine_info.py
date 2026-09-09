from __future__ import annotations
import typing
from underautomation.abb.rws.data.rapid_symbol_type import RapidSymbolType
from UnderAutomation.ABB.Rws.Data import RapidRoutineInfo as rapid_routine_info
from UnderAutomation.ABB.Rws.Data import RapidSymbolType as rapid_symbol_type

class RapidRoutineInfo:
	'''The routine the controller finds called at a given position of a module. Returned by RapidService.GetRoutine(). The controller refuses the request when the position does not sit on a routine call.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidRoutineInfo class'''
		if(_internal == 0):
			self._instance = rapid_routine_info()
		else:
			self._instance = _internal

	@property
	def symbol_url(self) -> str:
		'''Path of the routine, which the program pointer resources take'''
		return self._instance.SymbolUrl

	@symbol_url.setter
	def symbol_url(self, value: str):
		self._instance.SymbolUrl = value

	@property
	def name(self) -> str:
		'''Name of the routine'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def symbol_type(self) -> RapidSymbolType:
		'''Whether the routine is a procedure, a function or a trap'''
		return RapidSymbolType(int(self._instance.SymbolType))

	@symbol_type.setter
	def symbol_type(self, value: RapidSymbolType):
		self._instance.SymbolType = rapid_symbol_type(int(value))

	@property
	def named(self) -> bool | None:
		'''Whether the routine is named, null when the controller did not report it'''
		return self._instance.Named

	@named.setter
	def named(self, value: bool | None):
		self._instance.Named = value

	@property
	def local(self) -> bool | None:
		'''Whether the routine is local to its module, null when the controller did not report it'''
		return self._instance.Local

	@local.setter
	def local(self, value: bool | None):
		self._instance.Local = value

	@property
	def parameter_count(self) -> int | None:
		'''Number of parameters the routine takes, null when the controller did not report it. The controller reports -1 when the parameter list is not linked yet.'''
		return self._instance.ParameterCount

	@parameter_count.setter
	def parameter_count(self, value: int | None):
		self._instance.ParameterCount = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidRoutineInfo):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
