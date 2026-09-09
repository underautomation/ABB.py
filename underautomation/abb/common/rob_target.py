from __future__ import annotations
import typing
from underautomation.abb.common.robot_configuration import RobotConfiguration
from underautomation.abb.common.external_joints import ExternalJoints
from underautomation.abb.common.quaternion import Quaternion
from underautomation.abb.common.pose import Pose
from UnderAutomation.ABB.Common import RobTarget as rob_target

class RobTarget(Pose):
	'''A complete robot target: a Pose extended with the axis configuration used to reach it and the external axis values that travel with it.'''
	def __init__(self, x: float, y: float, z: float, orientation: Quaternion, configuration: RobotConfiguration, externalAxes: ExternalJoints, _internal = 0):
		'''Initializes a new target

		:param x: Coordinate along the X axis
		:param y: Coordinate along the Y axis
		:param z: Coordinate along the Z axis
		:param orientation: Orientation held at that position, the identity rotation when null
		:param configuration: Axis configuration used to reach the pose, all zero when null
		:param externalAxes: Values of the six external axes
		'''
		if(_internal == 0):
			self._instance = rob_target(x, y, z, orientation._instance if orientation else None, configuration._instance if configuration else None, externalAxes._instance if externalAxes else None)
		else:
			self._instance = _internal

	@property
	def configuration(self) -> RobotConfiguration:
		'''Axis configuration used to reach the pose. Never null.'''
		return RobotConfiguration(None, None, None, None, self._instance.Configuration)

	@configuration.setter
	def configuration(self, value: RobotConfiguration):
		self._instance.Configuration = value._instance if value else None

	@property
	def external_axes(self) -> ExternalJoints:
		'''Values of the six external axes, null when the reading does not report them'''
		return ExternalJoints(None, None, None, None, None, None, self._instance.ExternalAxes)

	@external_axes.setter
	def external_axes(self, value: ExternalJoints):
		self._instance.ExternalAxes = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobTarget):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
