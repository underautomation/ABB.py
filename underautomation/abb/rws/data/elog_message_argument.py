from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import ElogMessageArgument as elog_message_argument

class ElogMessageArgument:
	'''One argument of an event log message. The arguments are the values the controller substitutes into the text of the message, for example the name of the task that was started. Held by .'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the ElogMessageArgument class'''
		if(_internal == 0):
			self._instance = elog_message_argument()
		else:
			self._instance = _internal

	@property
	def index(self) -> int:
		'''Position of the argument in the message, starting at 1'''
		return self._instance.Index

	@index.setter
	def index(self, value: int):
		self._instance.Index = value

	@property
	def type(self) -> str:
		'''Type of the argument reported by the controller, for example "string", "long" or "float"'''
		return self._instance.Type

	@type.setter
	def type(self, value: str):
		self._instance.Type = value

	@property
	def value(self) -> str:
		'''Value of the argument, always as text'''
		return self._instance.Value

	@value.setter
	def value(self, value: str):
		self._instance.Value = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ElogMessageArgument):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
