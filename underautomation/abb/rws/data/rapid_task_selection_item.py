from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import RapidTaskSelectionItem as rapid_task_selection_item

class RapidTaskSelectionItem:
	'''One line of the task selection panel, telling whether a task is selected and whether an operator is allowed to change that. Returned by RapidService.GetTaskSelection().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidTaskSelectionItem class'''
		if(_internal == 0):
			self._instance = rapid_task_selection_item()
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
	def selected(self) -> bool | None:
		'''Whether the task is selected, null when the controller did not report it'''
		return self._instance.Selected

	@selected.setter
	def selected(self, value: bool | None):
		self._instance.Selected = value

	@property
	def motion_task(self) -> bool | None:
		'''Whether the task can move a mechanical unit, null when the controller did not report it'''
		return self._instance.MotionTask

	@motion_task.setter
	def motion_task(self, value: bool | None):
		self._instance.MotionTask = value

	@property
	def user_modify(self) -> bool | None:
		'''Whether an operator is allowed to change the selection of this task, null when the controller did not report it'''
		return self._instance.UserModify

	@user_modify.setter
	def user_modify(self, value: bool | None):
		self._instance.UserModify = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidTaskSelectionItem):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
