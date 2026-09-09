from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import IoDeviceConfiguration as io_device_configuration

class IoDeviceConfiguration:
	'''Runtime configuration properties of an I/O device. Returned by IoService.GetDeviceConfiguration().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the IoDeviceConfiguration class'''
		if(_internal == 0):
			self._instance = io_device_configuration()
		else:
			self._instance = _internal

	@property
	def device_name(self) -> str:
		'''Name of the device, for example "DN_Internal_Device"'''
		return self._instance.DeviceName

	@device_name.setter
	def device_name(self, value: str):
		self._instance.DeviceName = value

	@property
	def network_name(self) -> str:
		'''Name of the industrial network the device belongs to, for example "DeviceNet"'''
		return self._instance.NetworkName

	@network_name.setter
	def network_name(self, value: str):
		self._instance.NetworkName = value

	@property
	def input_bits(self) -> int | None:
		'''Number of input bits of the device, null when not reported'''
		return self._instance.InputBits

	@input_bits.setter
	def input_bits(self, value: int | None):
		self._instance.InputBits = value

	@property
	def output_bits(self) -> int | None:
		'''Number of output bits of the device, null when not reported'''
		return self._instance.OutputBits

	@output_bits.setter
	def output_bits(self, value: int | None):
		self._instance.OutputBits = value

	@property
	def rapid(self) -> bool | None:
		'''Whether a RAPID client can access the device in both manual and auto mode'''
		return self._instance.Rapid

	@rapid.setter
	def rapid(self, value: bool | None):
		self._instance.Rapid = value

	@property
	def local_manual(self) -> bool | None:
		'''Whether a local client can access the device in manual mode'''
		return self._instance.LocalManual

	@local_manual.setter
	def local_manual(self, value: bool | None):
		self._instance.LocalManual = value

	@property
	def local_auto(self) -> bool | None:
		'''Whether a local client can access the device in auto mode'''
		return self._instance.LocalAuto

	@local_auto.setter
	def local_auto(self, value: bool | None):
		self._instance.LocalAuto = value

	@property
	def remote_manual(self) -> bool | None:
		'''Whether a remote client can access the device in manual mode'''
		return self._instance.RemoteManual

	@remote_manual.setter
	def remote_manual(self, value: bool | None):
		self._instance.RemoteManual = value

	@property
	def remote_auto(self) -> bool | None:
		'''Whether a remote client can access the device in auto mode'''
		return self._instance.RemoteAuto

	@remote_auto.setter
	def remote_auto(self, value: bool | None):
		self._instance.RemoteAuto = value

	@property
	def device_address(self) -> str:
		'''Address of the device on its network, "-" when the network has no addressing'''
		return self._instance.DeviceAddress

	@device_address.setter
	def device_address(self, value: str):
		self._instance.DeviceAddress = value

	@property
	def deny_deactivate(self) -> bool | None:
		'''Whether deactivating the device is denied'''
		return self._instance.DenyDeactivate

	@deny_deactivate.setter
	def deny_deactivate(self, value: bool | None):
		self._instance.DenyDeactivate = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IoDeviceConfiguration):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
