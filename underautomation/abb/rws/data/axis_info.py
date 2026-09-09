from __future__ import annotations
import typing
from underautomation.abb.rws.data.mechanical_unit_status import MechanicalUnitStatus
from UnderAutomation.ABB.Rws.Data import AxisInfo as axis_info
from UnderAutomation.ABB.Rws.Data import MechanicalUnitStatus as mechanical_unit_status

class AxisInfo:
	'''State of one axis of a mechanical unit. Returned by MotionSystemService.GetAxis().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the AxisInfo class'''
		if(_internal == 0):
			self._instance = axis_info()
		else:
			self._instance = _internal

	@property
	def number(self) -> int:
		'''Number of the axis inside its mechanical unit, starting at 1'''
		return self._instance.Number

	@number.setter
	def number(self, value: int):
		self._instance.Number = value

	@property
	def status(self) -> MechanicalUnitStatus:
		'''Calibration and synchronization state of the axis'''
		return MechanicalUnitStatus(int(self._instance.Status))

	@status.setter
	def status(self, value: MechanicalUnitStatus):
		self._instance.Status = mechanical_unit_status(int(value))

	@property
	def logical_axis(self) -> int | None:
		'''Logical joint number of the axis, null when the controller did not report it'''
		return self._instance.LogicalAxis

	@logical_axis.setter
	def logical_axis(self, value: int | None):
		self._instance.LogicalAxis = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, AxisInfo):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
