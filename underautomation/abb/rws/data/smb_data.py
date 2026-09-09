from __future__ import annotations
import typing
from underautomation.abb.rws.data.smb_data_status import SmbDataStatus
from UnderAutomation.ABB.Rws.Data import SmbData as smb_data
from UnderAutomation.ABB.Rws.Data import SmbDataStatus as smb_data_status

class SmbData:
	'''Serial measurement board data of one mechanical unit, held twice: once in the controller cabinet and once in the memory of the robot itself. Returned by MotionSystemService.GetSmbData(). Comparing the cabinet properties with the robot ones tells whether the two copies still agree, which is what MotionSystemService.SetSmbData() repairs by copying one over the other.'''
	def __init__(self, _internal = 0):
		'''Initializes a new instance of the SmbData class'''
		if(_internal == 0):
			self._instance = smb_data()
		else:
			self._instance = _internal

	@property
	def cabinet_serial_number_valid(self) -> bool | None:
		'''Whether the serial number stored in the cabinet is usable, null when the controller did not report it'''
		return self._instance.CabinetSerialNumberValid

	@cabinet_serial_number_valid.setter
	def cabinet_serial_number_valid(self, value: bool | None):
		self._instance.CabinetSerialNumberValid = value

	@property
	def cabinet_serial_number_high_part(self) -> str:
		'''High part of the serial number stored in the cabinet'''
		return self._instance.CabinetSerialNumberHighPart

	@cabinet_serial_number_high_part.setter
	def cabinet_serial_number_high_part(self, value: str):
		self._instance.CabinetSerialNumberHighPart = value

	@property
	def cabinet_serial_number_low_part(self) -> str:
		'''Low part of the serial number stored in the cabinet'''
		return self._instance.CabinetSerialNumberLowPart

	@cabinet_serial_number_low_part.setter
	def cabinet_serial_number_low_part(self, value: str):
		self._instance.CabinetSerialNumberLowPart = value

	@property
	def cabinet_service_information_status(self) -> SmbDataStatus:
		'''State of the service information data stored in the cabinet'''
		return SmbDataStatus(int(self._instance.CabinetServiceInformationStatus))

	@cabinet_service_information_status.setter
	def cabinet_service_information_status(self, value: SmbDataStatus):
		self._instance.CabinetServiceInformationStatus = smb_data_status(int(value))

	@property
	def cabinet_absolute_accuracy_status(self) -> SmbDataStatus:
		'''State of the absolute accuracy data stored in the cabinet'''
		return SmbDataStatus(int(self._instance.CabinetAbsoluteAccuracyStatus))

	@cabinet_absolute_accuracy_status.setter
	def cabinet_absolute_accuracy_status(self, value: SmbDataStatus):
		self._instance.CabinetAbsoluteAccuracyStatus = smb_data_status(int(value))

	@property
	def cabinet_calibration_status(self) -> SmbDataStatus:
		'''State of the calibration data stored in the cabinet'''
		return SmbDataStatus(int(self._instance.CabinetCalibrationStatus))

	@cabinet_calibration_status.setter
	def cabinet_calibration_status(self, value: SmbDataStatus):
		self._instance.CabinetCalibrationStatus = smb_data_status(int(value))

	@property
	def cabinet_axis_calibration_status(self) -> SmbDataStatus:
		'''State of the axis calibration data stored in the cabinet'''
		return SmbDataStatus(int(self._instance.CabinetAxisCalibrationStatus))

	@cabinet_axis_calibration_status.setter
	def cabinet_axis_calibration_status(self, value: SmbDataStatus):
		self._instance.CabinetAxisCalibrationStatus = smb_data_status(int(value))

	@property
	def robot_serial_number_valid(self) -> bool | None:
		'''Whether the serial number stored in the robot is usable, null when the controller did not report it'''
		return self._instance.RobotSerialNumberValid

	@robot_serial_number_valid.setter
	def robot_serial_number_valid(self, value: bool | None):
		self._instance.RobotSerialNumberValid = value

	@property
	def robot_serial_number_high_part(self) -> str:
		'''High part of the serial number stored in the robot'''
		return self._instance.RobotSerialNumberHighPart

	@robot_serial_number_high_part.setter
	def robot_serial_number_high_part(self, value: str):
		self._instance.RobotSerialNumberHighPart = value

	@property
	def robot_serial_number_low_part(self) -> str:
		'''Low part of the serial number stored in the robot'''
		return self._instance.RobotSerialNumberLowPart

	@robot_serial_number_low_part.setter
	def robot_serial_number_low_part(self, value: str):
		self._instance.RobotSerialNumberLowPart = value

	@property
	def robot_service_information_status(self) -> SmbDataStatus:
		'''State of the service information data stored in the robot'''
		return SmbDataStatus(int(self._instance.RobotServiceInformationStatus))

	@robot_service_information_status.setter
	def robot_service_information_status(self, value: SmbDataStatus):
		self._instance.RobotServiceInformationStatus = smb_data_status(int(value))

	@property
	def robot_absolute_accuracy_status(self) -> SmbDataStatus:
		'''State of the absolute accuracy data stored in the robot'''
		return SmbDataStatus(int(self._instance.RobotAbsoluteAccuracyStatus))

	@robot_absolute_accuracy_status.setter
	def robot_absolute_accuracy_status(self, value: SmbDataStatus):
		self._instance.RobotAbsoluteAccuracyStatus = smb_data_status(int(value))

	@property
	def robot_calibration_status(self) -> SmbDataStatus:
		'''State of the calibration data stored in the robot'''
		return SmbDataStatus(int(self._instance.RobotCalibrationStatus))

	@robot_calibration_status.setter
	def robot_calibration_status(self, value: SmbDataStatus):
		self._instance.RobotCalibrationStatus = smb_data_status(int(value))

	@property
	def robot_axis_calibration_status(self) -> SmbDataStatus:
		'''State of the axis calibration data stored in the robot'''
		return SmbDataStatus(int(self._instance.RobotAxisCalibrationStatus))

	@robot_axis_calibration_status.setter
	def robot_axis_calibration_status(self, value: SmbDataStatus):
		self._instance.RobotAxisCalibrationStatus = smb_data_status(int(value))

	@property
	def drive_module(self) -> int | None:
		'''Number of the drive module the data belongs to, null when the controller did not report it'''
		return self._instance.DriveModule

	@drive_module.setter
	def drive_module(self, value: int | None):
		self._instance.DriveModule = value

	@property
	def measurement_link(self) -> int | None:
		'''Number of the measurement link the data belongs to, null when the controller did not report it'''
		return self._instance.MeasurementLink

	@measurement_link.setter
	def measurement_link(self, value: int | None):
		self._instance.MeasurementLink = value

	@property
	def measurement_board(self) -> int | None:
		'''Number of the measurement board the data belongs to, null when the controller did not report it'''
		return self._instance.MeasurementBoard

	@measurement_board.setter
	def measurement_board(self, value: int | None):
		self._instance.MeasurementBoard = value

	def __str__(self):
		return self._instance.ToString() if self._instance is not None else ""

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other) -> bool:
		if not isinstance(other, SmbData):
			NotImplemented
		return self._instance.Equals(other._instance)

	def __hash__(self) -> int:
		return self._instance.GetHashCode() if self._instance is not None else 0
