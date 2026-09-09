from __future__ import annotations
import typing
from datetime import datetime, timedelta
from UnderAutomation.ABB.Rws.Data import TimeServerInfo as time_server_info

class TimeServerInfo:
	'''Time server used by the controller to synchronize its clock. Returned by ControllerService.GetTimeServer().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the TimeServerInfo class'''
		if(_internal == 0):
			self._instance = time_server_info()
		else:
			self._instance = _internal

	@property
	def address(self) -> str:
		'''Address of the time server'''
		return self._instance.Address

	@address.setter
	def address(self, value: str):
		self._instance.Address = value

	@property
	def time(self) -> datetime | None:
		'''Time reported by the time server (UTC), if available. Only available when connected with version 2.'''
		return None if self._instance.Time is None else datetime(1, 1, 1) + timedelta(microseconds=self._instance.Time.Ticks // 10)

	@time.setter
	def time(self, value: datetime | None):
		self._instance.Time = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, TimeServerInfo):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
