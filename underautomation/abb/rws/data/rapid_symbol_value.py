from __future__ import annotations
import typing
from underautomation.abb.rws.data.rapid_text_range import RapidTextRange
from UnderAutomation.ABB.Rws.Data import RapidSymbolValue as rapid_symbol_value

class RapidSymbolValue:
	'''The value of a RAPID symbol and where it is declared. Returned by RapidService.GetSymbolValue(). The value is the text the controller wrote it as, which for a record is the bracketed form RAPID itself uses, for example [[515,0,712],[0.707107,0,0.707107,0],[0,0,0,0],[9E+09,9E+09,9E+09,9E+09,9E+09,9E+09]].'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidSymbolValue class'''
		if(_internal == 0):
			self._instance = rapid_symbol_value()
		else:
			self._instance = _internal

	@property
	def value(self) -> str:
		'''Value of the symbol, written the way RAPID writes it'''
		return self._instance.Value

	@value.setter
	def value(self, value: str):
		self._instance.Value = value

	@property
	def declaration_position(self) -> RapidTextRange:
		'''Where the symbol is declared, null when the controller did not report it'''
		return RapidTextRange(self._instance.DeclarationPosition)

	@declaration_position.setter
	def declaration_position(self, value: RapidTextRange):
		self._instance.DeclarationPosition = value._instance if value else None

	@property
	def initial_value_position(self) -> RapidTextRange:
		'''Where the initial value of the symbol is written, null when the controller did not report it. The controller reports zeros when the declaration carries no initial value.'''
		return RapidTextRange(self._instance.InitialValuePosition)

	@initial_value_position.setter
	def initial_value_position(self, value: RapidTextRange):
		self._instance.InitialValuePosition = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidSymbolValue):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
