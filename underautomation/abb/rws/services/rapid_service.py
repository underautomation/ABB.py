from __future__ import annotations
import typing
from underautomation.abb.rws.data.rapid_execution_info import RapidExecutionInfo
from underautomation.abb.rws.data.rapid_regain_mode import RapidRegainMode
from underautomation.abb.rws.data.rapid_execution_mode import RapidExecutionMode
from underautomation.abb.rws.data.rapid_execution_cycle import RapidExecutionCycle
from underautomation.abb.rws.data.rapid_start_condition import RapidStartCondition
from underautomation.abb.rws.data.rapid_stop_mode import RapidStopMode
from underautomation.abb.rws.data.rapid_task_scope import RapidTaskScope
from underautomation.abb.rws.data.rapid_hold_to_run_state import RapidHoldToRunState
from underautomation.abb.rws.data.rapid_task_selection_item import RapidTaskSelectionItem
from underautomation.abb.rws.data.rapid_alias_io_item import RapidAliasIoItem
from underautomation.abb.rws.data.rapid_module_item import RapidModuleItem
from underautomation.abb.rws.data.rapid_module_info import RapidModuleInfo
from underautomation.abb.rws.data.rapid_module_extension import RapidModuleExtension
from underautomation.abb.rws.data.rapid_module_text import RapidModuleText
from underautomation.abb.rws.data.rapid_set_text_range_result import RapidSetTextRangeResult
from underautomation.abb.rws.data.rapid_text_replace_mode import RapidTextReplaceMode
from underautomation.abb.rws.data.rapid_text_query_mode import RapidTextQueryMode
from underautomation.abb.rws.data.rapid_text_position import RapidTextPosition
from underautomation.abb.rws.data.rapid_module_attribute import RapidModuleAttribute
from underautomation.abb.rws.data.rapid_module_symbol import RapidModuleSymbol
from underautomation.abb.rws.data.rapid_routine_info import RapidRoutineInfo
from underautomation.abb.rws.data.rapid_routine_argument import RapidRoutineArgument
from underautomation.abb.rws.data.rapid_instruction_template import RapidInstructionTemplate
from underautomation.abb.rws.data.rapid_object_child import RapidObjectChild
from underautomation.abb.rws.data.rapid_modifiable_positions import RapidModifiablePositions
from underautomation.abb.rws.data.rapid_modifiable_position_item import RapidModifiablePositionItem
from underautomation.abb.common.rob_target import RobTarget
from underautomation.abb.common.joint_target import JointTarget
from underautomation.abb.rws.data.rapid_external_joint_states import RapidExternalJointStates
from underautomation.abb.rws.data.rapid_mechanical_unit_item import RapidMechanicalUnitItem
from underautomation.abb.rws.data.rapid_program_info import RapidProgramInfo
from underautomation.abb.rws.data.rapid_program_load_mode import RapidProgramLoadMode
from underautomation.abb.rws.data.rapid_breakpoint import RapidBreakpoint
from underautomation.abb.rws.data.rapid_build_error import RapidBuildError
from underautomation.abb.rws.data.rapid_program_counter_position import RapidProgramCounterPosition
from underautomation.abb.rws.data.rapid_pointers import RapidPointers
from underautomation.abb.rws.data.rapid_symbol_properties import RapidSymbolProperties
from underautomation.abb.rws.data.rapid_symbol_value import RapidSymbolValue
from underautomation.abb.rws.data.rapid_symbol_search_criteria import RapidSymbolSearchCriteria
from underautomation.abb.rws.data.rapid_object_list_extension import RapidObjectListExtension
from underautomation.abb.rws.data.rapid_object_list_type import RapidObjectListType
from underautomation.abb.rws.data.rapid_task_item import RapidTaskItem
from underautomation.abb.rws.data.rapid_task_info import RapidTaskInfo
from underautomation.abb.rws.data.rapid_spy_status import RapidSpyStatus
from underautomation.abb.rws.data.rapid_pointer_sync_state import RapidPointerSyncState
from underautomation.abb.rws.data.rapid_structural_change_count import RapidStructuralChangeCount
from underautomation.abb.rws.data.rapid_activation_record import RapidActivationRecord
from underautomation.abb.rws.data.rapid_service_routine_item import RapidServiceRoutineItem
from underautomation.abb.rws.data.rapid_preferred_data_type_item import RapidPreferredDataTypeItem
from underautomation.abb.rws.data.rapid_pallet_head_item import RapidPalletHeadItem
from underautomation.abb.rws.data.rapid_pallet_item import RapidPalletItem
from underautomation.abb.rws.data.rapid_ui_instruction import RapidUiInstruction
from underautomation.abb.rws.data.rapid_ui_instruction_parameter import RapidUiInstructionParameter
from UnderAutomation.ABB.Rws.Services import RapidService as rapid_service
from UnderAutomation.ABB.Rws.Data import RapidRegainMode as rapid_regain_mode
from UnderAutomation.ABB.Rws.Data import RapidExecutionMode as rapid_execution_mode
from UnderAutomation.ABB.Rws.Data import RapidExecutionCycle as rapid_execution_cycle
from UnderAutomation.ABB.Rws.Data import RapidStartCondition as rapid_start_condition
from UnderAutomation.ABB.Rws.Data import RapidStopMode as rapid_stop_mode
from UnderAutomation.ABB.Rws.Data import RapidTaskScope as rapid_task_scope
from UnderAutomation.ABB.Rws.Data import RapidHoldToRunState as rapid_hold_to_run_state
from UnderAutomation.ABB.Rws.Data import RapidTextReplaceMode as rapid_text_replace_mode
from UnderAutomation.ABB.Rws.Data import RapidTextQueryMode as rapid_text_query_mode
from UnderAutomation.ABB.Rws.Data import RapidModuleAttribute as rapid_module_attribute
from UnderAutomation.ABB.Rws.Data import RapidProgramLoadMode as rapid_program_load_mode
from UnderAutomation.ABB.Rws.Data import RapidObjectListType as rapid_object_list_type
from UnderAutomation.ABB.Rws.Data import RapidSpyStatus as rapid_spy_status
from UnderAutomation.ABB.Rws.Data import RapidPointerSyncState as rapid_pointer_sync_state

