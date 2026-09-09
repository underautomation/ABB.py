from __future__ import annotations
import typing
from underautomation.abb.rws.data.io_signal_type import IoSignalType
from UnderAutomation.ABB.Rws.Data import RapidAliasIoItem as rapid_alias_io_item
from UnderAutomation.ABB.Rws.Data import IoSignalType as io_signal_type

class RapidAliasIoItem:
	'''An I/O signal a running RAPID program has given an alias to with the AliasIO instruction. Returned by RapidService.GetAliasIo(). The controller only knows about an alias while the program that declares it is loaded, so this list is empty on a controller holding no such program.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidAliasIoItem class'''
		if(_internal == 0):
			self._instance = rapid_alias_io_item()
		else:
			self._instance = _internal

	@property
	def alias_name(self) -> str:
		'''Name the RAPID program refers to the signal by'''
		return self._instance.AliasName

	@alias_name.setter
	def alias_name(self, value: str):
		self._instance.AliasName = value

	@property
	def signal_name(self) -> str:
		'''Name of the I/O signal the alias points at'''
		return self._instance.SignalName

	@signal_name.setter
	def signal_name(self, value: str):
		self._instance.SignalName = value

	@property
	def type(self) -> IoSignalType:
		'''Type of the aliased signal'''
		return IoSignalType(int(self._instance.Type))

	@type.setter
	def type(self, value: IoSignalType):
		self._instance.Type = io_signal_type(int(value))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidAliasIoItem):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
