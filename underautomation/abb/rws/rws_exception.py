from __future__ import annotations
import typing
from UnderAutomation.ABB.Rws import RwsException as rws_exception

class RwsException:
	'''Exception thrown when an RWS API request fails. Compatible with RWS v1 and v2.'''
	def __init__(self, message: str, statusCode: int, responseBody: str, _internal = 0):
		'''Creates a new RWS exception with a message, status code and response body'''
		if(_internal == 0):
			self._instance = rws_exception(message, statusCode, responseBody)
		else:
			self._instance = _internal

	@property
	def response_body(self) -> str:
		'''Raw response body from the server, if available'''
		return self._instance.ResponseBody

	@property
	def status_code(self) -> int | None:
		'''HTTP status code returned by the server'''
		return self._instance.StatusCode

	@property
	def reason_phrase(self) -> str:
		'''HTTP reason phrase returned by the server (e.g. "Forbidden", "Method Not Allowed"), if available'''
		return self._instance.ReasonPhrase

	@property
	def rws_error_code(self) -> str:
		'''ABB internal error code extracted from the RWS error payload (e.g. "-1073445865"), if present'''
		return self._instance.RwsErrorCode

	@property
	def rws_error_message(self) -> str:
		'''Human readable error text extracted from the RWS error payload, if present'''
		return self._instance.RwsErrorMessage

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RwsException):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
