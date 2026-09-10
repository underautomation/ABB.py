"""
I/O - List Signals
==================
List every I/O signal of the controller with its value and its state, then search
signals by name, by type or by device using a search criteria.
Everything here is read only.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot, print_title, ask, enum_name
from underautomation.abb.rws.data.io_signal_search_criteria import IoSignalSearchCriteria

print_title("I/O: List Signals")

robot = connect_robot()

def print_signals(signals):
    print(f"  {'#':>4}  {'Name':<24} {'Type':<14} {'Value':>8}  {'Network/Device':<28} {'State':<12}")
    print(f"  {'-' * 4}  {'-' * 24} {'-' * 14} {'-' * 8}  {'-' * 28} {'-' * 12}")
    for i, s in enumerate(signals, 1):
        location = f"{s.network_name}/{s.device_name}"
        print(f"  {i:>4}. {s.name:<24} {enum_name(s.type):<14} {s.logical_value:>8}  {location:<28} {enum_name(s.logical_state):<12}")

try:
    io = robot.rws.io

    # Every signal declared on the controller
    signals = io.get_signals()
    print(f"Signals ({len(signals)})")
    print("-" * 100)
    print_signals(signals)

    # Search by name, the controller does the filtering
    pattern = ask("\nSearch signals whose name contains (Enter to skip)", "")
    if pattern:
        criteria = IoSignalSearchCriteria()
        criteria.name = pattern
        found = io.search_signals(criteria)
        print(f"\nSignals matching '{pattern}' ({len(found)})")
        print("-" * 100)
        print_signals(found)

finally:
    robot.disconnect()
    print("\nDisconnected.")
