from __future__ import annotations
import typing
from datetime import datetime, timedelta
from UnderAutomation.ABB.Rws.Data import SafetyConfiguration as safety_configuration

class SafetyConfiguration:
	'''Safety supervision configuration of the controller. Returned by ControllerService.GetSafetyConfiguration().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the SafetyConfiguration class'''
		if(_internal == 0):
			self._instance = safety_configuration()
		else:
			self._instance = _internal

	@property
	def configuration_status(self) -> str:
		'''Status of the configuration, for example "SCORCH_CONFIG_LOADED". Only available when connected with version 2.'''
		return self._instance.ConfigurationStatus

	@configuration_status.setter
	def configuration_status(self, value: str):
		self._instance.ConfigurationStatus = value

	@property
	def software_major_version(self) -> int | None:
		'''Safety software major version'''
		return self._instance.SoftwareMajorVersion

	@software_major_version.setter
	def software_major_version(self, value: int | None):
		self._instance.SoftwareMajorVersion = value

	@property
	def software_minor_version(self) -> int | None:
		'''Safety software minor version'''
		return self._instance.SoftwareMinorVersion

	@software_minor_version.setter
	def software_minor_version(self, value: int | None):
		self._instance.SoftwareMinorVersion = value

	@property
	def software_revision(self) -> int | None:
		'''Safety software revision'''
		return self._instance.SoftwareRevision

	@software_revision.setter
	def software_revision(self, value: int | None):
		self._instance.SoftwareRevision = value

	@property
	def file_major_version(self) -> int | None:
		'''Configuration file major version'''
		return self._instance.FileMajorVersion

	@file_major_version.setter
	def file_major_version(self, value: int | None):
		self._instance.FileMajorVersion = value

	@property
	def file_minor_version(self) -> int | None:
		'''Configuration file minor version'''
		return self._instance.FileMinorVersion

	@file_minor_version.setter
	def file_minor_version(self, value: int | None):
		self._instance.FileMinorVersion = value

	@property
	def file_revision(self) -> int | None:
		'''Configuration file revision'''
		return self._instance.FileRevision

	@file_revision.setter
	def file_revision(self, value: int | None):
		self._instance.FileRevision = value

	@property
	def creation_date(self) -> datetime | None:
		'''Creation date of the configuration, if available'''
		return None if self._instance.CreationDate is None else datetime(1, 1, 1) + timedelta(microseconds=self._instance.CreationDate.Ticks // 10)

	@creation_date.setter
	def creation_date(self, value: datetime | None):
		self._instance.CreationDate = value

	@property
	def created_by(self) -> str:
		'''Author of the configuration'''
		return self._instance.CreatedBy

	@created_by.setter
	def created_by(self, value: str):
		self._instance.CreatedBy = value

	@property
	def name(self) -> str:
		'''Name of the configuration'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def checksum(self) -> str:
		'''Checksum of the configuration, as base64 encoded data'''
		return self._instance.Checksum

	@checksum.setter
	def checksum(self, value: str):
		self._instance.Checksum = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SafetyConfiguration):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
