from __future__ import annotations
import typing
from underautomation.abb.rws.data.elog_domain import ElogDomain
from underautomation.abb.rws.data.elog_message import ElogMessage
from underautomation.abb.rws.data.elog_message_order import ElogMessageOrder
from UnderAutomation.ABB.Rws.Services import ElogService as elog_service
from UnderAutomation.ABB.Rws.Data import ElogMessageOrder as elog_message_order

class ElogService:
	'''Event Log Service - Provides access to the messages the controller logs: the list of the log domains, the messages they hold, and the operations that clear them or dump them to a file. None of these resources is available while the controller runs in bootserver mode.'''
	def __init__(self, _internal = 0):
		if(_internal == 0):
			self._instance = elog_service()
		else:
			self._instance = _internal

	def get_domains(self, language: str=None) -> typing.List[ElogDomain]:
		'''Gets every event log domain of the controller, with the number of messages each one holds (synchronous)

		:param language: Two letter code of the language the domain names are wanted in, for example "en" or "de". Leave null to skip the names and only read the numbers and the counts.
		:returns: Event log domains, ordered as the controller reports them
		'''
		return [ElogDomain(x) for x in self._instance.GetDomains(language)]

	def get_domain(self, domain: int) -> ElogDomain:
		'''Gets the number of messages one event log domain holds and the number it can hold (synchronous)

		:param domain: Number of the domain, as reported by String)
		:returns: The domain, without its name
		'''
		return ElogDomain(self._instance.GetDomain(domain))

	def get_messages(self, domain: int, order: ElogMessageOrder=ElogMessageOrder.NewestFirst, language: str=None, maxCount: int | None=None) -> typing.List[ElogMessage]:
		return [ElogMessage(x) for x in self._instance.GetMessages(domain, elog_message_order(int(order)), language, maxCount)]

	def get_message_titles(self, domain: int, language: str, order: ElogMessageOrder=ElogMessageOrder.NewestFirst, maxCount: int | None=None) -> typing.List[ElogMessage]:
		return [ElogMessage(x) for x in self._instance.GetMessageTitles(domain, language, elog_message_order(int(order)), maxCount)]

	def get_message(self, domain: int, sequenceNumber: int, language: str=None) -> ElogMessage:
		'''Gets one message of an event log domain (synchronous)

		:param domain: Number of the domain, as reported by String)
		:param sequenceNumber: Number identifying the message inside its domain
		:param language: Two letter code of the language the message texts are wanted in, for example "en" or "de". Leave null to read only the code, the severity and the timestamp.
		:returns: The message
		'''
		return ElogMessage(self._instance.GetMessage(domain, sequenceNumber, language))

	def get_message_by_sequence_number(self, sequenceNumber: int, language: str=None) -> ElogMessage:
		'''Gets one message from its sequence number alone, without naming the domain it belongs to (synchronous)

		:param sequenceNumber: Number identifying the message
		:param language: Two letter code of the language the message texts are wanted in, for example "en" or "de". Leave null to read only the code, the severity and the timestamp.
		:returns: The message
		'''
		return ElogMessage(self._instance.GetMessageBySequenceNumber(sequenceNumber, language))

	def clear_messages(self, domain: int) -> None:
		'''Deletes every message of one event log domain (synchronous)

		:param domain: Number of the domain, as reported by String)
		'''
		self._instance.ClearMessages(domain)

	def clear_all_messages(self) -> None:
		'''Deletes every message of every event log domain (synchronous)'''
		self._instance.ClearAllMessages()

	def save_in_system_dump_format(self, path: str) -> None:
		'''Asks the controller to write the whole event log to one file on its own file system (synchronous)

		:param path: Destination file on the controller, for example "$temp/elog.txt" or "/fileservice/$home/elog.txt". Both spellings of an environment variable are accepted.
		'''
		self._instance.SaveInSystemDumpFormat(path)

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, ElogService):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
