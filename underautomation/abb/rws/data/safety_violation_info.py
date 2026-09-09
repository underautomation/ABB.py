from __future__ import annotations
import typing
from underautomation.abb.rws.data.safety_violation_type import SafetyViolationType
from UnderAutomation.ABB.Rws.Data import SafetyViolationInfo as safety_violation_info
from UnderAutomation.ABB.Rws.Data import SafetyViolationType as safety_violation_type

class SafetyViolationInfo:
	'''Safety violation details reported by the safety controller. Returned by ControllerService.GetSafetyViolationInfo().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the SafetyViolationInfo class'''
		if(_internal == 0):
			self._instance = safety_violation_info()
		else:
			self._instance = _internal

	@property
	def violation_number(self) -> int | None:
		'''Number of violations'''
		return self._instance.ViolationNumber

	@violation_number.setter
	def violation_number(self, value: int | None):
		self._instance.ViolationNumber = value

	@property
	def violation_type(self) -> SafetyViolationType:
		'''Type of the current violation'''
		return SafetyViolationType(int(self._instance.ViolationType))

	@violation_type.setter
	def violation_type(self, value: SafetyViolationType):
		self._instance.ViolationType = safety_violation_type(int(value))

	@property
	def last_violation_instance_id(self) -> int | None:
		'''Instance id of the last violation'''
		return self._instance.LastViolationInstanceId

	@last_violation_instance_id.setter
	def last_violation_instance_id(self, value: int | None):
		self._instance.LastViolationInstanceId = value

	@property
	def unsynchronized(self) -> int | None:
		'''Indicates whether the robot is unsynchronized'''
		return self._instance.Unsynchronized

	@unsynchronized.setter
	def unsynchronized(self, value: int | None):
		self._instance.Unsynchronized = value

	@property
	def tool_id(self) -> int | None:
		'''Id of the tool involved in the violation'''
		return self._instance.ToolId

	@tool_id.setter
	def tool_id(self, value: int | None):
		self._instance.ToolId = value

	@property
	def drive_module_index(self) -> int | None:
		'''Index of the drive module involved in the violation'''
		return self._instance.DriveModuleIndex

	@drive_module_index.setter
	def drive_module_index(self, value: int | None):
		self._instance.DriveModuleIndex = value

	@property
	def violating_ssv(self) -> int | None:
		'''Violating safety supervision value'''
		return self._instance.ViolatingSsv

	@violating_ssv.setter
	def violating_ssv(self, value: int | None):
		self._instance.ViolatingSsv = value

	@property
	def tool_position_violation_status(self) -> int | None:
		'''Tool position violation status'''
		return self._instance.ToolPositionViolationStatus

	@tool_position_violation_status.setter
	def tool_position_violation_status(self, value: int | None):
		self._instance.ToolPositionViolationStatus = value

	@property
	def tool_position_active_status(self) -> int | None:
		'''Tool position supervision active status'''
		return self._instance.ToolPositionActiveStatus

	@tool_position_active_status.setter
	def tool_position_active_status(self, value: int | None):
		self._instance.ToolPositionActiveStatus = value

	@property
	def upper_arm_violation_status(self) -> int | None:
		'''Upper arm violation status'''
		return self._instance.UpperArmViolationStatus

	@upper_arm_violation_status.setter
	def upper_arm_violation_status(self, value: int | None):
		self._instance.UpperArmViolationStatus = value

	@property
	def tool_speed_violation_status(self) -> int | None:
		'''Tool speed violation status'''
		return self._instance.ToolSpeedViolationStatus

	@tool_speed_violation_status.setter
	def tool_speed_violation_status(self, value: int | None):
		self._instance.ToolSpeedViolationStatus = value

	@property
	def tool_speed_active_status(self) -> int | None:
		'''Tool speed supervision active status'''
		return self._instance.ToolSpeedActiveStatus

	@tool_speed_active_status.setter
	def tool_speed_active_status(self, value: int | None):
		self._instance.ToolSpeedActiveStatus = value

	@property
	def axis_range_violation_status(self) -> int | None:
		'''Axis range violation status'''
		return self._instance.AxisRangeViolationStatus

	@axis_range_violation_status.setter
	def axis_range_violation_status(self, value: int | None):
		self._instance.AxisRangeViolationStatus = value

	@property
	def axis_range_active_status(self) -> int | None:
		'''Axis range supervision active status'''
		return self._instance.AxisRangeActiveStatus

	@axis_range_active_status.setter
	def axis_range_active_status(self, value: int | None):
		self._instance.AxisRangeActiveStatus = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SafetyViolationInfo):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
