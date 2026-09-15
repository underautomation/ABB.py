from __future__ import annotations
import typing
from underautomation.abb.rws.rws_version import RwsVersion
from underautomation.abb.connection_parameters import ConnectionParameters
from UnderAutomation.ABB.Discovery import DiscoveredController as discovered_controller
from UnderAutomation.ABB.Rws import RwsVersion as rws_version

class DiscoveredController:
	'''An ABB robot controller found on the local network. Returned by .'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = discovered_controller()
		else:
			self._instance = _internal

	def to_connection_parameters(self) -> ConnectionParameters:
		'''Build connection parameters pointing at this controller, ready for ConnectionParameters). The address, the port, the scheme and the RWS version come from the discovery. The user name and the password keep their default values, change them if the controller needs other ones.

		:returns: Connection parameters for this controller
		'''
		return ConnectionParameters(None, self._instance.ToConnectionParameters())

	@property
	def system_name(self) -> str:
		'''Name of the robot system, as configured on the controller. Null when the controller was found by testing the ports of this machine rather than by hearing it announce itself, because a port tells nothing about the name.'''
		return self._instance.SystemName

	@property
	def instance_name(self) -> str:
		'''Full name the controller publishes on the network. It contains SystemName. Null when the controller did not announce itself.'''
		return self._instance.InstanceName

	@property
	def address(self) -> str:
		'''IPv4 address of the controller'''
		return self._instance.Address

	@property
	def port(self) -> int:
		'''Port the Robot Web Services interface listens on. A virtual controller gets a new port from RobotStudio at every start, so this value is the reason to discover the controller instead of writing the port down.'''
		return self._instance.Port

	@property
	def robot_ware_version(self) -> str:
		'''RobotWare version of the controller, for example "7.21.0". Null when the controller does not publish it. Only OmniCore controllers do.'''
		return self._instance.RobotWareVersion

	@property
	def system_id(self) -> str:
		'''Unique identifier of the robot system. Null when the controller does not publish it. Only OmniCore controllers do.'''
		return self._instance.SystemId

	@property
	def pc_sdk_port(self) -> int:
		'''Port of the PC SDK interface of the controller, or 0 when the controller does not publish it. This SDK does not use that interface, the value is given for information.'''
		return self._instance.PcSdkPort

	@property
	def probable_version(self) -> RwsVersion:
		'''RWS version this controller most probably speaks. This is deduced from what the controller publishes, not from a request sent to it. Check before relying on it.'''
		return RwsVersion(int(self._instance.ProbableVersion))

	@property
	def is_version_detected(self) -> bool:
		'''True when ProbableVersion is more than a guess. It is always true for a controller found by testing the ports of this machine, because the controller was asked. For a controller heard announcing itself, it is false when the announcement did not carry what the version is deduced from, and then holds the most common value rather than a deduction.'''
		return self._instance.IsVersionDetected

	@property
	def use_https(self) -> bool:
		'''True when the controller serves Robot Web Services over HTTPS. OmniCore controllers use HTTPS, IRC5 controllers use HTTP.'''
		return self._instance.UseHttps

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, DiscoveredController):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
