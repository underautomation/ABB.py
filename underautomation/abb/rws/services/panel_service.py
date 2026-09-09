from __future__ import annotations
import typing
from underautomation.abb.rws.data.controller_state import ControllerState
from underautomation.abb.rws.data.operation_mode import OperationMode
from underautomation.abb.rws.data.operation_mode_acknowledgement import OperationModeAcknowledgement
from underautomation.abb.rws.data.operation_mode_lock_state import OperationModeLockState
from underautomation.abb.rws.data.collision_detection_state import CollisionDetectionState
from underautomation.abb.rws.data.controller_restart_mode import ControllerRestartMode
from UnderAutomation.ABB.Rws.Services import PanelService as panel_service
from UnderAutomation.ABB.Rws.Data import ControllerState as controller_state
from UnderAutomation.ABB.Rws.Data import OperationMode as operation_mode
from UnderAutomation.ABB.Rws.Data import OperationModeAcknowledgement as operation_mode_acknowledgement
from UnderAutomation.ABB.Rws.Data import OperationModeLockState as operation_mode_lock_state
from UnderAutomation.ABB.Rws.Data import CollisionDetectionState as collision_detection_state
from UnderAutomation.ABB.Rws.Data import ControllerRestartMode as controller_restart_mode

class PanelService:
	'''Panel Service - Exposes what an operator reads and acts on from the control panel of the controller: the controller state, the operating mode and its selector lock, the speed ratio, the collision detection state, the language of the controller and its restart. None of these resources is available while the controller runs in bootserver mode.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = panel_service()
		else:
			self._instance = _internal

	def get_controller_state(self) -> ControllerState:
		'''Gets the state of the controller (synchronous)

		:returns: State of the controller, Unknown when it reports a state this library does not know
		'''
		return ControllerState(int(self._instance.GetControllerState()))

	def set_controller_state(self, state: ControllerState) -> None:
		'''Turns the motors of the robot on or off (synchronous)

		:param state: State to switch to, which can only be MotorsOn or MotorsOff. Every other state is reached by the controller on its own and cannot be requested.
		'''
		self._instance.SetControllerState(controller_state(int(state)))

	def get_operation_mode(self) -> OperationMode:
		'''Gets the operating mode the controller runs in (synchronous)

		:returns: Operating mode, Unknown when the controller reports a mode this library does not know
		'''
		return OperationMode(int(self._instance.GetOperationMode()))

	def acknowledge_operation_mode(self, acknowledgement: OperationModeAcknowledgement) -> None:
		'''Confirms a pending operating mode change (synchronous) The controller waits for this confirmation whenever the mode selector is turned, unless it is configured to acknowledge the change on its own.

		:param acknowledgement: Change to confirm
		'''
		self._instance.AcknowledgeOperationMode(operation_mode_acknowledgement(int(acknowledgement)))

	def get_operation_mode_lock_state(self) -> OperationModeLockState:
		'''Gets the lock state of the operating mode selector (synchronous)

		:returns: Lock state, Unknown when the controller reports a state this library does not know
		'''
		return OperationModeLockState(int(self._instance.GetOperationModeLockState()))

	def lock_operation_mode(self, pin: str, permanent: bool=False) -> None:
		'''Locks the operating mode selector with a pin code (synchronous)

		:param pin: Four digit pin code, which will be needed again to unlock the selector
		:param permanent: When true, the selector is locked permanently, which requires the key-less mode selector grant. When false (default), the lock can be released with String).
		'''
		self._instance.LockOperationMode(pin, permanent)

	def unlock_operation_mode(self, pin: str) -> None:
		'''Releases the lock of the operating mode selector (synchronous)

		:param pin: Four digit pin code the selector was locked with
		'''
		self._instance.UnlockOperationMode(pin)

	def get_speed_ratio(self) -> int:
		'''Gets the speed ratio the controller runs the programs at (synchronous)

		:returns: Speed ratio, as a percentage between 0 and 100
		'''
		return self._instance.GetSpeedRatio()

	def set_speed_ratio(self, speedRatio: int, useImplicitMastership: bool=True) -> None:
		'''Sets the speed ratio the controller runs the programs at (synchronous) Only accepted while the controller runs in automatic mode.

		:param speedRatio: Speed ratio, as a percentage between 0 and 100
		:param useImplicitMastership: A connection established with version 2 requires mastership to change the speed ratio. When true (default), mastership is taken implicitly for this request. Ignored on a version 1 connection, which needs none.
		'''
		self._instance.SetSpeedRatio(speedRatio, useImplicitMastership)

	def get_collision_detection_state(self) -> CollisionDetectionState:
		'''Gets the collision detection state of the controller (synchronous)

		:returns: Collision detection state, Unknown when the controller reports a state this library does not know
		'''
		return CollisionDetectionState(int(self._instance.GetCollisionDetectionState()))

	def set_language(self, languageCode: str) -> None:
		'''Sets the language the controller reports its messages in (synchronous)

		:param languageCode: Two letter language code, for example "en", "sv" or "de"
		'''
		self._instance.SetLanguage(languageCode)

	def restart(self, mode: ControllerRestartMode, useImplicitMastership: bool=True) -> None:
		'''Restarts the controller (synchronous)

		:param mode: How the controller restarts. The control panel accepts Restart, IStart, PStart and BStart; use Boolean) for the others.
		:param useImplicitMastership: A connection established with version 2 requires mastership on all domains to restart the controller. When true (default), mastership is taken implicitly for this request. Ignored on a version 1 connection, which needs none.
		'''
		self._instance.Restart(controller_restart_mode(int(mode)), useImplicitMastership)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, PanelService):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
