from __future__ import annotations
import typing
from underautomation.abb.common.pose import Pose
from UnderAutomation.ABB.Rws.Data import BaseFrame as base_frame

class BaseFrame(Pose):
	'''Where the base of a mechanical unit sits, and what kind of base it is: a Pose extended with the type of the frame. Returned by MotionSystemService.GetBaseFrame(). The position is expressed in millimetres.'''
	def __init__(self, _internal = 0):
		'''Initializes a new base frame at the origin, with no rotation'''
		if(_internal == 0):
			self._instance = base_frame()
		else:
			self._instance = _internal

	@property
	def type(self) -> str:
		'''Kind of base frame the controller reports, for example "IRBRobot"'''
		return self._instance.Type

	@type.setter
	def type(self, value: str):
		self._instance.Type = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, BaseFrame):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
