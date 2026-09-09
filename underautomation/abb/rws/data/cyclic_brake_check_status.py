from __future__ import annotations
import typing
from underautomation.abb.rws.data.cyclic_brake_check_test_status import CyclicBrakeCheckTestStatus
from underautomation.abb.rws.data.cyclic_brake_check_state import CyclicBrakeCheckState
from UnderAutomation.ABB.Rws.Data import CyclicBrakeCheckStatus as cyclic_brake_check_status
from UnderAutomation.ABB.Rws.Data import CyclicBrakeCheckTestStatus as cyclic_brake_check_test_status
from UnderAutomation.ABB.Rws.Data import CyclicBrakeCheckState as cyclic_brake_check_state

class CyclicBrakeCheckStatus:
	'''Cyclic brake check status of a mechanical unit. Returned by ControllerService.GetCyclicBrakeCheckStatus(driveNumber).'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the CyclicBrakeCheckStatus class'''
		if(_internal == 0):
			self._instance = cyclic_brake_check_status()
		else:
			self._instance = _internal

	@property
	def drive_number(self) -> int:
		'''Drive number of the mechanical unit this status belongs to'''
		return self._instance.DriveNumber

	@drive_number.setter
	def drive_number(self, value: int):
		self._instance.DriveNumber = value

	@property
	def next_brake_check_time(self) -> int | None:
		'''Remaining time before the next brake check is required, if reported by the controller'''
		return self._instance.NextBrakeCheckTime

	@next_brake_check_time.setter
	def next_brake_check_time(self, value: int | None):
		self._instance.NextBrakeCheckTime = value

	@property
	def last_brake_check_status(self) -> CyclicBrakeCheckTestStatus:
		'''Result of the last brake check'''
		return CyclicBrakeCheckTestStatus(int(self._instance.LastBrakeCheckStatus))

	@last_brake_check_status.setter
	def last_brake_check_status(self, value: CyclicBrakeCheckTestStatus):
		self._instance.LastBrakeCheckStatus = cyclic_brake_check_test_status(int(value))

	@property
	def status(self) -> CyclicBrakeCheckState:
		'''Current cyclic brake check state'''
		return CyclicBrakeCheckState(int(self._instance.Status))

	@status.setter
	def status(self, value: CyclicBrakeCheckState):
		self._instance.Status = cyclic_brake_check_state(int(value))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CyclicBrakeCheckStatus):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
