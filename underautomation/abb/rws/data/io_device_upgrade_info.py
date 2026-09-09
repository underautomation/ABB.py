from __future__ import annotations
import typing
from underautomation.abb.rws.data.io_firmware_upgrade_state import IoFirmwareUpgradeState
from underautomation.abb.rws.data.io_firmware_upgrade_status import IoFirmwareUpgradeStatus
from underautomation.abb.rws.data.io_firmware_module_info import IoFirmwareModuleInfo
from UnderAutomation.ABB.Rws.Data import IoDeviceUpgradeInfo as io_device_upgrade_info
from UnderAutomation.ABB.Rws.Data import IoFirmwareUpgradeState as io_firmware_upgrade_state
from UnderAutomation.ABB.Rws.Data import IoFirmwareUpgradeStatus as io_firmware_upgrade_status

class IoDeviceUpgradeInfo:
	'''Firmware upgrade status of an I/O device and of each of its modules. Returned by IoService.GetDeviceUpgradeInfo().Only applicable to a real controller.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the IoDeviceUpgradeInfo class'''
		if(_internal == 0):
			self._instance = io_device_upgrade_info()
		else:
			self._instance = _internal

	@property
	def state(self) -> IoFirmwareUpgradeState:
		'''Overall progress of the firmware upgrade of the device'''
		return IoFirmwareUpgradeState(int(self._instance.State))

	@state.setter
	def state(self, value: IoFirmwareUpgradeState):
		self._instance.State = io_firmware_upgrade_state(int(value))

	@property
	def status(self) -> IoFirmwareUpgradeStatus:
		'''Overall result of the firmware upgrade of the device'''
		return IoFirmwareUpgradeStatus(int(self._instance.Status))

	@status.setter
	def status(self, value: IoFirmwareUpgradeStatus):
		self._instance.Status = io_firmware_upgrade_status(int(value))

	@property
	def modules(self) -> typing.List[IoFirmwareModuleInfo]:
		'''Firmware status of each module of the device, empty when the controller reported none'''
		return [IoFirmwareModuleInfo(x) for x in self._instance.Modules]

	@modules.setter
	def modules(self, value: typing.List[IoFirmwareModuleInfo]):
		self._instance.Modules = [x._instance if x else None for x in value]

	@property
	def module_count(self) -> int:
		'''Number of modules reported by the controller'''
		return self._instance.ModuleCount

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IoDeviceUpgradeInfo):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
