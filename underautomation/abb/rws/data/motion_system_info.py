from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import MotionSystemInfo as motion_system_info

class MotionSystemInfo:
	'''Overview of the motion system of the controller. Returned by MotionSystemService.GetInfo().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the MotionSystemInfo class'''
		if(_internal == 0):
			self._instance = motion_system_info()
		else:
			self._instance = _internal

	@property
	def change_count(self) -> int | None:
		'''Counter the controller increments on every change of the motion system. Pass it to MotionSystemService.HasChanged() to find out whether anything moved since a previous reading, without fetching the whole state again.'''
		return self._instance.ChangeCount

	@change_count.setter
	def change_count(self, value: int | None):
		self._instance.ChangeCount = value

	@property
	def mechanical_unit_name(self) -> str:
		'''Name of the mechanical unit the jogging commands currently apply to'''
		return self._instance.MechanicalUnitName

	@mechanical_unit_name.setter
	def mechanical_unit_name(self, value: str):
		self._instance.MechanicalUnitName = value

	@property
	def poll_rate(self) -> int | None:
		'''Rate at which the controller refreshes the motion system state, null when it did not report it'''
		return self._instance.PollRate

	@poll_rate.setter
	def poll_rate(self, value: int | None):
		self._instance.PollRate = value

	@property
	def modal_payload_mode(self) -> bool | None:
		'''Whether the payload of the robot is set by the running program rather than by the mechanical unit, null when the controller did not report it'''
		return self._instance.ModalPayloadMode

	@modal_payload_mode.setter
	def modal_payload_mode(self, value: bool | None):
		self._instance.ModalPayloadMode = value

	@property
	def absolute_accuracy_active(self) -> bool | None:
		'''Whether absolute accuracy is switched on, null when the controller did not report it'''
		return self._instance.AbsoluteAccuracyActive

	@absolute_accuracy_active.setter
	def absolute_accuracy_active(self, value: bool | None):
		self._instance.AbsoluteAccuracyActive = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MotionSystemInfo):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
