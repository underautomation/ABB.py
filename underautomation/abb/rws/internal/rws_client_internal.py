from __future__ import annotations
import typing
from underautomation.abb.rws.internal.rws_client_base import RwsClientBase
from UnderAutomation.ABB.Rws.Internal import RwsClientInternal as rws_client_internal

class RwsClientInternal(RwsClientBase):
	'''Internal RWS client for use by AbbController. This class is used internally and should not be instantiated directly.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = rws_client_internal()
		else:
			self._instance = _internal

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RwsClientInternal):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
