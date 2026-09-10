"""
I/O - Write, Pulse and Simulate a Signal
========================================
Pick an output signal, write a value on it, invert it, send a pulse train and turn
the simulation on so a value can be forced without any hardware behind the signal.
The original value is put back at the end.

The controller protects the signals of category "internal", the ones it uses itself
for the panel, the drives and the safety chain. Writing one of them is answered with
403 Forbidden, which the example prints. Pick a signal of your own I/O configuration
to see the write go through.
"""
import sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot, print_title, pick, ask_float, confirm, enum_name, short_error

print_title("I/O: Write, Pulse and Simulate a Signal")

robot = connect_robot()

try:
    io = robot.rws.io

    # Only outputs can be written, so the list is filtered on the signal type
    outputs = [s for s in io.get_signals() if "Output" in enum_name(s.type)]
    if not outputs:
        print("No output signal found on this controller.")
        raise SystemExit(0)

    # The signals the user configured come first, the internal ones last
    writable = [s for s in outputs if s.category != "internal"]
    signals = writable + [s for s in outputs if s.category == "internal"]

    if not writable:
        print("Every output of this controller is an internal signal.")
        print("The controller will refuse to write them, which the example reports.\n")

    print(f"Pick an output signal among the {len(signals)} found:")
    selected = pick(signals, "Signal",
                    lambda s: f"{s.name:<24} {enum_name(s.type):<14} {s.category:<10} value={s.logical_value}")
    if selected is None:
        print("Nothing selected.")
        raise SystemExit(0)

    network, device, name = selected.network_name, selected.device_name, selected.name
    initial_value = selected.logical_value
    print(f"\nSelected {name}, current value {initial_value}")

    # Write a value
    value = ask_float("Value to write", 1.0)
    try:
        io.set_signal_value(network, device, name, value)
        print(f"  Value is now {io.get_signal(network, device, name).logical_value}")
    except Exception as e:
        print(f"  The controller refused the write: {short_error(e)}")

    # Invert the signal, only meaningful for a digital output
    if confirm("\nInvert the signal?"):
        try:
            io.invert_signal(network, device, name, value)
            print(f"  Value is now {io.get_signal(network, device, name).logical_value}")
        except Exception as e:
            print(f"  The controller refused: {short_error(e)}")

    # Send a pulse train: 3 pulses of 500 ms on, 500 ms off
    if confirm("\nSend 3 pulses of 500 ms?"):
        try:
            io.pulse_signal(network, device, name, 1.0, 3, 500, 500)
            time.sleep(3)
            print(f"  Value after the pulses: {io.get_signal(network, device, name).logical_value}")
        except Exception as e:
            print(f"  The controller refused: {short_error(e)}")

    # Simulation lets a value be forced when no hardware answers behind the signal
    if confirm("\nTurn the simulation on for this signal?"):
        try:
            io.set_signal_state(network, device, name, True)
            print(f"  Simulated: {enum_name(io.get_signal(network, device, name).logical_state)}")
            io.set_signal_state(network, device, name, False)
            print("  Simulation turned off again")
        except Exception as e:
            print(f"  The controller refused: {short_error(e)}")

    # Put the original value back
    try:
        io.set_signal_value(network, device, name, initial_value)
        print(f"\nRestored {name} to {io.get_signal(network, device, name).logical_value}")
    except Exception as e:
        print(f"\nCould not restore {name}: {short_error(e)}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
