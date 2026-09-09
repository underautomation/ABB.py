from __future__ import annotations
import typing
from UnderAutomation.ABB.Common import RobotConfiguration as robot_configuration

class RobotConfiguration:
	'''The axis configuration the robot uses to reach a pose. Several joint combinations reach the same tool position and orientation. The configuration names the one to use, as the quarter revolution each of the deciding axes sits in.'''
	def __init__(self, quarter1: int, quarter4: int, quarter6: int, quarterX: int, _internal = 0):
		'''Initializes a new configuration

		:param quarter1: Quarter revolution axis 1 sits in
		:param quarter4: Quarter revolution axis 4 sits in
		:param quarter6: Quarter revolution axis 6 sits in
		:param quarterX: Index of the arm configuration
		'''
		if(_internal == 0):
			self._instance = robot_configuration(quarter1, quarter4, quarter6, quarterX)
		else:
			self._instance = _internal

	@property
	def quarter1(self) -> int:
		'''Quarter revolution axis 1 sits in'''
		return self._instance.Quarter1

	@quarter1.setter
	def quarter1(self, value: int):
		self._instance.Quarter1 = value

	@property
	def quarter4(self) -> int:
		'''Quarter revolution axis 4 sits in'''
		return self._instance.Quarter4

	@quarter4.setter
	def quarter4(self, value: int):
		self._instance.Quarter4 = value

	@property
	def quarter6(self) -> int:
		'''Quarter revolution axis 6 sits in'''
		return self._instance.Quarter6

	@quarter6.setter
	def quarter6(self, value: int):
		self._instance.Quarter6 = value

	@property
	def quarter_x(self) -> int:
		'''Index of the arm configuration, which tells the remaining joint combinations apart'''
		return self._instance.QuarterX

	@quarter_x.setter
	def quarter_x(self, value: int):
		self._instance.QuarterX = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RobotConfiguration):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
