from __future__ import annotations
import typing
from underautomation.abb.rws.data.rapid_execution_state import RapidExecutionState
from underautomation.abb.rws.data.rapid_execution_cycle import RapidExecutionCycle
from UnderAutomation.ABB.Rws.Data import RapidExecutionInfo as rapid_execution_info
from UnderAutomation.ABB.Rws.Data import RapidExecutionState as rapid_execution_state
from UnderAutomation.ABB.Rws.Data import RapidExecutionCycle as rapid_execution_cycle

class RapidExecutionInfo:
	'''Overall RAPID execution state of the controller. Returned by RapidService.GetExecutionState().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidExecutionInfo class'''
		if(_internal == 0):
			self._instance = rapid_execution_info()
		else:
			self._instance = _internal

	@property
	def state(self) -> RapidExecutionState:
		'''Whether RAPID code is currently running'''
		return RapidExecutionState(int(self._instance.State))

	@state.setter
	def state(self, value: RapidExecutionState):
		self._instance.State = rapid_execution_state(int(value))

	@property
	def cycle(self) -> RapidExecutionCycle:
		'''Number of cycles the program is set to run'''
		return RapidExecutionCycle(int(self._instance.Cycle))

	@cycle.setter
	def cycle(self, value: RapidExecutionCycle):
		self._instance.Cycle = rapid_execution_cycle(int(value))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidExecutionInfo):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
