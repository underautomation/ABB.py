from __future__ import annotations
import typing
from underautomation.abb.rws.data.calibration_info import CalibrationInfo
from underautomation.abb.rws.data.motor_calibration_name import MotorCalibrationName
from underautomation.abb.rws.data.smb_data import SmbData
from underautomation.abb.rws.data.smb_data_transfer import SmbDataTransfer
from underautomation.abb.rws.data.smb_data_memory import SmbDataMemory
from underautomation.abb.rws.data.motion_system_info import MotionSystemInfo
from underautomation.abb.rws.data.motion_system_error_state import MotionSystemErrorState
from underautomation.abb.common.robot_joints import RobotJoints
from underautomation.abb.rws.data.jog_increment_mode import JogIncrementMode
from underautomation.abb.common.rob_target import RobTarget
from underautomation.abb.common.pose import Pose
from underautomation.abb.common.joint_target import JointTarget
from underautomation.abb.common.external_joints import ExternalJoints
from underautomation.abb.common.robot_configuration import RobotConfiguration
from underautomation.abb.rws.data.joint_solution import JointSolution
from underautomation.abb.rws.data.mechanical_unit_item import MechanicalUnitItem
from underautomation.abb.rws.data.mechanical_unit_info import MechanicalUnitInfo
from underautomation.abb.rws.data.axis_info import AxisInfo
from underautomation.abb.rws.data.base_frame import BaseFrame
from underautomation.abb.rws.data.coordinate_system import CoordinateSystem
from underautomation.abb.rws.data.lead_through_status import LeadThroughStatus
from underautomation.abb.rws.data.motion_supervision import MotionSupervision
from underautomation.abb.rws.data.path_supervision import PathSupervision
from underautomation.abb.rws.data.mechanical_unit_mode import MechanicalUnitMode
from underautomation.abb.rws.data.jog_mode import JogMode
from UnderAutomation.ABB.Rws.Services import MotionSystemService as motion_system_service
from UnderAutomation.ABB.Rws.Data import SmbDataTransfer as smb_data_transfer
from UnderAutomation.ABB.Rws.Data import SmbDataMemory as smb_data_memory
from UnderAutomation.ABB.Rws.Data import JogIncrementMode as jog_increment_mode
from UnderAutomation.ABB.Rws.Data import CoordinateSystem as coordinate_system
from UnderAutomation.ABB.Rws.Data import LeadThroughStatus as lead_through_status
from UnderAutomation.ABB.Rws.Data import MechanicalUnitMode as mechanical_unit_mode
from UnderAutomation.ABB.Rws.Data import JogMode as jog_mode

