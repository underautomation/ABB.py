from __future__ import annotations
import typing
from underautomation.abb.rws.data.io_signal_type import IoSignalType
from UnderAutomation.ABB.Rws.Data import IoSignalSearchCriteria as io_signal_search_criteria
from UnderAutomation.ABB.Rws.Data import IoSignalType as io_signal_type

class IoSignalSearchCriteria:
	'''Criteria used to search I/O signals with IoService.SearchSignals() and IoService.SearchSignalsExtended(). Every property is optional: the properties left to null are not sent to the controller, and an empty criteria matches every signal.Two criteria can be combined by passing a second instance to the search methods, in which case a signal is returned only when it matches both. One of the two criteria should then have set to true, otherwise the result is the same as with a single criteria.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the IoSignalSearchCriteria class'''
		if(_internal == 0):
			self._instance = io_signal_search_criteria()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Name of the searched signals'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def device_name(self) -> str:
		'''Name of the device the searched signals are connected to'''
		return self._instance.DeviceName

	@device_name.setter
	def device_name(self, value: str):
		self._instance.DeviceName = value

	@property
	def network_name(self) -> str:
		'''Name of the network the searched signals belong to'''
		return self._instance.NetworkName

	@network_name.setter
	def network_name(self, value: str):
		self._instance.NetworkName = value

	@property
	def category(self) -> str:
		'''Category of the searched signals, for example "safety"'''
		return self._instance.Category

	@category.setter
	def category(self, value: str):
		self._instance.Category = value

	@property
	def category_prefix(self) -> str:
		'''Category prefix of the searched signals'''
		return self._instance.CategoryPrefix

	@category_prefix.setter
	def category_prefix(self, value: str):
		self._instance.CategoryPrefix = value

	@property
	def type(self) -> IoSignalType | None:
		'''Type of the searched signals, null to search every type'''
		return IoSignalType(int(self._instance.Type))

	@type.setter
	def type(self, value: IoSignalType | None):
		self._instance.Type = value

	@property
	def invert(self) -> bool | None:
		'''Whether the criteria is inverted: the signals matching it are excluded from the result'''
		return self._instance.Invert

	@invert.setter
	def invert(self, value: bool | None):
		self._instance.Invert = value

	@property
	def blocked(self) -> bool | None:
		'''Whether only the blocked (simulated) signals are searched'''
		return self._instance.Blocked

	@blocked.setter
	def blocked(self, value: bool | None):
		self._instance.Blocked = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IoSignalSearchCriteria):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
