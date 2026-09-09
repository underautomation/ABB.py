from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import SystemProduct as system_product

class SystemProduct:
	'''One software product installed on the controller. Returned by SystemService.GetProducts().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the SystemProduct class'''
		if(_internal == 0):
			self._instance = system_product()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Name of the product, for example "RobotWare" or "RobotControl"'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def version(self) -> str:
		'''Full version of the product, build information included. Null when the controller only reports the version name.'''
		return self._instance.Version

	@version.setter
	def version(self, value: str):
		self._instance.Version = value

	@property
	def version_name(self) -> str:
		'''Human readable version of the product'''
		return self._instance.VersionName

	@version_name.setter
	def version_name(self, value: str):
		self._instance.VersionName = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SystemProduct):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
