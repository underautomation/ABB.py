from __future__ import annotations
import typing
from UnderAutomation.ABB.Common import ExternalJoints as external_joints

class ExternalJoints:
	'''The six external axis values that travel with a robot position. An axis the robot system does not define comes back as 9E9, which is how the controller says "not in use" rather than an actual position.'''
	def __init__(self, axisA: float, axisB: float, axisC: float, axisD: float, axisE: float, axisF: float, _internal = 0):
		'''Initializes the six external axes

		:param axisA: Value of external axis A
		:param axisB: Value of external axis B
		:param axisC: Value of external axis C
		:param axisD: Value of external axis D
		:param axisE: Value of external axis E
		:param axisF: Value of external axis F
		'''
		if(_internal == 0):
			self._instance = external_joints(axisA, axisB, axisC, axisD, axisE, axisF)
		else:
			self._instance = _internal

	@property
	def axis_a(self) -> float:
		'''Value of external axis A'''
		return self._instance.AxisA

	@axis_a.setter
	def axis_a(self, value: float):
		self._instance.AxisA = value

	@property
	def axis_b(self) -> float:
		'''Value of external axis B'''
		return self._instance.AxisB

	@axis_b.setter
	def axis_b(self, value: float):
		self._instance.AxisB = value

	@property
	def axis_c(self) -> float:
		'''Value of external axis C'''
		return self._instance.AxisC

	@axis_c.setter
	def axis_c(self, value: float):
		self._instance.AxisC = value

	@property
	def axis_d(self) -> float:
		'''Value of external axis D'''
		return self._instance.AxisD

	@axis_d.setter
	def axis_d(self, value: float):
		self._instance.AxisD = value

	@property
	def axis_e(self) -> float:
		'''Value of external axis E'''
		return self._instance.AxisE

	@axis_e.setter
	def axis_e(self, value: float):
		self._instance.AxisE = value

	@property
	def axis_f(self) -> float:
		'''Value of external axis F'''
		return self._instance.AxisF

	@axis_f.setter
	def axis_f(self, value: float):
		self._instance.AxisF = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ExternalJoints):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# Value the controller reports for an external axis that is not in use
ExternalJoints.NotInUse = external_joints.NotInUse
