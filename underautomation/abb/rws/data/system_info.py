from __future__ import annotations
import typing
from datetime import datetime, timedelta
from UnderAutomation.ABB.Rws.Data import SystemInfo as system_info

class SystemInfo:
	'''Identity and software version of the system running on the controller. Returned by SystemService.GetInfo().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the SystemInfo class'''
		if(_internal == 0):
			self._instance = system_info()
		else:
			self._instance = _internal

	@property
	def name(self) -> str:
		'''Name of the system installed on the controller'''
		return self._instance.Name

	@name.setter
	def name(self, value: str):
		self._instance.Name = value

	@property
	def version(self) -> str:
		'''Version of the robot software the system runs'''
		return self._instance.Version

	@version.setter
	def version(self, value: str):
		self._instance.Version = value

	@property
	def version_name(self) -> str:
		'''Human readable version of the robot software the system runs'''
		return self._instance.VersionName

	@version_name.setter
	def version_name(self, value: str):
		self._instance.VersionName = value

	@property
	def distribution_version(self) -> str:
		'''Version of the software distribution the system was installed from. Null when the controller does not report it.'''
		return self._instance.DistributionVersion

	@distribution_version.setter
	def distribution_version(self, value: str):
		self._instance.DistributionVersion = value

	@property
	def system_id(self) -> str:
		'''Unique identifier of the system'''
		return self._instance.SystemId

	@system_id.setter
	def system_id(self, value: str):
		self._instance.SystemId = value

	@property
	def start_time(self) -> datetime | None:
		'''Moment the system was last started, null when the controller did not report it'''
		return None if self._instance.StartTime is None else datetime(1, 1, 1) + timedelta(microseconds=self._instance.StartTime.Ticks // 10)

	@start_time.setter
	def start_time(self, value: datetime | None):
		self._instance.StartTime = value

	@property
	def major(self) -> int | None:
		'''Major number of the version, null when the controller did not report it'''
		return self._instance.Major

	@major.setter
	def major(self, value: int | None):
		self._instance.Major = value

	@property
	def minor(self) -> int | None:
		'''Minor number of the version, null when the controller did not report it'''
		return self._instance.Minor

	@minor.setter
	def minor(self, value: int | None):
		self._instance.Minor = value

	@property
	def build(self) -> int | None:
		'''Build number of the version, null when the controller did not report it'''
		return self._instance.Build

	@build.setter
	def build(self, value: int | None):
		self._instance.Build = value

	@property
	def revision(self) -> int | None:
		'''Revision number of the version, null when the controller did not report it'''
		return self._instance.Revision

	@revision.setter
	def revision(self, value: int | None):
		self._instance.Revision = value

	@property
	def sub_revision(self) -> int | None:
		'''Sub revision number of the version, null when the controller did not report it'''
		return self._instance.SubRevision

	@sub_revision.setter
	def sub_revision(self, value: int | None):
		self._instance.SubRevision = value

	@property
	def build_tag(self) -> str:
		'''Free text describing the build the system was produced by, null when the controller did not report it'''
		return self._instance.BuildTag

	@build_tag.setter
	def build_tag(self, value: str):
		self._instance.BuildTag = value

	@property
	def api_compatibility_revision(self) -> int | None:
		'''Revision of the programming interface the system is compatible with, null when the controller did not report it'''
		return self._instance.ApiCompatibilityRevision

	@api_compatibility_revision.setter
	def api_compatibility_revision(self, value: int | None):
		self._instance.ApiCompatibilityRevision = value

	@property
	def title(self) -> str:
		'''Title of the system, null when the controller did not report it'''
		return self._instance.Title

	@title.setter
	def title(self, value: str):
		self._instance.Title = value

	@property
	def type(self) -> str:
		'''Type of the system, null when the controller did not report it'''
		return self._instance.Type

	@type.setter
	def type(self, value: str):
		self._instance.Type = value

	@property
	def description(self) -> str:
		'''Description of the system, null when the controller did not report it'''
		return self._instance.Description

	@description.setter
	def description(self, value: str):
		self._instance.Description = value

	@property
	def date(self) -> datetime | None:
		'''Date the system was produced, null when the controller did not report it'''
		return None if self._instance.Date is None else datetime(1, 1, 1) + timedelta(microseconds=self._instance.Date.Ticks // 10)

	@date.setter
	def date(self, value: datetime | None):
		self._instance.Date = value

	@property
	def configuration_timestamp(self) -> str:
		'''Timestamp of the configuration the system was built with, as the controller spells it. Null when the controller did not report it, which is the usual case on a virtual controller.'''
		return self._instance.ConfigurationTimestamp

	@configuration_timestamp.setter
	def configuration_timestamp(self, value: str):
		self._instance.ConfigurationTimestamp = value

	@property
	def options(self) -> typing.List[str]:
		'''Options installed on the system, in the order the controller reports them'''
		return self._instance.Options

	@options.setter
	def options(self, value: typing.List[str]):
		self._instance.Options = value

	@property
	def option_count(self) -> int:
		'''Number of options installed on the system'''
		return self._instance.OptionCount

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SystemInfo):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
