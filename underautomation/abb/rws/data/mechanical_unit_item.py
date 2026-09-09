from __future__ import annotations
import typing
from underautomation.abb.rws.data.mechanical_unit_mode import MechanicalUnitMode
from UnderAutomation.ABB.Rws.Data import MechanicalUnitItem as mechanical_unit_item
from UnderAutomation.ABB.Rws.Data import MechanicalUnitMode as mechanical_unit_mode

class MechanicalUnitItem:
	'''One mechanical unit of the motion system, as listed by MotionSystemService.GetMechanicalUnits(). Only the few properties the list carries are filled in. Read the unit itself with MotionSystemService.GetMechanicalUnit() to get a .'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the MechanicalUnitItem class'''
		if(_internal == 0):
			self._instance = mechanical_unit_item()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Name of the mechanical unit, for example "ROB_1"'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def mode(self) -> MechanicalUnitMode:
		'''Whether the unit is activated'''
		return MechanicalUnitMode(int(self._instance.Mode))

	@mode.setter
	def mode(self, value: MechanicalUnitMode):
		self._instance.Mode = mechanical_unit_mode(int(value))

	@property
	def activation_allowed(self) -> bool | None:
		'''Whether the unit can be activated, null when the controller did not report it'''
		return self._instance.ActivationAllowed

	@activation_allowed.setter
	def activation_allowed(self, value: bool | None):
		self._instance.ActivationAllowed = value

	@property
	def drive_module(self) -> int | None:
		'''Number of the drive module the unit is connected to, null when the controller did not report it'''
		return self._instance.DriveModule

	@drive_module.setter
	def drive_module(self, value: int | None):
		self._instance.DriveModule = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MechanicalUnitItem):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
