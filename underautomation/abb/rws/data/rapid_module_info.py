from __future__ import annotations
import typing
from underautomation.abb.rws.data.rapid_module_attribute import RapidModuleAttribute
from underautomation.abb.rws.data.rapid_module_item import RapidModuleItem
from UnderAutomation.ABB.Rws.Data import RapidModuleInfo as rapid_module_info
from UnderAutomation.ABB.Rws.Data import RapidModuleAttribute as rapid_module_attribute

class RapidModuleInfo(RapidModuleItem):
	'''Everything the controller reports about one module. Returned by RapidService.GetModule(); the module lists only carry the properties of the base class.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidModuleInfo class'''
		if(_internal == 0):
			self._instance = rapid_module_info()
		else:
			self._instance = _internal

	@property
	def file_name(self) -> str:
		'''Name of the file the module was loaded from, for example "MainModule.mod"'''
		return self._instance.FileName

	@file_name.setter
	def file_name(self, value: str):
		self._instance.FileName = value

	@property
	def attributes(self) -> typing.List[RapidModuleAttribute]:
		'''Properties declared on the module, empty when it declares none'''
		return [RapidModuleAttribute(int(x)) for x in self._instance.Attributes]

	@attributes.setter
	def attributes(self, value: typing.List[RapidModuleAttribute]):
		self._instance.Attributes = rapid_module_attribute(int(value))

	@property
	def attribute_count(self) -> int:
		'''Number of properties declared on the module'''
		return self._instance.AttributeCount

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidModuleInfo):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
