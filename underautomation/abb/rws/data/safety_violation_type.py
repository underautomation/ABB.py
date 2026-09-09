from enum import IntEnum

class SafetyViolationType(IntEnum):
	'''Type of safety violation reported by the safety controller'''
	Unknown = 0 # The violation type could not be determined
	None_ = 1 # No violation
	SafeToolZone = 2 # Safe Tool Zone (stz)
	SafeAxisRange = 3 # Safe Axis Range (sar)
	SafeToolSpeed = 4 # Safe Tool Speed (sts)
	SafeAxisSpeed = 5 # Safe Axis Speed (sas)
	ToolOrientationMonitoring = 6 # Tool Orientation Monitoring (tom)
	OperationalSafetyRange = 7 # Operational Safety Range (osr)
	SafeStandstill = 8 # Safe Standstill (sst)
	ReducedToolSpeed = 9 # Reduced Tool Speed in manual mode (red_tool_speed)
	ReducedAxisSpeed = 10 # Reduced Axis Speed in manual mode (red_axis_speed)
	UnsynchronizedSpeedLimit = 11 # Reduced Axis Speed due to unsynchronized robot (unsync_speed_lim)
	EmergencyStop = 12 # Emergency stop triggered (empstop)
	Other = 13 # Internal error (other)
	Invalid = 14 # The safety controller reports an invalid violation
