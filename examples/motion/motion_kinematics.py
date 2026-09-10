"""
Motion - Forward and Inverse Kinematics
=======================================
Ask the controller to convert between joint values and a Cartesian pose:
  - forward kinematics, joints to pose, with get_pose_from_joints()
  - inverse kinematics, pose to joints, with get_joints_from_pose()
  - every joint combination that reaches the pose, with get_all_joint_solutions()

The calculation runs on the controller, so the real kinematic model of the robot is
used. The robot does not move.

Units: these three methods work in radians for the joints and in metres for the
position, while get_rob_target() and get_joint_target() answer in degrees and in
millimetres.
"""
import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot, print_title, pick, ask_float, short_error
from underautomation.abb.common.pose import Pose
from underautomation.abb.common.joint_target import JointTarget
from underautomation.abb.common.robot_joints import RobotJoints
from underautomation.abb.common.external_joints import ExternalJoints
from underautomation.abb.common.robot_configuration import RobotConfiguration

print_title("Motion: Forward and Inverse Kinematics")

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

    # Start from where the robot stands today
    current = motion.get_joint_target(name)
    j = current.robot_axes
    print(f"\nCurrent joints of {name} (degrees)")
    print(f"  [{j.axis1:.3f}, {j.axis2:.3f}, {j.axis3:.3f}, {j.axis4:.3f}, {j.axis5:.3f}, {j.axis6:.3f}]")

    print("\nEnter the joint values in degrees, press Enter to keep the current one:")
    axes = [
        ask_float("  J1", j.axis1),
        ask_float("  J2", j.axis2),
        ask_float("  J3", j.axis3),
        ask_float("  J4", j.axis4),
        ask_float("  J5", j.axis5),
        ask_float("  J6", j.axis6),
    ]

    # These methods work in radians
    joints = JointTarget(
        RobotJoints(*[math.radians(a) for a in axes]),
        ExternalJoints(0, 0, 0, 0, 0, 0),
    )

    # The tool frame: identity means the calculation is done on the tool0 flange
    tool = Pose(0, 0, 0, 1, 0, 0, 0)

    # ─── Forward kinematics: joints to pose ──────────────────────────────────
    pose = motion.get_pose_from_joints(name, tool, joints)
    print("\nForward kinematics, joints to pose")
    print("-" * 60)
    print(f"  X = {pose.x:>12.6f} m   ({pose.x * 1000:.3f} mm)")
    print(f"  Y = {pose.y:>12.6f} m   ({pose.y * 1000:.3f} mm)")
    print(f"  Z = {pose.z:>12.6f} m   ({pose.z * 1000:.3f} mm)")
    q = pose.orientation
    print(f"  Q = [{q.q1:.6f}, {q.q2:.6f}, {q.q3:.6f}, {q.q4:.6f}]")
    c = pose.configuration
    print(f"  Configuration = [{c.quarter1}, {c.quarter4}, {c.quarter6}, {c.quarter_x}]")

    # ─── Inverse kinematics: pose back to joints ─────────────────────────────
    target = Pose(pose.x, pose.y, pose.z, q.q1, q.q2, q.q3, q.q4)
    configuration = RobotConfiguration(c.quarter1, c.quarter4, c.quarter6, c.quarter_x)
    external = ExternalJoints(0, 0, 0, 0, 0, 0)

    solution = motion.get_joints_from_pose(name, target, external, tool, joints, configuration)
    s = solution.robot_axes
    print("\nInverse kinematics, pose back to joints (degrees)")
    print("-" * 60)
    print(f"  [{math.degrees(s.axis1):.3f}, {math.degrees(s.axis2):.3f}, {math.degrees(s.axis3):.3f}, "
          f"{math.degrees(s.axis4):.3f}, {math.degrees(s.axis5):.3f}, {math.degrees(s.axis6):.3f}]")

    # ─── Every joint combination that reaches the same pose ──────────────────
    try:
        solutions = motion.get_all_joint_solutions(name, target, external, tool, configuration)
        print(f"\nAll joint solutions ({len(solutions)}), in degrees")
        print("-" * 90)
        print(f"  {'#':<4} {'J1':>10} {'J2':>10} {'J3':>10} {'J4':>10} {'J5':>10} {'J6':>10}   Configuration")
        print("-" * 90)
        for i, sol in enumerate(solutions, 1):
            a = sol.robot_axes
            sc = sol.configuration
            values = [math.degrees(v) for v in (a.axis1, a.axis2, a.axis3, a.axis4, a.axis5, a.axis6)]
            row = " ".join(f"{v:>10.3f}" for v in values)
            print(f"  {i:<4} {row}   [{sc.quarter1}, {sc.quarter4}, {sc.quarter6}, {sc.quarter_x}]")
    except Exception as e:
        print(f"\nAll joint solutions not available: {short_error(e)}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
