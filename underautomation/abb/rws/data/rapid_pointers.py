from __future__ import annotations
import typing
from underautomation.abb.rws.data.rapid_pointer_position import RapidPointerPosition
from UnderAutomation.ABB.Rws.Data import RapidPointers as rapid_pointers

class RapidPointers:
	'''The program pointer and the motion pointer of a task, read in one request. Returned by RapidService.GetPointers(). The program pointer says which instruction runs next, the motion pointer which one the robot is actually executing; they drift apart because the controller plans the path ahead of the movement.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidPointers class'''
		if(_internal == 0):
			self._instance = rapid_pointers()
		else:
			self._instance = _internal

	@property
	def program_pointer(self) -> RapidPointerPosition:
		'''Instruction the task will execute next'''
		return RapidPointerPosition(self._instance.ProgramPointer)

	@program_pointer.setter
	def program_pointer(self, value: RapidPointerPosition):
		self._instance.ProgramPointer = value._instance if value else None

	@property
	def motion_pointer(self) -> RapidPointerPosition:
		'''Instruction the robot is currently moving for'''
		return RapidPointerPosition(self._instance.MotionPointer)

	@motion_pointer.setter
	def motion_pointer(self, value: RapidPointerPosition):
		self._instance.MotionPointer = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidPointers):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
