from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import IoNetworkConfiguration as io_network_configuration

class IoNetworkConfiguration:
	'''Runtime configuration properties of an I/O network. Returned by IoService.GetNetworkConfiguration().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the IoNetworkConfiguration class'''
		if(_internal == 0):
			self._instance = io_network_configuration()
		else:
			self._instance = _internal

	@property
	def network_name(self) -> str:
		'''Name of the network, for example "Local"'''
		return self._instance.NetworkName

	@network_name.setter
	def network_name(self, value: str):
		self._instance.NetworkName = value

	@property
	def network_type(self) -> str:
		'''Type of the network, for example "Local" or "LOC"'''
		return self._instance.NetworkType

	@network_type.setter
	def network_type(self, value: str):
		self._instance.NetworkType = value

	@property
	def network_address(self) -> str:
		'''Industrial network address, "-" when the network has no addressing'''
		return self._instance.NetworkAddress

	@network_address.setter
	def network_address(self, value: str):
		self._instance.NetworkAddress = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, IoNetworkConfiguration):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
