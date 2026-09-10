"""
RAPID - Write a Variable
========================
Read a RAPID variable, write a new value on it, then put the original value back.
Writing a symbol needs the edit mastership, which the example takes and releases
explicitly so the whole sequence is visible.

The value is a string written the way RAPID writes it: 42 for a num, "text" for a
string, [1,2,3] for a pos, TRUE or FALSE for a bool.

Holding the mastership is not always enough: in manual mode the FlexPendant keeps the
ownership and the controller answers 403, which the example prints.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot, print_title, ask, pick, confirm, default_task, enum_name, short_error
from underautomation.abb.rws.data.rapid_symbol_search_criteria import RapidSymbolSearchCriteria
from underautomation.abb.rws.data.rapid_symbol_search_view import RapidSymbolSearchView
from underautomation.abb.rws.data.mastership_domain import MastershipDomain

print_title("RAPID: Write a Variable")

robot = connect_robot()

try:
    rapid = robot.rws.rapid

    tasks = rapid.get_tasks()
    if not tasks:
        print("No RAPID task on this controller.")
        raise SystemExit(0)

    task = default_task(tasks)
    print(f"Searching writable variables in task {task.name}")

    # Look for the variables and persistents of the task
    criteria = RapidSymbolSearchCriteria()
    criteria.view = RapidSymbolSearchView.Block
    criteria.block_url = f"RAPID/{task.name}"
    criteria.recursive = True

    data_type = ask("Data type to filter on, for example num (Enter for all)", "")
    if data_type:
        criteria.data_type = data_type

    symbols = [s for s in rapid.search_symbols(criteria) if not s.read_only]
    if not symbols:
        print("No writable symbol found with these criteria.")
        raise SystemExit(0)

    print(f"\nWritable symbols ({len(symbols)}):")
    selected = pick(symbols[:40], "Symbol", lambda s: f"{s.name:<28} {s.data_type}")
    if selected is None:
        print("Nothing selected.")
        raise SystemExit(0)

    url = selected.symbol_url

    # Read the value first, so it can be restored
    initial = rapid.get_symbol_value(url).value
    print(f"\nCurrent value of {selected.name} ({selected.data_type}): {initial}")

    new_value = ask("New value, written the way RAPID writes it", initial)

    # The edit mastership is needed to write a symbol
    mastership = robot.rws.mastership

    print("\nRequesting the Edit mastership...")
    mastership.request(MastershipDomain.Edit)
    try:
        info = mastership.get_info(MastershipDomain.Edit)
        print(f"  Mastership held by me: {info.held_by_me} (holder: {enum_name(info.holder)})")

        try:
            rapid.set_symbol_value(url, new_value)
            print(f"  New value: {rapid.get_symbol_value(url).value}")

            if confirm(f"\nRestore the original value {initial}?"):
                rapid.set_symbol_value(url, initial)
                print(f"  Restored: {rapid.get_symbol_value(url).value}")
        except Exception as e:
            print(f"  The controller refused the write: {short_error(e)}")
    finally:
        mastership.release(MastershipDomain.Edit)
        print("Edit mastership released.")

finally:
    robot.disconnect()
    print("\nDisconnected.")
