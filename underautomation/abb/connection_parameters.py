from __future__ import annotations
import typing
from underautomation.abb.rws.rws_connect_parameters import RwsConnectParameters
from UnderAutomation.ABB import ConnectionParameters as connection_parameters

class ConnectionParameters:
	'''Connection parameters for an ABB robot controller'''
	def __init__(self, address: str, _internal = 0):
		'''Instantiate new connection parameters with a specified address

		:param address: IP address or hostname of the robot controller
		'''
		if(_internal == 0):
			self._instance = connection_parameters(address)
		else:
			self._instance = _internal

	@property
	def address(self) -> str:
		'''Address of the robot controller (IP or host name), default value is 127.0.0.1'''
		return self._instance.Address

	@address.setter
	def address(self, value: str):
		self._instance.Address = value

	@property
	def ping_before_connect(self) -> bool:
		'''Send a ping command before initializing any connections'''
		return self._instance.PingBeforeConnect

	@ping_before_connect.setter
	def ping_before_connect(self, value: bool):
		self._instance.PingBeforeConnect = value

	@property
	def rws(self) -> RwsConnectParameters:
		'''RWS2 (Robot Web Services 2) connection parameters'''
		return RwsConnectParameters(self._instance.Rws)

	@rws.setter
	def rws(self, value: RwsConnectParameters):
		self._instance.Rws = value._instance if value else None

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ConnectionParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
