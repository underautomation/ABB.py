from __future__ import annotations
import typing
from underautomation.abb.rws.data.mechanical_unit_mode import MechanicalUnitMode
from underautomation.abb.rws.data.mechanical_unit_type import MechanicalUnitType
from UnderAutomation.ABB.Rws.Data import RapidMechanicalUnitItem as rapid_mechanical_unit_item
from UnderAutomation.ABB.Rws.Data import MechanicalUnitMode as mechanical_unit_mode
from UnderAutomation.ABB.Rws.Data import MechanicalUnitType as mechanical_unit_type

class RapidMechanicalUnitItem:
	'''A mechanical unit the positions of a task are expressed in. Returned by RapidService.GetMechanicalUnits(). This is the view the RAPID task has of the unit; MotionSystemService.GetMechanicalUnits() answers with everything the motion system knows about the same units.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidMechanicalUnitItem class'''
		if(_internal == 0):
			self._instance = rapid_mechanical_unit_item()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Name of the unit, for example "ROB_1"'''
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
	def type(self) -> MechanicalUnitType:
		'''Kind of unit'''
		return MechanicalUnitType(int(self._instance.Type))

	@type.setter
	def type(self, value: MechanicalUnitType):
		self._instance.Type = mechanical_unit_type(int(value))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidMechanicalUnitItem):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
