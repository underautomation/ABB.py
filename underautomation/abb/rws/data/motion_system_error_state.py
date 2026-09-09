from __future__ import annotations
import typing
from underautomation.abb.rws.data.motion_error_state import MotionErrorState
from UnderAutomation.ABB.Rws.Data import MotionSystemErrorState as motion_system_error_state
from UnderAutomation.ABB.Rws.Data import MotionErrorState as motion_error_state

class MotionSystemErrorState:
	'''Error state of the motion system, and how many errors it has counted. Returned by MotionSystemService.GetErrorState().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the MotionSystemErrorState class'''
		if(_internal == 0):
			self._instance = motion_system_error_state()
		else:
			self._instance = _internal

	@property
	def state(self) -> MotionErrorState:
		'''Last error the motion system ran into'''
		return MotionErrorState(int(self._instance.State))

	@state.setter
	def state(self, value: MotionErrorState):
		self._instance.State = motion_error_state(int(value))

	@property
	def raw_state(self) -> str:
		'''Error state exactly as the controller reported it, useful when State is Unknown'''
		return self._instance.RawState

	@raw_state.setter
	def raw_state(self, value: str):
		self._instance.RawState = value

	@property
	def count(self) -> int | None:
		'''Number of errors counted since the controller started, incremented on every new error, null when the controller did not report it'''
		return self._instance.Count

	@count.setter
	def count(self, value: int | None):
		self._instance.Count = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MotionSystemErrorState):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
