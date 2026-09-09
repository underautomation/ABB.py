from __future__ import annotations
import typing
from underautomation.abb.rws.data.system_energy_state import SystemEnergyState
from underautomation.abb.rws.data.system_energy_mechanical_unit import SystemEnergyMechanicalUnit
from datetime import datetime, timedelta
from UnderAutomation.ABB.Rws.Data import SystemEnergy as system_energy
from UnderAutomation.ABB.Rws.Data import SystemEnergyState as system_energy_state

class SystemEnergy:
	'''Energy the controller has consumed, for the current measurement interval and since the last reset. Returned by SystemService.GetEnergy().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the SystemEnergy class'''
		if(_internal == 0):
			self._instance = system_energy()
		else:
			self._instance = _internal

	@property
	def is_measurement_valid(self) -> bool:
		'''Whether the reported measurement is valid. When false, every energy value of this instance is meaningless and the measurement has to be read again later.'''
		return self._instance.IsMeasurementValid

	@is_measurement_valid.setter
	def is_measurement_valid(self, value: bool):
		self._instance.IsMeasurementValid = value

	@property
	def state(self) -> SystemEnergyState:
		'''State of the energy measurement'''
		return SystemEnergyState(int(self._instance.State))

	@state.setter
	def state(self, value: SystemEnergyState):
		self._instance.State = system_energy_state(int(value))

	@property
	def change_count(self) -> int | None:
		'''Counter the controller increments every time a new measurement is available. Comparing it with the previous one tells whether the values changed without reading them all.'''
		return self._instance.ChangeCount

	@change_count.setter
	def change_count(self, value: int | None):
		self._instance.ChangeCount = value

	@property
	def time_stamp(self) -> datetime | None:
		'''Moment the measurement was taken, null when the controller did not report it'''
		return None if self._instance.TimeStamp is None else datetime(1, 1, 1) + timedelta(microseconds=self._instance.TimeStamp.Ticks // 10)

	@time_stamp.setter
	def time_stamp(self, value: datetime | None):
		self._instance.TimeStamp = value

	@property
	def reset_time(self) -> datetime | None:
		'''Moment the accumulated energy was last reset, null when the controller did not report it'''
		return None if self._instance.ResetTime is None else datetime(1, 1, 1) + timedelta(microseconds=self._instance.ResetTime.Ticks // 10)

	@reset_time.setter
	def reset_time(self, value: datetime | None):
		self._instance.ResetTime = value

	@property
	def interval_length(self) -> int | None:
		'''Length of the measurement interval in seconds, which the average power is computed from, null when the controller did not report it'''
		return self._instance.IntervalLength

	@interval_length.setter
	def interval_length(self, value: int | None):
		self._instance.IntervalLength = value

	@property
	def interval_energy(self) -> float | None:
		'''Total energy consumed during the current measurement interval, in joules, null when the controller did not report it'''
		return self._instance.IntervalEnergy

	@interval_energy.setter
	def interval_energy(self, value: float | None):
		self._instance.IntervalEnergy = value

	@property
	def accumulated_energy(self) -> float | None:
		'''Total energy consumed since the last reset, in joules, null when the controller did not report it'''
		return self._instance.AccumulatedEnergy

	@accumulated_energy.setter
	def accumulated_energy(self, value: float | None):
		self._instance.AccumulatedEnergy = value

	@property
	def mechanical_units(self) -> typing.List[SystemEnergyMechanicalUnit]:
		'''Energy consumed by each mechanical unit during the current measurement interval'''
		return [SystemEnergyMechanicalUnit(x) for x in self._instance.MechanicalUnits]

	@mechanical_units.setter
	def mechanical_units(self, value: typing.List[SystemEnergyMechanicalUnit]):
		self._instance.MechanicalUnits = [x._instance if x else None for x in value]

	@property
	def average_power(self) -> float | None:
		'''Average power consumed during the current measurement interval, in watts. Null when the interval energy or the interval length is missing, or when the interval is empty.'''
		return self._instance.AveragePower

	@property
	def mechanical_unit_count(self) -> int:
		'''Number of mechanical units the controller reported'''
		return self._instance.MechanicalUnitCount

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SystemEnergy):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
