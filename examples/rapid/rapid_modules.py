"""
RAPID - Modules and Source Code
===============================
List the modules loaded in a RAPID task, read the details of one of them and print
its source code. The example can also search a text inside the module.
Everything here is read only.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot, print_title, ask, pick, enum_name, short_error, default_task

print_title("RAPID: Modules and Source Code")

robot = connect_robot()

try:
    rapid = robot.rws.rapid

    tasks = rapid.get_tasks()
    if not tasks:
        print("No RAPID task on this controller.")
        raise SystemExit(0)

    print("Pick a task:")
    task = pick(tasks, "Task", lambda t: t.name)
    if task is None:
        task = default_task(tasks)

    # Modules loaded in the task
    modules = rapid.get_modules(task.name)
    print(f"\nModules of {task.name} ({len(modules)})")
    print(f"  {'Name':<28} {'Type':<16}")
    print(f"  {'-' * 28} {'-' * 16}")
    for m in modules:
        print(f"  {m.name:<28} {enum_name(m.type):<16}")

    if not modules:
        raise SystemExit(0)

    print("\nPick a module:")
    module = pick(modules, "Module", lambda m: f"{m.name:<28} {enum_name(m.type)}")
    if module is None:
        raise SystemExit(0)

    # Details of the module
    try:
        info = rapid.get_module(task.name, module.name)
        print(f"\nModule {module.name}")
        print("-" * 60)
        print(f"  {info}")
    except Exception as e:
        print(f"\nModule details not available: {short_error(e)}")

    # The change count tells whether the source changed since the last read
    try:
        print(f"  Change count: {rapid.get_module_change_count(task.name, module.name)}")
    except Exception as e:
        print(f"  Change count not available: {short_error(e)}")

    # Source code of the module
    text = rapid.get_module_text(task.name, module.name)
    print(f"\nSource of {module.name} ({text.declared_length} characters)")
    print("-" * 60)
    for i, line in enumerate(text.text.splitlines(), 1):
        print(f"  {i:>4} | {line}")

    # Search a text inside the module, the controller returns the position
    needle = ask("\nText to search in the module (Enter to skip)", "")
    if needle:
        try:
            position = rapid.search_module_text(task.name, module.name, needle)
            print(f"  Found at {position}")
        except Exception as e:
            print(f"  Not found: {short_error(e)}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
