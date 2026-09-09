from __future__ import annotations
import typing
from underautomation.abb.rws.data.io_network_item import IoNetworkItem
from underautomation.abb.rws.data.io_network_configuration import IoNetworkConfiguration
from underautomation.abb.rws.data.io_client_action import IoClientAction
from underautomation.abb.rws.data.io_network_configuration_type import IoNetworkConfigurationType
from underautomation.abb.rws.data.io_network_logical_state import IoNetworkLogicalState
from underautomation.abb.rws.data.io_device_item import IoDeviceItem
from underautomation.abb.rws.data.io_device_configuration import IoDeviceConfiguration
from underautomation.abb.rws.data.io_device_upgrade_info import IoDeviceUpgradeInfo
from underautomation.abb.rws.data.io_device_logical_state import IoDeviceLogicalState
from underautomation.abb.rws.data.io_signal_item import IoSignalItem
from underautomation.abb.rws.data.io_signal_configuration import IoSignalConfiguration
from underautomation.abb.rws.data.io_signal_search_criteria import IoSignalSearchCriteria
from underautomation.abb.rws.data.io_network_physical_state import IoNetworkPhysicalState
from UnderAutomation.ABB.Rws.Services import IoService as io_service
from UnderAutomation.ABB.Rws.Data import IoClientAction as io_client_action
from UnderAutomation.ABB.Rws.Data import IoNetworkConfigurationType as io_network_configuration_type
from UnderAutomation.ABB.Rws.Data import IoNetworkLogicalState as io_network_logical_state
from UnderAutomation.ABB.Rws.Data import IoDeviceLogicalState as io_device_logical_state
from UnderAutomation.ABB.Rws.Data import IoNetworkPhysicalState as io_network_physical_state

