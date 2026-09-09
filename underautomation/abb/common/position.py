from __future__ import annotations
import typing
from UnderAutomation.ABB.Common import Position as position

class Position:
	'''A point in space, expressed in the coordinate system of whoever produced it. Most readings of the controller express a position in millimetres, while the kinematics calculations work in metres. The method that returns or takes a position says which one it uses.'''
	def __init__(self, x: float, y: float, z: float, _internal = 0):
		'''Initializes a new position

		:param x: Coordinate along the X axis
		:param y: Coordinate along the Y axis
		:param z: Coordinate along the Z axis
		'''
		if(_internal == 0):
			self._instance = position(x, y, z)
		else:
			self._instance = _internal

	@property
	def x(self) -> float:
		'''Coordinate along the X axis'''
		return self._instance.X

	@x.setter
	def x(self, value: float):
		self._instance.X = value

	@property
	def y(self) -> float:
		'''Coordinate along the Y axis'''
		return self._instance.Y

	@y.setter
	def y(self, value: float):
		self._instance.Y = value

	@property
	def z(self) -> float:
		'''Coordinate along the Z axis'''
		return self._instance.Z

	@z.setter
	def z(self, value: float):
		self._instance.Z = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Position):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
