from __future__ import annotations
import typing
from underautomation.abb.rws.data.rapid_text_range import RapidTextRange
from UnderAutomation.ABB.Rws.Data import RapidObjectChildRange as rapid_object_child_range

class RapidObjectChildRange:
	'''One named part of a RAPID object, and where it sits in the source. Carried by .'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidObjectChildRange class'''
		if(_internal == 0):
			self._instance = rapid_object_child_range()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Name of the part as the controller worded it, for example "data-decl" or "endmod"'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def range(self) -> RapidTextRange:
		'''Where the part sits in the source'''
		return RapidTextRange(self._instance.Range)

	@range.setter
	def range(self, value: RapidTextRange):
		self._instance.Range = value._instance if value else None

	@property
	def is_present(self) -> bool:
		'''Whether the controller reported a real span for the part, which it does not when the object does not hold it'''
		return self._instance.IsPresent

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidObjectChildRange):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
