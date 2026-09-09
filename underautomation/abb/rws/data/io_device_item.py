from __future__ import annotations
import typing
from underautomation.abb.rws.data.io_device_physical_state import IoDevicePhysicalState
from underautomation.abb.rws.data.io_device_logical_state import IoDeviceLogicalState
from UnderAutomation.ABB.Rws.Data import IoDeviceItem as io_device_item
from UnderAutomation.ABB.Rws.Data import IoDevicePhysicalState as io_device_physical_state
from UnderAutomation.ABB.Rws.Data import IoDeviceLogicalState as io_device_logical_state

class IoDeviceItem:
	'''I/O device (unit) connected to an I/O network of the robot controller. Returned by IoService.GetDevices(), IoService.GetDevice() and IoService.SearchDevices().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the IoDeviceItem class'''
		if(_internal == 0):
			self._instance = io_device_item()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Name of the device, for example "DRV_1" or "PANEL"'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def network_name(self) -> str:
		'''Name of the network the device is connected to, for example "Local"'''
		return self._instance.NetworkName

	@network_name.setter
	def network_name(self, value: str):
		self._instance.NetworkName = value

	@property
	def path(self) -> str:
		'''Full path of the device, "{network}/{device}" (for example "Local/DRV_1")'''
		return self._instance.Path

	@path.setter
	def path(self, value: str):
		self._instance.Path = value

	@property
	def type(self) -> str:
		'''Type of the device, for example "DRV_1_TYPE". Not reported by every controller, null when absent. A virtual controller leaves it out.'''
		return self._instance.Type

	@type.setter
	def type(self, value: str):
		self._instance.Type = value

	@property
	def physical_state(self) -> IoDevicePhysicalState:
		'''Physical state of the device'''
		return IoDevicePhysicalState(int(self._instance.PhysicalState))

	@physical_state.setter
	def physical_state(self, value: IoDevicePhysicalState):
		self._instance.PhysicalState = io_device_physical_state(int(value))

	@property
	def logical_state(self) -> IoDeviceLogicalState:
		'''Logical state of the device'''
		return IoDeviceLogicalState(int(self._instance.LogicalState))

	@logical_state.setter
	def logical_state(self, value: IoDeviceLogicalState):
		self._instance.LogicalState = io_device_logical_state(int(value))

	@property
	def address(self) -> str:
		'''Address of the device on its network, "-" when the network has no addressing'''
		return self._instance.Address

	@address.setter
	def address(self, value: str):
		self._instance.Address = value

	@property
	def input_data(self) -> str:
		'''Input data of the device, as an hexadecimal string (for example "1FFFE063"). Only reported when reading a single device with IoService.GetDevice().'''
		return self._instance.InputData

	@input_data.setter
	def input_data(self, value: str):
		self._instance.InputData = value

	@property
	def input_mask(self) -> str:
		'''Input mask of the device, as an hexadecimal string. A bit set to zero is an input bit that is not written. Only reported when reading a single device with IoService.GetDevice().'''
		return self._instance.InputMask

	@input_mask.setter
	def input_mask(self, value: str):
		self._instance.InputMask = value

	@property
	def output_data(self) -> str:
		'''Output data of the device, as an hexadecimal string (for example "0000000E"). Only reported when reading a single device with IoService.GetDevice().'''
		return self._instance.OutputData

	@output_data.setter
	def output_data(self, value: str):
		self._instance.OutputData = value

	@property
	def output_mask(self) -> str:
		'''Output mask of the device, as an hexadecimal string. A bit set to zero is an output bit that is not written. Only reported when reading a single device with IoService.GetDevice().'''
		return self._instance.OutputMask

	@output_mask.setter
	def output_mask(self, value: str):
		self._instance.OutputMask = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IoDeviceItem):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
