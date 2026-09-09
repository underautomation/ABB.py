from __future__ import annotations
import typing
from underautomation.abb.rws.data.rapid_joint_state import RapidJointState
from UnderAutomation.ABB.Rws.Data import RapidExternalJointStates as rapid_external_joint_states
from UnderAutomation.ABB.Rws.Data import RapidJointState as rapid_joint_state

class RapidExternalJointStates:
	'''What each of the six external joints of a task is doing, which says how to read the corresponding value of an external axis. Returned by RapidService.GetExternalJointStates(). A joint reported as carries no meaningful position.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the RapidExternalJointStates class'''
		if(_internal == 0):
			self._instance = rapid_external_joint_states()
		else:
			self._instance = _internal

	@property
	def joint1(self) -> RapidJointState:
		'''State of the first external joint'''
		return RapidJointState(int(self._instance.Joint1))

	@joint1.setter
	def joint1(self, value: RapidJointState):
		self._instance.Joint1 = rapid_joint_state(int(value))

	@property
	def joint2(self) -> RapidJointState:
		'''State of the second external joint'''
		return RapidJointState(int(self._instance.Joint2))

	@joint2.setter
	def joint2(self, value: RapidJointState):
		self._instance.Joint2 = rapid_joint_state(int(value))

	@property
	def joint3(self) -> RapidJointState:
		'''State of the third external joint'''
		return RapidJointState(int(self._instance.Joint3))

	@joint3.setter
	def joint3(self, value: RapidJointState):
		self._instance.Joint3 = rapid_joint_state(int(value))

	@property
	def joint4(self) -> RapidJointState:
		'''State of the fourth external joint'''
		return RapidJointState(int(self._instance.Joint4))

	@joint4.setter
	def joint4(self, value: RapidJointState):
		self._instance.Joint4 = rapid_joint_state(int(value))

	@property
	def joint5(self) -> RapidJointState:
		'''State of the fifth external joint'''
		return RapidJointState(int(self._instance.Joint5))

	@joint5.setter
	def joint5(self, value: RapidJointState):
		self._instance.Joint5 = rapid_joint_state(int(value))

	@property
	def joint6(self) -> RapidJointState:
		'''State of the sixth external joint'''
		return RapidJointState(int(self._instance.Joint6))

	@joint6.setter
	def joint6(self, value: RapidJointState):
		self._instance.Joint6 = rapid_joint_state(int(value))

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, RapidExternalJointStates):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
