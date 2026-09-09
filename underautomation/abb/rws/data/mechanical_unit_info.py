from __future__ import annotations
import typing
from underautomation.abb.rws.data.mechanical_unit_status import MechanicalUnitStatus
from underautomation.abb.rws.data.mechanical_unit_mode import MechanicalUnitMode
from underautomation.abb.rws.data.jog_mode import JogMode
from underautomation.abb.rws.data.mechanical_unit_type import MechanicalUnitType
from underautomation.abb.rws.data.coordinate_system import CoordinateSystem
from UnderAutomation.ABB.Rws.Data import MechanicalUnitInfo as mechanical_unit_info
from UnderAutomation.ABB.Rws.Data import MechanicalUnitStatus as mechanical_unit_status
from UnderAutomation.ABB.Rws.Data import MechanicalUnitMode as mechanical_unit_mode
from UnderAutomation.ABB.Rws.Data import JogMode as jog_mode
from UnderAutomation.ABB.Rws.Data import MechanicalUnitType as mechanical_unit_type
from UnderAutomation.ABB.Rws.Data import CoordinateSystem as coordinate_system

class MechanicalUnitInfo:
	'''Everything the controller knows about one mechanical unit. Returned by MotionSystemService.GetMechanicalUnit().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the MechanicalUnitInfo class'''
		if(_internal == 0):
			self._instance = mechanical_unit_info()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Name of the mechanical unit, for example "ROB_1"'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def tool_name(self) -> str:
		'''Name of the active tool'''
		return self._instance.ToolName

	@tool_name.setter
	def tool_name(self, value: str):
		self._instance.ToolName = value

	@property
	def work_object_name(self) -> str:
		'''Name of the active work object'''
		return self._instance.WorkObjectName

	@work_object_name.setter
	def work_object_name(self, value: str):
		self._instance.WorkObjectName = value

	@property
	def payload_name(self) -> str:
		'''Name of the active payload'''
		return self._instance.PayloadName

	@payload_name.setter
	def payload_name(self, value: str):
		self._instance.PayloadName = value

	@property
	def total_payload_name(self) -> str:
		'''Name of the active total payload, which is the payload plus the load of the tool'''
		return self._instance.TotalPayloadName

	@total_payload_name.setter
	def total_payload_name(self, value: str):
		self._instance.TotalPayloadName = value

	@property
	def status(self) -> MechanicalUnitStatus:
		'''Calibration and synchronization state of the unit'''
		return MechanicalUnitStatus(int(self._instance.Status))

	@status.setter
	def status(self, value: MechanicalUnitStatus):
		self._instance.Status = mechanical_unit_status(int(value))

	@property
	def mode(self) -> MechanicalUnitMode:
		'''Whether the unit is activated'''
		return MechanicalUnitMode(int(self._instance.Mode))

	@mode.setter
	def mode(self, value: MechanicalUnitMode):
		self._instance.Mode = mechanical_unit_mode(int(value))

	@property
	def jog_mode(self) -> JogMode:
		'''How the jogging commands sent to the unit are interpreted'''
		return JogMode(int(self._instance.JogMode))

	@jog_mode.setter
	def jog_mode(self, value: JogMode):
		self._instance.JogMode = jog_mode(int(value))

	@property
	def type(self) -> MechanicalUnitType:
		'''Kind of mechanical unit'''
		return MechanicalUnitType(int(self._instance.Type))

	@type.setter
	def type(self, value: MechanicalUnitType):
		self._instance.Type = mechanical_unit_type(int(value))

	@property
	def task_name(self) -> str:
		'''Name of the RAPID task that drives the unit'''
		return self._instance.TaskName

	@task_name.setter
	def task_name(self, value: str):
		self._instance.TaskName = value

	@property
	def coordinate_system(self) -> CoordinateSystem:
		'''Reference frame the cartesian positions of the unit are expressed in'''
		return CoordinateSystem(int(self._instance.CoordinateSystem))

	@coordinate_system.setter
	def coordinate_system(self, value: CoordinateSystem):
		self._instance.CoordinateSystem = coordinate_system(int(value))

	@property
	def axes(self) -> int | None:
		'''Number of axes of the unit, null when the controller did not report it'''
		return self._instance.Axes

	@axes.setter
	def axes(self, value: int | None):
		self._instance.Axes = value

	@property
	def total_axes(self) -> int | None:
		'''Number of axes of the unit and of the units integrated with it, null when the controller did not report it'''
		return self._instance.TotalAxes

	@total_axes.setter
	def total_axes(self, value: int | None):
		self._instance.TotalAxes = value

	@property
	def is_integrated_unit(self) -> str:
		'''Name of the mechanical unit this one is integrated into. A unit that is integrated into no other one is reported with a placeholder name rather than an empty value.'''
		return self._instance.IsIntegratedUnit

	@is_integrated_unit.setter
	def is_integrated_unit(self, value: str):
		self._instance.IsIntegratedUnit = value

	@property
	def has_integrated_unit(self) -> str:
		'''Name of the mechanical unit integrated into this one. A unit that integrates no other one is reported with a placeholder name rather than an empty value.'''
		return self._instance.HasIntegratedUnit

	@has_integrated_unit.setter
	def has_integrated_unit(self, value: str):
		self._instance.HasIntegratedUnit = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MechanicalUnitInfo):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
