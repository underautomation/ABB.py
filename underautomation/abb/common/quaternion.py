from __future__ import annotations
import typing
from UnderAutomation.ABB.Common import Quaternion as quaternion

class Quaternion:
	'''An orientation in space, expressed as a unit quaternion. The controller rejects a quaternion that is not normalized, so keep ² + ² + ² + ² equal to 1.'''
	def __init__(self, q1: float, q2: float, q3: float, q4: float, _internal = 0):
		'''Initializes a new quaternion

		:param q1: Real component
		:param q2: First imaginary component
		:param q3: Second imaginary component
		:param q4: Third imaginary component
		'''
		if(_internal == 0):
			self._instance = quaternion(q1, q2, q3, q4)
		else:
			self._instance = _internal

	@property
	def q1(self) -> float:
		'''Real component of the quaternion'''
		return self._instance.Q1

	@q1.setter
	def q1(self, value: float):
		self._instance.Q1 = value

	@property
	def q2(self) -> float:
		'''First imaginary component of the quaternion'''
		return self._instance.Q2

	@q2.setter
	def q2(self, value: float):
		self._instance.Q2 = value

	@property
	def q3(self) -> float:
		'''Second imaginary component of the quaternion'''
		return self._instance.Q3

	@q3.setter
	def q3(self, value: float):
		self._instance.Q3 = value

	@property
	def q4(self) -> float:
		'''Third imaginary component of the quaternion'''
		return self._instance.Q4

	@q4.setter
	def q4(self, value: float):
		self._instance.Q4 = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, Quaternion):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
