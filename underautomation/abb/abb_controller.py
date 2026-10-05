from __future__ import annotations
import typing
from underautomation.abb.connection_parameters import ConnectionParameters
from underautomation.abb.rws.internal.rws_client_internal import RwsClientInternal
from underautomation.abb.discovery.discovered_controller import DiscoveredController
from underautomation.abb.license.license_info import LicenseInfo
from UnderAutomation.ABB import AbbController as abb_controller

class _StaticProperty:
	'''Property of the class, readable from the class or from an instance'''
	def __init__(self, fget, fset=None):
		self._fget = fget
		self._fset = fset
		self.__doc__ = fget.__doc__

	def __get__(self, obj, owner=None):
		return self._fget()

	def __set__(self, obj, value):
		if self._fset is None:
			raise AttributeError("read-only property")
		self._fset(value)

class AbbController:
	'''Main class of the SDK that represents a connection to an ABB robot controller'''
	def __init__(self, _internal = 0):
		'''Instantiate a new ABB robot controller connection'''
		if(_internal == 0):
			self._instance = abb_controller()
		else:
			self._instance = _internal

	def connect(self, ip_or_parameters: str | ConnectionParameters) -> None:
		'''Connect to robot by IP with default connection parameters
		Initialize a connection to the robot with specified parameters

		:param ip_or_parameters: IP address or hostname of the robot controller. Or: Connection parameters.
		'''
		self._instance.Connect(getattr(ip_or_parameters, '_instance', ip_or_parameters))

	def disconnect(self) -> None:
		'''Disconnect from the robot controller'''
		self._instance.Disconnect()

	@staticmethod
	def discover(timeoutMilliseconds: int=2000) -> typing.List[DiscoveredController]:
		'''Search the local network for ABB robot controllers, during the given time. Two ways of finding a controller run together: the announcements the controllers of the network send, and a test of the ports this machine serves, which is what finds the virtual controllers of RobotStudio whatever port they were given. No license is needed.

		:param timeoutMilliseconds: How long the search lasts, in milliseconds. Below 1000 ms a slow controller may be missed. Default is 2000 ms.
		:returns: The controllers that answered, or an empty array when none did
		'''
		return [DiscoveredController(x) for x in abb_controller.Discover(timeoutMilliseconds)]

	@staticmethod
	def register_license(licensee: str, key: str) -> LicenseInfo:
		'''If you have a license and a key, please call this static method to register the product and exit the trial period. You can register a product even if the trial period has ended.

		:param licensee: Your organization name
		:param key: The associated key supplied by UnderAutomation
		:returns: Information about the supplied license
		'''
		return LicenseInfo(None, None, abb_controller.RegisterLicense(licensee, key))

	@property
	def address(self) -> str:
		'''IP or robot name'''
		return self._instance.Address

	@property
	def enabled(self) -> bool:
		'''Check if the robot controller is connected'''
		return self._instance.Enabled

	@property
	def rws(self) -> RwsClientInternal:
		'''RWS client providing access to Robot Web Services API (controller, panel, IO, RAPID, file system, subscriptions)'''
		return RwsClientInternal(self._instance.Rws)

	@staticmethod
	def _get_license_info() -> LicenseInfo:
		'''Return information about your license'''
		return LicenseInfo(None, None, abb_controller.LicenseInfo)

	license_info = _StaticProperty(_get_license_info)
	del _get_license_info

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, AbbController):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
