from __future__ import annotations
import typing
from underautomation.abb.rws.data.rapid_symbol_search_view import RapidSymbolSearchView
from underautomation.abb.rws.data.rapid_symbol_variable_type import RapidSymbolVariableType
from underautomation.abb.rws.data.rapid_symbol_type import RapidSymbolType
from UnderAutomation.ABB.Rws.Data import RapidSymbolSearchCriteria as rapid_symbol_search_criteria
from UnderAutomation.ABB.Rws.Data import RapidSymbolSearchView as rapid_symbol_search_view
from UnderAutomation.ABB.Rws.Data import RapidSymbolVariableType as rapid_symbol_variable_type
from UnderAutomation.ABB.Rws.Data import RapidSymbolType as rapid_symbol_type

class RapidSymbolSearchCriteria:
	'''What a symbol search looks for. Passed to RapidService.SearchSymbols(). Every property is optional; leaving one alone means the search does not filter on it. A search with no criterion at all walks the whole system, which is slow, so at least set .'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidSymbolSearchCriteria class'''
		if(_internal == 0):
			self._instance = rapid_symbol_search_criteria()
		else:
			self._instance = _internal

	@property
	def view(self) -> RapidSymbolSearchView:
		'''Which part of the system the search walks'''
		return RapidSymbolSearchView(int(self._instance.View))

	@view.setter
	def view(self, value: RapidSymbolSearchView):
		self._instance.View = rapid_symbol_search_view(int(value))

	@property
	def variable_type(self) -> RapidSymbolVariableType:
		'''Which variables the search keeps, by what may be done with them'''
		return RapidSymbolVariableType(int(self._instance.VariableType))

	@variable_type.setter
	def variable_type(self, value: RapidSymbolVariableType):
		self._instance.VariableType = rapid_symbol_variable_type(int(value))

	@property
	def block_url(self) -> str:
		'''Path the search starts from, for example "RAPID/T_ROB1"'''
		return self._instance.BlockUrl

	@block_url.setter
	def block_url(self, value: str):
		self._instance.BlockUrl = value

	@property
	def recursive(self) -> bool | None:
		'''Whether the search also walks what the starting point contains, null to leave it to the controller'''
		return self._instance.Recursive

	@recursive.setter
	def recursive(self, value: bool | None):
		self._instance.Recursive = value

	@property
	def position_row(self) -> int | None:
		'''Line the search starts from, used together with Scope'''
		return self._instance.PositionRow

	@position_row.setter
	def position_row(self, value: int | None):
		self._instance.PositionRow = value

	@property
	def position_column(self) -> int | None:
		'''Column the search starts from, used together with Scope'''
		return self._instance.PositionColumn

	@position_column.setter
	def position_column(self, value: int | None):
		self._instance.PositionColumn = value

	@property
	def stack_frame(self) -> int | None:
		'''Frame of the call stack the search starts from, used together with Stack'''
		return self._instance.StackFrame

	@stack_frame.setter
	def stack_frame(self, value: int | None):
		self._instance.StackFrame = value

	@property
	def only_used(self) -> bool | None:
		'''Whether only the symbols the program actually refers to are kept, null to leave it to the controller'''
		return self._instance.OnlyUsed

	@only_used.setter
	def only_used(self, value: bool | None):
		self._instance.OnlyUsed = value

	@property
	def skip_shared(self) -> bool | None:
		'''Whether the symbols shared between tasks are skipped, null to leave it to the controller'''
		return self._instance.SkipShared

	@skip_shared.setter
	def skip_shared(self, value: bool | None):
		self._instance.SkipShared = value

	@property
	def name_pattern(self) -> str:
		'''Regular expression the name of a symbol has to match to be kept'''
		return self._instance.NamePattern

	@name_pattern.setter
	def name_pattern(self, value: str):
		self._instance.NamePattern = value

	@property
	def symbol_types(self) -> typing.List[RapidSymbolType]:
		'''Kinds of symbol the search keeps, empty to keep every kind'''
		return [RapidSymbolType(int(x)) for x in self._instance.SymbolTypes]

	@symbol_types.setter
	def symbol_types(self, value: typing.List[RapidSymbolType]):
		self._instance.SymbolTypes = rapid_symbol_type(int(value))

	@property
	def data_type(self) -> str:
		'''Name of the type a symbol has to have to be kept, for example "robtarget"'''
		return self._instance.DataType

	@data_type.setter
	def data_type(self, value: str):
		self._instance.DataType = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidSymbolSearchCriteria):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
