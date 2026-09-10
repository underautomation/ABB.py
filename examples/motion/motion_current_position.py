"""
Motion - Current Position
=========================
Read where the robot stands right now: its Cartesian position (robtarget) in the
coordinate system you choose, its joint values (jointtarget) and the physical values
read on the axes. Everything here is read only.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot, print_title, pick, enum_name, short_error, default_task
from underautomation.abb.rws.data.coordinate_system import CoordinateSystem

print_title("Motion: Current Position")

def print_rob_target(target):
    print(f"  X = {target.x:>12.3f} mm")
    print(f"  Y = {target.y:>12.3f} mm")
    print(f"  Z = {target.z:>12.3f} mm")
    q = target.orientation
    print(f"  Q = [{q.q1:.6f}, {q.q2:.6f}, {q.q3:.6f}, {q.q4:.6f}]")
    c = target.configuration
    print(f"  Configuration = [{c.quarter1}, {c.quarter4}, {c.quarter6}, {c.quarter_x}]")
    e = target.external_axes
    print(f"  External axes = [{e.axis_a}, {e.axis_b}, {e.axis_c}, {e.axis_d}, {e.axis_e}, {e.axis_f}]")

def print_joint_target(target):
    j = target.robot_axes
    print(f"  J1 = {j.axis1:>10.3f} deg")
    print(f"  J2 = {j.axis2:>10.3f} deg")
    print(f"  J3 = {j.axis3:>10.3f} deg")
    print(f"  J4 = {j.axis4:>10.3f} deg")
    print(f"  J5 = {j.axis5:>10.3f} deg")
    print(f"  J6 = {j.axis6:>10.3f} deg")
    e = target.external_axes
    print(f"  External axes = [{e.axis_a}, {e.axis_b}, {e.axis_c}, {e.axis_d}, {e.axis_e}, {e.axis_f}]")

robot = connect_robot()

try:
    motion = robot.rws.motion_system

    units = motion.get_mechanical_units()
    if not units:
        print("No mechanical unit on this controller.")
        raise SystemExit(0)

    print("Pick a mechanical unit:")
    selected = pick(units, "Mechanical unit", lambda u: u.name)
    if selected is None:
        selected = units[0]
    name = selected.name
    print(f"Reading the position of {name}")

    # The same position expressed in the four coordinate systems
    for system in (CoordinateSystem.World, CoordinateSystem.Base, CoordinateSystem.Tool, CoordinateSystem.WorkObject):
        try:
            target = motion.get_rob_target(name, system)
            print(f"\nrobtarget in {enum_name(system)}")
            print("-" * 60)
            print_rob_target(target)
        except Exception as e:
            print(f"\nrobtarget in {enum_name(system)}: not available ({short_error(e)})")

    # Joint values of the unit
    try:
        joints = motion.get_joint_target(name)
        print("\njointtarget")
        print("-" * 60)
        print_joint_target(joints)
    except Exception as e:
        print(f"\njointtarget: not available ({short_error(e)})")

    # Physical values read on the motors, before the calibration offsets
    try:
        physical = motion.get_physical_joints(name)
        print("\nPhysical joints")
        print("-" * 60)
        print(f"  [{physical.axis1:.3f}, {physical.axis2:.3f}, {physical.axis3:.3f}, "
              f"{physical.axis4:.3f}, {physical.axis5:.3f}, {physical.axis6:.3f}]")
    except Exception as e:
        print(f"\nPhysical joints: not available ({short_error(e)})")

    # The RAPID service gives the position seen by a task, with its tool and work object
    try:
        tasks = robot.rws.rapid.get_tasks()
        task = default_task(tasks)
        if task is not None:
            task_name = task.name
            print(f"\nPosition seen by the RAPID task {task_name}")
            print("-" * 60)
            print_rob_target(robot.rws.rapid.get_rob_target(task_name))
    except Exception as e:
        print(f"  Not available: {short_error(e)}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
