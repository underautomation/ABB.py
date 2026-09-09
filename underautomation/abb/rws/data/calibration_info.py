from __future__ import annotations
import typing
from underautomation.abb.rws.data.calibration_joint_info import CalibrationJointInfo
from UnderAutomation.ABB.Rws.Data import CalibrationInfo as calibration_info

class CalibrationInfo:
	'''How a mechanical unit was calibrated, joint by joint. Returned by MotionSystemService.GetCalibrationInfo().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the CalibrationInfo class'''
		if(_internal == 0):
			self._instance = calibration_info()
		else:
			self._instance = _internal

	@property
	def calibration_window_type(self) -> int | None:
		'''Kind of calibration window the controller offers for this unit, null when the controller did not report it'''
		return self._instance.CalibrationWindowType

	@calibration_window_type.setter
	def calibration_window_type(self, value: int | None):
		self._instance.CalibrationWindowType = value

	@property
	def active_joint_count(self) -> int | None:
		'''Number of joints of the unit that are in use, null when the controller did not report it'''
		return self._instance.ActiveJointCount

	@active_joint_count.setter
	def active_joint_count(self, value: int | None):
		self._instance.ActiveJointCount = value

	@property
	def joint_count(self) -> int | None:
		'''Number of entries in Joints, which is fixed and larger than ActiveJointCount. Null when the controller did not report it.'''
		return self._instance.JointCount

	@joint_count.setter
	def joint_count(self, value: int | None):
		self._instance.JointCount = value

	@property
	def calibration_method_used(self) -> str:
		'''Name of the calibration method the unit was last calibrated with, for example "AxisCalibration"'''
		return self._instance.CalibrationMethodUsed

	@calibration_method_used.setter
	def calibration_method_used(self, value: str):
		self._instance.CalibrationMethodUsed = value

	@property
	def joints(self) -> typing.List[CalibrationJointInfo]:
		'''One entry per joint slot of the unit, the unused ones marked as such. Never null.'''
		return [CalibrationJointInfo(x) for x in self._instance.Joints]

	@joints.setter
	def joints(self, value: typing.List[CalibrationJointInfo]):
		self._instance.Joints = [x._instance if x else None for x in value]

	@property
	def existing_joint_count(self) -> int:
		'''Number of joints that exist on the unit, counted from Joints'''
		return self._instance.ExistingJointCount

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CalibrationInfo):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
