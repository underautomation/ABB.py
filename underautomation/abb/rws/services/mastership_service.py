from __future__ import annotations
import typing
from underautomation.abb.rws.data.mastership_domain import MastershipDomain
from underautomation.abb.rws.data.mastership_info import MastershipInfo
from UnderAutomation.ABB.Rws.Services import MastershipService as mastership_service
from UnderAutomation.ABB.Rws.Data import MastershipDomain as mastership_domain

class MastershipService:
	'''Mastership Service - Takes and gives back the exclusive right to change a domain of the controller. Most write operations are refused unless the client holds the mastership of the domain they belong to: moving a mechanical unit needs , changing the system parameters or the RAPID programs needs .Only one client holds a domain at a time, and it keeps it until is called or the connection ends. Take it as late and give it back as early as possible: while it is held, the operator of the robot cannot change the same domain from the teach pendant.Mastership belongs to the connection that took it, so every call made through the same client is the holder. None of these resources is available while the controller runs in bootserver mode.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = mastership_service()
		else:
			self._instance = _internal

	def get_domains(self) -> typing.List[MastershipDomain]:
		'''Gets the domains the connected controller can give the mastership of (synchronous)

		:returns: Domains the controller exposes, which are not the same on a connection established with version 1 and on one established with version 2. Edit can be asked for on either, even when it is not listed here: it then stands for the domains covering the same ground.
		'''
		return [MastershipDomain(int(x)) for x in self._instance.GetDomains()]

	def get_info(self, domain: MastershipDomain) -> MastershipInfo:
		'''Gets who holds the mastership of one domain (synchronous)

		:param domain: Domain to read the state of
		:returns: State of the domain, with HeldByMe telling whether this connection is allowed to write in it
		'''
		return MastershipInfo(self._instance.GetInfo(mastership_domain(int(domain))))

	def request(self, domain: MastershipDomain) -> None:
		'''Takes the mastership of one domain (synchronous)

		:param domain: Domain to take
		'''
		self._instance.Request(mastership_domain(int(domain)))

	def release(self, domain: MastershipDomain) -> None:
		'''Gives back the mastership of one domain (synchronous)

		:param domain: Domain to give back
		'''
		self._instance.Release(mastership_domain(int(domain)))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MastershipService):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
