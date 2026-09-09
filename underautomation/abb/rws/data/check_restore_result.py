from __future__ import annotations
import typing
from underautomation.abb.rws.data.check_restore_status import CheckRestoreStatus
from UnderAutomation.ABB.Rws.Data import CheckRestoreResult as check_restore_result
from UnderAutomation.ABB.Rws.Data import CheckRestoreStatus as check_restore_status

class CheckRestoreResult:
	'''Result of a backup restore check. Returned by ControllerService.CheckRestore(...).'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the CheckRestoreResult class'''
		if(_internal == 0):
			self._instance = check_restore_result()
		else:
			self._instance = _internal

	@property
	def status(self) -> CheckRestoreStatus:
		'''Status of the check'''
		return CheckRestoreStatus(int(self._instance.Status))

	@status.setter
	def status(self, value: CheckRestoreStatus):
		self._instance.Status = check_restore_status(int(value))

	@property
	def is_accepted(self) -> bool:
		'''Indicates whether the backup can be restored'''
		return self._instance.IsAccepted

	@property
	def path(self) -> str:
		'''File missing or corrupted in the backup, if reported by the controller'''
		return self._instance.Path

	@path.setter
	def path(self, value: str):
		self._instance.Path = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, CheckRestoreResult):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
