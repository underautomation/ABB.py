from __future__ import annotations
import typing
from underautomation.abb.rws.data.controller_type import ControllerType
from underautomation.abb.rws.data.controller_level import ControllerLevel
from UnderAutomation.ABB.Rws.Data import ControllerIdentity as controller_identity
from UnderAutomation.ABB.Rws.Data import ControllerType as controller_type
from UnderAutomation.ABB.Rws.Data import ControllerLevel as controller_level

class ControllerIdentity:
	'''Identity of the robot controller. Returned by ControllerService.GetIdentity().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the ControllerIdentity class'''
		if(_internal == 0):
			self._instance = controller_identity()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Name of the controller'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def id(self) -> str:
		'''Controller id, available only for a real controller'''
		return self._instance.Id

	@id.setter
	def id(self, value: str):
		self._instance.Id = value

	@property
	def type(self) -> ControllerType:
		'''Indicates whether the controller is a real or a virtual controller'''
		return ControllerType(int(self._instance.Type))

	@type.setter
	def type(self, value: ControllerType):
		self._instance.Type = controller_type(int(value))

	@property
	def mac_address(self) -> str:
		'''MAC address of the controller, available only for a real controller'''
		return self._instance.MacAddress

	@mac_address.setter
	def mac_address(self, value: str):
		self._instance.MacAddress = value

	@property
	def level(self) -> ControllerLevel:
		'''Indicates whether the controller runs at system level or in bootserver mode'''
		return ControllerLevel(int(self._instance.Level))

	@level.setter
	def level(self, value: ControllerLevel):
		self._instance.Level = controller_level(int(value))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ControllerIdentity):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
