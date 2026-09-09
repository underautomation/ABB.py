from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import MotorCalibrationName as motor_calibration_name

class MotorCalibrationName:
	'''Names one joint of a mechanical unit carries: the joint itself and the calibration data attached to it. Returned by MotionSystemService.GetMotorCalibrationNames().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the MotorCalibrationName class'''
		if(_internal == 0):
			self._instance = motor_calibration_name()
		else:
			self._instance = _internal

	@property
	def number(self) -> int:
		'''Number of the joint inside its mechanical unit, starting at 1'''
		return self._instance.Number

	@number.setter
	def number(self, value: int):
		self._instance.Number = value

	@property
	def joint_name(self) -> str:
		'''Name of the joint, for example "rob1_1"'''
		return self._instance.JointName

	@joint_name.setter
	def joint_name(self, value: str):
		self._instance.JointName = value

	@property
	def calibration_name(self) -> str:
		'''Name of the calibration data of the joint, usually the same as JointName'''
		return self._instance.CalibrationName

	@calibration_name.setter
	def calibration_name(self, value: str):
		self._instance.CalibrationName = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MotorCalibrationName):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
