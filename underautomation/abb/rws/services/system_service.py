from __future__ import annotations
import typing
from underautomation.abb.rws.data.system_info import SystemInfo
from underautomation.abb.rws.data.system_product import SystemProduct
from underautomation.abb.rws.data.system_energy import SystemEnergy
from UnderAutomation.ABB.Rws.Services import SystemService as system_service

class SystemService:
	'''System Service - Describes the system installed on the controller: its name and software version, the options and the products it was built with, the type of robot it drives, its license, and the energy it consumes. None of these resources is available while the controller runs in bootserver mode.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = system_service()
		else:
			self._instance = _internal

	def get_info(self) -> SystemInfo:
		'''Gets the name, the software version and the installed options of the system (synchronous)

		:returns: Description of the system running on the controller
		'''
		return SystemInfo(self._instance.GetInfo())

	def get_options(self) -> typing.List[str]:
		'''Gets the options installed on the system (synchronous)

		:returns: Names of the options, in the order the controller reports them, empty when there is none
		'''
		return self._instance.GetOptions()

	def get_license(self) -> str:
		'''Gets the license the robot software runs under (synchronous)

		:returns: Name of the license, for example "VIRTUAL_USE" on a simulated controller
		'''
		return self._instance.GetLicense()

	def get_robot_types(self) -> typing.List[str]:
		'''Gets the type of every robot the controller drives (synchronous)

		:returns: Robot types, for example "IRB 120-3/0.6", empty when the controller drives no standard robot
		'''
		return self._instance.GetRobotTypes()

	def get_products(self, name: str=None) -> typing.List[SystemProduct]:
		'''Gets the software products installed on the controller, with their versions (synchronous)

		:param name: Name of a single product to report, null to report every installed product
		:returns: Installed products, empty when the controller reports none
		'''
		return [SystemProduct(x) for x in self._instance.GetProducts(name)]

	def get_energy(self) -> SystemEnergy:
		'''Gets the energy the controller consumed, for the current interval and since the last reset (synchronous)

		:returns: Energy measurement, broken down per mechanical unit and per axis
		'''
		return SystemEnergy(self._instance.GetEnergy())

	def get_energy_change_count(self) -> int | None:
		'''Gets the counter the controller increments each time a new energy measurement is available (synchronous)

		:returns: Current value of the counter, null when the controller did not report it
		'''
		return self._instance.GetEnergyChangeCount()

	def reset_accumulated_energy(self) -> None:
		'''Sets the accumulated energy counter of the controller back to zero (synchronous)'''
		self._instance.ResetAccumulatedEnergy()

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SystemService):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
