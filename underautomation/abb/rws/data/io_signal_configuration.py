from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import IoSignalConfiguration as io_signal_configuration

class IoSignalConfiguration:
	'''Runtime configuration properties of an I/O signal. Returned by IoService.GetSignalConfiguration().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the IoSignalConfiguration class'''
		if(_internal == 0):
			self._instance = io_signal_configuration()
		else:
			self._instance = _internal

	@property
	def signal_name(self) -> str:
		'''Name of the signal, for example "DRV1CHAIN2"'''
		return self._instance.SignalName

	@signal_name.setter
	def signal_name(self, value: str):
		self._instance.SignalName = value

	@property
	def signal_bits(self) -> int | None:
		'''Number of bits of the signal, null when not reported'''
		return self._instance.SignalBits

	@signal_bits.setter
	def signal_bits(self, value: int | None):
		self._instance.SignalBits = value

	@property
	def rapid(self) -> bool | None:
		'''Whether a RAPID client can write the signal in both manual and auto mode'''
		return self._instance.Rapid

	@rapid.setter
	def rapid(self, value: bool | None):
		self._instance.Rapid = value

	@property
	def local_manual(self) -> bool | None:
		'''Whether a local client can write the signal in manual mode'''
		return self._instance.LocalManual

	@local_manual.setter
	def local_manual(self, value: bool | None):
		self._instance.LocalManual = value

	@property
	def local_auto(self) -> bool | None:
		'''Whether a local client can write the signal in auto mode'''
		return self._instance.LocalAuto

	@local_auto.setter
	def local_auto(self, value: bool | None):
		self._instance.LocalAuto = value

	@property
	def remote_manual(self) -> bool | None:
		'''Whether a remote client can write the signal in manual mode'''
		return self._instance.RemoteManual

	@remote_manual.setter
	def remote_manual(self, value: bool | None):
		self._instance.RemoteManual = value

	@property
	def remote_auto(self) -> bool | None:
		'''Whether a remote client can write the signal in auto mode'''
		return self._instance.RemoteAuto

	@remote_auto.setter
	def remote_auto(self, value: bool | None):
		self._instance.RemoteAuto = value

	@property
	def set_by_device_transfer(self) -> bool | None:
		'''Whether the bits of this signal are set by a device transfer operation. Not reported by every controller, null when absent from the response.'''
		return self._instance.SetByDeviceTransfer

	@set_by_device_transfer.setter
	def set_by_device_transfer(self, value: bool | None):
		self._instance.SetByDeviceTransfer = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IoSignalConfiguration):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
