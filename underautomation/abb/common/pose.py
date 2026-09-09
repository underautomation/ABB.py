from __future__ import annotations
import typing
from underautomation.abb.common.quaternion import Quaternion
from underautomation.abb.common.position import Position
from UnderAutomation.ABB.Common import Pose as pose

class Pose(Position):
	'''A position and the orientation the robot holds there: a Position extended with a Quaternion.'''
	def __init__(self, x: float, y: float, z: float, q1: float, q2: float, q3: float, q4: float, _internal = 0):
		'''Initializes a new pose

		:param x: Coordinate along the X axis
		:param y: Coordinate along the Y axis
		:param z: Coordinate along the Z axis
		:param q1: Real component of the orientation
		:param q2: First imaginary component of the orientation
		:param q3: Second imaginary component of the orientation
		:param q4: Third imaginary component of the orientation
		'''
		if(_internal == 0):
			self._instance = pose(x, y, z, q1, q2, q3, q4)
		else:
			self._instance = _internal

	@property
	def orientation(self) -> Quaternion:
		'''Orientation held at this position. Never null: a pose built without one carries the identity rotation.'''
		return Quaternion(None, None, None, None, self._instance.Orientation)

	@orientation.setter
	def orientation(self, value: Quaternion):
		self._instance.Orientation = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Pose):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
