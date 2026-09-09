from __future__ import annotations
import typing
from underautomation.abb.rws.data.elog_message_type import ElogMessageType
from underautomation.abb.rws.data.elog_message_argument import ElogMessageArgument
from datetime import datetime, timedelta
from UnderAutomation.ABB.Rws.Data import ElogMessage as elog_message
from UnderAutomation.ABB.Rws.Data import ElogMessageType as elog_message_type

class ElogMessage:
	'''One message of the controller event log. Returned by ElogService.GetMessages(), ElogService.GetMessageTitles(), ElogService.GetMessage() and ElogService.GetMessageBySequenceNumber().The texts (, , , and ) are only filled when a language was asked for.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the ElogMessage class'''
		if(_internal == 0):
			self._instance = elog_message()
		else:
			self._instance = _internal

	@property
	def domain_number(self) -> int | None:
		'''Number of the domain the message belongs to, null when the controller did not report it'''
		return self._instance.DomainNumber

	@domain_number.setter
	def domain_number(self, value: int | None):
		self._instance.DomainNumber = value

	@property
	def sequence_number(self) -> int | None:
		'''Number identifying the message inside its domain. Messages are numbered in the order they were logged, so a higher number is a more recent message.'''
		return self._instance.SequenceNumber

	@sequence_number.setter
	def sequence_number(self, value: int | None):
		self._instance.SequenceNumber = value

	@property
	def type(self) -> ElogMessageType:
		'''Severity of the message'''
		return ElogMessageType(int(self._instance.Type))

	@type.setter
	def type(self, value: ElogMessageType):
		self._instance.Type = elog_message_type(int(value))

	@property
	def code(self) -> int | None:
		'''Number identifying the kind of event, the one printed on the teach pendant'''
		return self._instance.Code

	@code.setter
	def code(self, value: int | None):
		self._instance.Code = value

	@property
	def source_name(self) -> str:
		'''Part of the controller that logged the message, for example "MC0"'''
		return self._instance.SourceName

	@source_name.setter
	def source_name(self, value: str):
		self._instance.SourceName = value

	@property
	def timestamp(self) -> datetime | None:
		'''Moment the event was logged, null when the controller did not report it'''
		return None if self._instance.Timestamp is None else datetime(1, 1, 1) + timedelta(microseconds=self._instance.Timestamp.Ticks // 10)

	@timestamp.setter
	def timestamp(self, value: datetime | None):
		self._instance.Timestamp = value

	@property
	def title(self) -> str:
		'''Short text of the message. Only filled when a language was asked for.'''
		return self._instance.Title

	@title.setter
	def title(self, value: str):
		self._instance.Title = value

	@property
	def description(self) -> str:
		'''Long text describing what happened. Only filled when a language was asked for.'''
		return self._instance.Description

	@description.setter
	def description(self, value: str):
		self._instance.Description = value

	@property
	def consequences(self) -> str:
		'''Text describing what the event implies for the robot. Only filled when a language was asked for.'''
		return self._instance.Consequences

	@consequences.setter
	def consequences(self, value: str):
		self._instance.Consequences = value

	@property
	def causes(self) -> str:
		'''Text describing the probable causes of the event. Only filled when a language was asked for.'''
		return self._instance.Causes

	@causes.setter
	def causes(self, value: str):
		self._instance.Causes = value

	@property
	def actions(self) -> str:
		'''Text describing the recommended actions. Only filled when a language was asked for.'''
		return self._instance.Actions

	@actions.setter
	def actions(self, value: str):
		self._instance.Actions = value

	@property
	def arguments(self) -> typing.List[ElogMessageArgument]:
		'''Values the controller substitutes into the text of the message'''
		return [ElogMessageArgument(x) for x in self._instance.Arguments]

	@arguments.setter
	def arguments(self, value: typing.List[ElogMessageArgument]):
		self._instance.Arguments = [x._instance if x else None for x in value]

	@property
	def argument_count(self) -> int:
		'''Number of arguments of the message'''
		return self._instance.ArgumentCount

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ElogMessage):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
