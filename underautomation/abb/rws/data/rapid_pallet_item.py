from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import RapidPalletItem as rapid_pallet_item

class RapidPalletItem:
	'''One entry of an instruction palette category, which an editor offers as something the operator can insert at the cursor. Returned by RapidService.GetPallet().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidPalletItem class'''
		if(_internal == 0):
			self._instance = rapid_pallet_item()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Name shown for the entry, for example "MoveJ"'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def instruction(self) -> str:
		'''Instruction the entry inserts'''
		return self._instance.Instruction

	@instruction.setter
	def instruction(self, value: str):
		self._instance.Instruction = value

	@property
	def parameter(self) -> int | None:
		'''Parameter the entry preselects, null when the controller did not report it'''
		return self._instance.Parameter

	@parameter.setter
	def parameter(self, value: int | None):
		self._instance.Parameter = value

	@property
	def alternative(self) -> int | None:
		'''Alternative of the parameter the entry preselects, null when the controller did not report it'''
		return self._instance.Alternative

	@alternative.setter
	def alternative(self, value: int | None):
		self._instance.Alternative = value

	@property
	def keyword(self) -> int | None:
		'''Whether the entry is a language keyword rather than an instruction, null when the controller did not report it'''
		return self._instance.Keyword

	@keyword.setter
	def keyword(self, value: int | None):
		self._instance.Keyword = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidPalletItem):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
