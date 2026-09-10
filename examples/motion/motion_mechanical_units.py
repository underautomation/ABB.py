"""
Motion - Mechanical Units
=========================
List the mechanical units of the motion system, read the details of one of them,
its axes and its base frame, plus the global state of the motion system.
Everything here is read only.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot, print_title, pick, enum_name, short_error

print_title("Motion: Mechanical Units")

robot = connect_robot()

try:
    motion = robot.rws.motion_system

    # Global state of the motion system
    info = motion.get_info()
    print("Motion system")
    print("-" * 60)
    print(f"  {info}")
    print(f"  Error state             : {enum_name(motion.get_error_state())}")
    print(f"  Non motion execution    : {motion.get_non_motion_execution_mode()}")

    # Mechanical units: the robot arm, the track, the positioners
    units = motion.get_mechanical_units()
    print(f"\nMechanical units ({len(units)})")
    print(f"  {'Name':<20} {'Mode':<14} {'Drive module':<16} {'Activation allowed':<20}")
    print(f"  {'-' * 20} {'-' * 14} {'-' * 16} {'-' * 20}")
    for u in units:
        print(f"  {u.name:<20} {enum_name(u.mode):<14} {str(u.drive_module):<16} {str(u.activation_allowed):<20}")

    if not units:
        raise SystemExit(0)

    print("\nPick a mechanical unit:")
    selected = pick(units, "Mechanical unit", lambda u: u.name)
    if selected is None:
        selected = units[0]

    name = selected.name

    # Everything the controller says about this unit
    unit = motion.get_mechanical_unit(name)
    print(f"\nMechanical unit {name}")
    print("-" * 60)
    print(f"  Type              : {enum_name(unit.type)}")
    print(f"  Status            : {enum_name(unit.status)}")
    print(f"  Mode              : {enum_name(unit.mode)}")
    print(f"  Jog mode          : {enum_name(unit.jog_mode)}")
    print(f"  Task              : {unit.task_name}")
    print(f"  Coordinate system : {enum_name(unit.coordinate_system)}")
    print(f"  Tool              : {unit.tool_name}")
    print(f"  Work object       : {unit.work_object_name}")
    print(f"  Payload           : {unit.payload_name}")
    print(f"  Total payload     : {unit.total_payload_name}")
    print(f"  Axes              : {unit.axes} of {unit.total_axes}")
    print(f"  Integrated unit   : {enum_name(unit.is_integrated_unit)} / has one: {enum_name(unit.has_integrated_unit)}")

    # Each axis of the unit
    axis_count = motion.get_axis_count(name)
    print(f"\nAxes ({axis_count})")
    print("-" * 60)
    for axis in range(1, axis_count + 1):
        try:
            print(f"  Axis {axis}: {motion.get_axis(name, axis)}")
        except Exception as e:
            print(f"  Axis {axis}: not available ({short_error(e)})")

    # Base frame of the unit, expressed in the world coordinate system
    try:
        base = motion.get_base_frame(name)
        print(f"\nBase frame: {base}")
    except Exception as e:
        print(f"\nBase frame not available: {short_error(e)}")

    # Calibration of the unit
    try:
        print(f"Calibration: {motion.get_calibration_info(name)}")
    except Exception as e:
        print(f"Calibration not available: {short_error(e)}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
