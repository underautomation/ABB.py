from __future__ import annotations
import typing
from underautomation.abb.rws.data.io_firmware_upgrade_state import IoFirmwareUpgradeState
from underautomation.abb.rws.data.io_firmware_upgrade_status import IoFirmwareUpgradeStatus
from UnderAutomation.ABB.Rws.Data import IoFirmwareModuleInfo as io_firmware_module_info
from UnderAutomation.ABB.Rws.Data import IoFirmwareUpgradeState as io_firmware_upgrade_state
from UnderAutomation.ABB.Rws.Data import IoFirmwareUpgradeStatus as io_firmware_upgrade_status

class IoFirmwareModuleInfo:
	'''Firmware upgrade status of one module of an I/O device. Returned by IoService.GetDeviceUpgradeInfo().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the IoFirmwareModuleInfo class'''
		if(_internal == 0):
			self._instance = io_firmware_module_info()
		else:
			self._instance = _internal

	@property
	def index(self) -> str:
		'''Index of the module inside the device ("0", "1", ...)'''
		return self._instance.Index

	@index.setter
	def index(self, value: str):
		self._instance.Index = value

	@property
	def state(self) -> IoFirmwareUpgradeState:
		'''Progress of the firmware upgrade of this module'''
		return IoFirmwareUpgradeState(int(self._instance.State))

	@state.setter
	def state(self, value: IoFirmwareUpgradeState):
		self._instance.State = io_firmware_upgrade_state(int(value))

	@property
	def status(self) -> IoFirmwareUpgradeStatus:
		'''Result of the firmware upgrade of this module'''
		return IoFirmwareUpgradeStatus(int(self._instance.Status))

	@status.setter
	def status(self, value: IoFirmwareUpgradeStatus):
		self._instance.Status = io_firmware_upgrade_status(int(value))

	@property
	def program_name(self) -> str:
		'''Name of the program installed on the module, for example "A_HYPIOM_B_3_8"'''
		return self._instance.ProgramName

	@program_name.setter
	def program_name(self, value: str):
		self._instance.ProgramName = value

	@property
	def serial_number(self) -> str:
		'''Serial number of the module'''
		return self._instance.SerialNumber

	@serial_number.setter
	def serial_number(self, value: str):
		self._instance.SerialNumber = value

	@property
	def hardware_revision(self) -> str:
		'''Hardware revision of the module, for example "C.1"'''
		return self._instance.HardwareRevision

	@hardware_revision.setter
	def hardware_revision(self, value: str):
		self._instance.HardwareRevision = value

	@property
	def latest_program_name_available(self) -> str:
		'''Name of the latest program available for the module'''
		return self._instance.LatestProgramNameAvailable

	@latest_program_name_available.setter
	def latest_program_name_available(self, value: str):
		self._instance.LatestProgramNameAvailable = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IoFirmwareModuleInfo):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
