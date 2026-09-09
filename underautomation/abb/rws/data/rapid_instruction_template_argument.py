from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import RapidInstructionTemplateArgument as rapid_instruction_template_argument

class RapidInstructionTemplateArgument:
	'''One argument of the template the controller suggests for an instruction or a data type. Carried by .'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidInstructionTemplateArgument class'''
		if(_internal == 0):
			self._instance = rapid_instruction_template_argument()
		else:
			self._instance = _internal

	@property
	def argument_number(self) -> int | None:
		'''Position of the argument, null when the controller did not report it'''
		return self._instance.ArgumentNumber

	@argument_number.setter
	def argument_number(self, value: int | None):
		self._instance.ArgumentNumber = value

	@property
	def required(self) -> bool | None:
		'''Whether the argument has to be given, null when the controller did not report it'''
		return self._instance.Required

	@required.setter
	def required(self, value: bool | None):
		self._instance.Required = value

	@property
	def name(self) -> str:
		'''Name of the argument, for example "ToPoint"'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def declaration_needed(self) -> bool | None:
		'''Whether inserting the instruction also needs a declaration to be created for this argument, null when the controller did not report it'''
		return self._instance.DeclarationNeeded

	@declaration_needed.setter
	def declaration_needed(self, value: bool | None):
		self._instance.DeclarationNeeded = value

	@property
	def symbol(self) -> str:
		'''Name of the symbol the argument refers to, empty when the argument is written as a literal'''
		return self._instance.Symbol

	@symbol.setter
	def symbol(self, value: str):
		self._instance.Symbol = value

	@property
	def value(self) -> str:
		'''Value the argument is suggested with, written the way RAPID writes it'''
		return self._instance.Value

	@value.setter
	def value(self, value: str):
		self._instance.Value = value

	@property
	def data_type(self) -> str:
		'''Type of the argument, for example "robtarget"'''
		return self._instance.DataType

	@data_type.setter
	def data_type(self, value: str):
		self._instance.DataType = value

	@property
	def object_type(self) -> str:
		'''How the suggested symbol is declared, for example "CONST" or "TASK PERS"'''
		return self._instance.ObjectType

	@object_type.setter
	def object_type(self, value: str):
		self._instance.ObjectType = value

	@property
	def local(self) -> bool | None:
		'''Whether the suggested symbol is local to its module, null when the controller did not report it'''
		return self._instance.Local

	@local.setter
	def local(self, value: bool | None):
		self._instance.Local = value

	@property
	def dimensions(self) -> int | None:
		'''Number of array dimensions of the argument, null when the controller did not report it'''
		return self._instance.Dimensions

	@dimensions.setter
	def dimensions(self, value: int | None):
		self._instance.Dimensions = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidInstructionTemplateArgument):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
