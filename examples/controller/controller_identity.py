"""
Controller - Identity and Options
=================================
Read who the controller is: its name, its serial id, its type and its MAC address,
then the systems installed on it, the RobotWare options and the network interfaces.
Everything here is read only.

Some of these resources only exist on a real controller. A virtual controller answers
404 on them, which the example catches and reports.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from examples import connect_robot, print_title, ask, enum_name, short_error

print_title("Controller: Identity and Options")

robot = connect_robot()

try:
    controller = robot.rws.controller

    # Identity of the controller
    identity = controller.get_identity()
    print("Identity")
    print("-" * 60)
    print(f"  Name        : {identity.name}")
    print(f"  Id          : {identity.id}")
    print(f"  Type        : {enum_name(identity.type)}")
    print(f"  MAC address : {identity.mac_address}")
    print(f"  Level       : {enum_name(identity.level)}")

    # General information, including the controller clock
    info = controller.get_info()
    print("\nController info")
    print("-" * 60)
    print(f"  Name        : {info.name}")
    print(f"  Type        : {enum_name(info.type)}")
    print(f"  Level       : {enum_name(info.level)}")
    print(f"  System time : {info.system_time}")
    print(f"  Resources   : {', '.join(info.resources) if info.resources else '(none)'}")

    # Systems installed on the controller, a real controller only
    print("\nInstalled systems")
    print("-" * 60)
    try:
        systems = controller.get_installed_systems()
        for name in systems:
            print(f"  - {name}")
    except Exception as e:
        print(f"  Not available: {short_error(e)}")

    # Network interfaces, a real controller only
    print("\nNetwork interfaces")
    print("-" * 60)
    try:
        for itf in controller.get_network_interfaces():
            print(f"  Port {itf.port} ({itf.logical_name})")
            print(f"    Address : {itf.address}  Mask: {itf.mask}  Gateway: {itf.gateway}")
            print(f"    DHCP    : {itf.dhcp_enabled}  DNS: {itf.primary_dns} / {itf.secondary_dns}")
    except Exception as e:
        print(f"  Not available: {short_error(e)}")

    # Check one option and one RobotWare version
    option = ask("\nOption to look for", "RobotWare")
    try:
        print(f"  has_option('{option}') = {controller.has_option(option)}")
    except Exception as e:
        print(f"  Not available: {short_error(e)}")

    version = ask("RobotWare version to check compatibility with", "6.0")
    try:
        print(f"  is_robot_ware_version_compatible('{version}') = "
              f"{controller.is_robot_ware_version_compatible(version)}")
    except Exception as e:
        print(f"  Not available: {short_error(e)}")

    # Environment variables of the controller
    variable = ask("Environment variable to read", "$TEMP")
    try:
        print(f"  {variable} = {controller.get_environment_variable(variable)}")
    except Exception as e:
        print(f"  Could not read {variable}: {short_error(e)}")

finally:
    robot.disconnect()
    print("\nDisconnected.")
