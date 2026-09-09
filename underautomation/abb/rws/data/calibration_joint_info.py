from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import CalibrationJointInfo as calibration_joint_info

class CalibrationJointInfo:
	'''How one joint of a mechanical unit was calibrated. Held by .'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the CalibrationJointInfo class'''
		if(_internal == 0):
			self._instance = calibration_joint_info()
		else:
			self._instance = _internal

	@property
	def exists(self) -> bool:
		'''Whether the joint exists on this mechanical unit. The controller always answers with a fixed number of entries and marks the unused ones, which carry no name at all.'''
		return self._instance.Exists

	@exists.setter
	def exists(self, value: bool):
		self._instance.Exists = value

	@property
	def joint_name(self) -> str:
		'''Name of the joint, for example "rob1_1", empty for an entry that does not exist'''
		return self._instance.JointName

	@joint_name.setter
	def joint_name(self, value: str):
		self._instance.JointName = value

	@property
	def factory_calibration_method(self) -> str:
		'''Method the joint was calibrated with in the factory'''
		return self._instance.FactoryCalibrationMethod

	@factory_calibration_method.setter
	def factory_calibration_method(self, value: str):
		self._instance.FactoryCalibrationMethod = value

	@property
	def current_calibration_method(self) -> str:
		'''Method the joint is currently calibrated with'''
		return self._instance.CurrentCalibrationMethod

	@current_calibration_method.setter
	def current_calibration_method(self, value: str):
		self._instance.CurrentCalibrationMethod = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CalibrationJointInfo):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
