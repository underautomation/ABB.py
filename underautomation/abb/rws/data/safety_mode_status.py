from __future__ import annotations
import typing
from underautomation.abb.rws.data.safety_mode import SafetyMode
from UnderAutomation.ABB.Rws.Data import SafetyModeStatus as safety_mode_status
from UnderAutomation.ABB.Rws.Data import SafetyMode as safety_mode

class SafetyModeStatus:
	'''Safety mode status of the controller. Returned by ControllerService.GetSafetyMode().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the SafetyModeStatus class'''
		if(_internal == 0):
			self._instance = safety_mode_status()
		else:
			self._instance = _internal

	@property
	def mode(self) -> SafetyMode:
		'''Current safety mode'''
		return SafetyMode(int(self._instance.Mode))

	@mode.setter
	def mode(self, value: SafetyMode):
		self._instance.Mode = safety_mode(int(value))

	@property
	def user_data(self) -> int | None:
		'''User data associated with the safety mode, if reported by the controller'''
		return self._instance.UserData

	@user_data.setter
	def user_data(self, value: int | None):
		self._instance.UserData = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SafetyModeStatus):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
