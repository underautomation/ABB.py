from __future__ import annotations
import typing
from underautomation.abb.rws.data.rapid_text_range import RapidTextRange
from UnderAutomation.ABB.Rws.Data import RapidObjectListExtension as rapid_object_list_extension

class RapidObjectListExtension:
	'''Where one of the lists of a RAPID object sits in the source: the span of the whole list, and the spans of its first and last elements. Returned by RapidService.GetObjectListExtension(). An editor uses it to jump to the beginning or the end of a list without reading the module.The controller reports an empty span when the object holds no such list.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidObjectListExtension class'''
		if(_internal == 0):
			self._instance = rapid_object_list_extension()
		else:
			self._instance = _internal

	@property
	def list(self) -> RapidTextRange:
		'''Span of the whole list'''
		return RapidTextRange(self._instance.List)

	@list.setter
	def list(self, value: RapidTextRange):
		self._instance.List = value._instance if value else None

	@property
	def first(self) -> RapidTextRange:
		'''Span of the first element of the list'''
		return RapidTextRange(self._instance.First)

	@first.setter
	def first(self, value: RapidTextRange):
		self._instance.First = value._instance if value else None

	@property
	def last(self) -> RapidTextRange:
		'''Span of the last element of the list'''
		return RapidTextRange(self._instance.Last)

	@last.setter
	def last(self, value: RapidTextRange):
		self._instance.Last = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidObjectListExtension):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
