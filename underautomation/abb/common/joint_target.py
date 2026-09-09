from __future__ import annotations
import typing
from underautomation.abb.common.robot_joints import RobotJoints
from underautomation.abb.common.external_joints import ExternalJoints
from UnderAutomation.ABB.Common import JointTarget as joint_target

class JointTarget:
	'''A robot position expressed joint by joint: the six axes of the arm and the six external axes.'''
	def __init__(self, robotAxes: RobotJoints, externalAxes: ExternalJoints, _internal = 0):
		'''Initializes a new joint target

		:param robotAxes: Values of the six axes of the robot arm, zero when null
		:param externalAxes: Values of the six external axes, zero when null
		'''
		if(_internal == 0):
			self._instance = joint_target(robotAxes._instance if robotAxes else None, externalAxes._instance if externalAxes else None)
		else:
			self._instance = _internal

	@property
	def robot_axes(self) -> RobotJoints:
		'''Values of the six axes of the robot arm. Never null.'''
		return RobotJoints(None, None, None, None, None, None, self._instance.RobotAxes)

	@robot_axes.setter
	def robot_axes(self, value: RobotJoints):
		self._instance.RobotAxes = value._instance if value else None

	@property
	def external_axes(self) -> ExternalJoints:
		'''Values of the six external axes. Never null.'''
		return ExternalJoints(None, None, None, None, None, None, self._instance.ExternalAxes)

	@external_axes.setter
	def external_axes(self, value: ExternalJoints):
		self._instance.ExternalAxes = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, JointTarget):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
