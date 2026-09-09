from __future__ import annotations
import typing
from underautomation.abb.rws.data.controller_info import ControllerInfo
from datetime import datetime, timedelta
from underautomation.abb.rws.data.time_server_info import TimeServerInfo
from underautomation.abb.rws.data.controller_identity import ControllerIdentity
from underautomation.abb.rws.data.network_interface_item import NetworkInterfaceItem
from underautomation.abb.rws.data.network_configuration_method import NetworkConfigurationMethod
from underautomation.abb.rws.data.controller_restart_mode import ControllerRestartMode
from underautomation.abb.rws.data.backup_system_info import BackupSystemInfo
from underautomation.abb.rws.data.backup_state import BackupState
from underautomation.abb.rws.data.backup_restore_ignore import BackupRestoreIgnore
from underautomation.abb.rws.data.backup_restore_include import BackupRestoreInclude
from underautomation.abb.rws.data.check_restore_result import CheckRestoreResult
from underautomation.abb.rws.data.safety_mode_status import SafetyModeStatus
from underautomation.abb.rws.data.safety_mode import SafetyMode
from underautomation.abb.rws.data.safety_configuration import SafetyConfiguration
from underautomation.abb.rws.data.safety_load_operation_status import SafetyLoadOperationStatus
from underautomation.abb.rws.data.cyclic_brake_check_status import CyclicBrakeCheckStatus
from underautomation.abb.rws.data.safety_violation_info import SafetyViolationInfo
from underautomation.abb.rws.data.virtual_time_state import VirtualTimeState
from UnderAutomation.ABB.Rws.Services import ControllerService as controller_service
from UnderAutomation.ABB.Rws.Data import NetworkConfigurationMethod as network_configuration_method
from UnderAutomation.ABB.Rws.Data import ControllerRestartMode as controller_restart_mode
from UnderAutomation.ABB.Rws.Data import BackupState as backup_state
from UnderAutomation.ABB.Rws.Data import BackupRestoreIgnore as backup_restore_ignore
from UnderAutomation.ABB.Rws.Data import BackupRestoreInclude as backup_restore_include
from UnderAutomation.ABB.Rws.Data import SafetyMode as safety_mode
from UnderAutomation.ABB.Rws.Data import SafetyLoadOperationStatus as safety_load_operation_status
from UnderAutomation.ABB.Rws.Data import VirtualTimeState as virtual_time_state

