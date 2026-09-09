from __future__ import annotations
import typing
from underautomation.abb.rws.rws_version import RwsVersion
from underautomation.abb.rws.services.file_service import FileService
from underautomation.abb.rws.services.controller_service import ControllerService
from underautomation.abb.rws.services.io_service import IoService
from underautomation.abb.rws.services.elog_service import ElogService
from underautomation.abb.rws.services.system_service import SystemService
from underautomation.abb.rws.services.panel_service import PanelService
from underautomation.abb.rws.services.motion_system_service import MotionSystemService
from underautomation.abb.rws.services.mastership_service import MastershipService
from underautomation.abb.rws.services.rapid_service import RapidService
from UnderAutomation.ABB.Rws.Internal import RwsClientBase as rws_client_base
from UnderAutomation.ABB.Rws import RwsVersion as rws_version

class RwsClientBase:
	'''Base class providing HTTP communication with ABB RWS REST API. Handles Digest Authentication, request building and XML response parsing. Supports both RWS v1 and v2.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rws_client_base()
		else:
			self._instance = _internal

	def disconnect(self) -> None:
		'''Disconnect from the robot controller'''
		self._instance.Disconnect()

	@property
	def ip(self) -> str:
		'''IP address or hostname of the robot controller'''
		return self._instance.Ip

	@property
	def port(self) -> int:
		'''Port of the RWS service'''
		return self._instance.Port

	@property
	def use_https(self) -> bool:
		'''Whether the connection uses HTTPS'''
		return self._instance.UseHttps

	@property
	def timeout(self) -> int:
		'''HTTP request timeout in milliseconds'''
		return self._instance.Timeout

	@property
	def enabled(self) -> bool:
		'''Whether the client is connected and ready'''
		return self._instance.Enabled

	@property
	def version(self) -> RwsVersion:
		'''RWS protocol version this client talks to'''
		return RwsVersion(int(self._instance.Version))

	@property
	def file(self) -> FileService:
		'''File Service'''
		return FileService(self._instance.File)

	@property
	def controller(self) -> ControllerService:
		'''Controller Service'''
		return ControllerService(self._instance.Controller)

	@property
	def io(self) -> IoService:
		'''I/O System Service'''
		return IoService(self._instance.Io)

	@property
	def elog(self) -> ElogService:
		'''Event Log Service'''
		return ElogService(self._instance.Elog)

	@property
	def system(self) -> SystemService:
		'''System Service'''
		return SystemService(self._instance.System)

	@property
	def panel(self) -> PanelService:
		'''Control Panel Service'''
		return PanelService(self._instance.Panel)

	@property
	def motion_system(self) -> MotionSystemService:
		'''Motion System Service'''
		return MotionSystemService(self._instance.MotionSystem)

	@property
	def mastership(self) -> MastershipService:
		'''Mastership Service'''
		return MastershipService(self._instance.Mastership)

	@property
	def rapid(self) -> RapidService:
		'''RAPID Service'''
		return RapidService(self._instance.Rapid)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RwsClientBase):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
