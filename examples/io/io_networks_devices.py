"""
I/O - Networks and Devices
==========================
Browse the I/O topology of the controller: the fieldbus networks, the devices
attached to each of them and the configuration of a selected device.
Everything here is read only.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot, print_title, pick, enum_name, short_error

print_title("I/O: Networks and Devices")

robot = connect_robot()

try:
    io = robot.rws.io

    # Resources exposed by the I/O service
    resources = io.get_resources()
    print(f"I/O resources ({len(resources)})")
    print("-" * 60)
    for name in resources:
        print(f"  - {name}")

    # Fieldbus networks
    networks = io.get_networks()
    print(f"\nNetworks ({len(networks)})")
    print(f"  {'Name':<20} {'Physical state':<20} {'Logical state':<20}")
    print(f"  {'-' * 20} {'-' * 20} {'-' * 20}")
    for n in networks:
        print(f"  {n.name:<20} {enum_name(n.physical_state):<20} {enum_name(n.logical_state):<20}")

    # Devices, with the network they belong to
    devices = io.get_devices()
    print(f"\nDevices ({len(devices)})")
    print(f"  {'Name':<24} {'Network':<16} {'Type':<14} {'Physical':<16} {'Logical':<12}")
    print(f"  {'-' * 24} {'-' * 16} {'-' * 14} {'-' * 16} {'-' * 12}")
    for d in devices:
        print(f"  {d.name:<24} {d.network_name:<16} {enum_name(d.type):<14} {enum_name(d.physical_state):<16} {enum_name(d.logical_state):<12}")

    # Details of one device
    if devices:
        print("\nPick a device to inspect:")
        selected = pick(devices, "Device", lambda d: f"{d.name:<24} on {d.network_name}")
        if selected is not None:
            device = io.get_device(selected.network_name, selected.name)
            print(f"\nDevice {device.name}")
            print("-" * 60)
            print(f"  Path        : {device.path}")
            print(f"  Address     : {device.address}")
            print(f"  Input data  : {device.input_data} (mask {device.input_mask})")
            print(f"  Output data : {device.output_data} (mask {device.output_mask})")

            try:
                config = io.get_device_configuration(device.network_name, device.name)
                print(f"  Config      : {config}")
            except Exception as e:
                print(f"  Config      : not available ({short_error(e)})")

            # The signals carried by this device
            device_signals = [s for s in io.get_signals() if s.device_name == device.name]
            print(f"\n  Signals on this device ({len(device_signals)})")
            for s in device_signals:
                print(f"    {s.name:<24} {enum_name(s.type):<14} value={s.logical_value}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
