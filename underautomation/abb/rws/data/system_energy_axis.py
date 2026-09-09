from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws.Data import SystemEnergyAxis as system_energy_axis

class SystemEnergyAxis:
	'''Energy consumed by one axis of a mechanical unit during the current measurement interval. Held by .'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the SystemEnergyAxis class'''
		if(_internal == 0):
			self._instance = system_energy_axis()
		else:
			self._instance = _internal

	@property
	def number(self) -> int:
		'''Number of the axis inside its mechanical unit, starting at 1'''
		return self._instance.Number

	@number.setter
	def number(self, value: int):
		self._instance.Number = value

	@property
	def interval_energy(self) -> float | None:
		'''Energy the axis consumed during the current measurement interval, in joules, null when the controller did not report it'''
		return self._instance.IntervalEnergy

	@interval_energy.setter
	def interval_energy(self, value: float | None):
		self._instance.IntervalEnergy = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SystemEnergyAxis):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
