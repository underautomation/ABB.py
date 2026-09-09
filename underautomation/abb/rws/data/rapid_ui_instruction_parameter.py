from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import RapidUiInstructionParameter as rapid_ui_instruction_parameter

class RapidUiInstructionParameter:
	'''One parameter of the pending UI instruction: what the program passed in, or what it is waiting for. Returned by RapidService.GetUiInstructionParameters(). The parameters carrying the answer are the ones to write, typically named after a function key or after the completion flag of the instruction.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidUiInstructionParameter class'''
		if(_internal == 0):
			self._instance = rapid_ui_instruction_parameter()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Name of the parameter, for example "TPCompleted"'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def value(self) -> str:
		'''Value of the parameter, written the way RAPID writes it'''
		return self._instance.Value

	@value.setter
	def value(self, value: str):
		self._instance.Value = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidUiInstructionParameter):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
