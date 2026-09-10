"""
RAPID - Start and Stop the Program
==================================
Reset the program pointer, start the RAPID execution, follow its state and stop it.
The robot really moves when a motion task runs, so every step is confirmed first.

The controller has to be in automatic mode with the motors on for the start to be
accepted. In manual mode it answers with an error, which the example prints.
"""
import sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot, print_title, confirm, enum_name, short_error
from underautomation.abb.rws.data.rapid_execution_cycle import RapidExecutionCycle
from underautomation.abb.rws.data.rapid_execution_state import RapidExecutionState
from underautomation.abb.rws.data.rapid_stop_mode import RapidStopMode

print_title("RAPID: Start and Stop the Program")

robot = connect_robot()

try:
    rapid = robot.rws.rapid
    panel = robot.rws.panel

    print("Before starting")
    print("-" * 60)
    print(f"  Operation mode   : {enum_name(panel.get_operation_mode())}")
    print(f"  Controller state : {enum_name(panel.get_controller_state())}")
    print(f"  Speed ratio      : {panel.get_speed_ratio()} %")

    execution = rapid.get_execution_state()
    print(f"  Execution state  : {enum_name(execution.state)}")
    print(f"  Execution cycle  : {enum_name(execution.cycle)}")

    for t in rapid.get_tasks():
        print(f"  Task {t.name:<12} {enum_name(t.execution_state)}")

    # The program pointer goes back to the entry point of every task
    print()
    if confirm("Reset the program pointer of every task?"):
        try:
            rapid.reset_program_pointer()
            print("  Program pointer reset.")
        except Exception as e:
            print(f"  The controller refused: {short_error(e)}")

    # Starting the execution makes the robot move
    print()
    if not confirm("Start the RAPID execution? THE ROBOT WILL MOVE"):
        print("  Not started.")
        raise SystemExit(0)

    try:
        rapid.start(cycle=RapidExecutionCycle.Once)
        print("  Start requested.")
    except Exception as e:
        print(f"  The controller refused to start: {short_error(e)}")
        raise SystemExit(0)

    # Follow the execution for a few seconds
    for _ in range(10):
        state = rapid.get_execution_state()
        print(f"  State: {enum_name(state.state)}, cycle: {enum_name(state.cycle)}")
        if state.state == RapidExecutionState.Stopped:
            break
        time.sleep(1)

    # Stop the execution
    print()
    if confirm("Stop the RAPID execution?"):
        rapid.stop(RapidStopMode.Stop)
        time.sleep(1)
        print(f"  State: {enum_name(rapid.get_execution_state().state)}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