class IoService:
	'''I/O System Service - Provides access to the I/O resources of the controller: networks, devices and signals. None of these resources is available while the controller runs in bootserver mode.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = io_service()
		else:
			self._instance = _internal

	def get_resources(self) -> typing.List[str]:
		'''Gets the names of the I/O sub resources exposed by the controller (synchronous)

		:returns: Names of the I/O sub resources ("networks", "devices", "signals")
		'''
		return self._instance.GetResources()

	def get_networks(self) -> typing.List[IoNetworkItem]:
		'''Gets every I/O network defined in the controller (synchronous)

		:returns: I/O networks, for example "Local" and "Virtual"
		'''
		return [IoNetworkItem(x) for x in self._instance.GetNetworks()]

	def get_network(self, network: str) -> IoNetworkItem:
		'''Gets a single I/O network (synchronous)

		:param network: Name of the network, for example "Local"
		:returns: The I/O network
		'''
		return IoNetworkItem(self._instance.GetNetwork(network))

	def search_networks(self, name: str=None, physicalState: IoNetworkPhysicalState | None=None) -> typing.List[IoNetworkItem]:
		return [IoNetworkItem(x) for x in self._instance.SearchNetworks(name, physicalState)]

	def get_network_configuration(self, network: str) -> IoNetworkConfiguration:
		'''Gets the runtime configuration properties of an I/O network (synchronous)

		:param network: Name of the network, for example "Local"
		:returns: Runtime configuration of the network
		'''
		return IoNetworkConfiguration(self._instance.GetNetworkConfiguration(network))

	def set_network_configuration_type(self, network: str, configurationType: IoNetworkConfigurationType) -> IoClientAction:
		'''Runs the auto configuration of an I/O network (synchronous)

		:param network: Name of the network, for example "Local"
		:param configurationType: Part of the network to configure
		:returns: Action the client is expected to take, Unknown when the controller did not report one
		'''
		return IoClientAction(int(self._instance.SetNetworkConfigurationType(network, io_network_configuration_type(int(configurationType)))))

	def set_network_state(self, network: str, logicalState: IoNetworkLogicalState) -> None:
		'''Starts or stops an I/O network (synchronous)

		:param network: Name of the network, for example "Local"
		:param logicalState: New logical state of the network, Started or Stopped
		'''
		self._instance.SetNetworkState(network, io_network_logical_state(int(logicalState)))

	def get_devices(self) -> typing.List[IoDeviceItem]:
		'''Gets every I/O device defined in the controller (synchronous)

		:returns: I/O devices of every network
		'''
		return [IoDeviceItem(x) for x in self._instance.GetDevices()]

	def get_device(self, network: str, device: str) -> IoDeviceItem:
		'''Gets a single I/O device, including its input and output data (synchronous)

		:param network: Name of the network the device is connected to, for example "Local"
		:param device: Name of the device, for example "PANEL"
		:returns: The I/O device
		'''
		return IoDeviceItem(self._instance.GetDevice(network, device))

	def search_devices(self, name: str=None, logicalState: IoDeviceLogicalState | None=None, network: str=None) -> typing.List[IoDeviceItem]:
		return [IoDeviceItem(x) for x in self._instance.SearchDevices(name, logicalState, network)]

	def get_device_configuration(self, network: str, device: str) -> IoDeviceConfiguration:
		'''Gets the runtime configuration properties of an I/O device (synchronous)

		:param network: Name of the network the device is connected to, for example "DeviceNet"
		:param device: Name of the device, for example "DN_Internal_Device"
		:returns: Runtime configuration of the device
		'''
		return IoDeviceConfiguration(self._instance.GetDeviceConfiguration(network, device))

	def get_device_upgrade_info(self, network: str, device: str) -> IoDeviceUpgradeInfo:
		'''Gets the firmware upgrade status of an I/O device and of each of its modules (synchronous) Only available on a real controller.

		:param network: Name of the network the device is connected to, for example "EtherNetIP"
		:param device: Name of the device, for example "EN_Internal_Device"
		:returns: Firmware upgrade status of the device
		'''
		return IoDeviceUpgradeInfo(self._instance.GetDeviceUpgradeInfo(network, device))

	def set_device_state(self, network: str, device: str, logicalState: IoDeviceLogicalState) -> None:
		'''Enables or disables an I/O device (synchronous)

		:param network: Name of the network the device is connected to, for example "Local"
		:param device: Name of the device, for example "DRV_1"
		:param logicalState: New logical state of the device, Enabled or Disabled
		'''
		self._instance.SetDeviceState(network, device, io_device_logical_state(int(logicalState)))

	def set_device_input_data(self, network: str, device: str, startByte: int, signalData: int, dataMask: int) -> None:
		'''Writes one byte of the input data of an I/O device (synchronous) Only supported on a virtual controller.

		:param network: Name of the network the device is connected to, for example "Local"
		:param device: Name of the device, for example "DRV_1"
		:param startByte: Index of the written byte. For a 4 bytes long input data, it ranges from 0 to 3.
		:param signalData: Written value, from 0 to 255. Only the first 8 bits are used.
		:param dataMask: Mask of the written bits, from 0 to 255. A bit set to zero is left unchanged.
		'''
		self._instance.SetDeviceInputData(network, device, startByte, signalData, dataMask)

	def set_device_output_data(self, network: str, device: str, startByte: int, signalData: int, dataMask: int) -> None:
		'''Writes one byte of the output data of an I/O device (synchronous) Only supported on a virtual controller.

		:param network: Name of the network the device is connected to, for example "Local"
		:param device: Name of the device, for example "DRV_1"
		:param startByte: Index of the written byte. For a 4 bytes long output data, it ranges from 0 to 3.
		:param signalData: Written value, from 0 to 255. Only the first 8 bits are used.
		:param dataMask: Mask of the written bits, from 0 to 255. A bit set to zero is left unchanged.
		'''
		self._instance.SetDeviceOutputData(network, device, startByte, signalData, dataMask)

	def send_device_command(self, network: str, device: str, commandName: str, value: str, valueLength: int, timeout: int) -> None:
		'''Sends a command to an I/O device (synchronous) Only available on a real controller.

		:param network: Name of the network the device is connected to, for example "EtherNetIP"
		:param device: Name of the device, for example "Local_IO"
		:param commandName: Name of the device command, for example "FIRMWARE_INFO"
		:param value: Value of the command, an empty string when the command takes none
		:param valueLength: Number of bytes of value
		:param timeout: Maximum time in milliseconds to wait for the answer of the device
		'''
		self._instance.SendDeviceCommand(network, device, commandName, value, valueLength, timeout)

	def get_signals(self) -> typing.List[IoSignalItem]:
		'''Gets every I/O signal defined in the controller (synchronous) A controller usually exposes several hundreds of signals. Use to narrow the result down to a network, a device, a category or a signal type.

		:returns: I/O signals of every device
		'''
		return [IoSignalItem(x) for x in self._instance.GetSignals()]

	def get_signal(self, network: str, device: str, signal: str) -> IoSignalItem:
		'''Gets a single I/O signal, including its physical value and time stamps (synchronous)

		:param network: Name of the network the signal belongs to, for example "Local"
		:param device: Name of the device the signal is connected to, for example "DRV_1"
		:param signal: Name of the signal, for example "DRV1K1"
		:returns: The I/O signal
		'''
		return IoSignalItem(self._instance.GetSignal(network, device, signal))

	def get_signal_configuration(self, network: str, device: str, signal: str) -> IoSignalConfiguration:
		'''Gets the runtime configuration properties of an I/O signal (synchronous)

		:param network: Name of the network the signal belongs to, for example "Local"
		:param device: Name of the device the signal is connected to, for example "DRV_1"
		:param signal: Name of the signal, for example "DRV1K1"
		:returns: Runtime configuration of the signal
		'''
		return IoSignalConfiguration(self._instance.GetSignalConfiguration(network, device, signal))

	def set_signal_value(self, network: str, device: str, signal: str, value: float, logToEventLog: bool=False) -> None:
		'''Writes the value of an I/O signal (synchronous)

		:param network: Name of the network the signal belongs to, for example "Local"
		:param device: Name of the device the signal is connected to, for example "DRV_1"
		:param signal: Name of the signal, for example "DRV1K1"
		:param value: New logical value of the signal, 0 or 1 for a digital signal
		:param logToEventLog: Whether the change is written to the event log of the controller
		'''
		self._instance.SetSignalValue(network, device, signal, value, logToEventLog)

	def set_signal_value_delayed(self, network: str, device: str, signal: str, value: float, delay: int, logToEventLog: bool=False) -> None:
		'''Writes the value of an I/O signal in "queued delayed" mode (synchronous) The controller queues the write and applies it once the delay has elapsed.

		:param network: Name of the network the signal belongs to, for example "Local"
		:param device: Name of the device the signal is connected to, for example "DRV_1"
		:param signal: Name of the signal, for example "DRV1K1"
		:param value: New logical value of the signal, 0 or 1 for a digital signal
		:param delay: Delay in milliseconds before the value is applied
		:param logToEventLog: Whether the change is written to the event log of the controller
		'''
		self._instance.SetSignalValueDelayed(network, device, signal, value, delay, logToEventLog)

	def invert_signal(self, network: str, device: str, signal: str, value: float, logToEventLog: bool=False) -> None:
		'''Inverts the value of an I/O signal (synchronous) Only digital and group signals can be inverted.

		:param network: Name of the network the signal belongs to, for example "Local"
		:param device: Name of the device the signal is connected to, for example "DRV_1"
		:param signal: Name of the signal, for example "DRV1K1"
		:param value: Current logical value of the signal, which the controller requires even to invert it
		:param logToEventLog: Whether the change is written to the event log of the controller
		'''
		self._instance.InvertSignal(network, device, signal, value, logToEventLog)

	def pulse_signal(self, network: str, device: str, signal: str, value: float, pulses: int, activePulseLength: int | None=None, passivePulseLength: int | None=None, logToEventLog: bool=False) -> None:
		self._instance.PulseSignal(network, device, signal, value, pulses, activePulseLength, passivePulseLength, logToEventLog)

	def toggle_signal(self, network: str, device: str, signal: str, value: float, pulses: int, activePulseLength: int | None=None, passivePulseLength: int | None=None, logToEventLog: bool=False) -> None:
		self._instance.ToggleSignal(network, device, signal, value, pulses, activePulseLength, passivePulseLength, logToEventLog)

	def set_signal_state(self, network: str, device: str, signal: str, simulated: bool) -> None:
		'''Simulates or stops simulating an I/O signal (synchronous) A simulated signal keeps the logical value written by the client and no longer follows its physical value.

		:param network: Name of the network the signal belongs to, for example "Local"
		:param device: Name of the device the signal is connected to, for example "DRV_1"
		:param signal: Name of the signal, for example "DRV1K1"
		:param simulated: True to simulate the signal, false to stop simulating it
		'''
		self._instance.SetSignalState(network, device, signal, simulated)

	def search_signals(self, criteria: IoSignalSearchCriteria=None, secondCriteria: IoSignalSearchCriteria=None, start: int | None=None, limit: int | None=None) -> typing.List[IoSignalItem]:
		return [IoSignalItem(x) for x in self._instance.SearchSignals(criteria._instance if criteria else None, secondCriteria._instance if secondCriteria else None, start, limit)]

	def search_signals_extended(self, criteria: IoSignalSearchCriteria=None, secondCriteria: IoSignalSearchCriteria=None, start: int | None=None, limit: int | None=None) -> typing.List[IoSignalItem]:
		return [IoSignalItem(x) for x in self._instance.SearchSignalsExtended(criteria._instance if criteria else None, secondCriteria._instance if secondCriteria else None, start, limit)]

	def unblock_signals(self) -> None:
		'''Removes the simulation of every simulated I/O signal of the controller (synchronous)'''
		self._instance.UnblockSignals()

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IoService):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
