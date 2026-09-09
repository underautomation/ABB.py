from __future__ import annotations
import typing
from underautomation.abb.rws.data.rapid_module_type import RapidModuleType
from UnderAutomation.ABB.Rws.Data import RapidModuleItem as rapid_module_item
from UnderAutomation.ABB.Rws.Data import RapidModuleType as rapid_module_type

class RapidModuleItem:
	'''A module loaded into a task, as listed by RapidService.GetModules(). RapidService.GetModule() returns a , which adds the file the module came from and the attributes declared on it.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidModuleItem class'''
		if(_internal == 0):
			self._instance = rapid_module_item()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Name of the module, for example "MainModule"'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def type(self) -> RapidModuleType:
		'''Whether the module belongs to the program or to the system'''
		return RapidModuleType(int(self._instance.Type))

	@type.setter
	def type(self, value: RapidModuleType):
		self._instance.Type = rapid_module_type(int(value))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidModuleItem):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
