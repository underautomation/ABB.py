from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import RapidPalletHeadItem as rapid_pallet_head_item

class RapidPalletHeadItem:
	'''One category of the instruction palette the FlexPendant editor offers, for example "Prog.Flow". Returned by RapidService.GetPalletHeads(); its is what RapidService.GetPallet() takes.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidPalletHeadItem class'''
		if(_internal == 0):
			self._instance = rapid_pallet_head_item()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Name of the category, for example "Motion&Proc."'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def number(self) -> int | None:
		'''Number identifying the category, null when the controller did not report it'''
		return self._instance.Number

	@number.setter
	def number(self, value: int | None):
		self._instance.Number = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidPalletHeadItem):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
