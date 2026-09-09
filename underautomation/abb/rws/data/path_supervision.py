from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import PathSupervision as path_supervision

class PathSupervision:
	'''Collision detection settings of one mechanical unit while it follows a programmed path. Returned by MotionSystemService.GetPathSupervision().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the PathSupervision class'''
		if(_internal == 0):
			self._instance = path_supervision()
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
		if not isinstance(other, PathSupervision):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
