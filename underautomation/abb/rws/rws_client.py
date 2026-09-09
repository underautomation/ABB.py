from __future__ import annotations
import typing
from underautomation.abb.rws.rws_version import RwsVersion
from underautomation.abb.rws.internal.rws_client_base import RwsClientBase
from UnderAutomation.ABB.Rws import RwsClient as rws_client
from UnderAutomation.ABB.Rws import RwsVersion as rws_version

class RwsClient(RwsClientBase):
	'''Standalone public RWS client for ABB robot controllers. Supports both RWS v1 and v2. Use this class when you want to connect to a robot without using the AbbController class.'''
	def __init__(self, _internal = 0):
		'''Create a new RWS client instance'''
		if(_internal == 0):
			self._instance = rws_client()
		else:
			self._instance = _internal

	def connect(self, ip: str, username: str="Default User", password: str="robotics", port: int=0, timeout: int=10000, useHttps: bool=False, version: RwsVersion=RwsVersion.OmniCore_V2_0) -> None:
		'''Connect to the robot controller RWS service

		:param ip: IP address or hostname of the robot controller
		:param username: Username for Digest Authentication (default: "Default User")
		:param password: Password for Digest Authentication (default: "robotics")
		:param port: RWS service port. If set to 0, the default port will be used (80 for HTTP, 443 for HTTPS).
		:param timeout: HTTP request timeout in milliseconds (default: 10000)
		:param useHttps: Whether to use HTTPS (default: false)
		:param version: RWS protocol version (default: OmniCore_V2_0)
		'''
		self._instance.Connect(ip, username, password, port, timeout, useHttps, rws_version(int(version)))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RwsClient):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
