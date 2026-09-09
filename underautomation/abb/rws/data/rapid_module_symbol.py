from __future__ import annotations
import typing
from underautomation.abb.rws.data.rapid_symbol_type import RapidSymbolType
from UnderAutomation.ABB.Rws.Data import RapidModuleSymbol as rapid_module_symbol
from UnderAutomation.ABB.Rws.Data import RapidSymbolType as rapid_symbol_type

class RapidModuleSymbol:
	'''The declaration the controller finds at a given position of a module. Returned by RapidService.GetModuleSymbol(), which returns null when there is no declaration at that position.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidModuleSymbol class'''
		if(_internal == 0):
			self._instance = rapid_module_symbol()
		else:
			self._instance = _internal

	@property
	def version(self) -> str:
		'''Version the controller stamps on the declaration'''
		return self._instance.Version

	@version.setter
	def version(self, value: str):
		self._instance.Version = value

	@property
	def name(self) -> str:
		'''Name of the declared symbol'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def symbol_url(self) -> str:
		'''Path of the symbol, which the symbol resources take'''
		return self._instance.SymbolUrl

	@symbol_url.setter
	def symbol_url(self, value: str):
		self._instance.SymbolUrl = value

	@property
	def symbol_type(self) -> RapidSymbolType:
		'''What kind of symbol was declared'''
		return RapidSymbolType(int(self._instance.SymbolType))

	@symbol_type.setter
	def symbol_type(self, value: RapidSymbolType):
		self._instance.SymbolType = rapid_symbol_type(int(value))

	@property
	def linked(self) -> bool | None:
		'''Whether the declaration is complete, null when the controller did not report it'''
		return self._instance.Linked

	@linked.setter
	def linked(self, value: bool | None):
		self._instance.Linked = value

	@property
	def local(self) -> bool | None:
		'''Whether the symbol is local to its module, null when the controller did not report it'''
		return self._instance.Local

	@local.setter
	def local(self, value: bool | None):
		self._instance.Local = value

	@property
	def type_url(self) -> str:
		'''Path of the type of the symbol'''
		return self._instance.TypeUrl

	@type_url.setter
	def type_url(self, value: str):
		self._instance.TypeUrl = value

	@property
	def data_type(self) -> str:
		'''Name of the type of the symbol, for example "robtarget"'''
		return self._instance.DataType

	@data_type.setter
	def data_type(self, value: str):
		self._instance.DataType = value

	@property
	def dimensions(self) -> int | None:
		'''Number of array dimensions of the symbol, null when the controller did not report it'''
		return self._instance.Dimensions

	@dimensions.setter
	def dimensions(self, value: int | None):
		self._instance.Dimensions = value

	@property
	def storage(self) -> int | None:
		'''How the controller stores the symbol, null when it did not report it'''
		return self._instance.Storage

	@storage.setter
	def storage(self, value: int | None):
		self._instance.Storage = value

	@property
	def heap(self) -> bool | None:
		'''Whether the symbol is allocated on the heap, null when the controller did not report it'''
		return self._instance.Heap

	@heap.setter
	def heap(self, value: bool | None):
		self._instance.Heap = value

	@property
	def reference_count(self) -> int | None:
		'''How many times the symbol is referred to, null when the controller did not report it'''
		return self._instance.ReferenceCount

	@reference_count.setter
	def reference_count(self, value: int | None):
		self._instance.ReferenceCount = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidModuleSymbol):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
