from __future__ import annotations
import typing
from underautomation.abb.rws.data.mastership_domain import MastershipDomain
from underautomation.abb.rws.data.mastership_holder import MastershipHolder
from UnderAutomation.ABB.Rws.Data import MastershipInfo as mastership_info
from UnderAutomation.ABB.Rws.Data import MastershipDomain as mastership_domain
from UnderAutomation.ABB.Rws.Data import MastershipHolder as mastership_holder

class MastershipInfo:
	'''State of the mastership of one domain: who holds it, and whether this connection is the holder. Returned by MastershipService.GetInfo().'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the MastershipInfo class'''
		if(_internal == 0):
			self._instance = mastership_info()
		else:
			self._instance = _internal

	@property
	def domain(self) -> MastershipDomain:
		'''Domain this state describes'''
		return MastershipDomain(int(self._instance.Domain))

	@domain.setter
	def domain(self, value: MastershipDomain):
		self._instance.Domain = mastership_domain(int(value))

	@property
	def holder(self) -> MastershipHolder:
		'''Who holds the mastership of the domain'''
		return MastershipHolder(int(self._instance.Holder))

	@holder.setter
	def holder(self, value: MastershipHolder):
		self._instance.Holder = mastership_holder(int(value))

	@property
	def held_by_me(self) -> bool:
		'''Whether this connection is the one holding the mastership, and is therefore allowed to write in the domain'''
		return self._instance.HeldByMe

	@held_by_me.setter
	def held_by_me(self, value: bool):
		self._instance.HeldByMe = value

	@property
	def user_id(self) -> int | None:
		'''Identifier the controller gave the user holding the mastership, null when nobody holds it'''
		return self._instance.UserId

	@user_id.setter
	def user_id(self, value: int | None):
		self._instance.UserId = value

	@property
	def location(self) -> str:
		'''Where the holder is, as it declared itself, null when nobody holds the mastership'''
		return self._instance.Location

	@location.setter
	def location(self, value: str):
		self._instance.Location = value

	@property
	def alias(self) -> str:
		'''Alternate name of the location of the holder, null when nobody holds the mastership'''
		return self._instance.Alias

	@alias.setter
	def alias(self, value: str):
		self._instance.Alias = value

	@property
	def application(self) -> str:
		'''Name of the application holding the mastership, null when nobody holds it'''
		return self._instance.Application

	@application.setter
	def application(self, value: str):
		self._instance.Application = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, MastershipInfo):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
