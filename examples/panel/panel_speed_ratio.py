"""
Panel - Speed Ratio and Motors
==============================
Read the speed ratio, write a new one, then put the original value back.
The example can also switch the motors on and off.
Both operations need the mastership, which the SDK takes and releases for you when
useImplicitMastership stays at its default value.

A controller does not always accept these writes: in manual mode the FlexPendant
keeps the ownership of the panel and answers 403, which the example prints.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot, print_title, ask_int, confirm, enum_name, short_error
from underautomation.abb.rws.data.controller_state import ControllerState

print_title("Panel: Speed Ratio and Motors")

robot = connect_robot()

try:
    panel = robot.rws.panel

    # Read the current values first, so they can be restored at the end
    initial_ratio = panel.get_speed_ratio()
    print(f"Current speed ratio   : {initial_ratio} %")
    print(f"Current motor state   : {enum_name(panel.get_controller_state())}")
    print(f"Current operation mode: {enum_name(panel.get_operation_mode())}")

    # Change the speed ratio
    print()
    new_ratio = ask_int("New speed ratio in percent", 50)
    try:
        panel.set_speed_ratio(new_ratio)
        print(f"  Speed ratio is now {panel.get_speed_ratio()} %")

        # Put the original value back
        if confirm(f"\nRestore the speed ratio to {initial_ratio} %?"):
            panel.set_speed_ratio(initial_ratio)
            print(f"  Speed ratio restored to {panel.get_speed_ratio()} %")
    except Exception as e:
        print(f"  The controller refused: {short_error(e)}")

    # Switching the motors on makes the robot ready to move
    print()
    if confirm("Switch the motors on?"):
        try:
            panel.set_controller_state(ControllerState.MotorsOn)
            print(f"  Controller state: {enum_name(panel.get_controller_state())}")
        except Exception as e:
            print(f"  The controller refused: {short_error(e)}")

        if confirm("Switch the motors back off?"):
            try:
                panel.set_controller_state(ControllerState.MotorsOff)
                print(f"  Controller state: {enum_name(panel.get_controller_state())}")
            except Exception as e:
                print(f"  The controller refused: {short_error(e)}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
