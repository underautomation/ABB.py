from __future__ import annotations
import typing
from underautomation.abb.rws.data.rapid_task_trust_level import RapidTaskTrustLevel
from underautomation.abb.rws.data.rapid_execution_level import RapidExecutionLevel
from underautomation.abb.rws.data.rapid_task_execution_mode import RapidTaskExecutionMode
from underautomation.abb.rws.data.rapid_execution_type import RapidExecutionType
from underautomation.abb.rws.data.rapid_execution_cycle import RapidExecutionCycle
from underautomation.abb.rws.data.rapid_task_item import RapidTaskItem
from UnderAutomation.ABB.Rws.Data import RapidTaskInfo as rapid_task_info
from UnderAutomation.ABB.Rws.Data import RapidTaskTrustLevel as rapid_task_trust_level
from UnderAutomation.ABB.Rws.Data import RapidExecutionLevel as rapid_execution_level
from UnderAutomation.ABB.Rws.Data import RapidTaskExecutionMode as rapid_task_execution_mode
from UnderAutomation.ABB.Rws.Data import RapidExecutionType as rapid_execution_type
from UnderAutomation.ABB.Rws.Data import RapidExecutionCycle as rapid_execution_cycle

class RapidTaskInfo(RapidTaskItem):
	'''Everything the controller reports about one RAPID task. Returned by RapidService.GetTask(); the task lists only carry the properties of the base class.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidTaskInfo class'''
		if(_internal == 0):
			self._instance = rapid_task_info()
		else:
			self._instance = _internal

	@property
	def trust(self) -> RapidTaskTrustLevel:
		'''What the controller does to the system when this task stops unexpectedly'''
		return RapidTaskTrustLevel(int(self._instance.Trust))

	@trust.setter
	def trust(self, value: RapidTaskTrustLevel):
		self._instance.Trust = rapid_task_trust_level(int(value))

	@property
	def task_id(self) -> int | None:
		'''Identifier of the task, null when the controller did not report it'''
		return self._instance.TaskId

	@task_id.setter
	def task_id(self, value: int | None):
		self._instance.TaskId = value

	@property
	def execution_level(self) -> RapidExecutionLevel:
		'''Level at which the code of the task is currently executing'''
		return RapidExecutionLevel(int(self._instance.ExecutionLevel))

	@execution_level.setter
	def execution_level(self, value: RapidExecutionLevel):
		self._instance.ExecutionLevel = rapid_execution_level(int(value))

	@property
	def execution_mode(self) -> RapidTaskExecutionMode:
		'''Stepping mode the task was last started with'''
		return RapidTaskExecutionMode(int(self._instance.ExecutionMode))

	@execution_mode.setter
	def execution_mode(self, value: RapidTaskExecutionMode):
		self._instance.ExecutionMode = rapid_task_execution_mode(int(value))

	@property
	def execution_type(self) -> RapidExecutionType:
		'''What kind of code the task is currently running'''
		return RapidExecutionType(int(self._instance.ExecutionType))

	@execution_type.setter
	def execution_type(self, value: RapidExecutionType):
		self._instance.ExecutionType = rapid_execution_type(int(value))

	@property
	def execution_cycle(self) -> RapidExecutionCycle:
		'''Number of cycles the task is set to run. Only reported over a connection established with version 2, and left to otherwise.'''
		return RapidExecutionCycle(int(self._instance.ExecutionCycle))

	@execution_cycle.setter
	def execution_cycle(self, value: RapidExecutionCycle):
		self._instance.ExecutionCycle = rapid_execution_cycle(int(value))

	@property
	def production_entry_point(self) -> str:
		'''Routine the program pointer moves to when it is reset, for example "main"'''
		return self._instance.ProductionEntryPoint

	@production_entry_point.setter
	def production_entry_point(self, value: str):
		self._instance.ProductionEntryPoint = value

	@property
	def bind_reference(self) -> bool | None:
		'''Whether the task is bound to a configured task number, null when the controller did not report it'''
		return self._instance.BindReference

	@bind_reference.setter
	def bind_reference(self, value: bool | None):
		self._instance.BindReference = value

	@property
	def task_in_foreground(self) -> str:
		'''Name of the task running in the foreground, empty when there is none'''
		return self._instance.TaskInForeground

	@task_in_foreground.setter
	def task_in_foreground(self, value: str):
		self._instance.TaskInForeground = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidTaskInfo):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
