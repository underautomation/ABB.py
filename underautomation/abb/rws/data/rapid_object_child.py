from __future__ import annotations
import typing
from underautomation.abb.rws.data.rapid_object_child_range import RapidObjectChildRange
from underautomation.abb.rws.data.rapid_text_range import RapidTextRange
from UnderAutomation.ABB.Rws.Data import RapidObjectChild as rapid_object_child

class RapidObjectChild:
	'''The parts a RAPID object is made of, and where each of them sits in the source. Returned by RapidService.GetObjectChildren(). Which parts the controller reports depends entirely on what the object is: a module answers with its name, its attributes and its declaration lists, a routine with something else. They are therefore returned as a list of named spans rather than as fixed properties.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidObjectChild class'''
		if(_internal == 0):
			self._instance = rapid_object_child()
		else:
			self._instance = _internal

	def get_range(self, name: str) -> RapidTextRange:
		'''Returns the span of one part by its name, null when the controller did not report it

		:param name: Name of the part, for example "data-decl"
		:returns: Span of the part, null when there is no such part
		'''
		return RapidTextRange(self._instance.GetRange(name))

	@property
	def object_type(self) -> str:
		'''What the object is, for example "module"'''
		return self._instance.ObjectType

	@object_type.setter
	def object_type(self, value: str):
		self._instance.ObjectType = value

	@property
	def ranges(self) -> typing.List[RapidObjectChildRange]:
		'''The parts of the object, including the ones it does not hold, whose span is then empty'''
		return [RapidObjectChildRange(x) for x in self._instance.Ranges]

	@ranges.setter
	def ranges(self, value: typing.List[RapidObjectChildRange]):
		self._instance.Ranges = [x._instance if x else None for x in value]

	@property
	def range_count(self) -> int:
		'''Number of parts the controller reported'''
		return self._instance.RangeCount

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidObjectChild):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
