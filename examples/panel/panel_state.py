"""
Panel - Controller State and Operation Mode
===========================================
Read what the control panel reports: the controller state (motors on or off),
the operation mode selector, the lock state of that selector and the collision
detection state. Everything here is read only.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot, print_title, enum_name, short_error

print_title("Panel: Controller State and Operation Mode")

robot = connect_robot()

try:
    panel = robot.rws.panel

    print("Control panel")
    print("-" * 60)

    # Motors on / motors off / emergency stop ...
    print(f"  Controller state       : {enum_name(panel.get_controller_state())}")

    # Automatic, manual reduced speed, manual full speed
    print(f"  Operation mode         : {enum_name(panel.get_operation_mode())}")

    # Speed ratio applied to the programmed speed, in percent
    print(f"  Speed ratio            : {panel.get_speed_ratio()} %")

    try:
        print(f"  Mode selector lock     : {enum_name(panel.get_operation_mode_lock_state())}")
    except Exception as e:
        print(f"  Mode selector lock     : not available ({short_error(e)})")

    try:
        print(f"  Collision detection    : {enum_name(panel.get_collision_detection_state())}")
    except Exception as e:
        print(f"  Collision detection    : not available ({short_error(e)})")

finally:
    robot.disconnect()
    print("\nDisconnected.")