class RapidService:
	'''RAPID Service - Everything about the program the robot runs: the tasks it is split into, the modules and the source they hold, the symbols the program declares and the values they carry, where the program pointer stands, and starting, stopping and stepping the execution. None of these resources is available while the controller runs in bootserver mode.Most of the writes need the RAPID mastership, which RwsClient.Mastership takes.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rapid_service()
		else:
			self._instance = _internal

	def get_execution_state(self) -> RapidExecutionInfo:
		'''Gets whether the controller is executing RAPID code, and how many cycles it is set to run (synchronous)

		:returns: Execution state of the controller
		'''
		return RapidExecutionInfo(self._instance.GetExecutionState())

	def start(self, regain: RapidRegainMode=RapidRegainMode.Continue_, executionMode: RapidExecutionMode=RapidExecutionMode.Continue_, cycle: RapidExecutionCycle=RapidExecutionCycle.Forever, condition: RapidStartCondition=RapidStartCondition.None_, stopAtBreakpoint: bool=False, allTasksBySelection: bool=False) -> None:
		'''Starts executing the RAPID program from where the program pointer stands (synchronous) The controller has to be in automatic mode with the motors on, or in manual mode with the enabling device held. Reset the program pointer first with to start from the beginning.

		:param regain: What the robot does about the distance between where it stands and where the path it resumes expects it to be
		:param executionMode: How far the program advances before stopping again
		:param cycle: How many times the program runs before stopping
		:param condition: Condition the controller checks before it starts
		:param stopAtBreakpoint: Whether execution stops when it reaches a breakpoint
		:param allTasksBySelection: Whether every task the selection panel has enabled is started, rather than the normal tasks only
		'''
		self._instance.Start(rapid_regain_mode(int(regain)), rapid_execution_mode(int(executionMode)), rapid_execution_cycle(int(cycle)), rapid_start_condition(int(condition)), stopAtBreakpoint, allTasksBySelection)

	def start_from_production_entry(self) -> None:
		'''Starts executing from the production entry point of the program rather than from where the program pointer stands (synchronous)'''
		self._instance.StartFromProductionEntry()

	def stop(self, stopMode: RapidStopMode=RapidStopMode.Stop, scope: RapidTaskScope=RapidTaskScope.Normal) -> None:
		'''Stops the RAPID execution (synchronous)

		:param stopMode: How abruptly the execution is stopped
		:param scope: Whether the command applies to the normal tasks only or to every task
		'''
		self._instance.Stop(rapid_stop_mode(int(stopMode)), rapid_task_scope(int(scope)))

	def reset_program_pointer(self) -> None:
		'''Moves the program pointer of every task back to the entry point of its program (synchronous)'''
		self._instance.ResetProgramPointer()

	def set_execution_cycle(self, cycle: RapidExecutionCycle) -> None:
		'''Sets how many times the program runs before stopping (synchronous)

		:param cycle: Number of cycles to run; only Once and Forever are accepted
		'''
		self._instance.SetExecutionCycle(rapid_execution_cycle(int(cycle)))

	def set_hold_to_run(self, state: RapidHoldToRunState) -> None:
		'''Drives the hold-to-run control that lets the program run in manual mode (synchronous) Send to allow execution to start, then about every two seconds to keep it running; the controller stops the program as soon as it stops hearing from the client. Send to stop it at once.

		:param state: State to put the control in
		'''
		self._instance.SetHoldToRun(rapid_hold_to_run_state(int(state)))

	def get_task_selection(self) -> typing.List[RapidTaskSelectionItem]:
		'''Gets the task selection panel: which tasks are selected, and which of them an operator is allowed to change the selection of (synchronous)

		:returns: One entry per task the panel shows
		'''
		return [RapidTaskSelectionItem(x) for x in self._instance.GetTaskSelection()]

	def get_alias_io(self, start: int | None=None, limit: int | None=None) -> typing.List[RapidAliasIoItem]:
		return [RapidAliasIoItem(x) for x in self._instance.GetAliasIo(start, limit)]

	def get_modules(self, task: str) -> typing.List[RapidModuleItem]:
		'''Gets the modules loaded into a task (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:returns: One entry per module
		'''
		return [RapidModuleItem(x) for x in self._instance.GetModules(task)]

	def get_module(self, task: str, module: str) -> RapidModuleInfo:
		'''Gets the file a module came from and the properties declared on it (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:param module: Name of the module, for example "MainModule"
		:returns: State of the module
		'''
		return RapidModuleInfo(self._instance.GetModule(task, module))

	def get_module_change_count(self, task: str, module: str) -> int:
		'''Gets the counter the controller increments whenever a module changes (synchronous) Comparing it with what a previous reading gave is cheaper than fetching the source again to find out that nothing changed.

		:param task: Name of the task, for example "T_ROB1"
		:param module: Name of the module, for example "MainModule"
		:returns: Change counter of the module
		'''
		return self._instance.GetModuleChangeCount(task, module)

	def get_module_extension(self, task: str, module: str) -> RapidModuleExtension:
		'''Gets how many lines and columns the source of a module holds (synchronous) This is what it takes to ask for the whole of it with .

		:param task: Name of the task, for example "T_ROB1"
		:param module: Name of the module, for example "MainModule"
		:returns: Size of the module
		'''
		return RapidModuleExtension(self._instance.GetModuleExtension(task, module))

	def get_module_text(self, task: str, module: str) -> RapidModuleText:
		'''Gets the source of a module (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:param module: Name of the module, for example "MainModule"
		:returns: Source of the module and the counters that go with it
		'''
		return RapidModuleText(self._instance.GetModuleText(task, module))

	def set_module_text(self, task: str, module: str, text: str) -> None:
		'''Replaces the whole source of a module (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:param module: Name of the module, for example "MainModule"
		:param text: New source of the module
		'''
		self._instance.SetModuleText(task, module, text)

	def get_module_text_range(self, task: str, module: str, startRow: int, startColumn: int, endRow: int, endColumn: int) -> str:
		'''Gets a range of the source of a module (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:param module: Name of the module, for example "MainModule"
		:param startRow: Line the range starts at, counted from 1
		:param startColumn: Column the range starts at, counted from 1
		:param endRow: Line the range ends at
		:param endColumn: Column the range ends at
		:returns: The requested source
		'''
		return self._instance.GetModuleTextRange(task, module, startRow, startColumn, endRow, endColumn)

	def set_module_text_range(self, task: str, module: str, replaceMode: RapidTextReplaceMode, queryMode: RapidTextQueryMode, startRow: int, startColumn: int, endRow: int, endColumn: int, text: str) -> RapidSetTextRangeResult:
		'''Writes text into a range of the source of a module (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:param module: Name of the module, for example "MainModule"
		:param replaceMode: Whether the text replaces the range or is inserted around it
		:param queryMode: How hard the controller tries when the change would invalidate the program pointer
		:param startRow: Line the range starts at, counted from 1
		:param startColumn: Column the range starts at, counted from 1
		:param endRow: Line the range ends at
		:param endColumn: Column the range ends at
		:param text: Text to write
		:returns: What the controller did with the change, including the name the module ended up with
		'''
		return RapidSetTextRangeResult(self._instance.SetModuleTextRange(task, module, rapid_text_replace_mode(int(replaceMode)), rapid_text_query_mode(int(queryMode)), startRow, startColumn, endRow, endColumn, text))

	def search_module_text(self, task: str, module: str, text: str, startRow: int=1, startColumn: int=1) -> RapidTextPosition:
		'''Finds where a piece of text sits in the source of a module (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:param module: Name of the module, for example "MainModule"
		:param text: Text to look for
		:param startRow: Line to start looking from, counted from 1
		:param startColumn: Column to start looking from, counted from 1
		:returns: Where the text was found; its Found property is false when it was not
		'''
		return RapidTextPosition(self._instance.SearchModuleText(task, module, text, startRow, startColumn))

	def get_sync_pers_status(self, task: str, module: str) -> bool:
		'''Gets whether the persistent variables of a module are kept synchronized with the other tasks declaring them (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:param module: Name of the module, for example "MainModule"
		:returns: True when the persistent variables are synchronized
		'''
		return self._instance.GetSyncPersStatus(task, module)

	def sync_persistent_variables(self, task: str, module: str) -> None:
		'''Synchronizes the persistent variables of a module with the other tasks declaring them (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:param module: Name of the module, for example "MainModule"
		'''
		self._instance.SyncPersistentVariables(task, module)

	def save_module(self, task: str, module: str, name: str, path: str) -> None:
		'''Saves a module to the file system of the controller (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:param module: Name of the module to save
		:param name: Name to save it under; the controller appends the module extension itself
		:param path: Directory to save it into, which may use the environment variables of the controller such as its home or temporary directory
		'''
		self._instance.SaveModule(task, module, name, path)

	def get_possible_module_attributes(self, task: str, module: str, attributes: typing.List[RapidModuleAttribute]) -> typing.List[RapidModuleAttribute]:
		'''Gets which of the requested properties may be declared on a module (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:param module: Name of the module, for example "MainModule"
		:param attributes: Properties to ask about
		:returns: The properties of the request the module accepts
		'''
		return [RapidModuleAttribute(int(x)) for x in self._instance.GetPossibleModuleAttributes(task, module, rapid_module_attribute(int(attributes)))]

	def get_module_symbol(self, task: str, module: str, row: int, column: int) -> RapidModuleSymbol:
		'''Gets the declaration the controller finds at a position of a module (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:param module: Name of the module, for example "MainModule"
		:param row: Line to look at, counted from 1
		:param column: Column to look at, counted from 1
		:returns: The declaration, null when there is none at that position
		'''
		return RapidModuleSymbol(self._instance.GetModuleSymbol(task, module, row, column))

	def get_routine(self, task: str, module: str, row: int, column: int) -> RapidRoutineInfo:
		'''Gets the routine the controller finds called at a position of a module (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:param module: Name of the module, for example "MainModule"
		:param row: Line to look at, counted from 1
		:param column: Column to look at, counted from 1
		:returns: The routine called at that position
		'''
		return RapidRoutineInfo(self._instance.GetRoutine(task, module, row, column))

	def get_routine_arguments(self, task: str, module: str, row: int, column: int, mark: int | None=None, limit: int | None=None) -> typing.List[RapidRoutineArgument]:
		return [RapidRoutineArgument(x) for x in self._instance.GetRoutineArguments(task, module, row, column, mark, limit)]

	def get_instruction_template(self, task: str, module: str, name: str, isDataType: bool=False, row: int | None=None, column: int | None=None, parameterNumber: int | None=None, alternativeNumber: int | None=None) -> RapidInstructionTemplate:
		return RapidInstructionTemplate(self._instance.GetInstructionTemplate(task, module, name, isDataType, row, column, parameterNumber, alternativeNumber))

	def get_object_children(self, task: str, module: str, startLine: int, startColumn: int, endLine: int, endColumn: int) -> RapidObjectChild:
		'''Gets the parts a RAPID object is made of and where each of them sits in the source (synchronous) Pass the whole span of the object to get its parts; an editor uses this to know where the name, the attributes and the declaration lists of a module begin and end.

		:param task: Name of the task, for example "T_ROB1"
		:param module: Name of the module, for example "MainModule"
		:param startLine: Line the object starts at, counted from 1
		:param startColumn: Column the object starts at, counted from 1
		:param endLine: Line the object ends at
		:param endColumn: Column the object ends at
		:returns: The parts of the object
		'''
		return RapidObjectChild(self._instance.GetObjectChildren(task, module, startLine, startColumn, endLine, endColumn))

	def get_modifiable_positions(self, task: str, module: str, startRow: int, startColumn: int, endRow: int, endColumn: int) -> RapidModifiablePositions:
		'''Gets how many motion instructions of a range can have their position rewritten to where the robot currently stands (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:param module: Name of the module, for example "MainModule"
		:param startRow: Line the range starts at, counted from 1
		:param startColumn: Column the range starts at, counted from 1
		:param endRow: Line the range ends at
		:param endColumn: Column the range ends at
		:returns: How many instructions can be rewritten, and which range they cover
		'''
		return RapidModifiablePositions(self._instance.GetModifiablePositions(task, module, startRow, startColumn, endRow, endColumn))

	def get_all_modifiable_positions(self) -> typing.List[RapidModifiablePositionItem]:
		'''Gets every motion instruction of the system whose position can be rewritten to where the robot currently stands, wherever in whichever task it sits (synchronous)

		:returns: One entry per instruction, empty when the controller found none
		'''
		return [RapidModifiablePositionItem(x) for x in self._instance.GetAllModifiablePositions()]

	def modify_position(self, task: str, module: str, startRow: int, startColumn: int, endRow: int, endColumn: int, checkLimits: bool=True, checkDeactivatedAxes: bool=True, allowDeactivated: bool=False) -> None:
		'''Rewrites the positions of the motion instructions of a range to where the robot currently stands (synchronous) This is the teaching gesture: jog the robot where it should go, then write that position back into the program.

		:param task: Name of the task, for example "T_ROB1"
		:param module: Name of the module, for example "MainModule"
		:param startRow: Line the range starts at, counted from 1
		:param startColumn: Column the range starts at, counted from 1
		:param endRow: Line the range ends at
		:param endColumn: Column the range ends at
		:param checkLimits: Whether the controller refuses a position outside the working range
		:param checkDeactivatedAxes: Whether the controller refuses to rewrite an axis that is deactivated
		:param allowDeactivated: Whether a deactivated axis is rewritten anyway
		'''
		self._instance.ModifyPosition(task, module, startRow, startColumn, endRow, endColumn, checkLimits, checkDeactivatedAxes, allowDeactivated)

	def modify_all_positions(self, checkLimits: bool=True, checkDeactivatedAxes: bool=True) -> None:
		'''Rewrites the positions of every motion instruction of the system that can be rewritten, to where the robot currently stands (synchronous)

		:param checkLimits: Whether the controller refuses a position outside the working range
		:param checkDeactivatedAxes: Whether the controller refuses to rewrite an axis that is deactivated
		'''
		self._instance.ModifyAllPositions(checkLimits, checkDeactivatedAxes)

	def get_rob_target(self, task: str, tool: str=None, workObject: str=None) -> RobTarget:
		'''Gets where the tool of a task currently stands, as a position and an orientation (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:param tool: Name of the tool to express the position in, null to use the one the task is currently using
		:param workObject: Name of the work object to express the position in, null to use the one the task is currently using
		:returns: Position, orientation, configuration and external axes of the tool
		'''
		return RobTarget(None, None, None, None, None, None, self._instance.GetRobTarget(task, tool, workObject))

	def get_joint_target(self, task: str) -> JointTarget:
		'''Gets the joint values of the robot of a task (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:returns: Values of the six robot axes and of the external axes
		'''
		return JointTarget(None, None, self._instance.GetJointTarget(task))

	def get_external_joint_states(self, task: str) -> RapidExternalJointStates:
		'''Gets what each of the six external joints of a task is doing (synchronous) This is what says how to read the corresponding value of : a joint reported as not active carries no meaningful position.

		:param task: Name of the task, for example "T_ROB1"
		:returns: State of each external joint
		'''
		return RapidExternalJointStates(self._instance.GetExternalJointStates(task))

	def get_mechanical_units(self, task: str) -> typing.List[RapidMechanicalUnitItem]:
		'''Gets the mechanical units the positions of a task are expressed in (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:returns: One entry per unit the task can move
		'''
		return [RapidMechanicalUnitItem(x) for x in self._instance.GetMechanicalUnits(task)]

	def get_program(self, task: str) -> RapidProgramInfo:
		'''Gets the program loaded into a task (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:returns: The loaded program, null when the task holds none
		'''
		return RapidProgramInfo(self._instance.GetProgram(task))

	def load_program(self, task: str, programPath: str, loadMode: RapidProgramLoadMode=RapidProgramLoadMode.Add) -> None:
		'''Loads a program into a task (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:param programPath: Path of the program on the controller, for example "$HOME/myprogram.pgf"
		:param loadMode: What happens to the modules the task already holds
		'''
		self._instance.LoadProgram(task, programPath, rapid_program_load_mode(int(loadMode)))

	def unload_program(self, task: str) -> None:
		'''Unloads the program of a task (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		'''
		self._instance.UnloadProgram(task)

	def save_program(self, task: str, path: str) -> None:
		'''Saves the program of a task to the file system of the controller (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:param path: Directory to save the program into, for example "$HOME/myprograms"
		'''
		self._instance.SaveProgram(task, path)

	def set_program_name(self, task: str, name: str) -> None:
		'''Renames the program of a task (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:param name: New name of the program
		'''
		self._instance.SetProgramName(task, name)

	def set_entry_point(self, task: str, routine: str) -> None:
		'''Sets the routine the program pointer moves to when it is reset (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:param routine: Name of the routine, for example "main"
		'''
		self._instance.SetEntryPoint(task, routine)

	def get_breakpoints(self, task: str, start: int | None=None, limit: int | None=None) -> typing.List[RapidBreakpoint]:
		return [RapidBreakpoint(x) for x in self._instance.GetBreakpoints(task, start, limit)]

	def set_breakpoint(self, task: str, module: str, row: int, column: int) -> RapidBreakpoint:
		'''Sets a breakpoint at a position of a module (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:param module: Name of the module to break in
		:param row: Line to break at, counted from 1
		:param column: Column to break at, counted from 1
		:returns: The breakpoint as the controller placed it
		'''
		return RapidBreakpoint(self._instance.SetBreakpoint(task, module, row, column))

	def get_build_errors(self, task: str, start: int | None=None, limit: int | None=None) -> typing.List[RapidBuildError]:
		return [RapidBuildError(x) for x in self._instance.GetBuildErrors(task, start, limit)]

	def get_program_counter_position(self, task: str) -> RapidProgramCounterPosition:
		'''Gets which piece of source the program pointer of a task points at (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:returns: Position of the program pointer
		'''
		return RapidProgramCounterPosition(self._instance.GetProgramCounterPosition(task))

	def get_pointers(self, task: str) -> RapidPointers:
		'''Gets where the program pointer and the motion pointer of a task stand (synchronous) The program pointer says which instruction runs next, the motion pointer which one the robot is actually executing; they drift apart because the controller plans the path ahead of the movement.

		:param task: Name of the task, for example "T_ROB1"
		:returns: The two pointers of the task
		'''
		return RapidPointers(self._instance.GetPointers(task))

	def set_program_pointer_to_cursor(self, task: str, module: str, routine: str, row: int, column: int) -> None:
		'''Moves the program pointer of a task to a position of a module (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:param module: Name of the module to move the pointer into
		:param routine: Name of the routine the position sits in
		:param row: Line to move the pointer to, counted from 1
		:param column: Column to move the pointer to, counted from 1
		'''
		self._instance.SetProgramPointerToCursor(task, module, routine, row, column)

	def set_program_pointer_to_routine(self, task: str, module: str, routine: str, userLevel: bool=False) -> None:
		'''Moves the program pointer of a task to the beginning of a routine (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:param module: Name of the module holding the routine
		:param routine: Name of the routine
		:param userLevel: Whether the pointer is moved at user level, which is what a service routine has to be started with
		'''
		self._instance.SetProgramPointerToRoutine(task, module, routine, userLevel)

	def set_program_pointer_to_routine_url(self, task: str, routineUrl: str, userLevel: bool=False) -> None:
		'''Moves the program pointer of a task to a routine named by its path (synchronous) This is what the paths GetServiceRoutines() reports are for.

		:param task: Name of the task, for example "T_ROB1"
		:param routineUrl: Path of the routine, for example "RAPID/T_ROB1/BASEFUN/LoadIdentify"
		:param userLevel: Whether the pointer is moved at user level, which is what a service routine has to be started with
		'''
		self._instance.SetProgramPointerToRoutineUrl(task, routineUrl, userLevel)

	def set_program_pointer_to_next_instruction(self, task: str) -> None:
		'''Moves the program pointer of a task forward by one instruction (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		'''
		self._instance.SetProgramPointerToNextInstruction(task)

	def set_program_pointer_to_previous_instruction(self, task: str) -> None:
		'''Moves the program pointer of a task back by one instruction (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		'''
		self._instance.SetProgramPointerToPreviousInstruction(task)

	def get_symbol_properties(self, symbolUrl: str) -> RapidSymbolProperties:
		'''Gets what a RAPID symbol is declared as (synchronous)

		:param symbolUrl: Path of the symbol, for example "RAPID/T_ROB1/user/reg1"
		:returns: Declaration of the symbol
		'''
		return RapidSymbolProperties(self._instance.GetSymbolProperties(symbolUrl))

	def get_symbol_value(self, symbolUrl: str) -> RapidSymbolValue:
		'''Gets the value of a RAPID symbol and where it is declared (synchronous)

		:param symbolUrl: Path of the symbol, for example "RAPID/T_ROB1/user/reg1"
		:returns: Value of the symbol, written the way RAPID writes it
		'''
		return RapidSymbolValue(self._instance.GetSymbolValue(symbolUrl))

	def set_symbol_value(self, symbolUrl: str, value: str) -> None:
		'''Sets the value a RAPID symbol currently holds (synchronous)

		:param symbolUrl: Path of the symbol, for example "RAPID/T_ROB1/user/reg1"
		:param value: New value, written the way RAPID writes it; a record needs the bracketed form, for example "[[515,0,712],[1,0,0,0],[0,0,0,0],[9E9,9E9,9E9,9E9,9E9,9E9]]"
		'''
		self._instance.SetSymbolValue(symbolUrl, value)

	def set_symbol_initial_value(self, symbolUrl: str, value: str) -> None:
		'''Sets the value a RAPID symbol is declared with, which is the one it goes back to when the program is reset (synchronous)

		:param symbolUrl: Path of the symbol, for example "RAPID/T_ROB1/user/reg1"
		:param value: New initial value, written the way RAPID writes it
		'''
		self._instance.SetSymbolInitialValue(symbolUrl, value)

	def search_symbols(self, criteria: RapidSymbolSearchCriteria) -> typing.List[RapidSymbolProperties]:
		'''Finds the RAPID symbols matching a set of criteria (synchronous)

		:param criteria: What to look for; set at least its search path, because a search with no criterion walks the whole system
		:returns: One entry per symbol found, empty when none matched
		'''
		return [RapidSymbolProperties(x) for x in self._instance.SearchSymbols(criteria._instance if criteria else None)]

	def validate_symbol_value(self, task: str, dataType: str, value: str) -> bool:
		'''Asks the controller whether a value would be accepted for a given RAPID type, without writing it anywhere (synchronous) This is what an editor uses to tell an operator that what they typed is wrong before the write is attempted.

		:param task: Name of the task the type is looked up in, for example "T_ROB1"
		:param dataType: Name of the type, for example "robtarget"
		:param value: Value to check, written the way RAPID writes it
		:returns: True when the controller accepts the value, false when it rejects it
		'''
		return self._instance.ValidateSymbolValue(task, dataType, value)

	def get_object_list_extension(self, symbolUrl: str, type: RapidObjectListType=RapidObjectListType.Statements) -> RapidObjectListExtension:
		'''Gets where one of the lists a RAPID object holds sits in the source: the span of the whole list, and the spans of its first and last elements (synchronous) An editor uses this to jump to the beginning or the end of a list without reading the whole module.

		:param symbolUrl: Path of the object, for example "RAPID/T_ROB1/MainModule"
		:param type: Which of its lists is being asked about
		:returns: Where the list and its ends sit
		'''
		return RapidObjectListExtension(self._instance.GetObjectListExtension(symbolUrl, rapid_object_list_type(int(type))))

	def get_tasks(self) -> typing.List[RapidTaskItem]:
		'''Gets every RAPID task of the controller and what each of them is doing (synchronous)

		:returns: One entry per task
		'''
		return [RapidTaskItem(x) for x in self._instance.GetTasks()]

	def get_task(self, task: str) -> RapidTaskInfo:
		'''Gets everything the controller reports about one task (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:returns: State of the task
		'''
		return RapidTaskInfo(self._instance.GetTask(task))

	def activate_tasks(self) -> None:
		'''Activates every task of the controller (synchronous)'''
		self._instance.ActivateTasks()

	def deactivate_tasks(self) -> None:
		'''Deactivates every task of the controller (synchronous)'''
		self._instance.DeactivateTasks()

	def activate_task(self, task: str) -> None:
		'''Activates one task (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		'''
		self._instance.ActivateTask(task)

	def deactivate_task(self, task: str) -> None:
		'''Deactivates one task (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		'''
		self._instance.DeactivateTask(task)

	def build_task(self, task: str) -> None:
		'''Links the program of a task, which is what turns the modules it holds into something runnable (synchronous) Read GetBuildErrors() afterwards to find out what the controller refused.

		:param task: Name of the task, for example "T_ROB1"
		'''
		self._instance.BuildTask(task)

	def abort_execution_level(self, task: str) -> None:
		'''Abandons the routine the task is currently running and returns to the level below it (synchronous) This is how a trap or a service routine started by hand is left without stopping the program underneath it.

		:param task: Name of the task, for example "T_ROB1"
		'''
		self._instance.AbortExecutionLevel(task)

	def load_module(self, task: str, modulePath: str, replace: bool=False) -> str:
		'''Loads a module file into a task (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:param modulePath: Path of the module file on the controller, for example "$HOME/mymodule.mod"
		:param replace: Whether a module of the same name already loaded is replaced
		:returns: Name of the loaded module, null when the controller did not report it
		'''
		return self._instance.LoadModule(task, modulePath, replace)

	def unload_module(self, task: str, module: str) -> None:
		'''Unloads a module from a task (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:param module: Name of the module to unload
		'''
		self._instance.UnloadModule(task, module)

	def get_spy_status(self) -> RapidSpyStatus:
		'''Gets whether the controller is recording the RAPID execution trace to a file (synchronous)

		:returns: Whether the trace is being written
		'''
		return RapidSpyStatus(int(self._instance.GetSpyStatus()))

	def start_spy(self, logFile: str) -> None:
		'''Starts recording the RAPID execution trace into a file (synchronous) The trace names every instruction the controller runs, which is what it takes to find out why a program took a branch it should not have.

		:param logFile: Path of the file to write, which lands in the home directory when it carries no directory of its own
		'''
		self._instance.StartSpy(logFile)

	def stop_spy(self) -> None:
		'''Stops recording the RAPID execution trace (synchronous)'''
		self._instance.StopSpy()

	def get_program_pointer_sync_state(self) -> RapidPointerSyncState:
		'''Gets whether the program pointers of every task are synchronized with each other (synchronous)

		:returns: Whether the program pointers are synchronized
		'''
		return RapidPointerSyncState(int(self._instance.GetProgramPointerSyncState()))

	def get_motion_pointer_sync_state(self) -> RapidPointerSyncState:
		'''Gets whether the motion pointers of every task are synchronized with each other (synchronous)

		:returns: Whether the motion pointers are synchronized
		'''
		return RapidPointerSyncState(int(self._instance.GetMotionPointerSyncState()))

	def get_task_program_pointer_sync_state(self, task: str) -> RapidPointerSyncState:
		'''Gets whether the program pointer of one task is synchronized with the others (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:returns: Whether the program pointer of the task is synchronized
		'''
		return RapidPointerSyncState(int(self._instance.GetTaskProgramPointerSyncState(task)))

	def get_task_motion_pointer_sync_state(self, task: str) -> RapidPointerSyncState:
		'''Gets whether the motion pointer of one task is synchronized with the others (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:returns: Whether the motion pointer of the task is synchronized
		'''
		return RapidPointerSyncState(int(self._instance.GetTaskMotionPointerSyncState(task)))

	def get_structural_change_count(self, task: str) -> RapidStructuralChangeCount:
		'''Gets the two counters a task keeps of what has changed in it (synchronous) Comparing them with what a previous reading gave is cheaper than fetching the modules again to find out that nothing moved.

		:param task: Name of the task, for example "T_ROB1"
		:returns: Change counters of the task
		'''
		return RapidStructuralChangeCount(self._instance.GetStructuralChangeCount(task))

	def get_activation_record(self, task: str, stackFrame: int=1) -> RapidActivationRecord:
		'''Gets one frame of the call stack of a task: which routine is running and where execution stands in it (synchronous)

		:param task: Name of the task, for example "T_ROB1"
		:param stackFrame: Frame to read, 1 being the one holding the program pointer and the number growing towards the entry point of the program
		:returns: The requested stack frame
		'''
		return RapidActivationRecord(self._instance.GetActivationRecord(task, stackFrame))

	def get_service_routines(self, task: str, start: int | None=None, limit: int | None=None) -> typing.List[RapidServiceRoutineItem]:
		return [RapidServiceRoutineItem(x) for x in self._instance.GetServiceRoutines(task, start, limit)]

	def get_preferred_data_types(self, task: str, instruction: str, parameter: str) -> typing.List[RapidPreferredDataTypeItem]:
		'''Gets the data types the controller suggests for one argument of an instruction (synchronous) An editor uses this to offer only the types that fit where the operator is typing.

		:param task: Name of the task, for example "T_ROB1"
		:param instruction: Name of the instruction, for example "AliasIO"
		:param parameter: Name of the argument of that instruction, for example "FromSignal"
		:returns: One entry per suggested type
		'''
		return [RapidPreferredDataTypeItem(x) for x in self._instance.GetPreferredDataTypes(task, instruction, parameter)]

	def get_pallet_heads(self, task: str, start: int | None=None, limit: int | None=None) -> typing.List[RapidPalletHeadItem]:
		return [RapidPalletHeadItem(x) for x in self._instance.GetPalletHeads(task, start, limit)]

	def get_pallet(self, task: str, palletNumber: int, start: int | None=None, limit: int | None=None) -> typing.List[RapidPalletItem]:
		return [RapidPalletItem(x) for x in self._instance.GetPallet(task, palletNumber, start, limit)]

	def get_active_ui_instruction(self) -> RapidUiInstruction:
		'''Gets the dialogue a running RAPID program is currently asking an operator for (synchronous) Answering it means writing its parameters with , addressed by the path this returns.

		:returns: The pending instruction, null when the program is not asking for anything
		'''
		return RapidUiInstruction(self._instance.GetActiveUiInstruction())

	def get_ui_instruction_parameters(self, stackUrl: str) -> typing.List[RapidUiInstructionParameter]:
		'''Gets every parameter of a pending UI instruction: what the program passed in, and what it is waiting for (synchronous)

		:param stackUrl: Path identifying the call, as GetActiveUiInstruction reports it
		:returns: One entry per parameter
		'''
		return [RapidUiInstructionParameter(x) for x in self._instance.GetUiInstructionParameters(stackUrl)]

	def get_ui_instruction_parameter(self, stackUrl: str, parameter: str) -> str:
		'''Gets the value of one parameter of a pending UI instruction (synchronous)

		:param stackUrl: Path identifying the call, as GetActiveUiInstruction reports it
		:param parameter: Name of the parameter, for example "TPCompleted"
		:returns: Value of the parameter, written the way RAPID writes it
		'''
		return self._instance.GetUiInstructionParameter(stackUrl, parameter)

	def set_ui_instruction_parameter(self, stackUrl: str, parameter: str, value: str) -> None:
		'''Answers a pending UI instruction by writing one of its parameters (synchronous) An instruction is normally answered by writing the parameter carrying the answer and then the one marking it as completed.

		:param stackUrl: Path identifying the call, as GetActiveUiInstruction reports it
		:param parameter: Name of the parameter to write, for example "TPCompleted"
		:param value: Value to write, written the way RAPID writes it
		'''
		self._instance.SetUiInstructionParameter(stackUrl, parameter, value)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidService):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
