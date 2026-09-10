"""
I/O - Read One Signal
=====================
Pick a signal from the list and read everything the controller says about it:
its logical and physical value, its quality, its timestamps and its configuration.
Everything here is read only.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot, print_title, pick, enum_name, short_error

print_title("I/O: Read One Signal")

robot = connect_robot()

try:
    io = robot.rws.io

    signals = io.get_signals()
    if not signals:
        print("No signal found on this controller.")
        raise SystemExit(0)

    print(f"Pick a signal among the {len(signals)} declared on the controller:")
    selected = pick(signals, "Signal", lambda s: f"{s.name:<24} {s.network_name}/{s.device_name}")
    if selected is None:
        print("Nothing selected.")
        raise SystemExit(0)

    # Read the signal again by its full location, the values are refreshed
    signal = io.get_signal(selected.network_name, selected.device_name, selected.name)

    print(f"\nSignal {signal.name}")
    print("-" * 60)
    print(f"  Path              : {signal.path}")
    print(f"  Network / Device  : {signal.network_name} / {signal.device_name}")
    print(f"  Type              : {enum_name(signal.type)}")
    print(f"  Category          : {signal.category}")
    print(f"  Logical value     : {signal.logical_value}")
    print(f"  Logical state     : {enum_name(signal.logical_state)}")
    print(f"  Physical value    : {signal.physical_value}")
    print(f"  Physical state    : {enum_name(signal.physical_state)}")
    print(f"  Quality           : {enum_name(signal.quality)}")
    print(f"  Write access level: {enum_name(signal.write_access_level)}")
    print(f"  Logical time      : {signal.logical_time_seconds}.{signal.logical_time_microseconds:06d}")
    print(f"  Physical time     : {signal.physical_time_seconds}.{signal.physical_time_microseconds:06d}")

    # The configuration comes from the system parameters, not from the live value
    try:
        config = io.get_signal_configuration(signal.network_name, signal.device_name, signal.name)
        print("\nConfiguration")
        print("-" * 60)
        print(f"  {config}")
    except Exception as e:
        print(f"\nConfiguration not available: {short_error(e)}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
