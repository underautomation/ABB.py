from __future__ import annotations
import typing
from underautomation.abb.rws.data.io_signal_type import IoSignalType
from underautomation.abb.rws.data.io_signal_logical_state import IoSignalLogicalState
from underautomation.abb.rws.data.io_signal_physical_state import IoSignalPhysicalState
from UnderAutomation.ABB.Rws.Data import IoSignalItem as io_signal_item
from UnderAutomation.ABB.Rws.Data import IoSignalType as io_signal_type
from UnderAutomation.ABB.Rws.Data import IoSignalLogicalState as io_signal_logical_state
from UnderAutomation.ABB.Rws.Data import IoSignalPhysicalState as io_signal_physical_state

class IoSignalItem:
	'''I/O signal defined in the robot controller. Returned by IoService.GetSignals(), IoService.GetSignal(), IoService.SearchSignals() and IoService.SearchSignalsExtended().Depending on the method used, only a subset of the properties is filled in: the signal lists carry the name, type, category, logical value and logical state only.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the IoSignalItem class'''
		if(_internal == 0):
			self._instance = io_signal_item()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Name of the signal, for example "DRV1BRAKE"'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def network_name(self) -> str:
		'''Name of the network the signal belongs to, for example "Local"'''
		return self._instance.NetworkName

	@network_name.setter
	def network_name(self, value: str):
		self._instance.NetworkName = value

	@property
	def device_name(self) -> str:
		'''Name of the device the signal is connected to, for example "DRV_1"'''
		return self._instance.DeviceName

	@device_name.setter
	def device_name(self, value: str):
		self._instance.DeviceName = value

	@property
	def path(self) -> str:
		'''Full path of the signal, "{network}/{device}/{signal}" (for example "Local/DRV_1/DRV1BRAKE")'''
		return self._instance.Path

	@path.setter
	def path(self, value: str):
		self._instance.Path = value

	@property
	def type(self) -> IoSignalType:
		'''Type of the signal'''
		return IoSignalType(int(self._instance.Type))

	@type.setter
	def type(self, value: IoSignalType):
		self._instance.Type = io_signal_type(int(value))

	@property
	def category(self) -> str:
		'''Category the signal belongs to, for example "safety"'''
		return self._instance.Category

	@category.setter
	def category(self, value: str):
		self._instance.Category = value

	@property
	def logical_value(self) -> float | None:
		'''Logical value of the signal, null when the controller did not report it'''
		return self._instance.LogicalValue

	@logical_value.setter
	def logical_value(self, value: float | None):
		self._instance.LogicalValue = value

	@property
	def logical_state(self) -> IoSignalLogicalState:
		'''Logical state of the signal (simulated or not)'''
		return IoSignalLogicalState(int(self._instance.LogicalState))

	@logical_state.setter
	def logical_state(self, value: IoSignalLogicalState):
		self._instance.LogicalState = io_signal_logical_state(int(value))

	@property
	def physical_state(self) -> IoSignalPhysicalState:
		'''Physical state of the signal. Only reported when reading a single signal with IoService.GetSignal().'''
		return IoSignalPhysicalState(int(self._instance.PhysicalState))

	@physical_state.setter
	def physical_state(self, value: IoSignalPhysicalState):
		self._instance.PhysicalState = io_signal_physical_state(int(value))

	@property
	def physical_value(self) -> float | None:
		'''Physical value of the signal, null when the controller did not report it. Only reported by IoService.GetSignal() and IoService.SearchSignalsExtended().'''
		return self._instance.PhysicalValue

	@physical_value.setter
	def physical_value(self, value: float | None):
		self._instance.PhysicalValue = value

	@property
	def logical_time_seconds(self) -> int | None:
		'''Seconds part of the global time at which the logical value was updated, null when not reported'''
		return self._instance.LogicalTimeSeconds

	@logical_time_seconds.setter
	def logical_time_seconds(self, value: int | None):
		self._instance.LogicalTimeSeconds = value

	@property
	def logical_time_microseconds(self) -> int | None:
		'''Microseconds part of the global time at which the logical value was updated, null when not reported'''
		return self._instance.LogicalTimeMicroseconds

	@logical_time_microseconds.setter
	def logical_time_microseconds(self, value: int | None):
		self._instance.LogicalTimeMicroseconds = value

	@property
	def physical_time_seconds(self) -> int | None:
		'''Seconds part of the global time at which the physical value was updated, null when not reported'''
		return self._instance.PhysicalTimeSeconds

	@physical_time_seconds.setter
	def physical_time_seconds(self, value: int | None):
		self._instance.PhysicalTimeSeconds = value

	@property
	def physical_time_microseconds(self) -> int | None:
		'''Microseconds part of the global time at which the physical value was updated, null when not reported'''
		return self._instance.PhysicalTimeMicroseconds

	@physical_time_microseconds.setter
	def physical_time_microseconds(self, value: int | None):
		self._instance.PhysicalTimeMicroseconds = value

	@property
	def quality(self) -> str:
		'''Quality of the signal, reported as a numeric code by IoService.GetSignal() and as a textual value (for example "good") by IoService.SearchSignalsExtended()'''
		return self._instance.Quality

	@quality.setter
	def quality(self, value: str):
		self._instance.Quality = value

	@property
	def write_access_level(self) -> str:
		'''Access level required to write the signal, for example "None". Only reported by IoService.SearchSignalsExtended().'''
		return self._instance.WriteAccessLevel

	@write_access_level.setter
	def write_access_level(self, value: str):
		self._instance.WriteAccessLevel = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IoSignalItem):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
