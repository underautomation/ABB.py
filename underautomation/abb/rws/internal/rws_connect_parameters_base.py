from __future__ import annotations
import typing
from underautomation.abb.rws.rws_version import RwsVersion
from UnderAutomation.ABB.Rws.Internal import RwsConnectParametersBase as rws_connect_parameters_base
from UnderAutomation.ABB.Rws import RwsVersion as rws_version

class RwsConnectParametersBase:
	'''Base class for connection parameters. Contains core properties needed for RWS connection.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rws_connect_parameters_base()
		else:
			self._instance = _internal

	@property
	def ip(self) -> str:
		'''IP address or hostname of the robot controller'''
		return self._instance.Ip

	@ip.setter
	def ip(self, value: str):
		self._instance.Ip = value

	@property
	def port(self) -> int:
		'''RWS service port (if set to 0, the SDK will use 80 for HTTP, 443 for HTTPS)'''
		return self._instance.Port

	@port.setter
	def port(self, value: int):
		self._instance.Port = value

	@property
	def username(self) -> str:
		'''Username for Digest Authentication (Default is "Default User")'''
		return self._instance.Username

	@username.setter
	def username(self, value: str):
		self._instance.Username = value

	@property
	def password(self) -> str:
		'''Password for Digest Authentication (Default is "robotics")'''
		return self._instance.Password

	@password.setter
	def password(self, value: str):
		self._instance.Password = value

	@property
	def timeout(self) -> int:
		'''HTTP request timeout in milliseconds (default: 1000ms)'''
		return self._instance.Timeout

	@timeout.setter
	def timeout(self, value: int):
		self._instance.Timeout = value

	@property
	def use_https(self) -> bool:
		'''Whether to use HTTPS instead of HTTP (default: false)'''
		return self._instance.UseHttps

	@use_https.setter
	def use_https(self, value: bool):
		self._instance.UseHttps = value

	@property
	def version(self) -> RwsVersion:
		'''RWS protocol version to use. If not specified, OmniCore_V2_0 (RWS 2.0) is used. RWS 2.0 is available in RobotWare >= 7, which ships the new OmniCore controller generation. For older RobotWare versions running on IRC5 controllers, use (RWS 1.0).'''
		return RwsVersion(int(self._instance.Version))

	@version.setter
	def version(self, value: RwsVersion):
		self._instance.Version = rws_version(int(value))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RwsConnectParametersBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
