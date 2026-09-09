from __future__ import annotations
import typing
from underautomation.abb.rws.data.rapid_ui_instruction_event import RapidUiInstructionEvent
from underautomation.abb.rws.data.rapid_execution_level import RapidExecutionLevel
from UnderAutomation.ABB.Rws.Data import RapidUiInstruction as rapid_ui_instruction
from UnderAutomation.ABB.Rws.Data import RapidUiInstructionEvent as rapid_ui_instruction_event
from UnderAutomation.ABB.Rws.Data import RapidExecutionLevel as rapid_execution_level

class RapidUiInstruction:
	'''The dialogue a running RAPID program is currently asking an operator for. Returned by RapidService.GetActiveUiInstruction(), which returns null when no instruction is pending. Answering one means writing its parameters with RapidService.SetUiInstructionParameter(), using to address them.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidUiInstruction class'''
		if(_internal == 0):
			self._instance = rapid_ui_instruction()
		else:
			self._instance = _internal

	@property
	def instruction(self) -> str:
		'''Name of the RAPID instruction that opened the dialogue, for example "TPReadNum"'''
		return self._instance.Instruction

	@instruction.setter
	def instruction(self, value: str):
		self._instance.Instruction = value

	@property
	def event(self) -> RapidUiInstructionEvent:
		'''What the instruction is asking of the client'''
		return RapidUiInstructionEvent(int(self._instance.Event))

	@event.setter
	def event(self, value: RapidUiInstructionEvent):
		self._instance.Event = rapid_ui_instruction_event(int(value))

	@property
	def stack_url(self) -> str:
		'''Path identifying the call, which the parameter methods take'''
		return self._instance.StackUrl

	@stack_url.setter
	def stack_url(self, value: str):
		self._instance.StackUrl = value

	@property
	def execution_level(self) -> RapidExecutionLevel:
		'''Level at which the instruction is executing'''
		return RapidExecutionLevel(int(self._instance.ExecutionLevel))

	@execution_level.setter
	def execution_level(self, value: RapidExecutionLevel):
		self._instance.ExecutionLevel = rapid_execution_level(int(value))

	@property
	def message(self) -> str:
		'''Text the instruction displays'''
		return self._instance.Message

	@message.setter
	def message(self, value: str):
		self._instance.Message = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidUiInstruction):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
