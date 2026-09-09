from __future__ import annotations
import typing
from underautomation.abb.rws.data.system_energy_axis import SystemEnergyAxis
from UnderAutomation.ABB.Rws.Data import SystemEnergyMechanicalUnit as system_energy_mechanical_unit

class SystemEnergyMechanicalUnit:
	'''Energy consumed by one mechanical unit, broken down per axis. Held by .'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the SystemEnergyMechanicalUnit class'''
		if(_internal == 0):
			self._instance = system_energy_mechanical_unit()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Name of the mechanical unit, for example "ROB_1"'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def axes(self) -> typing.List[SystemEnergyAxis]:
		'''Energy consumed by each axis of the mechanical unit during the current measurement interval'''
		return [SystemEnergyAxis(x) for x in self._instance.Axes]

	@axes.setter
	def axes(self, value: typing.List[SystemEnergyAxis]):
		self._instance.Axes = [x._instance if x else None for x in value]

	@property
	def axis_count(self) -> int:
		'''Number of axes the controller reported for this mechanical unit'''
		return self._instance.AxisCount

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SystemEnergyMechanicalUnit):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
