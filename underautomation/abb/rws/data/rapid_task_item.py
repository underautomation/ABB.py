from __future__ import annotations
import typing
from underautomation.abb.rws.data.rapid_task_type import RapidTaskType
from underautomation.abb.rws.data.rapid_task_state import RapidTaskState
from underautomation.abb.rws.data.rapid_task_execution_state import RapidTaskExecutionState
from UnderAutomation.ABB.Rws.Data import RapidTaskItem as rapid_task_item
from UnderAutomation.ABB.Rws.Data import RapidTaskType as rapid_task_type
from UnderAutomation.ABB.Rws.Data import RapidTaskState as rapid_task_state
from UnderAutomation.ABB.Rws.Data import RapidTaskExecutionState as rapid_task_execution_state

class RapidTaskItem:
	'''A RAPID task of the controller, as listed by RapidService.GetTasks(). RapidService.GetTask() returns a , which adds everything the controller reports for a single task only.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidTaskItem class'''
		if(_internal == 0):
			self._instance = rapid_task_item()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Name of the task, for example "T_ROB1"'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def type(self) -> RapidTaskType:
		'''Kind of task, which decides when the controller runs it'''
		return RapidTaskType(int(self._instance.Type))

	@type.setter
	def type(self, value: RapidTaskType):
		self._instance.Type = rapid_task_type(int(value))

	@property
	def task_state(self) -> RapidTaskState:
		'''How far the controller has got in preparing the program of the task'''
		return RapidTaskState(int(self._instance.TaskState))

	@task_state.setter
	def task_state(self, value: RapidTaskState):
		self._instance.TaskState = rapid_task_state(int(value))

	@property
	def execution_state(self) -> RapidTaskExecutionState:
		'''Whether the task is running, and whether it could be'''
		return RapidTaskExecutionState(int(self._instance.ExecutionState))

	@execution_state.setter
	def execution_state(self, value: RapidTaskExecutionState):
		self._instance.ExecutionState = rapid_task_execution_state(int(value))

	@property
	def active(self) -> bool | None:
		'''Whether the task is active, null when the controller did not report it'''
		return self._instance.Active

	@active.setter
	def active(self, value: bool | None):
		self._instance.Active = value

	@property
	def motion_task(self) -> bool | None:
		'''Whether the task can move a mechanical unit, null when the controller did not report it'''
		return self._instance.MotionTask

	@motion_task.setter
	def motion_task(self, value: bool | None):
		self._instance.MotionTask = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidTaskItem):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
