from __future__ import annotations
import typing
from underautomation.abb.rws.data.io_network_physical_state import IoNetworkPhysicalState
from underautomation.abb.rws.data.io_network_logical_state import IoNetworkLogicalState
from UnderAutomation.ABB.Rws.Data import IoNetworkItem as io_network_item
from UnderAutomation.ABB.Rws.Data import IoNetworkPhysicalState as io_network_physical_state
from UnderAutomation.ABB.Rws.Data import IoNetworkLogicalState as io_network_logical_state

class IoNetworkItem:
	'''I/O network defined in the robot controller. Returned by IoService.GetNetworks(), IoService.GetNetwork() and IoService.SearchNetworks().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the IoNetworkItem class'''
		if(_internal == 0):
			self._instance = io_network_item()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Name of the network, for example "Local", "Virtual" or "EtherNetIP"'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def path(self) -> str:
		'''Full path of the network, which is its name for a network (for example "Local")'''
		return self._instance.Path

	@path.setter
	def path(self, value: str):
		self._instance.Path = value

	@property
	def physical_state(self) -> IoNetworkPhysicalState:
		'''Physical state of the network'''
		return IoNetworkPhysicalState(int(self._instance.PhysicalState))

	@physical_state.setter
	def physical_state(self, value: IoNetworkPhysicalState):
		self._instance.PhysicalState = io_network_physical_state(int(value))

	@property
	def logical_state(self) -> IoNetworkLogicalState:
		'''Logical state of the network'''
		return IoNetworkLogicalState(int(self._instance.LogicalState))

	@logical_state.setter
	def logical_state(self, value: IoNetworkLogicalState):
		self._instance.LogicalState = io_network_logical_state(int(value))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IoNetworkItem):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
