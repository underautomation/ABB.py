from __future__ import annotations
import typing
from UnderAutomation.ABB.Common import RobotJoints as robot_joints

class RobotJoints:
	'''The six joint values of a robot arm. Readings of the controller express them in degrees, while the kinematics calculations work in radians. The method that returns or takes them says which one it uses.'''
	def __init__(self, axis1: float, axis2: float, axis3: float, axis4: float, axis5: float, axis6: float, _internal = 0):
		'''Initializes the six axes

		:param axis1: Value of axis 1
		:param axis2: Value of axis 2
		:param axis3: Value of axis 3
		:param axis4: Value of axis 4
		:param axis5: Value of axis 5
		:param axis6: Value of axis 6
		'''
		if(_internal == 0):
			self._instance = robot_joints(axis1, axis2, axis3, axis4, axis5, axis6)
		else:
			self._instance = _internal

	@property
	def axis1(self) -> float:
		'''Value of axis 1'''
		return self._instance.Axis1

	@axis1.setter
	def axis1(self, value: float):
		self._instance.Axis1 = value

	@property
	def axis2(self) -> float:
		'''Value of axis 2'''
		return self._instance.Axis2

	@axis2.setter
	def axis2(self, value: float):
		self._instance.Axis2 = value

	@property
	def axis3(self) -> float:
		'''Value of axis 3'''
		return self._instance.Axis3

	@axis3.setter
	def axis3(self, value: float):
		self._instance.Axis3 = value

	@property
	def axis4(self) -> float:
		'''Value of axis 4'''
		return self._instance.Axis4

	@axis4.setter
	def axis4(self, value: float):
		self._instance.Axis4 = value

	@property
	def axis5(self) -> float:
		'''Value of axis 5'''
		return self._instance.Axis5

	@axis5.setter
	def axis5(self, value: float):
		self._instance.Axis5 = value

	@property
	def axis6(self) -> float:
		'''Value of axis 6'''
		return self._instance.Axis6

	@axis6.setter
	def axis6(self, value: float):
		self._instance.Axis6 = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotJoints):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
