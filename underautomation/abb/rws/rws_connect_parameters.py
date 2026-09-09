from __future__ import annotations
import typing
from underautomation.abb.rws.internal.rws_connect_parameters_base import RwsConnectParametersBase
from UnderAutomation.ABB.Rws import RwsConnectParameters as rws_connect_parameters

class RwsConnectParameters(RwsConnectParametersBase):
	'''Connection parameters for ABB Robot Web Services (RWS). Supports both RWS v1 and v2.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rws_connect_parameters()
		else:
			self._instance = _internal

	@property
	def enable(self) -> bool:
		'''Enable or disable the RWS client connection'''
		return self._instance.Enable

	@enable.setter
	def enable(self, value: bool):
		self._instance.Enable = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RwsConnectParameters):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0

# Default RWS port (80 for HTTP, 443 for HTTPS)
RwsConnectParameters.DEFAULT_PORT = rws_connect_parameters.DEFAULT_PORT

# Default username for Digest Authentication
RwsConnectParameters.DEFAULT_USERNAME = rws_connect_parameters.DEFAULT_USERNAME

# Default password for Digest Authentication
RwsConnectParameters.DEFAULT_PASSWORD = rws_connect_parameters.DEFAULT_PASSWORD

# Default timeout in milliseconds
RwsConnectParameters.DEFAULT_TIMEOUT = rws_connect_parameters.DEFAULT_TIMEOUT