class MotionSystemService:
	'''Motion System Service - Everything about how the robot stands and how it moves: the mechanical units of the system and their axes, where the tool currently is, the calibration and the revolution counters, jogging, the collision supervision, and the kinematics calculations that convert a pose into joint values and back. None of these resources is available while the controller runs in bootserver mode.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = motion_system_service()
		else:
			self._instance = _internal

	def get_calibration_info(self, mechanicalUnit: str) -> CalibrationInfo:
		'''Gets how each joint of a mechanical unit was calibrated (synchronous)

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:returns: Calibration of the unit, with one entry per joint slot
		'''
		return CalibrationInfo(self._instance.GetCalibrationInfo(mechanicalUnit))

	def get_motor_calibration_names(self, mechanicalUnit: str) -> typing.List[MotorCalibrationName]:
		'''Gets the name each joint of a mechanical unit carries, and the name of its calibration data (synchronous)

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:returns: One entry per joint of the unit
		'''
		return [MotorCalibrationName(x) for x in self._instance.GetMotorCalibrationNames(mechanicalUnit)]

	def get_smb_data(self, mechanicalUnit: str) -> SmbData:
		'''Gets the serial measurement board data of a mechanical unit, as held by the controller cabinet and by the robot itself (synchronous) The two copies are meant to agree. When they do not, one of them is written over the other with .

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:returns: Both copies of the measurement board data
		'''
		return SmbData(self._instance.GetSmbData(mechanicalUnit))

	def set_smb_data(self, mechanicalUnit: str, direction: SmbDataTransfer) -> None:
		'''Copies one of the two serial measurement board data stores over the other (synchronous)

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:param direction: Which copy overwrites which
		'''
		self._instance.SetSmbData(mechanicalUnit, smb_data_transfer(int(direction)))

	def clear_smb_data(self, mechanicalUnit: str, memory: SmbDataMemory) -> None:
		'''Erases one of the two serial measurement board data stores (synchronous)

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:param memory: Which of the two copies to erase
		'''
		self._instance.ClearSmbData(mechanicalUnit, smb_data_memory(int(memory)))

	def get_info(self) -> MotionSystemInfo:
		'''Gets an overview of the motion system: the mechanical unit jogging applies to, the change counter and the payload and accuracy settings (synchronous)

		:returns: Overview of the motion system
		'''
		return MotionSystemInfo(self._instance.GetInfo())

	def has_changed(self, changeCount: int) -> bool:
		'''Tells whether the motion system changed since it reported the given change count (synchronous) Reading once and asking this afterwards is cheaper than fetching the whole state again to find out that nothing moved.

		:param changeCount: Change count a previous reading reported
		:returns: True when the motion system changed since then, false when it did not
		'''
		return self._instance.HasChanged(changeCount)

	def get_error_state(self) -> MotionSystemErrorState:
		'''Gets the last error the motion system ran into, and how many errors it has counted (synchronous) Most of these errors are raised by a jogging request the controller could not honour, and stay reported until a new one replaces them.

		:returns: Error state of the motion system
		'''
		return MotionSystemErrorState(self._instance.GetErrorState())

	def get_non_motion_execution_mode(self) -> bool:
		'''Tells whether the controller runs RAPID programs without moving the robot (synchronous) In that mode the program executes normally but every motion instruction is skipped, which is how a program is tested without the robot leaving its position.

		:returns: True when the motion instructions are skipped, false when the robot really moves
		'''
		return self._instance.GetNonMotionExecutionMode()

	def set_non_motion_execution_mode(self, enabled: bool) -> None:
		'''Chooses whether the controller runs RAPID programs without moving the robot (synchronous)

		:param enabled: True to skip every motion instruction, false to let the robot move
		'''
		self._instance.SetNonMotionExecutionMode(enabled)

	def get_collision_prediction_mode(self) -> bool:
		'''Tells whether the controller predicts collisions before they happen (synchronous) Collision prediction stops the robot before it hits something it knows about, where the motion supervision only reacts once the arm meets an unexpected resistance.

		:returns: True when collision prediction is switched on
		'''
		return self._instance.GetCollisionPredictionMode()

	def set_collision_prediction_mode(self, enabled: bool) -> None:
		'''Switches collision prediction on or off (synchronous)

		:param enabled: True to predict collisions, false to switch the prediction off
		'''
		self._instance.SetCollisionPredictionMode(enabled)

	def jog(self, axes: RobotJoints, changeCount: int, incrementMode: JogIncrementMode=JogIncrementMode.None_) -> None:
		'''Moves the mechanical unit currently selected for jogging (synchronous) The unit is the one chose, and how the six values are interpreted depends on its jog mode: axis by axis, along the axes of a coordinate system, and so on.

		:param axes: Value requested for each of the six axes
		:param changeCount: Change count of the last reading of the motion system, which the controller uses to reject a command based on a state that has moved on since
		:param incrementMode: Size of the step to move by, None to move continuously for as long as the command is repeated
		'''
		self._instance.Jog(axes._instance if axes else None, changeCount, jog_increment_mode(int(incrementMode)))

	def set_jogging_mechanical_unit(self, mechanicalUnit: str) -> None:
		'''Chooses which mechanical unit the jogging commands apply to (synchronous)

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		'''
		self._instance.SetJoggingMechanicalUnit(mechanicalUnit)

	def set_position_target(self, target: RobTarget) -> None:
		'''Sends the robot to a cartesian target (synchronous) The position is expressed in millimetres, in the coordinate system currently active for the mechanical unit selected for jogging.

		:param target: Target to move to, with the axis configuration to reach it in and the external axis values that travel with it
		'''
		self._instance.SetPositionTarget(target._instance if target else None)

	def get_pose_from_joints(self, mechanicalUnit: str, toolFrame: Pose, joints: JointTarget, robotHoldsWorkObject: bool=False, logErrors: bool=False) -> RobTarget:
		'''Asks the controller where the tool would be if the robot stood at the given joint values, without moving it there (synchronous)

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:param toolFrame: Position and orientation of the tool relative to the mounting flange
		:param joints: Joint values to compute the pose of
		:param robotHoldsWorkObject: True when the robot carries the work object and the tool is fixed in the cell, false in the usual case where the robot carries the tool
		:param logErrors: True to have the controller write an event log message when the calculation fails
		:returns: Pose the tool would be at, with the axis configuration and the external axis values
		'''
		return RobTarget(None, None, None, None, None, None, self._instance.GetPoseFromJoints(mechanicalUnit, toolFrame._instance if toolFrame else None, joints._instance if joints else None, robotHoldsWorkObject, logErrors))

	def get_joints_from_cartesian(self, mechanicalUnit: str, pose: Pose, externalAxes: ExternalJoints, toolFrame: Pose, previousJoints: JointTarget, configuration: RobotConfiguration, robotHoldsWorkObject: bool=False, logErrors: bool=False) -> JointTarget:
		'''Asks the controller which joint values put the tool at the given pose, staying close to the joint values the robot is already in (synchronous)

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:param pose: Pose to reach, in metres
		:param externalAxes: External axis values that go with that pose
		:param toolFrame: Position and orientation of the tool relative to the mounting flange
		:param previousJoints: Joint values the robot is currently in, which decide between the solutions the pose admits
		:param configuration: Axis configuration to reach the pose in
		:param robotHoldsWorkObject: True when the robot carries the work object and the tool is fixed in the cell, false in the usual case where the robot carries the tool
		:param logErrors: True to have the controller write an event log message when the calculation fails
		:returns: Joint values that reach the pose, in radians
		'''
		return JointTarget(None, None, self._instance.GetJointsFromCartesian(mechanicalUnit, pose._instance if pose else None, externalAxes._instance if externalAxes else None, toolFrame._instance if toolFrame else None, previousJoints._instance if previousJoints else None, configuration._instance if configuration else None, robotHoldsWorkObject, logErrors))

	def get_joints_from_pose(self, mechanicalUnit: str, pose: Pose, externalAxes: ExternalJoints, toolFrame: Pose, previousJoints: JointTarget, configuration: RobotConfiguration, robotHoldsWorkObject: bool=False, logErrors: bool=False) -> JointTarget:
		'''Asks the controller which joint values put the tool at the given pose (synchronous)

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:param pose: Pose to reach, in metres
		:param externalAxes: External axis values that go with that pose
		:param toolFrame: Position and orientation of the tool relative to the mounting flange
		:param previousJoints: Joint values the robot is currently in, which decide between the solutions the pose admits
		:param configuration: Axis configuration to reach the pose in
		:param robotHoldsWorkObject: True when the robot carries the work object and the tool is fixed in the cell, false in the usual case where the robot carries the tool
		:param logErrors: True to have the controller write an event log message when the calculation fails
		:returns: Joint values that reach the pose, in radians
		'''
		return JointTarget(None, None, self._instance.GetJointsFromPose(mechanicalUnit, pose._instance if pose else None, externalAxes._instance if externalAxes else None, toolFrame._instance if toolFrame else None, previousJoints._instance if previousJoints else None, configuration._instance if configuration else None, robotHoldsWorkObject, logErrors))

	def get_all_joint_solutions(self, mechanicalUnit: str, pose: Pose, externalAxes: ExternalJoints, toolFrame: Pose, configuration: RobotConfiguration, robotHoldsWorkObject: bool=False) -> typing.List[JointSolution]:
		'''Asks the controller for every joint combination that puts the tool at the given pose (synchronous) A six axis robot usually reaches the same pose in eight different ways, each one in a different axis configuration.

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:param pose: Pose to reach, in metres
		:param externalAxes: External axis values that go with that pose
		:param toolFrame: Position and orientation of the tool relative to the mounting flange
		:param configuration: Axis configuration the pose is given in
		:param robotHoldsWorkObject: True when the robot carries the work object and the tool is fixed in the cell, false in the usual case where the robot carries the tool
		:returns: One entry per solution, each with the joint values in radians and the axis configuration it corresponds to
		'''
		return [JointSolution(x) for x in self._instance.GetAllJointSolutions(mechanicalUnit, pose._instance if pose else None, externalAxes._instance if externalAxes else None, toolFrame._instance if toolFrame else None, configuration._instance if configuration else None, robotHoldsWorkObject)]

	def get_mechanical_units(self) -> typing.List[MechanicalUnitItem]:
		'''Lists the mechanical units of the motion system (synchronous)

		:returns: Mechanical units, with their activation state. Empty when the system declares none.
		'''
		return [MechanicalUnitItem(x) for x in self._instance.GetMechanicalUnits()]

	def get_mechanical_unit(self, mechanicalUnit: str) -> MechanicalUnitInfo:
		'''Gets everything the controller knows about one mechanical unit (synchronous)

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:returns: Properties of the mechanical unit
		'''
		return MechanicalUnitInfo(self._instance.GetMechanicalUnit(mechanicalUnit))

	def set_mechanical_unit(self, mechanicalUnit: str, tool: str=None, workObject: str=None, payload: str=None, totalPayload: str=None, mode: MechanicalUnitMode | None=None, jogMode: JogMode | None=None, coordinateSystem: CoordinateSystem | None=None) -> None:
		self._instance.SetMechanicalUnit(mechanicalUnit, tool, workObject, payload, totalPayload, mode, jogMode, coordinateSystem)

	def get_axis_count(self, mechanicalUnit: str) -> int:
		'''Gets how many axes a mechanical unit has (synchronous)

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:returns: Number of axes, which are numbered from 1 to that value
		'''
		return self._instance.GetAxisCount(mechanicalUnit)

	def get_axis(self, mechanicalUnit: str, axis: int) -> AxisInfo:
		'''Gets the state of one axis of a mechanical unit (synchronous)

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:param axis: Number of the axis, starting at 1
		:returns: State of the axis
		'''
		return AxisInfo(self._instance.GetAxis(mechanicalUnit, axis))

	def get_axis_pose(self, mechanicalUnit: str, axis: int) -> Pose:
		'''Gets where one axis of a mechanical unit sits (synchronous) The position is expressed in millimetres.

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:param axis: Number of the axis, starting at 1
		:returns: Position and orientation of the axis
		'''
		return Pose(None, None, None, None, None, None, None, self._instance.GetAxisPose(mechanicalUnit, axis))

	def set_axis_pose(self, mechanicalUnit: str, axis: int, pose: Pose) -> None:
		'''Declares where one axis of a mechanical unit sits (synchronous) The position is expressed in millimetres.

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:param axis: Number of the axis, starting at 1
		:param pose: Position and orientation to declare for the axis
		'''
		self._instance.SetAxisPose(mechanicalUnit, axis, pose._instance if pose else None)

	def commutate(self, mechanicalUnit: str, axis: int) -> None:
		'''Commutates the motor of one axis, which teaches the controller how the rotor of that motor is oriented (synchronous) Needed once after a motor has been replaced, before the axis can be calibrated.

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:param axis: Number of the axis, starting at 1
		'''
		self._instance.Commutate(mechanicalUnit, axis)

	def synchronize_axis_revolution_counter(self, mechanicalUnit: str, axis: int) -> None:
		'''Synchronizes the revolution counter of one axis, telling the controller that the axis stands at its synchronization mark (synchronous)

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:param axis: Number of the axis, starting at 1
		'''
		self._instance.SynchronizeAxisRevolutionCounter(mechanicalUnit, axis)

	def update_revolution_counter(self, mechanicalUnit: str, axis: int) -> None:
		'''Updates the revolution counter of one axis of a mechanical unit (synchronous)

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:param axis: Number of the axis, starting at 1
		'''
		self._instance.UpdateRevolutionCounter(mechanicalUnit, axis)

	def fine_calibrate(self, mechanicalUnit: str, axis: int) -> None:
		'''Fine calibrates one axis of a mechanical unit (synchronous)

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:param axis: Number of the axis, starting at 1
		'''
		self._instance.FineCalibrate(mechanicalUnit, axis)

	def get_base_frame(self, mechanicalUnit: str) -> BaseFrame:
		'''Gets where the base of a mechanical unit sits (synchronous) The position is expressed in millimetres.

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:returns: Base frame of the mechanical unit, with the kind of base it is
		'''
		return BaseFrame(self._instance.GetBaseFrame(mechanicalUnit))

	def set_base_frame(self, mechanicalUnit: str, baseFrame: Pose) -> None:
		'''Declares where the base of a mechanical unit sits (synchronous) The position is expressed in millimetres.

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:param baseFrame: Position and orientation of the base of the unit
		'''
		self._instance.SetBaseFrame(mechanicalUnit, baseFrame._instance if baseFrame else None)

	def get_rob_target(self, mechanicalUnit: str, coordinateSystem: CoordinateSystem=CoordinateSystem.Base, tool: str=None, workObject: str=None) -> RobTarget:
		'''Gets where the tool of a mechanical unit currently is (synchronous) The position is expressed in millimetres.

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:param coordinateSystem: Reference frame to express the position in
		:param tool: Name of the tool to measure from, null to use the tool active on the unit
		:param workObject: Name of the work object to measure against, null to use the one active on the unit
		:returns: Position, orientation, axis configuration and external axis values of the tool
		'''
		return RobTarget(None, None, None, None, None, None, self._instance.GetRobTarget(mechanicalUnit, coordinate_system(int(coordinateSystem)), tool, workObject))

	def get_cartesian_position(self, mechanicalUnit: str, coordinateSystem: CoordinateSystem=CoordinateSystem.Base, tool: str=None, workObject: str=None, logErrors: bool=False) -> RobTarget:
		'''Gets where the tool of a mechanical unit currently is, without the external axes (synchronous) The position is expressed in millimetres.

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:param coordinateSystem: Reference frame to express the position in
		:param tool: Name of the tool to measure from, null to use the tool active on the unit
		:param workObject: Name of the work object to measure against, null to use the one active on the unit
		:param logErrors: True to have the controller write an event log message when the reading fails
		:returns: Position, orientation and axis configuration of the tool. ExternalAxes is null: this reading does not report them, use String) when they are needed.
		'''
		return RobTarget(None, None, None, None, None, None, self._instance.GetCartesianPosition(mechanicalUnit, coordinate_system(int(coordinateSystem)), tool, workObject, logErrors))

	def get_joint_target(self, mechanicalUnit: str, alwaysRead: bool=False) -> JointTarget:
		'''Gets the joint values a mechanical unit currently stands at (synchronous) The robot axes are expressed in degrees.

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:param alwaysRead: True to have the controller measure the position again instead of answering with the value it already holds
		:returns: Joint values of the six robot axes and of the six external axes
		'''
		return JointTarget(None, None, self._instance.GetJointTarget(mechanicalUnit, alwaysRead))

	def get_physical_joints(self, mechanicalUnit: str) -> RobotJoints:
		'''Gets the physical joint values of a mechanical unit, as its measurement system reads them (synchronous)

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:returns: Physical value of the six axes
		'''
		return RobotJoints(None, None, None, None, None, None, self._instance.GetPhysicalJoints(mechanicalUnit))

	def set_mechanical_unit_position(self, mechanicalUnit: str, position: JointTarget) -> None:
		'''Places a mechanical unit at the given joint values without moving it there (synchronous) Only a virtual controller accepts this: it teleports the simulated robot, which a real one cannot do.

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:param position: Joint values to place the unit at, robot axes in degrees
		'''
		self._instance.SetMechanicalUnitPosition(mechanicalUnit, position._instance if position else None)

	def get_lead_through(self, mechanicalUnit: str) -> LeadThroughStatus:
		'''Tells whether an operator can push the arm of a mechanical unit around by hand (synchronous)

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:returns: Whether the arm gives way when pushed
		'''
		return LeadThroughStatus(int(self._instance.GetLeadThrough(mechanicalUnit)))

	def set_lead_through(self, mechanicalUnit: str, active: bool) -> None:
		'''Lets an operator push the arm of a mechanical unit around by hand, or stops letting them (synchronous)

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:param active: True to let the arm give way when pushed, false to have it hold its position
		'''
		self._instance.SetLeadThrough(mechanicalUnit, active)

	def get_motion_supervision(self, mechanicalUnit: str) -> MotionSupervision:
		'''Gets the collision detection settings that apply while a mechanical unit is jogged (synchronous)

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:returns: Whether the supervision is switched on, and how sensitive it is
		'''
		return MotionSupervision(self._instance.GetMotionSupervision(mechanicalUnit))

	def set_motion_supervision_mode(self, mechanicalUnit: str, enabled: bool) -> None:
		'''Switches the jogging collision detection of a mechanical unit on or off (synchronous)

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:param enabled: True to watch for collisions while the unit is jogged, false to stop watching
		'''
		self._instance.SetMotionSupervisionMode(mechanicalUnit, enabled)

	def set_motion_supervision_level(self, mechanicalUnit: str, sensitivity: int) -> None:
		'''Sets how sensitive the jogging collision detection of a mechanical unit is (synchronous)

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:param sensitivity: Sensitivity as a percentage: the lower the value, the sooner a collision is reported
		'''
		self._instance.SetMotionSupervisionLevel(mechanicalUnit, sensitivity)

	def get_path_supervision(self, mechanicalUnit: str) -> PathSupervision:
		'''Gets the collision detection settings that apply while a mechanical unit follows a programmed path (synchronous)

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:returns: Whether the supervision is switched on, and how sensitive it is
		'''
		return PathSupervision(self._instance.GetPathSupervision(mechanicalUnit))

	def set_path_supervision_mode(self, mechanicalUnit: str, enabled: bool) -> None:
		'''Switches the path collision detection of a mechanical unit on or off (synchronous)

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:param enabled: True to watch for collisions along the programmed path, false to stop watching
		'''
		self._instance.SetPathSupervisionMode(mechanicalUnit, enabled)

	def set_path_supervision_level(self, mechanicalUnit: str, level: int) -> None:
		'''Sets how sensitive the path collision detection of a mechanical unit is (synchronous)

		:param mechanicalUnit: Name of the mechanical unit, for example "ROB_1"
		:param level: Sensitivity as a percentage: the lower the value, the sooner a collision is reported
		'''
		self._instance.SetPathSupervisionLevel(mechanicalUnit, level)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MotionSystemService):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
