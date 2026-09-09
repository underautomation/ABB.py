from __future__ import annotations
import typing
from underautomation.abb.rws.data.rapid_instruction_template_argument import RapidInstructionTemplateArgument
from UnderAutomation.ABB.Rws.Data import RapidInstructionTemplate as rapid_instruction_template

class RapidInstructionTemplate:
	'''The template the controller suggests for an instruction or a data type: the arguments to write and the values to write them with. Returned by RapidService.GetInstructionTemplate(). An editor uses it to insert a complete, valid instruction rather than a bare keyword.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidInstructionTemplate class'''
		if(_internal == 0):
			self._instance = rapid_instruction_template()
		else:
			self._instance = _internal

	@property
	def argument_count(self) -> int | None:
		'''Number of arguments the controller reported, null when it did not report it'''
		return self._instance.ArgumentCount

	@argument_count.setter
	def argument_count(self, value: int | None):
		self._instance.ArgumentCount = value

	@property
	def mark(self) -> int | None:
		'''Index the controller started reporting from, null when it did not report it'''
		return self._instance.Mark

	@mark.setter
	def mark(self, value: int | None):
		self._instance.Mark = value

	@property
	def complete(self) -> bool | None:
		'''Whether every argument has been reported, null when the controller did not report it'''
		return self._instance.Complete

	@complete.setter
	def complete(self, value: bool | None):
		self._instance.Complete = value

	@property
	def version(self) -> str:
		'''Version the controller stamps on the template'''
		return self._instance.Version

	@version.setter
	def version(self, value: str):
		self._instance.Version = value

	@property
	def selected_parameter(self) -> int | None:
		'''Argument the controller suggests selecting first, null when it did not report it'''
		return self._instance.SelectedParameter

	@selected_parameter.setter
	def selected_parameter(self, value: int | None):
		self._instance.SelectedParameter = value

	@property
	def arguments(self) -> typing.List[RapidInstructionTemplateArgument]:
		'''The suggested arguments'''
		return [RapidInstructionTemplateArgument(x) for x in self._instance.Arguments]

	@arguments.setter
	def arguments(self, value: typing.List[RapidInstructionTemplateArgument]):
		self._instance.Arguments = [x._instance if x else None for x in value]

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidInstructionTemplate):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
