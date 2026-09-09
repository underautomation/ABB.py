from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import NetworkInterfaceItem as network_interface_item

class NetworkInterfaceItem:
	'''Network interface of the robot controller. Returned by ControllerService.GetNetworkInterfaces().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the NetworkInterfaceItem class'''
		if(_internal == 0):
			self._instance = network_interface_item()
		else:
			self._instance = _internal

	@property
	def port(self) -> str:
		'''Physical port of the interface, for example "X6" or "X23"'''
		return self._instance.Port

	@port.setter
	def port(self, value: str):
		self._instance.Port = value

	@property
	def logical_name(self) -> str:
		'''Logical name of the interface, for example "WAN", "LAN1" or "SERVICE"'''
		return self._instance.LogicalName

	@logical_name.setter
	def logical_name(self, value: str):
		self._instance.LogicalName = value

	@property
	def network(self) -> str:
		'''Network the interface belongs to ("Public", "Private", "Ability", "Drive"). Only available when connected with version 2.'''
		return self._instance.Network

	@network.setter
	def network(self, value: str):
		self._instance.Network = value

	@property
	def address(self) -> str:
		'''IP address of the interface'''
		return self._instance.Address

	@address.setter
	def address(self, value: str):
		self._instance.Address = value

	@property
	def mask(self) -> str:
		'''Subnet mask of the interface'''
		return self._instance.Mask

	@mask.setter
	def mask(self, value: str):
		self._instance.Mask = value

	@property
	def primary_dns(self) -> str:
		'''Primary DNS server of the interface. Only available when connected with version 2.'''
		return self._instance.PrimaryDns

	@primary_dns.setter
	def primary_dns(self, value: str):
		self._instance.PrimaryDns = value

	@property
	def secondary_dns(self) -> str:
		'''Secondary DNS server of the interface. Only available when connected with version 2.'''
		return self._instance.SecondaryDns

	@secondary_dns.setter
	def secondary_dns(self, value: str):
		self._instance.SecondaryDns = value

	@property
	def dhcp_enabled(self) -> bool | None:
		'''DHCP status of the interface, if reported by the controller'''
		return self._instance.DhcpEnabled

	@dhcp_enabled.setter
	def dhcp_enabled(self, value: bool | None):
		self._instance.DhcpEnabled = value

	@property
	def gateway(self) -> str:
		'''Default gateway of the interface, if applicable'''
		return self._instance.Gateway

	@gateway.setter
	def gateway(self, value: str):
		self._instance.Gateway = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, NetworkInterfaceItem):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
