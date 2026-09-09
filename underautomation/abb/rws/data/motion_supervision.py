from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import MotionSupervision as motion_supervision

class MotionSupervision:
	'''Collision detection settings of one mechanical unit while it is jogged. Returned by MotionSystemService.GetMotionSupervision().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the MotionSupervision class'''
		if(_internal == 0):
			self._instance = motion_supervision()
		else:
			self._instance = _internal

	@property
	def enabled(self) -> bool | None:
		'''Whether the supervision is switched on, null when the controller did not report it'''
		return self._instance.Enabled

	@enabled.setter
	def enabled(self, value: bool | None):
		self._instance.Enabled = value

	@property
	def level(self) -> int | None:
		'''Sensitivity of the supervision, as a percentage: the lower the value, the sooner a collision is reported. Null when the controller did not report it.'''
		return self._instance.Level

	@level.setter
	def level(self, value: int | None):
		self._instance.Level = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MotionSupervision):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
