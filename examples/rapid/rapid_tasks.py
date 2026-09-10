"""
RAPID - Tasks and Execution State
=================================
List the RAPID tasks of the controller, read the details of one of them, the program
it holds and the position of its program pointer, then the global execution state.
Everything here is read only.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot, print_title, pick, enum_name, short_error

print_title("RAPID: Tasks and Execution State")

robot = connect_robot()

try:
    rapid = robot.rws.rapid

    # Global execution state of the controller
    execution = rapid.get_execution_state()
    print("Execution")
    print("-" * 60)
    print(f"  State : {enum_name(execution.state)}")
    print(f"  Cycle : {enum_name(execution.cycle)}")

    # Every RAPID task
    tasks = rapid.get_tasks()
    print(f"\nTasks ({len(tasks)})")
    print(f"  {'Name':<16} {'Type':<14} {'Task state':<14} {'Execution':<14} {'Active':<8} {'Motion':<8}")
    print(f"  {'-' * 16} {'-' * 14} {'-' * 14} {'-' * 14} {'-' * 8} {'-' * 8}")
    for t in tasks:
        print(f"  {t.name:<16} {enum_name(t.type):<14} {enum_name(t.task_state):<14} {enum_name(t.execution_state):<14} {str(t.active):<8} {str(t.motion_task):<8}")

    if not tasks:
        print("No task on this controller.")
        raise SystemExit(0)

    print("\nPick a task to inspect:")
    selected = pick(tasks, "Task", lambda t: t.name)
    if selected is None:
        print("Nothing selected.")
        raise SystemExit(0)

    task_name = selected.name

    # Details of the task
    info = rapid.get_task(task_name)
    print(f"\nTask {task_name}")
    print("-" * 60)
    print(f"  Task id                : {info.task_id}")
    print(f"  Trust level            : {enum_name(info.trust)}")
    print(f"  Execution level        : {enum_name(info.execution_level)}")
    print(f"  Execution mode         : {enum_name(info.execution_mode)}")
    print(f"  Execution type         : {enum_name(info.execution_type)}")
    print(f"  Execution cycle        : {enum_name(info.execution_cycle)}")
    print(f"  Production entry point : {info.production_entry_point}")
    print(f"  In foreground          : {info.task_in_foreground}")

    # Program loaded in the task
    try:
        program = rapid.get_program(task_name)
        print(f"\n  Program: {program}")
    except Exception as e:
        print(f"\n  No program loaded: {short_error(e)}")

    # Program pointer and motion pointer
    try:
        pointers = rapid.get_pointers(task_name)
        print(f"  Pointers: {pointers}")
    except Exception as e:
        print(f"  Pointers not available: {short_error(e)}")

    # Mechanical units driven by this task
    try:
        units = rapid.get_mechanical_units(task_name)
        print(f"\n  Mechanical units ({len(units)})")
        for u in units:
            print(f"    {u}")
    except Exception as e:
        print(f"  Mechanical units not available: {short_error(e)}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
