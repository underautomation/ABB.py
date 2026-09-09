from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import RapidPreferredDataTypeItem as rapid_preferred_data_type_item

class RapidPreferredDataTypeItem:
	'''A data type the controller suggests for one argument of an instruction, so that an editor can offer the operator the types that fit where the cursor stands. Returned by RapidService.GetPreferredDataTypes().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidPreferredDataTypeItem class'''
		if(_internal == 0):
			self._instance = rapid_preferred_data_type_item()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Name of the suggestion, for example "signaldi"'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def data_type(self) -> str:
		'''Data type of the suggestion'''
		return self._instance.DataType

	@data_type.setter
	def data_type(self, value: str):
		self._instance.DataType = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidPreferredDataTypeItem):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
