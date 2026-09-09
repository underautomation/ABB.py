from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import ElogDomain as elog_domain

class ElogDomain:
	'''One event log domain of the controller, for example the common, the operational or the safety log. Returned by ElogService.GetDomains() and ElogService.GetDomain().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the ElogDomain class'''
		if(_internal == 0):
			self._instance = elog_domain()
		else:
			self._instance = _internal

	@property
	def number(self) -> int:
		'''Number identifying the domain, which is the value to pass to the methods reading its messages'''
		return self._instance.Number

	@number.setter
	def number(self, value: int):
		self._instance.Number = value

	@property
	def name(self) -> str:
		'''Name of the domain, for example "Operational" or "Safety". Only filled when a language was asked for, null otherwise.'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def message_count(self) -> int | None:
		'''Number of messages currently held by the domain, null when the controller did not report it'''
		return self._instance.MessageCount

	@message_count.setter
	def message_count(self, value: int | None):
		self._instance.MessageCount = value

	@property
	def buffer_size(self) -> int | None:
		'''Number of messages the domain can hold before the oldest ones are discarded, null when the controller did not report it'''
		return self._instance.BufferSize

	@buffer_size.setter
	def buffer_size(self, value: int | None):
		self._instance.BufferSize = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ElogDomain):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
