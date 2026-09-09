from __future__ import annotations
import typing
from underautomation.abb.rws.data.controller_type import ControllerType
from underautomation.abb.rws.data.controller_level import ControllerLevel
from datetime import datetime, timedelta
from UnderAutomation.ABB.Rws.Data import ControllerInfo as controller_info
from UnderAutomation.ABB.Rws.Data import ControllerType as controller_type
from UnderAutomation.ABB.Rws.Data import ControllerLevel as controller_level

class ControllerInfo:
	'''Overview of the controller resources. Returned by ControllerService.GetInfo().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the ControllerInfo class'''
		if(_internal == 0):
			self._instance = controller_info()
		else:
			self._instance = _internal

	@property
	def system_time(self) -> datetime | None:
		'''Current system time of the controller (UTC), if available'''
		return None if self._instance.SystemTime is None else datetime(1, 1, 1) + timedelta(microseconds=self._instance.SystemTime.Ticks // 10)

	@system_time.setter
	def system_time(self, value: datetime | None):
		self._instance.SystemTime = value

	@property
	def name(self) -> str:
		'''Name of the controller'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def type(self) -> ControllerType:
		'''Indicates whether the controller is a real or a virtual controller'''
		return ControllerType(int(self._instance.Type))

	@type.setter
	def type(self, value: ControllerType):
		self._instance.Type = controller_type(int(value))

	@property
	def level(self) -> ControllerLevel:
		'''Indicates whether the controller runs at system level or in bootserver mode'''
		return ControllerLevel(int(self._instance.Level))

	@level.setter
	def level(self, value: ControllerLevel):
		self._instance.Level = controller_level(int(value))

	@property
	def resources(self) -> typing.List[str]:
		'''Names of the sub resources exposed by the controller ("clock", "identity", "network", ...)'''
		return self._instance.Resources

	@resources.setter
	def resources(self, value: typing.List[str]):
		self._instance.Resources = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ControllerInfo):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
