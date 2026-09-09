from __future__ import annotations
import typing
from underautomation.abb.connection_parameters import ConnectionParameters
from underautomation.abb.rws.internal.rws_client_internal import RwsClientInternal
from underautomation.abb.license.license_info import LicenseInfo
from UnderAutomation.ABB import AbbController as abb_controller

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

		:param ip_or_parameters: IP address or hostname of the robot controller — or — Connection parameters
		'''
		self._instance.Connect(getattr(ip_or_parameters, '_instance', ip_or_parameters))

	def disconnect(self) -> None:
		'''Disconnect from the robot controller'''
		self._instance.Disconnect()

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

	@property
	def license_info(self) -> LicenseInfo:
		'''Return information about your license'''
		return LicenseInfo(None, None, self._instance.LicenseInfo)

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
