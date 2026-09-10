"""
RAPID - Read Variables
======================
Search the RAPID symbols of a task, then read the value and the properties of the
one you pick. The value comes back the way RAPID writes it, for example [1,2,3] for
a pos or "text" for a string.
Everything here is read only.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot, print_title, ask, pick, enum_name, default_task
from underautomation.abb.rws.data.rapid_symbol_search_criteria import RapidSymbolSearchCriteria
from underautomation.abb.rws.data.rapid_symbol_search_view import RapidSymbolSearchView

print_title("RAPID: Read Variables")

robot = connect_robot()

try:
    rapid = robot.rws.rapid

    tasks = rapid.get_tasks()
    if not tasks:
        print("No RAPID task on this controller.")
        raise SystemExit(0)

    print("Pick the task to search in:")
    task = pick(tasks, "Task", lambda t: t.name)
    if task is None:
        task = default_task(tasks)
    print(f"Searching in task {task.name}")

    # A search with no criterion walks the whole system, so a block is always given
    criteria = RapidSymbolSearchCriteria()
    criteria.view = RapidSymbolSearchView.Block
    criteria.block_url = f"RAPID/{task.name}"
    criteria.recursive = True

    pattern = ask("Name pattern, a regular expression (Enter for all)", "")
    if pattern:
        criteria.name_pattern = pattern

    data_type = ask("Data type to filter on, for example num or robtarget (Enter for all)", "")
    if data_type:
        criteria.data_type = data_type

    symbols = rapid.search_symbols(criteria)
    print(f"\nSymbols found ({len(symbols)})")
    print(f"  {'Name':<28} {'Data type':<18} {'Symbol type':<16} {'Read only':<10}")
    print(f"  {'-' * 28} {'-' * 18} {'-' * 16} {'-' * 10}")
    for s in symbols[:60]:
        print(f"  {s.name:<28} {str(s.data_type):<18} {enum_name(s.symbol_type):<16} {str(s.read_only):<10}")
    if len(symbols) > 60:
        print(f"  ... and {len(symbols) - 60} more")

    if not symbols:
        raise SystemExit(0)

    print("\nPick a symbol to read:")
    selected = pick(symbols[:60], "Symbol", lambda s: f"{s.name:<28} {s.data_type}")
    if selected is None:
        print("Nothing selected.")
        raise SystemExit(0)

    # Properties come from the declaration, the value comes from the running system
    properties = rapid.get_symbol_properties(selected.symbol_url)
    print(f"\nProperties of {properties.name}")
    print("-" * 60)
    print(f"  Symbol URL   : {properties.symbol_url}")
    print(f"  Data type    : {properties.data_type}")
    print(f"  Symbol type  : {enum_name(properties.symbol_type)}")
    print(f"  Storage      : {enum_name(properties.storage)}")
    print(f"  Dimensions   : {properties.dimensions}")
    print(f"  Local        : {properties.local}")
    print(f"  Read only    : {properties.read_only}")
    print(f"  Task variable: {properties.task_variable}")

    value = rapid.get_symbol_value(selected.symbol_url)
    print(f"\nValue of {properties.name}")
    print("-" * 60)
    print(f"  {value.value}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