class ControllerService:
	'''Controller Service - Provides access to the controller resources: clock, identity, network, installed systems, options, backups, safety controller and virtual time.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = controller_service()
		else:
			self._instance = _internal

	def get_info(self) -> ControllerInfo:
		'''Gets an overview of the controller resources (synchronous) Contains the current system time, the controller identity and the list of available sub resources.

		:returns: Controller information
		'''
		return ControllerInfo(self._instance.GetInfo())

	def get_environment_variable(self, name: str) -> str:
		'''Gets the value of a controller environment variable (synchronous)

		:param name: Name of the environment variable, with or without the leading dollar sign (e.g. "$TEMP" or "TEMP")
		:returns: Value of the environment variable (e.g. "/hd0a/TEMP")
		'''
		return self._instance.GetEnvironmentVariable(name)

	def get_clock(self) -> datetime:
		'''Gets the current system time of the controller (synchronous) The time returned by the controller is always UTC.

		:returns: Current controller time (UTC)
		'''
		return datetime(1, 1, 1) + timedelta(microseconds=self._instance.GetClock().Ticks // 10)

	def set_clock(self, dateTime: datetime) -> None:
		'''Sets the system time of the controller (synchronous) The controller clock is always UTC, pass a UTC date and time.Instead of setting the time explicitly, a time server can be configured with .

		:param dateTime: New controller date and time (UTC)
		'''
		self._instance.SetClock(dateTime)

	def get_time_zone(self) -> str:
		'''Gets the time zone used by the controller (synchronous)

		:returns: Time zone as defined by the tz database, for example "Europe/Stockholm"
		'''
		return self._instance.GetTimeZone()

	def set_time_zone(self, timeZone: str) -> None:
		'''Sets the time zone used by the controller (synchronous) Available only on a real controller.

		:param timeZone: Time zone as defined by the tz database, for example "Europe/Stockholm"
		'''
		self._instance.SetTimeZone(timeZone)

	def get_time_server(self, serverIp: str=None) -> TimeServerInfo:
		'''Gets the time server used by the controller to synchronize its clock (synchronous) Available only on a real controller.

		:param serverIp: Optional IP of a specific time server to query. Requires a connection established with version 2, leave null to get the default time server.
		:returns: Time server information, or null when no time server is configured
		'''
		return TimeServerInfo(self._instance.GetTimeServer(serverIp))

	def set_time_server(self, timeServer: str) -> None:
		'''Sets the time server used by the controller to synchronize its clock (synchronous) Available only on a real controller.

		:param timeServer: Address of the time server, for example "132.163.4.101"
		'''
		self._instance.SetTimeServer(timeServer)

	def get_identity(self) -> ControllerIdentity:
		'''Gets the identity of the controller: name, id, type, MAC address and level (synchronous)

		:returns: Controller identity
		'''
		return ControllerIdentity(self._instance.GetIdentity())

	def set_identity(self, name: str, id: str=None) -> None:
		'''Sets the identity of the controller (synchronous) Available only on a real controller.

		:param name: New name of the controller, null to leave it unchanged
		:param id: New controller id, null to leave it unchanged
		'''
		self._instance.SetIdentity(name, id)

	def set_language(self, language: str) -> None:
		'''Sets the language of the controller (synchronous)

		:param language: Language as per RFC 3066, for example "en" or "de". A not supported language results in a bad request.
		'''
		self._instance.SetLanguage(language)

	def get_network_interfaces(self) -> typing.List[NetworkInterfaceItem]:
		'''Gets the IP configuration of all network interfaces of the controller (synchronous) Not applicable to a virtual controller.

		:returns: Network interfaces of the controller
		'''
		return [NetworkInterfaceItem(x) for x in self._instance.GetNetworkInterfaces()]

	def set_network_configuration(self, method: NetworkConfigurationMethod, address: str=None, mask: str=None, gateway: str=None) -> None:
		'''Sets the IP configuration of the LAN adapter of the controller (synchronous) The controller must be restarted for the change to take effect. Requires the UAS grant UAS_CONTROLLER_PROPERTIES_WRITE.Not supported by a virtual controller.

		:param method: IP configuration method
		:param address: IP address, required when method is FixIp
		:param mask: Subnet mask, required when method is FixIp
		:param gateway: Default gateway, applicable when method is FixIp
		'''
		self._instance.SetNetworkConfiguration(network_configuration_method(int(method)), address, mask, gateway)

	def restart(self, mode: ControllerRestartMode, useImplicitMastership: bool=True) -> None:
		'''Restarts or shuts down the controller (synchronous)

		:param mode: Restart mode
		:param useImplicitMastership: A connection established with version 2 requires mastership on all domains to restart the controller. When true (default), mastership is taken implicitly for this request. Ignored on a version 1 connection, which needs none.
		'''
		self._instance.Restart(controller_restart_mode(int(mode)), useImplicitMastership)

	def get_installed_systems(self) -> typing.List[str]:
		'''Gets the names of the systems installed on the controller (synchronous)

		:returns: Names of the installed systems
		'''
		return self._instance.GetInstalledSystems()

	def has_option(self, option: str) -> bool:
		'''Verifies whether an option is present on the controller (synchronous) The option name is case sensitive, for example "SAFEMOVEPRO".

		:param option: Option to verify
		:returns: True when the option is installed on the controller, false otherwise
		'''
		return self._instance.HasOption(option)

	def is_robot_ware_version_compatible(self, robotWareVersion: str) -> bool:
		'''Checks whether a RobotWare version is compatible with the controller hardware (synchronous) Supported only on a real controller.

		:param robotWareVersion: RobotWare version to check, for example "6.03.0101"
		:returns: True when the RobotWare version is compatible with the controller hardware
		'''
		return self._instance.IsRobotWareVersionCompatible(robotWareVersion)

	def get_backup_resources(self) -> typing.List[str]:
		'''Gets the names of the backup sub resources exposed by the controller (synchronous)

		:returns: Names of the backup sub resources ("backup-info", "backup-state", "check-restore")
		'''
		return self._instance.GetBackupResources()

	def get_backup_info(self, backupPath: str) -> BackupSystemInfo:
		'''Gets information about a backup stored on the controller file system (synchronous)

		:param backupPath: Path of the backup folder on the controller file system. Environment variables are allowed, written either "$temp/mybackup" or "~temp/mybackup", with or without the "/fileservice" prefix.
		:returns: Name, versions and options of the backed up system
		'''
		return BackupSystemInfo(self._instance.GetBackupInfo(backupPath))

	def get_backup_state(self) -> BackupState:
		'''Gets the state of the backup operation of the controller (synchronous) Used to follow a backup started with .

		:returns: Current backup state
		'''
		return BackupState(int(self._instance.GetBackupState()))

	def create_backup(self, backupPath: str, archive: bool=False) -> None:
		'''Creates a backup of the current system on the controller file system (synchronous) The backup is created asynchronously by the controller: this method returns as soon as the request is accepted. Poll to know when the backup is finished.Requires the UAS grant UAS_BACKUP. Creating a backup may affect RAPID execution and can cause system stops.

		:param backupPath: Destination path of the backup, it must be part of the controller file system. Environment variables such as $TEMP or $SYSTEM are allowed, written either "$temp/mybackup" or "~temp/mybackup", with or without the "/fileservice" prefix. The backup cannot be created under the $HOME directory, nor use the name of an environment variable directory.
		:param archive: When true, the backup is stored as an archive
		'''
		self._instance.CreateBackup(backupPath, archive)

	def restore_backup(self, backupPath: str, ignore: BackupRestoreIgnore=BackupRestoreIgnore.None_, deleteDirectory: bool=True, includeControllerSettings: bool=True, includeSafetySettings: bool=True, include: BackupRestoreInclude=BackupRestoreInclude.All) -> None:
		'''Restores a backup stored on the controller file system (synchronous) When the backup can be restored, the controller restarts.Requires the UAS grant to restore a backup. Use first to detect mismatches.

		:param backupPath: Path of the backup folder on the controller file system. Environment variables are allowed, written either "$temp/mybackup" or "~temp/mybackup", with or without the "/fileservice" prefix.
		:param ignore: Mismatches between the backup and the current system that are ignored
		:param deleteDirectory: When true, the backup directory is deleted once the restore is finished
		:param includeControllerSettings: Include the controller settings in the restore. RobotWare 7 does not support restoring controller settings and ignores this flag.
		:param includeSafetySettings: Include the safety settings in the restore
		:param include: Content to restore
		'''
		self._instance.RestoreBackup(backupPath, backup_restore_ignore(int(ignore)), deleteDirectory, includeControllerSettings, includeSafetySettings, backup_restore_include(int(include)))

	def check_restore(self, backupPath: str, ignore: BackupRestoreIgnore=BackupRestoreIgnore.None_, includeControllerSettings: bool=True, includeSafetySettings: bool=True, include: BackupRestoreInclude=BackupRestoreInclude.All) -> CheckRestoreResult:
		'''Checks a backup for mismatches and other problems before restoring it (synchronous)

		:param backupPath: Path of the backup folder on the controller file system. Environment variables are allowed, written either "$temp/mybackup" or "~temp/mybackup", with or without the "/fileservice" prefix.
		:param ignore: Mismatches between the backup and the current system that are ignored
		:param includeControllerSettings: Include the controller settings in the restore
		:param includeSafetySettings: Include the safety settings in the restore
		:param include: Content to restore
		:returns: Result of the check, including the missing or corrupted file when the controller reports one
		'''
		return CheckRestoreResult(self._instance.CheckRestore(backupPath, backup_restore_ignore(int(ignore)), includeControllerSettings, includeSafetySettings, backup_restore_include(int(include))))

	def get_safety_resources(self) -> typing.List[str]:
		'''Gets the names of the safety sub resources exposed by the controller (synchronous)

		:returns: Names of the safety sub resources ("safety-mode", "safety-configuration", "violation-info", ...)
		'''
		return self._instance.GetSafetyResources()

	def get_safety_mode(self) -> SafetyModeStatus:
		'''Gets the safety mode of the controller (synchronous)

		:returns: Current safety mode and its user data
		'''
		return SafetyModeStatus(self._instance.GetSafetyMode())

	def set_safety_mode(self, mode: SafetyMode) -> None:
		'''Sets the safety mode of the controller (synchronous) The controller must be in manual mode.

		:param mode: New safety mode, one of Active, Commissioning or Service
		'''
		self._instance.SetSafetyMode(safety_mode(int(mode)))

	def get_safety_configuration(self) -> SafetyConfiguration:
		'''Gets the safety supervision configuration of the controller (synchronous)

		:returns: Versions, creation date and checksum of the safety configuration
		'''
		return SafetyConfiguration(self._instance.GetSafetyConfiguration())

	def load_safety_configuration(self, filePath: str) -> None:
		'''Loads a safety configuration file into the controller (synchronous) The configuration file must already exist on the controller file system.Use to check whether loading is currently allowed.

		:param filePath: Path of the safety configuration file on the controller (e.g. "$home/file.xml")
		'''
		self._instance.LoadSafetyConfiguration(filePath)

	def invalidate_safety_configuration(self) -> None:
		'''Removes the validation information from the safety configuration file (synchronous) Requires the UAS grant UAS_SAFETY_SERVICES.'''
		self._instance.InvalidateSafetyConfiguration()

	def get_safety_load_operation_status(self) -> SafetyLoadOperationStatus:
		'''Checks whether a new safety configuration is allowed to be loaded (synchronous) The user must have the safety services privileges.

		:returns: Ok when a configuration can be loaded, the blocking reason otherwise
		'''
		return SafetyLoadOperationStatus(int(self._instance.GetSafetyLoadOperationStatus()))

	def get_cyclic_brake_check_status(self, driveNumber: int) -> CyclicBrakeCheckStatus:
		'''Gets the cyclic brake check status of a mechanical unit (synchronous)

		:param driveNumber: Drive number of the mechanical unit
		:returns: Cyclic brake check status of the mechanical unit
		'''
		return CyclicBrakeCheckStatus(self._instance.GetCyclicBrakeCheckStatus(driveNumber))

	def get_safety_violation_info(self) -> SafetyViolationInfo:
		'''Gets the safety violation details reported by the safety controller (synchronous) The user must have the safety services privileges.

		:returns: Safety violation details
		'''
		return SafetyViolationInfo(self._instance.GetSafetyViolationInfo())

	def get_virtual_time_resources(self) -> typing.List[str]:
		'''Gets the names of the virtual time sub resources exposed by the controller (synchronous) Supported only on a virtual controller.

		:returns: Names of the virtual time sub resources ("vttime", "vtspeed", "vtstate", "vttimeslice")
		'''
		return self._instance.GetVirtualTimeResources()

	def get_virtual_time(self) -> int:
		'''Gets the current value of the virtual time, in milliseconds (synchronous) The virtual time is zeroed when the virtual controller starts. Supported only on a virtual controller.

		:returns: Virtual time in milliseconds
		'''
		return self._instance.GetVirtualTime()

	def get_virtual_time_speed(self) -> int:
		'''Gets the speed of the virtual time, in percent relative to real time (synchronous) -1 means full speed. Supported only on a virtual controller.

		:returns: Speed of the virtual time in percent
		'''
		return self._instance.GetVirtualTimeSpeed()

	def set_virtual_time_speed(self, speed: int) -> None:
		'''Sets the speed of the virtual time, in percent relative to real time (synchronous) 100 makes the virtual time run approximately at real time speed, -1 runs it as fast as possible.Supported only on a virtual controller.

		:param speed: Speed in percent, or -1 for full speed
		'''
		self._instance.SetVirtualTimeSpeed(speed)

	def get_virtual_time_state(self) -> VirtualTimeState:
		'''Gets the state of the virtual time server (synchronous) Supported only on a virtual controller.

		:returns: State of the virtual time server
		'''
		return VirtualTimeState(int(self._instance.GetVirtualTimeState()))

	def set_virtual_time_state(self, state: VirtualTimeState) -> None:
		'''Sets the state of the virtual time server (synchronous) Supported only on a virtual controller.

		:param state: New state of the virtual time server
		'''
		self._instance.SetVirtualTimeState(virtual_time_state(int(state)))

	def get_virtual_time_slice(self) -> int:
		'''Gets the time slice of the virtual controller, in milliseconds (synchronous) Supported only on a virtual controller.

		:returns: Time slice in milliseconds
		'''
		return self._instance.GetVirtualTimeSlice()

	def set_virtual_time_slice(self, milliseconds: int) -> None:
		'''Sets the time slice of the virtual controller, in milliseconds (synchronous) The minimum value is 10 ms, lower values are replaced by the controller with the default value of 10 ms.Supported only on a virtual controller.

		:param milliseconds: Time slice in milliseconds
		'''
		self._instance.SetVirtualTimeSlice(milliseconds)

	def run_virtual_time(self) -> None:
		'''Executes the virtual time according to the current state of the virtual time server (synchronous) Supported only on a virtual controller.'''
		self._instance.RunVirtualTime()

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ControllerService):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
