from __future__ import annotations
import typing
from underautomation.abb.rws.data.rapid_symbol_type import RapidSymbolType
from UnderAutomation.ABB.Rws.Data import RapidSymbolProperties as rapid_symbol_properties
from UnderAutomation.ABB.Rws.Data import RapidSymbolType as rapid_symbol_type

class RapidSymbolProperties:
	'''What a RAPID symbol is declared as. Returned by RapidService.GetSymbolProperties() and RapidService.SearchSymbols(). A search fills in and leaves alone, a direct read does the opposite on some controllers, so treat both as optional.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidSymbolProperties class'''
		if(_internal == 0):
			self._instance = rapid_symbol_properties()
		else:
			self._instance = _internal

	@property
	def symbol_url(self) -> str:
		'''Path of the symbol, which the other symbol methods take'''
		return self._instance.SymbolUrl

	@symbol_url.setter
	def symbol_url(self, value: str):
		self._instance.SymbolUrl = value

	@property
	def name(self) -> str:
		'''Name of the symbol, for example "reg1"'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def symbol_type(self) -> RapidSymbolType:
		'''What kind of symbol this is'''
		return RapidSymbolType(int(self._instance.SymbolType))

	@symbol_type.setter
	def symbol_type(self, value: RapidSymbolType):
		self._instance.SymbolType = rapid_symbol_type(int(value))

	@property
	def named(self) -> bool | None:
		'''Whether the symbol is named, null when the controller did not report it'''
		return self._instance.Named

	@named.setter
	def named(self, value: bool | None):
		self._instance.Named = value

	@property
	def data_type(self) -> str:
		'''Name of the type of the symbol, for example "num"'''
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
	def dimension(self) -> str:
		'''Size of each array dimension as the controller worded it, empty when the symbol is not an array'''
		return self._instance.Dimension

	@dimension.setter
	def dimension(self, value: str):
		self._instance.Dimension = value

	@property
	def heap(self) -> bool | None:
		'''Whether the symbol is allocated on the heap, null when the controller did not report it'''
		return self._instance.Heap

	@heap.setter
	def heap(self, value: bool | None):
		self._instance.Heap = value

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
	def read_only(self) -> bool | None:
		'''Whether the symbol may not be written, null when the controller did not report it'''
		return self._instance.ReadOnly

	@read_only.setter
	def read_only(self, value: bool | None):
		self._instance.ReadOnly = value

	@property
	def task_variable(self) -> bool | None:
		'''Whether the symbol is global within its task, null when the controller did not report it'''
		return self._instance.TaskVariable

	@task_variable.setter
	def task_variable(self, value: bool | None):
		self._instance.TaskVariable = value

	@property
	def storage(self) -> str:
		'''How the controller stores the symbol, for example "loaded"'''
		return self._instance.Storage

	@storage.setter
	def storage(self, value: str):
		self._instance.Storage = value

	@property
	def type_url(self) -> str:
		'''Path of the type of the symbol, for example "RAPID/num"'''
		return self._instance.TypeUrl

	@type_url.setter
	def type_url(self, value: str):
		self._instance.TypeUrl = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidSymbolProperties):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
