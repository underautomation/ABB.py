from __future__ import annotations
import typing
from underautomation.abb.common.robot_configuration import RobotConfiguration
from underautomation.abb.common.joint_target import JointTarget
from UnderAutomation.ABB.Rws.Data import JointSolution as joint_solution

class JointSolution(JointTarget):
	'''One of the joint combinations that reach a given pose: a JointTarget extended with the axis configuration it corresponds to. Returned by MotionSystemService.GetAllJointSolutions(). The joint values are expressed in radians.'''
	def __init__(self, _internal = 0):
		'''Initializes a new solution with every axis at zero'''
		if(_internal == 0):
			self._instance = joint_solution()
		else:
			self._instance = _internal

	@property
	def configuration(self) -> RobotConfiguration:
		'''Axis configuration this solution corresponds to. Never null.'''
		return RobotConfiguration(None, None, None, None, self._instance.Configuration)

	@configuration.setter
	def configuration(self, value: RobotConfiguration):
		self._instance.Configuration = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, JointSolution):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
